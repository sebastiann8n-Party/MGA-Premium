from dataclasses import dataclass, field
from typing import List, Dict

@dataclass
class DatosMercado:
    anio: str
    oferta: int
    demanda: int
    deficit: int
    tipo: str # Historico, Sin Proyecto, Con Proyecto
    descripcion: str

@dataclass
class ProductoMercado:
    nombre: str
    datos: List[DatosMercado]

@dataclass
class EspecificacionTecnica:
    producto: str
    descripcion: str
    detalles: List[str] # Lista de características

@dataclass
class Ubicacion:
    departamento: str
    municipio: str
    direccion: str
    justificacion: List[str]
    zonas_sensores: Dict[str, int] # Region -> Cantidad

@dataclass
class CadenaValorItem:
    actividad: str
    insumos: str
    tipo_insumo: str
    etapa: str # Inversión / Operación
    valor: float # En millones
    unidad_tiempo: str = "" # /año si es recurrente

@dataclass
class CadenaValor:
    nombre: str
    items: List[CadenaValorItem]

@dataclass
class Riesgo:
    nivel: str
    tipo: str
    descripcion: str
    probabilidad: str
    impacto: str
    mitigacion: str

@dataclass
class Beneficio:
    nombre: str
    tipo: str
    medicion: str
    descripcion: str
    flujos: List[Dict[str, str]] # [{'Periodo': '2026', 'Valor': '$100,000'}]

class MgaPreparacion:
    """Módulo 2 de MGA: Preparación Completo (Mercado, Técnico, Legal, Riesgos)."""
    
    def __init__(self):
        self.productos_mercado: List[ProductoMercado] = []
        self.especificaciones: List[EspecificacionTecnica] = []
        self.ubicacion: Ubicacion = None
        self.cadenas_valor: List[CadenaValor] = []
        self.riesgos: List[Riesgo] = []
        self.beneficios: List[Beneficio] = []
        self.analisis_deficit: str = ""

    def agregar_producto_mercado(self, prod: ProductoMercado):
        self.productos_mercado.append(prod)

    def agregar_especificacion(self, espec: EspecificacionTecnica):
        self.especificaciones.append(espec)

    def set_ubicacion(self, ubic: Ubicacion):
        self.ubicacion = ubic

    def agregar_cadena_valor(self, cadena: CadenaValor):
        self.cadenas_valor.append(cadena)

    def agregar_riesgo(self, riesgo: Riesgo):
        self.riesgos.append(riesgo)

    def agregar_beneficio(self, ben: Beneficio):
        self.beneficios.append(ben)

    def render_content(self) -> dict:
        contenido = []
        
        # Cap 1: Necesidades (Mercado)
        contenido.append({"tipo": "titulo2", "texto": "Capítulo 1: Necesidades (Estudio de Mercado)"})
        for prod in self.productos_mercado:
            datos_tabla = [
                {"Año": d.anio, "Oferta": d.oferta, "Demanda": d.demanda, "Déficit": d.deficit, "Descripción": d.descripcion}
                for d in prod.datos
            ]
            contenido.append({"tipo": "titulo2", "texto": f"Producto: {prod.nombre}"})
            contenido.append({"tipo": "tabla", "titulo": "Balance Oferta-Demanda", "datos": datos_tabla})
        
        if self.analisis_deficit:
            contenido.append({"tipo": "parrafo", "texto": f"Análisis del Déficit: {self.analisis_deficit}"})

        # Cap 2: Análisis Técnico
        contenido.append({"tipo": "titulo2", "texto": "Capítulo 2: Análisis Técnico"})
        for espec in self.especificaciones:
            contenido.append({"tipo": "titulo2", "texto": f"Especificación: {espec.producto}"})
            contenido.append({"tipo": "parrafo", "texto": espec.descripcion})
            contenido.append({"tipo": "lista", "titulo": "Detalles Técnicos:", "items": espec.detalles})

        # Cap 3: Localización
        if self.ubicacion:
            contenido.append({"tipo": "titulo2", "texto": "Capítulo 3: Localización"})
            contenido.append({"tipo": "parrafo", "texto": f"Sede Principal: {self.ubicacion.municipio}, {self.ubicacion.departamento}. {self.ubicacion.direccion}."})
            contenido.append({"tipo": "lista", "titulo": "Justificación:", "items": self.ubicacion.justificacion})
            
            zonas_list = [f"{k}: {v} sensores" for k,v in self.ubicacion.zonas_sensores.items()]
            contenido.append({"tipo": "lista", "titulo": "Distribución de Sensores:", "items": zonas_list})

        # Cap 4: Cadena de Valor
        contenido.append({"tipo": "titulo2", "texto": "Capítulo 4: Cadena de Valor"})
        for cv in self.cadenas_valor:
            datos_cv = [
                {"Actividad": i.actividad, "Insumos": i.insumos, "Etapa": i.etapa, "Valor (MM)": f"${i.valor:,.0f}{i.unidad_tiempo}"}
                for i in cv.items
            ]
            contenido.append({"tipo": "tabla", "titulo": f"Cadena: {cv.nombre}", "datos": datos_cv})

        # Cap 5: Riesgos
        contenido.append({"tipo": "titulo2", "texto": "Capítulo 5: Riesgos"})
        datos_riesgos = [
            {"Nivel": r.nivel, "Tipo": r.tipo, "Riesgo": r.descripcion, "Prob": r.probabilidad, "Mitigación": r.mitigacion}
            for r in self.riesgos
        ]
        contenido.append({"tipo": "tabla", "titulo": "Matriz de Riesgos", "datos": datos_riesgos})

        # Cap 6: Beneficios
        contenido.append({"tipo": "titulo2", "texto": "Capítulo 6: Ingresos y Beneficios"})
        for ben in self.beneficios:
            contenido.append({"tipo": "titulo2", "texto": f"Beneficio: {ben.nombre}"})
            contenido.append({"tipo": "parrafo", "texto": f"Tipo: {ben.tipo} | Medición: {ben.medicion}"})
            contenido.append({"tipo": "parrafo", "texto": ben.descripcion})
            contenido.append({"tipo": "tabla", "titulo": "Valoración", "datos": ben.flujos})

        return {
            "titulo": "MÓDULO 2: PREPARACIÓN",
            "cuerpo": contenido
        }
