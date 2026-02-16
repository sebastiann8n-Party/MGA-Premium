import google.generativeai as genai
import json
import os
from tenacity import retry, stop_after_attempt, wait_exponential
from typing import Optional, Dict, Any
from pydantic import ValidationError

try:
    from .schemas import APACitationData, FullDocumentSchema
except ImportError:
    # Fallback para ejecución directa
    from schemas import APACitationData, FullDocumentSchema

# Configuración optimizada para ahorro de tokens (Flash)
DEFAULT_MODEL = 'gemini-1.5-flash'

class GeminiExtractor:
    def __init__(self, api_key: Optional[str] = None):
        # Prioridad: Argumento -> Variable de Entorno -> Error
        self.api_key = api_key or os.getenv("GEMINI_API_KEY")
        if not self.api_key:
            print("[WARN] API Key no configurada. Las llamadas fallarán si no se setea GEMINI_API_KEY.")
        else:
            genai.configure(api_key=self.api_key)
        
        # CONFIGURACIÓN CRÍTICA: Forzar modo JSON nativo
        self.model = genai.GenerativeModel(
            DEFAULT_MODEL,
            generation_config={"response_mime_type": "application/json", "temperature": 0.1}
        )

        # Drivers Cognitivos (System Prompts)
        self.citation_prompt = """
        ROL: Eres un bibliotecario experto en catalogación APA 7.0.
        TAREA: Convierte el texto de entrada en un objeto JSON estructurado para citación bibliográfica.
        """

        self.full_doc_prompt = """
        ROL: Eres un Editor Académico Senior y Arquitecto de Datos especializado en Normas APA 7ª Edición.
        TAREA: Estructura el texto crudo en un objeto JSON estricto para un motor de renderizado DOCX.
        
        REGLAS DE CLASIFICACIÓN (PARAGRAPH BLOCKS):
        1. "titulo1": Títulos principales, introducciones de sección mayor.
        2. "titulo2": Subtítulos dentro de una sección.
        3. "cuerpo": Párrafos estándar de argumentación.
        4. "cita_larga": Bloques textuales >40 palabras (menciones a autores, citas en bloque).
        5. "referencia": Entradas bibliográficas al final.

        REGLAS DE EXTRACCIÓN (METADATA):
        - Infiere Título, Autor e Institución.
        - Si no encuentras institución, usa "Institución Independiente".
        - Si no encuentras autor, usa "Autor Desconocido".
        """

    @retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, min=2, max=10))
    def extract_citation_data(self, raw_text: str) -> APACitationData:
        """
        Extrae datos bibliográficos de un texto usando Gemini en modo JSON.
        """
        if not self.api_key: raise ValueError("API Key faltante.")

        try:
            response = self.model.generate_content(
                f"{self.citation_prompt}\n\nENTRADA: '{raw_text}'\n\nResponde JSON que cumpla el esquema APACitationData."
            )
            
            # Limpieza defensiva aunque usemos mode JSON
            clean_text = response.text.replace('```json', '').replace('```', '').strip()
            data_dict = json.loads(clean_text)
            return APACitationData(**data_dict)

        except Exception as e:
            print(f"Error en extracción citación: {str(e)}")
            raise

    @retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, min=2, max=10))
    def extract_full_document(self, user_instruction: str, raw_content: str) -> FullDocumentSchema:
        """
        PROMPT MAESTRO: Convierte contenido crudo en estructura documental APA completa.
        """
        if not self.api_key: raise ValueError("API Key faltante.")

        full_prompt = f"""
        {self.full_doc_prompt}

        INSTRUCCIÓN ADICIONAL: {user_instruction}
        
        CONTENIDO BASE:
        "{raw_content[:15000]}" 

        Genera el JSON compatible con FullDocumentSchema (metadata, content, references).
        """

        try:
            response = self.model.generate_content(full_prompt)
            clean_text = response.text.replace('```json', '').replace('```', '').strip()
            data_dict = json.loads(clean_text)
            
            # Validación Pydantic (La Barrera de Seguridad)
            return FullDocumentSchema(**data_dict)
            
        except json.JSONDecodeError:
            print("❌ Error Crítico: La IA no devolvió un JSON válido.")
            raise
        except ValidationError as e:
            print(f"❌ Error de Esquema Pydantic: {e}")
            raise
        except Exception as e:
            print(f"Error Genérico en Full Document: {str(e)}")
            raise

class GeminiExtractor:
    def __init__(self, api_key: Optional[str] = None):
        # Prioridad: Argumento -> Variable de Entorno -> Error
        self.api_key = api_key or os.getenv("GEMINI_API_KEY")
        if not self.api_key:
            # Nota: En producción esto debería manejar logs, aquí lanzamos error para feedback inmediato
            print("[WARN] API Key no configurada. Las llamadas fallarán si no se setea GEMINI_API_KEY.")
        else:
            genai.configure(api_key=self.api_key)
        
        self.model = genai.GenerativeModel(DEFAULT_MODEL)

    @retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, min=2, max=10))
    def extract_citation_data(self, raw_text: str) -> APACitationData:
        """
        Extrae datos bibliográficos de un texto o URL procesado usando Gemini.
        Maneja reintentos automáticos para fallos transitorios de API.
        """
        if not self.api_key:
             raise ValueError("API Key faltante. Configura GEMINI_API_KEY.")

        # Prompt system-like instruccional
        prompt = f"""
        Actúa como un bibliotecario experto en catalogación APA 7.0.
        Tu misión única es convertir el texto de entrada en un objeto JSON estructurado válido según el esquema solicitado.
        
        ENTRADA: "{raw_text}"
        
        ESQUEMA JSON OBLIGATORIO:
        {{
            "authors": [
                {{"is_corporate": boolean, "surname": "string", "initials": "string (ej: 'J. R.')"}}
            ],
            "date": {{"year": "string (YYYY o s.f.)", "month_day": "string (opcional para news)"}},
            "title": "string (sentence case, solo primera mayúscula)",
            "source": {{
                "container_title": "string (nombre de revista/libro host)",
                "volume": "string (solo numero)",
                "issue": "string (solo numero)",
                "pages": "string (ej: 10-20)",
                "doi_url": "string (url completa)",
                "publisher": "string"
            }},
            "type_of_work": "string (book, article, website, report, thesis)"
        }}

        REGLAS:
        1. Si falta información, usa null o cadenas vacías, NO inventes.
        2. Para autores: Si es organización, is_corporate=true y surname=Nombre Organización.
        3. Para fecha: Si no hay fecha, year="s.f.".
        4. RESPUESTA: Solo el JSON, sin bloques de código ```json.
        """

        try:
            # Generación con temperatura 0 para determinismo
            response = self.model.generate_content(
                prompt,
                generation_config=genai.types.GenerationConfig(temperature=0.0)
            )
            
            clean_text = response.text.replace('```json', '').replace('```', '').strip()
            
            # Validación dual: JSON válido -> Esquema Pydantic válido
            data_dict = json.loads(clean_text)
            
            # Pydantic se encarga de validar tipos y estructura
            validated_object = APACitationData(**data_dict)
            return validated_object

        except json.JSONDecodeError:
            print(f"Error: La IA devolvió un JSON malformado: {clean_text[:50]}...")
            raise
        except Exception as e:
            print(f"Error crítico en extracción Gemini: {str(e)}")
            raise

    @retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, min=2, max=10))
    def extract_full_document(self, user_instruction: str, raw_content: str) -> FullDocumentSchema:
        """
        PROMPT MAESTRO: Convierte contenido crudo en estructura documental APA completa.
        """
        if not self.api_key:
             raise ValueError("API Key faltante.")

        prompt = f"""
        Eres un Editor Académico Senior experto en normas APA 7.
        Tu tarea es estructurar el contenido provisto en un formato JSON estricto listo para renderizado.

        INSTRUCCIÓN USUARIO: {user_instruction}
        CONTENIDO BASE:
        "{raw_content[:4000]}..." (truncado para seguridad de tokens)

        ESQUEMA JSON OBLIGATORIO (FullDocumentSchema):
        {{
            "metadata": {{
                "title": "string (Título académico >10 chars)",
                "author": "string (Nombre completo)",
                "institution": "string (Universidad/Entidad)",
                "date": "string (Fecha actual si no se especifica)"
            }},
            "content": [
                {{
                    "role": "titulo1" | "titulo2" | "cuerpo" | "cita_larga",
                    "content": "string (Texto limpio)"
                }},
                ...
            ],
            "references": ["string (Referencia bibliográfica completa 1)", "string (Referencia 2)..."]
        }}

        REGLAS:
        1. Identifica jerarquía de títulos.
        2. Detecta párrafos >40 palabras que sean citas textuales y asígnales role='cita_larga'.
        3. Agrupa las referencias bibliográficas al final en una lista de strings.
        4. Validarás con Pydantic: NO falles en la estructura.
        5. RESPUESTA: Solo JSON puro.
        """

        try:
            response = self.model.generate_content(
                prompt,
                generation_config=genai.types.GenerationConfig(temperature=0.1)
            )
            clean_text = response.text.replace('```json', '').replace('```', '').strip()
            data_dict = json.loads(clean_text)
            
            # Validación Pydantic del documento completo
            return FullDocumentSchema(**data_dict)
            
        except Exception as e:
            print(f"Error Full Document Extraction: {str(e)}")
            raise

# Bloque de prueba (solo npx/local execution)
if __name__ == "__main__":
    # Mock para testing rápido si no hay key
    sample_text = "El libro 'Clean Code' escrito por Robert C. Martin en 2008, publicado por Prentice Hall."
    print(f"Procesando: {sample_text}")
    # extractor = GeminiExtractor()
    # print(extractor.extract_citation_data(sample_text))
