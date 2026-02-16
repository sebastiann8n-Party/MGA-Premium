from dataclasses import dataclass
from typing import List, Optional
from .apa_citas import Autor

@dataclass
class ReferenciaBase:
    autores: List[Autor]
    anio: str
    titulo: str
    
    def formatear_autores(self) -> str:
        n = len(self.autores)
        nombres = [f"{a.apellido}, {a.iniciales}" for a in self.autores]
        
        if n == 1:
            return nombres[0]
        elif n <= 20:
            return f"{', '.join(nombres[:-1])} & {nombres[-1]}"
        else:
            # APA 7: Listar primeros 19 ... último autor
            return f"{', '.join(nombres[:19])} ... {nombres[-1]}"

class ReferenciaLibro(ReferenciaBase):
    editorial: str
    
    def generar(self) -> str:
        """Genera referencia de libro: Autor. (Año). *Título*. Editorial."""
        autores = self.formatear_autores()
        return f"{autores} ({self.anio}). *{self.titulo}*. {self.editorial}."

class ReferenciaWeb(ReferenciaBase):
    sitio_web: str
    url: str
    
    def generar(self) -> str:
        """Genera referencia web: Autor. (Año). *Título*. Sitio Web. URL."""
        autores = self.formatear_autores()
        return f"{autores} ({self.anio}). *{self.titulo}*. {self.sitio_web}. {self.url}"

class ReferenciaArticulo(ReferenciaBase):
    revista: str
    volumen: str
    numero: Optional[str]
    paginas: str
    doi: Optional[str] = None
    
    def generar(self) -> str:
        """Genera referencia artículo: Autor. (Año). Título. *Revista*, *Vol*(Num), págs."""
        autores = self.formatear_autores()
        base = f"{autores} ({self.anio}). {self.titulo}. *{self.revista}*, *{self.volumen}*"
        
        if self.numero:
            base += f"({self.numero})"
            
        base += f", {self.paginas}."
        
        if self.doi:
            base += f" https://doi.org/{self.doi}"
            
        return base
