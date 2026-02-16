from dataclasses import dataclass, field
from typing import List, Dict, Optional

@dataclass
class Problema:
    descripcion: str
    causas_directas: List[str]
    causas_indirectas: List[str]
    efectos_directos: List[str]
    efectos_indirectos: List[str]
    magnitud_actual: str = ""

@dataclass
class Poblacion:
    ubicacion: str
    cantidad: int
    caracteristicas: List[str]
    fuente_info: str = ""

@dataclass
class Alternativa:
    nombre: str
    descripcion: str
    seleccionada: bool = False
    justificacion: str = ""

@dataclass
class Objetivo:
    general: str
    especificos: List[str]
    fines_directos: List[str] = field(default_factory=list)
    fines_indirectos: List[str] = field(default_factory=list)
    indicador: str = "" # Descripción del indicador de propósito

@dataclass
class Participante:
    entidad: str
    posicion: str # Beneficiario, Cooperante, Oponente
    intereses: str
    contribucion: str

class MgaIdentificacion:
    """Módulo 1 de MGA: Identificación Completa (Alineado a CITES)."""
    
    def __init__(self, 
                 nombre_proyecto: str, 
                 bpin: str,
                 localizacion: str,
                 problema: Problema, 
                 poblacion: Poblacion,
                 objetivos: Objetivo):
        self.nombre_proyecto = nombre_proyecto
        self.bpin = bpin
        self.localizacion = localizacion
        self.problema = problema
        self.poblacion = poblacion
        self.objetivos = objetivos
        
        self.alternativas: List[Alternativa] = []
        self.participantes: List[Participante] = []
        self.contribucion_politica: List[str] = []

    def agregar_alternativa(self, alt: Alternativa):
        self.alternativas.append(alt)

    def agregar_participante(self, part: Participante):
        self.participantes.append(part)
        
    def set_contribucion_politica(self, lineas: List[str]):
        self.contribucion_politica = lineas

    def render_content(self) -> dict:
        """Retorna el contenido estructurado para el Document Factory."""
        
        # Construcción de listas formateadas
        lista_causas = [f"Directa: {c}" for c in self.problema.causas_directas] + \
                       [f"Indirecta: {c}" for c in self.problema.causas_indirectas]
        
        lista_efectos = [f"Directo: {e}" for e in self.problema.efectos_directos] + \
                        [f"Indirecto: {e}" for e in self.problema.efectos_indirectos]
        
        datos_alternativas = [
            {"Alternativa": alt.nombre, "Seleccionada": "SI" if alt.seleccionada else "NO", "Descripción": alt.descripcion}
            for alt in self.alternativas
        ]
        
        datos_participantes = [
            {"Entidad": p.entidad, "Posición": p.posicion, "Intereses": p.intereses}
            for p in self.participantes
        ]

        lista_fines = [f"Directo: {f}" for f in self.objetivos.fines_directos] + \
                      [f"Indirecto: {f}" for f in self.objetivos.fines_indirectos]

        return {
            "titulo": f"MÓDULO 1: IDENTIFICACIÓN - {self.nombre_proyecto}",
            "cuerpo": [
                {"tipo": "parrafo", "texto": f"Código BPIN: {self.bpin} | Localización: {self.localizacion}"},
                
                # Cap 1: Plan de Desarrollo
                {"tipo": "titulo2", "texto": "Capítulo 1: Plan de Desarrollo y Política Pública"},
                {"tipo": "lista", "titulo": "Contribución a Políticas:", "items": self.contribucion_politica},
                
                # Cap 2: Problemática
                {"tipo": "titulo2", "texto": "Capítulo 2: Problemática"},
                {"tipo": "parrafo", "texto": f"Problema Central: {self.problema.descripcion}"},
                {"tipo": "parrafo", "texto": f"Magnitud Actual: {self.problema.magnitud_actual}"},
                {"tipo": "lista", "titulo": "Árbol de Causas:", "items": lista_causas},
                {"tipo": "lista", "titulo": "Árbol de Efectos:", "items": lista_efectos},
                
                # Cap 3: Participantes
                {"tipo": "titulo2", "texto": "Capítulo 3: Participantes"},
                {"tipo": "tabla", "titulo": "Matriz de Involucrados", "datos": datos_participantes},
                
                # Cap 4: Población
                {"tipo": "titulo2", "texto": "Capítulo 4: Población"},
                {"tipo": "parrafo", "texto": f"Población Objetivo: {self.poblacion.cantidad:,} habitantes en {self.poblacion.ubicacion}."},
                {"tipo": "parrafo", "texto": f"Fuente: {self.poblacion.fuente_info}"},
                {"tipo": "lista", "titulo": "Características Demográficas:", "items": self.poblacion.caracteristicas},
                
                # Cap 5: Objetivos
                {"tipo": "titulo2", "texto": "Capítulo 5: Objetivos"},
                {"tipo": "parrafo", "texto": f"Objetivo General: {self.objetivos.general}"},
                {"tipo": "lista", "titulo": "Objetivos Específicos:", "items": self.objetivos.especificos},
                {"tipo": "lista", "titulo": "Árbol de Fines:", "items": lista_fines},
                {"tipo": "parrafo", "texto": f"Indicador de Propósito: {self.objetivos.indicador}"},
                
                # Cap 6: Alternativas
                {"tipo": "titulo2", "texto": "Capítulo 6: Alternativas de Solución"},
                {"tipo": "tabla", "titulo": "Evaluación de Alternativas", "datos": datos_alternativas},
                {"tipo": "parrafo", "texto": f"Justificación Selección: {next((a.justificacion for a in self.alternativas if a.seleccionada), '')}"},
            ]
        }
