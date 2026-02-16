# Skill: Exportación, Calidad y Automatización de Guardado

## Misión
Garantizar que las visualizaciones mantengan su impacto y legibilidad fuera del entorno de desarrollo, asegurando alta resolución para reportes, presentaciones y la automatización de flujos de trabajo de exportación.

## 1. Exportación Estática (Matplotlib/Seaborn)
El comando clave es `plt.savefig()`. Para calidad profesional, siempre ajusta el DPI y el encuadre.

```python
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))
# ... código del gráfico ...

# Guardado en Alta Resolución (PNG para web, PDF para impresión)
plt.savefig('grafico_alta_calidad.png', dpi=300, bbox_inches='tight', transparent=True)
plt.savefig('grafico_vectorial.pdf', bbox_inches='tight')
```
*   **dpi=300:** Resolución mínima para impresión.
*   **bbox_inches='tight':** Elimina espacios en blanco innecesarios alrededor del gráfico.

## 2. Interactividad y Botones de Guardado (Plotly)
Plotly permite configurar la "Barra de Modo" (Modebar) para personalizar los botones que ve el usuario final.

```python
import plotly.express as px

fig = px.scatter(df, x="x", y="y")

# Configurar botones de guardado y comportamiento
config = {
  'toImageButtonOptions': {
    'format': 'png', # o 'svg', 'jpeg', 'webp'
    'filename': 'mi_analisis_custom',
    'height': 800,
    'width': 1200,
    'scale': 2 # Multiplica la resolución
  }
}

fig.show(config=config)
```

## 3. Exportación Automática por Script
Para flujos de trabajo masivos, automatiza el guardado usando bucles o funciones.

```python
import os
from datetime import datetime

def guardar_grafico_auto(figURA, nombre_base):
    # Crear carpeta si no existe
    if not os.path.exists('reportes_salida'):
        os.makedirs('reportes_salida')
    
    fecha = datetime.now().strftime("%Y%m%d_%H%M")
    nombre_archivo = f"reportes_salida/{nombre_base}_{fecha}.png"
    
    figURA.savefig(nombre_archivo, dpi=300, bbox_inches='tight')
    print(f"✅ Archivo guardado: {nombre_archivo}")

# Uso:
# fig, ax = plt.subplots()
# ...
# guardar_grafico_auto(fig, "ventas_mensuales")
```

## 4. Exportación a PDF Multipágina
Ideal para reportes completos en un solo archivo.

```python
from matplotlib.backends.backend_pdf import PdfPages

with PdfPages('Reporte_Completo.pdf') as pdf:
    # Gráfico 1
    plt.figure()
    plt.plot([1, 2, 3])
    plt.title('Página 1')
    pdf.savefig()
    plt.close()
    
    # Gráfico 2
    plt.figure()
    plt.bar(['A', 'B'], [5, 10])
    plt.title('Página 2')
    pdf.savefig()
    plt.close()

print("📁 Reporte PDF generado con éxito.")
```

## Resumen de Comandos de Oro
| Formato | Comando | Uso Recomendado |
|---|---|---|
| PNG | `plt.savefig(..., dpi=300)` | Presentaciones y Web |
| PDF | `plt.savefig('archivo.pdf')` | Reportes técnicos |
| SVG | `fig.write_image('img.svg')` | Diseño gráfico (vectorial) |
| HTML | `fig.write_html('dashboard.html')` | Dashboards interactivos |
