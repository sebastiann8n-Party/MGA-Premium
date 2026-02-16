import os
import json
import argparse
import sys
import google.generativeai as genai
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH

# --- 1. CONFIGURACIÓN DEL CEREBRO (Gemini) ---
API_KEY = os.environ.get("GEMINI_API_KEY")

def analyze_unstructured_text(text_input, api_key=None):
    """
    Toma un texto desordenado (notas, correos, ideas) y lo estructura 
    en el formato JSON estricto que requiere el Wizard MGA.
    """
    current_key = api_key if api_key else API_KEY
    
    if not current_key:
        print("[AVISO] No API Key. Retornando Mock Data.")
        return _get_mock_mga_data()

    try:
        genai.configure(api_key=current_key)
        model = genai.GenerativeModel('gemini-2.0-flash')

        prompt = f"""
        Actúa como un Experto en Formulación de Proyectos bajo la Metodología General Ajustada (MGA).
        Tu tarea es leer el siguiente texto desordenado y extraer/inferir la información para estructurarla en un JSON.
        
        TEXTO DEL USUARIO:
        "{text_input}"

        REGLAS DE EXTRACCIÓN:
        1. Identifica un Título corto y la Entidad responsable.
        2. Resume el Problema Central y el Objetivo General.
        3. Identifica la Población y Ubicación.
        4. Crea una Descripción Técnica de la solución.
        5. Infiere una tabla de Especificaciones Técnicas (al menos 3 items).
        6. Infiere un Cronograma (Fases, Actividades, Duración, Responsable).
        7. Infiere un Presupuesto (Ítem, Unidad, Cantidad, Valor Unitario). Estima valores realistas en COP si no están.
        8. Infiere Riesgos (Riesgo, Probabilidad, Impacto, Mitigación).

        FORMATO JSON DE SALIDA (ESTRICTO):
        {{
            "title": "Título del Proyecto",
            "entity": "Entidad Proponente",
            "sections": {{
                "identificacion": {{
                    "problema": "...",
                    "objetivo": "...",
                    "poblacion": "...",
                    "ubicacion": "..."
                }},
                "tecnica": {{
                    "descripcion": "...",
                    "especificaciones": [
                        {{"Característica": "...", "Detalle": "..."}}
                    ]
                }},
                "cronograma": [
                    {{"Fase": "...", "Actividad": "...", "Duración": "...", "Responsable": "..."}}
                ],
                "presupuesto": [
                    {{"Ítem": "...", "Unidad": "...", "Cantidad": 1, "Valor Unitario": 1000}}
                ],
                "riesgos": [
                    {{"Riesgo": "...", "Probabilidad": "Alta/Media/Baja", "Impacto": "Alto/Medio/Bajo", "Mitigación": "..."}}
                ]
            }}
        }}
        
        Responde SOLO con el JSON válido. Sin markdown, sin explicaciones.
        """

        response = model.generate_content(prompt)
        # Limpieza básica por si el modelo incluye markdown
        clean_json = response.text.replace('```json', '').replace('```', '').strip()
        data = json.loads(clean_json)
        return data

    except Exception as e:
        print(f"[ERROR AI ENGINE]: {e}")
        return _get_mock_mga_data()

def _get_mock_mga_data():
    """Datos de prueba por si falla la API o no hay key"""
    return {
        "title": "Proyecto Demo MGA (Offline)",
        "entity": "Entidad de Prueba",
        "sections": {
            "identificacion": {
                "problema": "El usuario no tiene API Key configurada para generar datos reales.",
                "objetivo": "Demostrar la estructura de datos del Wizard sin costos.",
                "poblacion": "Usuarios Demo",
                "ubicacion": "Entorno Local"
            },
            "tecnica": {
                "descripcion": "Se utiliza un generador de datos fijos (Mock) para simular la respuesta de la IA.",
                "especificaciones": [
                    {"Característica": "Modo", "Detalle": "Offline"},
                    {"Característica": "Costo", "Detalle": "0 Tokens"}
                ]
            },
            "cronograma": [
                {"Fase": "Inicio", "Actividad": "Configurar API Key", "Duración": "5 min", "Responsable": "Usuario"}
            ],
            "presupuesto": [
                {"Ítem": "Licencia Gemini", "Unidad": "Unidad", "Cantidad": 1, "Valor Unitario": 0}
            ],
            "riesgos": [
                {"Riesgo": "Falta de Datos", "Probabilidad": "Alta", "Impacto": "Alto", "Mitigación": "Obtener API Key"}
            ]
        }
    }

# --- Legacy Compatibility (Optional) ---
class CITESReportBuilder:
    # Mantenemos referencia para no romper imports antiguos si los hubiera, 
    # pero idealmente se usa desde cites_builder.py
    pass

