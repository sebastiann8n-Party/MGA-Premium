from docx.enum.style import WD_STYLE_TYPE
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_LINE_SPACING
from docx.shared import Pt, Inches, RGBColor

class APAStyler:
    """
    Gestor de estilos APA 7 para documentos .docx.
    Define fuentes, márgenes y espaciados programáticamente.
    """

    @staticmethod
    def apply_document_settings(document):
        """Configuración global del documento (Márgenes, Fuente base)."""
        section = document.sections[0]
        # Configuración de márgenes (MGA: T 1.0, B 1.0, L 1.25, R 1.25)
        section.top_margin = Inches(1)
        section.bottom_margin = Inches(1)
        section.left_margin = Inches(1.25)
        section.right_margin = Inches(1.25)

        # Configuración de estilos base (Normal)
        style = document.styles['Normal']
        font = style.font
        font.name = 'Times New Roman'
        font.size = Pt(12)
        
        # Párrafo base: Alineación izquierda (no justificada en APA 7 estudiante), interlineado doble
        paragraph_format = style.paragraph_format
        paragraph_format.alignment = WD_ALIGN_PARAGRAPH.LEFT
        paragraph_format.line_spacing = 2.0
        paragraph_format.space_after = Pt(0) # Sin espacio extra entre párrafos

    @staticmethod
    def create_custom_styles(document):
        """Crea o actualiza estilos específicos para la estructura APA."""
        
        # 1. Título Nivel 1 (Centrado, Negrita)
        styles = document.styles
        if 'APA Heading 1' not in styles:
            h1 = styles.add_style('APA Heading 1', WD_STYLE_TYPE.PARAGRAPH)
            h1.base_style = styles['Normal']
            h1.font.bold = True
            h1.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
        
        # 2. Título Nivel 2 (Izquierda, Negrita)
        if 'APA Heading 2' not in styles:
            h2 = styles.add_style('APA Heading 2', WD_STYLE_TYPE.PARAGRAPH)
            h2.base_style = styles['Normal']
            h2.font.bold = True
            h2.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.LEFT

        # 3. Cita Larga (Sangría 0.5 pulgada todo el bloque)
        if 'APA Block Quote' not in styles:
            bq = styles.add_style('APA Block Quote', WD_STYLE_TYPE.PARAGRAPH)
            bq.base_style = styles['Normal']
            bq.paragraph_format.left_indent = Inches(0.5)

        # 4. Referencias (Sangría francesa 0.5 pulgada)
        if 'APA Reference' not in styles:
            ref = styles.add_style('APA Reference', WD_STYLE_TYPE.PARAGRAPH)
            ref.base_style = styles['Normal']
            ref.paragraph_format.left_indent = Inches(0.5)
            ref.paragraph_format.first_line_indent = Inches(-0.5) # Truco de sangría francesa
