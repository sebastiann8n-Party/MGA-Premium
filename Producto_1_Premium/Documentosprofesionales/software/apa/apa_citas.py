from dataclasses import dataclass
from typing import List, Optional

@dataclass
class Autor:
    apellido: str
    iniciales: str  # Ejemplo: "A. B."

@dataclass
class Cita:
    autores: List[Autor]
    anio: str
    texto_cita: Optional[str] = None
    pagina: Optional[str] = None

class ApaCitas:
    """
    Generador de citas narrativas y parentéticas según Normas APA 7ma Edición.
    """

    @staticmethod
    def _formatear_autores(autores: List[Autor], tipo: str = "parentetica") -> str:
        """Formatea la lista de autores según el tipo de cita."""
        n = len(autores)
        nombres = [a.apellido for a in autores]

        if n == 1:
            return nombres[0]
        elif n == 2:
            conector = " y " if tipo == "narrativa" else " & "
            return f"{nombres[0]}{conector}{nombres[1]}"
        else:
            # 3 o más autores: Apellido del primero + et al.
            return f"{nombres[0]} et al."

    @staticmethod
    def generar_parentetica(cita: Cita) -> str:
        """
        Ejemplo: (Sánchez, 2026) o (Sánchez & Pérez, 2026, p. 12)
        """
        texto_autores = ApaCitas._formatear_autores(cita.autores, "parentetica")
        base = f"({texto_autores}, {cita.anio}"
        
        if cita.pagina:
            base += f", p. {cita.pagina}"
        
        return base + ")"

    @staticmethod
    def generar_narrativa(cita: Cita) -> str:
        """
        Ejemplo: Sánchez (2026) afirma...
        """
        texto_autores = ApaCitas._formatear_autores(cita.autores, "narrativa")
        base = f"{texto_autores} ({cita.anio})"
        
        return base
