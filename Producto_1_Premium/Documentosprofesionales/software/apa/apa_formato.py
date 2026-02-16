from dataclasses import dataclass
from typing import Dict

@dataclass
class EstiloPagina:
    margenes: Dict[str, float]  # cm
    fuente: str
    tamanio: int
    interlineado: float
    sangria_primera_linea: float # cm

class ApaFormato:
    """Configuración de estilos según APA 7."""
    
    @staticmethod
    def obtener_estilo_estandar() -> EstiloPagina:
        return EstiloPagina(
            margenes={"superior": 2.54, "inferior": 2.54, "izquierdo": 2.54, "derecho": 2.54},
            fuente="Times New Roman",
            tamanio=12,
            interlineado=2.0,
            sangria_primera_linea=1.27
        )

    @staticmethod
    def obtener_estilo_profesional() -> EstiloPagina:
        """Variante profesional permitida (Sans Serif)."""
        return EstiloPagina(
            margenes={"superior": 2.54, "inferior": 2.54, "izquierdo": 2.54, "derecho": 2.54},
            fuente="Calibri", # O Arial
            tamanio=11,
            interlineado=1.5, # Ajuste común en documentos técnicos
            sangria_primera_linea=1.27
        )
