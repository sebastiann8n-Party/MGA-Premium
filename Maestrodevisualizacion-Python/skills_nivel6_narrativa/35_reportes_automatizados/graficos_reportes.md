# Skill: Reportes Automatizados (PDF/HTML)

## Misión
Automatizar la **entrega de valor** generando documentos estáticos (PDF) o interactivos (HTML) procesables, sin tener que copiar y pegar gráficos en Word/PPT. Desde un análisis de un script, crear un entregable final profesional.

## Guía de Ejes

### Conceptos Clave
-   **Reproducibilidad**: Cualquier usuario debe poder ejecutar el código y obtener el mismo reporte actualizado con nuevos datos.
-   **Markdown**: Usar texto enriquecido (títulos, negritas, listas) junto con el código.
-   **Estructura**: Introducción -> Resumen Ejecutivo -> Detalles Técnicos -> Conclusiones.

### Herramientas
-   **Jupyter Notebook -> PDF/HTML**: La forma más rápida.
-   **Streamlit**: Para dashboards web vivos.
-   **Datapane / Sweetviz / Pandas Profiling**: Para reportes automáticos de EDA.
-   **FPDF / ReportLab**: Para control pixel-perfecto en PDF (complejo, pero profesional).

---

## Implementación

### 1. Pandas Profiling (EDA Automático)
Genera un reporte HTML completo con una línea de código.

```python
import pandas as pd
from ydata_profiling import ProfileReport

df = pd.read_csv("datos_cliente.csv")
profile = ProfileReport(df, title="Reporte de Calidad de Datos")
profile.to_file("reporte_calidad.html")
```

### 2. Jupyter a HTML (Sin Código Visible)
Usar `nbconvert` para exportar el notebook ocultando las celdas de código, dejando solo el texto y los gráficos.

```bash
jupyter nbconvert --to html --no-input --TemplateExporter.exclude_input=True analisis.ipynb
```

### 3. FPDF (Generación de PDF Personalizado)
Para facturas, certificados o reportes corporativos estrictos.

```python
from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 15)
        self.cell(80)
        self.cell(30, 10, 'Reporte Mensual de Ventas', 0, 0, 'C')
        self.ln(20)

pdf = PDF()
pdf.add_page()
pdf.set_font('Arial', '', 12)
pdf.cell(200, 10, txt="Resumen: Las ventas aumentaron un 15% este mes.", ln=1, align='L')
pdf.image('grafico_ventas.png', x=10, y=40, w=100) # Imagen guardada previamente con matplotlib
pdf.output("reporte_mensual.pdf")
```

---

## Reglas de Diseño
1.  **Marca (Branding)**: Incluye siempre el logo de la empresa y los colores corporativos.
2.  **Fechas**: Todo reporte debe tener fecha de generación y rango de fechas de los datos.
3.  **Resumen Ejecutivo**: La primera página debe contener los KPIs más importantes. Nadie lee la página 50 si la 1 no convence.

## Origen
Skill basada en Nivel 6 (Narrativa) enfocada en la automatización de entregables.
