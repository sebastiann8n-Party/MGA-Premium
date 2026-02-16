import sys
import os
import re
import argparse
import traceback

# Ajuste de path para importar módulos hermanos
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from backend.schemas import FullDocumentSchema, DocumentMetadata, ParagraphBlock, TableBlock, TableRow
from software.cites_builder import run_cites_pipeline

def parse_markdown_generic(file_path):
    """
    Parser robusto para Markdown Estándar (GFM) y extensiones específicas MGA.
    Soporta:
    - Headers (#, ##, 1. Título)
    - Listas (-, *)
    - Tablas GFM (| col | col |)
    - Bloques de texto
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"No se encontró el archivo: {file_path}")

    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    # Metadatos por defecto (podrían extraerse de YAML frontmatter si existiera)
    metadata = DocumentMetadata(
        title="DOCUMENTO TÉCNICO GENERADO",
        author="Google Antigravity Engine",
        institution="Proyecto CITES - MGA",
        date="Febrero 2026"
    )

    content_blocks = []
    
    # Regex Patterns
    regex_h1_num = re.compile(r"^\d+\.\s+[A-ZÁÉÍÓÚÑ\s]+$") # 1. TITULO
    regex_h1_md = re.compile(r"^#\s+(.+)$") # # Título
    regex_h2_num = re.compile(r"^\d+\.\d+\s+.+$") # 1.1 Subtítulo
    regex_h2_md = re.compile(r"^##\s+(.+)$") # ## Subtítulo
    
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        if not line:
            i += 1
            continue
            
        # --- 1. DETECCIÓN DE TABLAS (GFM Standard) ---
        # Heurística: Línea empieza con pipe, y la siguiente es separador |---|
        if line.startswith("|"):
            # Verificar si es una tabla válida (mínimo header + separador)
            if i + 1 < len(lines) and set(lines[i+1].strip()) <= set("|-: "):
                 # Es una tabla!
                 headers = [c.strip() for c in line.split("|") if c.strip()]
                 i += 2 # Saltar header y separador
                 
                 rows = []
                 while i < len(lines) and lines[i].strip().startswith("|"):
                     row_cells = [c.strip() for c in lines[i].split("|") if c.strip()]
                     if row_cells:
                         # Rellenar celdas faltantes si la fila es más corta que el header
                         while len(row_cells) < len(headers):
                             row_cells.append("")
                         rows.append(TableRow(cells=row_cells[:len(headers)]))
                     i += 1
                 
                 content_blocks.append(ParagraphBlock(
                     role="tabla", 
                     content=TableBlock(headers=headers, rows=rows)
                 ))
                 continue
        
        # --- 2. DETECCIÓN DE TABLAS "TEXTO" (Legacy/Heurística MGA) ---
        # Mantiene compatibilidad con formatos no estándar tipo "Componente  Especificación"
        if "Componente" in line and "Especificación Técnica" in line and not line.startswith("|"):
             headers = ["Componente", "Especificación Técnica", "Cantidad", "Vida Útil", "Costo"]
             i += 1
             rows = []
             while i < len(lines) and "TOTAL" not in lines[i] and not lines[i].strip().startswith("#"):
                 row_line = lines[i].strip()
                 if row_line:
                     parts = [p.strip() for p in row_line.split("  ") if p.strip()]
                     # Padding simple
                     while len(parts) < 5: parts.append("")
                     rows.append(TableRow(cells=parts[:5]))
                 i += 1
             content_blocks.append(ParagraphBlock(role="tabla", content=TableBlock(headers=headers, rows=rows)))
             continue

        # --- 3. LISTAS ---
        if line.startswith("- ") or line.startswith("* "):
            content_blocks.append(ParagraphBlock(role="lista_item", content=line[2:].strip()))
            i += 1
            continue

        # --- 4. TÍTULOS ---
        match_h1_md = regex_h1_md.match(line)
        match_h1_num = regex_h1_num.match(line)
        
        if match_h1_md:
            content_blocks.append(ParagraphBlock(role="titulo1", content=match_h1_md.group(1)))
        elif match_h1_num:
             # Limpiar "1. " si ya viene
             content = line
             if "." in line[:5]: content = line.split(".", 1)[1].strip()
             content_blocks.append(ParagraphBlock(role="titulo1", content=content))
        elif regex_h2_num.match(line):
             content = line
             if "." in line[:5]: content = line.split(" ", 1)[1].strip()
             content_blocks.append(ParagraphBlock(role="titulo2", content=content))
        elif regex_h2_md.match(line):
            content_blocks.append(ParagraphBlock(role="titulo2", content=regex_h2_md.group(1)))
        else:
            # Texto Normal / Key-Value
            content_blocks.append(ParagraphBlock(role="cuerpo", content=line))
        
        i += 1

    # Referencias Placeholder (Mejora: extraer de sección "Referencias" si existe)
    references = ["Documento generado automáticamente por CITES Engine Local."]

    return FullDocumentSchema(
        metadata=metadata,
        content=content_blocks,
        references=references
    )

def main():
    parser = argparse.ArgumentParser(description="Motor de Generación de Documentos CITES/MGA Local")
    parser.add_argument("input", help="Ruta del archivo Markdown (.md) de entrada")
    parser.add_argument("--output", "-o", help="Ruta del archivo DOCX de salida (opcional)")
    
    args = parser.parse_args()
    
    input_path = os.path.abspath(args.input)
    if not os.path.exists(input_path):
        print(f"Error: No se encuentra el archivo de entrada: {input_path}")
        return

    # Determinación de Output
    if args.output:
        output_path = os.path.abspath(args.output)
    else:
        # Default: misma carpeta, extensión .docx
        base_name = os.path.splitext(input_path)[0]
        output_path = f"{base_name}_MGA.docx"

    print(f"--- INICIANDO MOTOR LOCAL CITES ---")
    print(f"Entrada: {input_path}")
    print(f"Salida:  {output_path}")
    
    try:
        data = parse_markdown_generic(input_path)
        run_cites_pipeline(data, output_path)
        print(f"Proceso finalizado con exito.")
    except Exception as e:
        print(f"Error critico en ejecucion: {e}")
        traceback.print_exc()

if __name__ == "__main__":
    main()
