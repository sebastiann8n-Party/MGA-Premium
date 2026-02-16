import sys
import os
import re

# Ajuste de path para importar módulos hermanos
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from backend.schemas import FullDocumentSchema, DocumentMetadata, ParagraphBlock, TableBlock, TableRow
from software.cites_builder import run_cites_pipeline as run_pipeline # Alias para minimizar cambios

def parse_markdown_to_schema(file_path):
    """
    Lee un archivo de texto/markdown y aplica heurísticas para estructurarlo
    en el esquema APA/MGA definido, incluyendo tablas y listas.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"No se encontró el archivo: {file_path}")

    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    metadata = DocumentMetadata(
        title="APARTADO TÉCNICO - ANEXO MGA",
        author="Equipo de Formulación CITES",
        institution="MinIgualdad - UNGRD",
        date="Febrero 2026"
    )

    content_blocks = []
    regex_h1 = re.compile(r"^\d+\.\s+[A-ZÁÉÍÓÚÑ\s]+$")
    regex_h2 = re.compile(r"^\d+\.\d+\s+.+$")
    
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        if not line:
            i += 1
            continue
            
        # 1. Detección de Tablas de Texto (Específicas de ejemplo1.md)
        if "Componente" in line and "Especificación Técnica" in line:
            headers = ["Componente", "Especificación Técnica", "Cantidad", "Vida Útil", "Costo"]
            i += 1 # Saltar encabezado manual
            rows = []
            # Recolectar filas hasta encontrar "TOTAL"
            while i < len(lines) and "TOTAL" not in lines[i]:
                row_line = lines[i].strip()
                if row_line:
                    # Heurística: cada componente suele ocupar varias líneas en el .md original 
                    # pero aquí lo simplificamos o buscamos patrones
                    # Para ejemplo1.md, parece que cada componente es una línea después de la otra
                    parts = [p.strip() for p in row_line.split("  ") if p.strip()] # Intento de split por doble espacio
                    if len(parts) < 2: # Si no funciona, tomamos la línea como celda 1
                        parts = [row_line, "", "", "", ""]
                    rows.append(TableRow(cells=parts[:5]))
                i += 1
            content_blocks.append(ParagraphBlock(role="tabla", content=TableBlock(headers=headers, rows=rows)))
            continue

        # 2. Detección de Listas Numeradas o con ":" (Procesos Operativos)
        if ":" in line and len(line.split(":")[0].split()) < 5:
            content_blocks.append(ParagraphBlock(role="lista_item", content=line))
            i += 1
            continue

        # 3. Detección de Títulos
        if regex_h1.match(line):
            content_blocks.append(ParagraphBlock(role="titulo1", content=line))
        elif regex_h2.match(line):
            content_blocks.append(ParagraphBlock(role="titulo2", content=line))
        else:
            # Cuerpo normal
            content_blocks.append(ParagraphBlock(role="cuerpo", content=line))
        
        i += 1

    references = [
        "Departamento Nacional de Planeación. (2013). Resolución 1450 de 2013.",
        "DNP. (2024). Guía para la Formulación de Proyectos de Inversión Pública MGA."
    ]

    return FullDocumentSchema(
        metadata=metadata,
        content=content_blocks,
        references=references
    )

def generar_documento_real():
    input_file = r"x:\skills-analista\contexto\Producto_1_Premium\ejemplo1.md"
    output_path = os.path.join(os.path.dirname(__file__), "..", "salida", "Anexo_Tecnico_MGA.docx")
    
    print(f"Leyendo origen: {input_file}")
    
    try:
        document_data = parse_markdown_to_schema(input_file)
        print("Parsing exitoso. Esquema validado.")
        
        run_pipeline(document_data, output_path)
        print(f"Documento final generado: {os.path.abspath(output_path)}")
        
    except Exception as e:
        print(f"Error en generacion: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    generar_documento_real()
