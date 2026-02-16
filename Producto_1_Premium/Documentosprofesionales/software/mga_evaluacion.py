from dataclasses import dataclass
from typing import List, Optional

@dataclass
class FlujoCajaDetail:
    periodo: int # Año 0, 1, 2...
    inversion: float
    costos_op: float
    beneficios: float
    flujo_neto: float
    
@dataclass
class IndicadorManual:
    nombre: str
    valor: str
    interpretacion: str

class MgaEvaluacion:
    """Módulo 3: Evaluación Financiera y Económica."""
    
    def __init__(self, tasa_social_descuento: float = 0.12):
        self.tsd = tasa_social_descuento
        self.flujos_detalle: List[FlujoCajaDetail] = []
        self.indicadores_manuales: List[IndicadorManual] = []
        self.analisis_resultados: str = ""
        self.decision: str = ""

    def agregar_flujo_detalle(self, anio: int, inv: float, costos: float, ben: float, neto: float):
        self.flujos_detalle.append(FlujoCajaDetail(anio, inv, costos, ben, neto))

    def agregar_indicador(self, nombre: str, valor: str, interp: str):
        self.indicadores_manuales.append(IndicadorManual(nombre, valor, interp))
        
    def set_analisis(self, texto: str):
        self.analisis_resultados = texto
        
    def set_decision(self, texto: str):
        self.decision = texto

    def render_content(self) -> dict:
        # Construir tabla de flujos detallada
        tabla_flujos = [
            {
                "Año": f.periodo, 
                "Inversión": f"${f.inversion:,.0f}",
                "Costos Op": f"${f.costos_op:,.0f}",
                "Beneficios": f"${f.beneficios:,.0f}",
                "Flujo Neto": f"${f.flujo_neto:,.0f}"
            }
            for f in sorted(self.flujos_detalle, key=lambda x: x.periodo)
        ]

        # Construir tabla de indicadores
        tabla_indicadores = [
            {"Indicador": i.nombre, "Valor": i.valor, "Interpretación": i.interpretacion}
            for i in self.indicadores_manuales
        ]

        contenido = [
            {"tipo": "parrafo", "texto": f"Evaluación realizada con Tasa Social de Descuento (TSD) del {self.tsd*100}%."},
            {"tipo": "titulo2", "texto": "Capítulo 1: Flujo Económico"},
            {"tipo": "tabla", "titulo": "Flujo de Caja Económico (Millones COP)", "datos": tabla_flujos},
            
            {"tipo": "titulo2", "texto": "Capítulo 2: Indicadores y Decisión"},
            {"tipo": "titulo2", "texto": "Indicadores de Evaluación"},
        ]
        
        if tabla_indicadores:
            contenido.append({"tipo": "tabla", "titulo": "Resumen de Indicadores", "datos": tabla_indicadores})
            
        if self.analisis_resultados:
            contenido.append({"tipo": "titulo2", "texto": "Análisis de Resultados"})
            contenido.append({"tipo": "parrafo", "texto": self.analisis_resultados})
            
        if self.decision:
            contenido.append({"tipo": "titulo2", "texto": "Decisión Final"})
            contenido.append({"tipo": "parrafo", "texto": self.decision})

        return {
            "titulo": "MÓDULO 3: EVALUACIÓN ECONÓMICA Y SOCIAL",
            "cuerpo": contenido
        }
