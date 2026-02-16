from pydantic import BaseModel, Field, field_validator, ConfigDict
from typing import Optional, List, Union, Literal
import datetime

class APAAuthor(BaseModel):
    """
    Representación de un autor (persona o entidad).
    APA 7: Apellidos, Iniciales.
    """
    is_corporate: bool = Field(default=False, description="True si es una institución (ej. ONU)")
    surname: str = Field(..., description="Apellido del autor o nombre completo de la institución")
    initials: Optional[str] = Field(None, description="Iniciales del nombre (solo si no es corporativo)")
    
    model_config = ConfigDict(extra='allow') # Flexibilidad para metadatos extra no previstos

class APADate(BaseModel):
    """
    Manejo flexible de fechas.
    APA 7: (Año) o (Año, Día de Mes) o (s.f.)
    """
    year: str = Field(..., pattern=r"^(1\d{3}|20\d{2}|s\.f\.)$", description="Año de publicación (4 dígitos) o 's.f.'")
    month_day: Optional[str] = Field(None, description="Formato: '2 de mayo' (para periódicos/blogs)")

    model_config = ConfigDict(extra='allow')

class APASource(BaseModel):
    """
    Datos de la fuente de publicación.
    """
    container_title: Optional[str] = Field(None, description="Nombre de la revista, periódico o libro compilador")
    volume: Optional[str] = Field(None, description="Volumen de la revista")
    issue: Optional[str] = Field(None, description="Número de la revista")
    pages: Optional[str] = Field(None, description="Rango de páginas (ej. 100-115)")
    doi_url: Optional[str] = Field(None, description="DOI (https://doi.org/...) o URL directa")
    publisher: Optional[str] = Field(None, description="Editorial (para libros)")

    model_config = ConfigDict(extra='allow')

class APACitationData(BaseModel):
    """
    Esquema Maestro para una referencia bibliográfica APA 7.
    """
    authors: List[APAAuthor] = Field(..., description="Lista de autores")
    date: APADate = Field(..., description="Fecha de publicación")
    title: str = Field(..., description="Título del trabajo (artículo, libro, informe)")
    source: APASource = Field(..., description="Datos de la fuente container")
    type_of_work: str = Field(default="generic", description="book, article, webpage, report")

    model_config = ConfigDict(extra='allow')

    @field_validator('title')
    def capitalize_title(cls, v):
        """Aplica Sentence case (APA): Primera letra mayúscula, resto minúscula (salvo nombres propios, no detectable aquí)."""
        if not v:
            return v
        return v[0].upper() + v[1:] if len(v) > 0 else v

# --- Nuevos Contratos de Datos (Estructura Documental) ---

class DocumentMetadata(BaseModel):
    """Contrato para la página de portada APA 7."""
    title: str = Field(..., min_length=10, description="Título del documento")
    author: str = Field(..., description="Nombre del autor principal")
    institution: str = Field(..., description="Afiliación institucional")
    date: str = Field(default_factory=lambda: datetime.date.today().strftime("%B %d, %Y"), description="Fecha formateada")
    
    model_config = ConfigDict(extra='ignore')

class TableRow(BaseModel):
    cells: List[str]

class TableBlock(BaseModel):
    rows: List[TableRow]
    headers: List[str]

class ParagraphBlock(BaseModel):
    """Contrato para cada unidad de contenido del documento."""
    role: Literal["titulo1", "titulo2", "titulo3", "cuerpo", "cita_larga", "referencia", "lista_item", "tabla"] = Field(..., description="Rol semántico del bloque")
    content: Union[str, TableBlock] = Field(..., description="Texto o estructura de tabla")
    
    model_config = ConfigDict(extra='ignore')

    @field_validator('content')
    @classmethod
    def validate_content_length(cls, v, info):
        # Validación de reglas de negocio dadas por el usuario
        if info.data.get('role') == 'cita_larga':
            # Advertencia lógica: citas largas suelen ser > 40 palabras.
            # No bloqueamos, pero podríamos loguear.
            pass
        return v

class FullDocumentSchema(BaseModel):
    """Contrato final del documento completo."""
    metadata: DocumentMetadata
    content: List[ParagraphBlock]
    references: List[str] = Field(..., description="Lista de referencias bibliográficas ya formateadas o raw")

    model_config = ConfigDict(extra='ignore')
