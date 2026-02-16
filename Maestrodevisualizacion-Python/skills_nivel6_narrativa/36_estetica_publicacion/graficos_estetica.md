# Skill: Estética de Publicación (Diseño Gráfico de Datos)

## Misión
Asegurar que las visualizaciones cumplan con **estándares de publicación** (académicos, de prensa o marketing). Requiere atención al detalle en tipografía, colores accesibles (colorblind-safe) y formatos de exportación de alta calidad (vectorial SVG).

## Guía de Ejes

### Conceptos Clave
-   **Accesibilidad (Accessibility)**: Probar las paletas de color para daltónicos. Asegurarse que el texto tenga suficiente contraste.
-   **Resolución (DPI)**: Para impresión (PDF, Papel) usar 300 DPI. Para pantalla (Web, PPT) 72-96 DPI.
-   **Vectorial (SVG/PDF)**: Los gráficos deben ser infinitamente escalables sin perder calidad (a diferencia de PNG/JPG).
-   **Tipografía (Fonts)**: Usar fuentes sans-serif modernas (Roboto, Lato, Inter) para datos. Serif solo para títulos largos.

---

## Implementación

### 1. Paletas Accesibles (Seaborn / Matplotlib)
Usar paletas predefinidas como 'colorblind' o diseñar propias con herramientas como HCL Wizard.

```python
import matplotlib.pyplot as plt
import seaborn as sns

# Configuración Global de Estilo
sns.set_style("whitegrid")
sns.set_context("talk") # Escala para presentaciones (letras grandes)
sns.set_palette("colorblind") # Paleta segura

# Definir fuente personalizada (requiere tenerla instalada)
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = ['Roboto', 'Arial']

# Gráfico
plt.figure(figsize=(8, 6), dpi=300) # Alta Resolución
plt.plot([1, 2, 3], [4, 5, 6], label="Serie A")
plt.xlabel("Eje X (unidades)", fontweight='bold')
plt.title("Título Profesional", pad=20)
plt.legend(frameon=False) # Leyenda limpia

# Guardar en Vectorial
plt.savefig("grafico_alta_calidad.svg", format='svg', bbox_inches='tight')
plt.savefig("grafico_impresion.pdf", format='pdf', bbox_inches='tight')
```

### 2. Plotly (Templates y Branding)
Crear un tema corporativo reutilizable.

```python
import plotly.io as pio
import plotly.graph_objects as go

# Definir Template Corporativo
pio.templates["mi_empresa"] = go.layout.Template(
    layout=go.Layout(
        font=dict(family="Lato", size=14),
        title_font=dict(family="Lato", size=24, color="#333"),
        colorway=['#003f5c', '#58508d', '#bc5090', '#ff6361', '#ffa600'], # Paleta
        plot_bgcolor="white",
        paper_bgcolor="white",
        xaxis=dict(showgrid=True, gridcolor='lightgrey'),
        yaxis=dict(showgrid=True, gridcolor='lightgrey')
    )
)
pio.templates.default = "mi_empresa"
```

---

## Reglas de Diseño
1.  **Espacio en Blanco (White Space)**: Deja respirar al grafico. Aumenta los márgenes.
2.  **Alineación**: Títulos alineados a la izquierda (como se lee en occidente). Leyendas cerca de los datos.
3.  **Consistencia**: Si usas Roboto en un gráfico, úsala en todos.

## Origen
Skill basada en Nivel 6 (Narrativa) enfocada en calidad visual y estándares de publicación.
