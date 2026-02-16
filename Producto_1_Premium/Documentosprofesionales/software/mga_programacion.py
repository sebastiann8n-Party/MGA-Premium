from dataclasses import dataclass, field
from typing import List, Dict

@dataclass
class Indicador:
    nombre: str
    medicion: str # Unidad
    meta: str
    fuente_verificacion: str
    tipo_fuente: str = "Informe técnico"

@dataclass
class FuenteFinanciacionDetail:
    etapa: str
    tipo_entidad: str
    nombre_entidad: str
    tipo_recurso: str
    monto: float
    periodo: str

@dataclass
class CronogramaActividad:
    concepto: str
    meses_1_6: str = ""
    meses_7_12: str = ""
    meses_13_24: str = ""
    meses_25_36: str = ""
    meses_37_48: str = ""

@dataclass
class ResumenEjecutivo:
    item: str
    descripcion: str

class MgaProgramacion:
    """Módulo 4: Programación, Indicadores y Resumen Ejecutivo."""
    
    def __init__(self):
        self.indicadores_producto: List[Indicador] = []
        self.indicadores_gestion: List[Indicador] = []
        self.fuentes_financiamiento: List[FuenteFinanciacionDetail] = []
        self.supuestos: List[str] = []
        self.cronograma: List[CronogramaActividad] = []
        self.resumen_ejecutivo: List[ResumenEjecutivo] = []
        self.cierre_financiero: Dict[str, str] = {}
        self.firma_responsable: Dict[str, str] = {}

    def agregar_indicador_producto(self, ind: Indicador):
        self.indicadores_producto.append(ind)

    def agregar_indicador_gestion(self, ind: Indicador):
        self.indicadores_gestion.append(ind)

    def agregar_fuente(self, fuente: FuenteFinanciacionDetail):
        self.fuentes_financiamiento.append(fuente)

    def agregar_actividad_cronograma(self, act: CronogramaActividad):
        self.cronograma.append(act)

    def agregar_supuesto(self, supuesto: str):
        self.supuestos.append(supuesto)
        
    def agregar_item_resumen(self, item: str, desc: str):
        self.resumen_ejecutivo.append(ResumenEjecutivo(item, desc))

    def set_cierre_financiero(self, inversion: str, op_anual: str, horizonte: str):
        self.cierre_financiero = {"Inversión Total": inversion, "Costos Op. Anuales": op_anual, "Horizonte": horizonte}

    def set_firma(self, nombre: str, cc: str, cargo: str, dep: str, fecha: str):
        self.firma_responsable = {"Nombre": nombre, "C.C.": cc, "Cargo": cargo, "Dependencia": dep, "Fecha": fecha}

    def render_content(self) -> dict:
        contenido = []
        
        # Cap 1: Indicadores de Producto
        contenido.append({"tipo": "titulo2", "texto": "Capítulo 1: Indicadores de Producto"})
        datos_ind_prod = [
            {"Indicador": i.nombre, "Unidad": i.medicion, "Meta": i.meta, "Fuente Verif.": i.fuente_verificacion}
            for i in self.indicadores_producto
        ]
        contenido.append({"tipo": "tabla", "titulo": "Matriz de Indicadores de Producto", "datos": datos_ind_prod})

        # Cap 2: Indicadores de Gestión
        contenido.append({"tipo": "titulo2", "texto": "Capítulo 2: Indicadores de Gestión"})
        datos_ind_ges = [
            {"Indicador": i.nombre, "Unidad": i.medicion, "Meta": i.meta, "Fuente Verif.": i.fuente_verificacion}
            for i in self.indicadores_gestion
        ]
        contenido.append({"tipo": "tabla", "titulo": "Matriz de Indicadores de Gestión", "datos": datos_ind_ges})

        # Cap 3: Fuentes de Financiación
        contenido.append({"tipo": "titulo2", "texto": "Capítulo 3: Fuentes de Financiación"})
        if self.cierre_financiero:
             contenido.append({"tipo": "lista", "titulo": "Cierre Financiero:", "items": [f"{k}: {v}" for k,v in self.cierre_financiero.items()]})
        
        datos_fuentes = [
            {"Etapa": f.etapa, "Entidad": f.nombre_entidad, "Recurso": f.tipo_recurso, "Monto": f"${f.monto:,.0f}", "Periodo": f.periodo}
            for f in self.fuentes_financiamiento
        ]
        contenido.append({"tipo": "tabla", "titulo": "Matriz de Cofinanciación", "datos": datos_fuentes})

        # Cap 4: Resumen del Proyecto
        contenido.append({"tipo": "titulo2", "texto": "Capítulo 4: Resumen del Proyecto"})
        contenido.append({"tipo": "lista", "titulo": "Supuestos del Proyecto:", "items": self.supuestos})
        
        datos_crono = [
            {"Actividad": c.concepto, "1-6": c.meses_1_6, "7-12": c.meses_7_12, "13-24": c.meses_13_24, "25-36": c.meses_25_36, "37-48": c.meses_37_48}
            for c in self.cronograma
        ]
        contenido.append({"tipo": "tabla", "titulo": "Cronograma de Ejecución", "datos": datos_crono})
        
        datos_resumen = [{"Item": r.item, "Descripción": r.descripcion} for r in self.resumen_ejecutivo]
        contenido.append({"tipo": "tabla", "titulo": "Resumen Ejecutivo", "datos": datos_resumen})

        # Firma
        if self.firma_responsable:
            contenido.append({"tipo": "titulo2", "texto": "Firma del Responsable"})
            lines = [f"{k}: {v}" for k,v in self.firma_responsable.items()]
            contenido.append({"tipo": "lista", "titulo": "Datos de Firma:", "items": lines})
            contenido.append({"tipo": "parrafo", "texto": "_________________________________"})
            contenido.append({"tipo": "parrafo", "texto": "Firma Director Ejecutivo CITES"})

        return {
            "titulo": "MÓDULO 4: PROGRAMACIÓN",
            "cuerpo": contenido
        }
