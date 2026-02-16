# Skill: Gráfico de Flujo de Árbol (Stream Graph / ThemeRiver)

## Misión
Visualizar la **evolución de múltiples categorías a lo largo del tiempo**. Es una variante del área apilada (stacked area) pero centrada alrededor de un eje central, dando la impresión de un "río" que fluye y cambia de grosor (volumen total) en cada momento.

## Guía de Ejes

### Conceptos Clave
-   **Ancho del Río**: Representa la suma total de valores en ese punto temporal.
-   **Bandas de Color**: Cada banda representa una categoría individual.
-   **Forma Orgánica**: Las curvas suaves facilitan seguir la evolución de una categoría sin los saltos bruscos de las barras apiladas.

### ¿Cuándo usarlo?
-   Popularidad de géneros musicales a través de las décadas.
-   Evolución de palabras clave en noticias (Topic modeling).
-   Distribución de votos en elecciones a lo largo de la campaña.
-   Análisis de sentimientos a lo largo de un libro o película.

---

## Implementación

### 1. Altair (Gramática Declarativa)
Altair es excelente para crear gráficos de area centrados (streamgraphs) de forma elegante.

```python
import altair as alt
import pandas as pd
from vega_datasets import data

# Cargar dataset de ejemplo (Desempleo por industria a través del tiempo)
source = data.unemployment_across_industries.url

alt.Chart(source).mark_area().encode(
    alt.X('yearmonth(date):T',
        axis=alt.Axis(format='%Y', domain=False, tickSize=0)
    ),
    alt.Y('sum(count):Q', stack='center', axis=None), # Stack='center' es la clave
    alt.Color('series:N',
        scale=alt.Scale(scheme='category20b')
    )
).properties(
    width=600,
    height=400,
    title='Desempleo por Sector (ThemeRiver)'
).interactive()
```

### 2. Plotly (Simulación con Stacked Area)
Plotly no tiene un `streamgraph` nativo "perfecto", pero se puede emular usando `stackgroup` y ajustando manualmente los datos para centrarlos, o simplemente usar un Stacked Area normal estilizado.

```python
import plotly.express as px

# Datos: Medallas olímpicas por país y año
df = px.data.medals_long()

fig = px.area(df, x="medal", y="count", color="nation", 
              pattern_shape="nation", pattern_shape_sequence=[".", "x", "+"])
fig.show()
```
*Nota: Para el efecto "río" real en Plotly, se requiere pre-procesamiento complejo de los datos (Wiggle layout) que no es nativo.*

### 3. Matplotlib (Stackplot)
Matplotlib ofrece `stackplot` con opción `baseline='wiggle'` para crear el efecto streamgraph real.

```python
import matplotlib.pyplot as plt
import numpy as np

# Datos simulados
x = range(1, 6)
y = [ [1, 4, 6, 8, 9], [2, 2, 7, 10, 12], [2, 8, 5, 10, 6] ]

# Paleta de colores
pal = ["#9b59b6", "#e74c3c", "#34495e", "#2ecc71"]

# Plot
plt.stackplot(x, y, labels=['A','B','C'], baseline='wiggle', colors=pal, alpha=0.8)

plt.legend(loc='upper left')
plt.title("Stream Graph con Matplotlib")
plt.show()
```

---

## Reglas de Diseño

1.  **Orden de Capas**: Coloca las categorías con mayor variabilidad (picos grandes) en los bordes y las más estables en el centro para facilitar la lectura.
2.  **Etiquetado**: Etiquetar streamgraphs es difícil. Usa etiquetas directas al inicio o final del flujo, o tooltips interactivos.
3.  **Color**: Usa colores contrastantes si las categorías son pocas (<10), o una paleta secuencial si hay un orden implícito.
4.  **No para Precisión**: Si el usuario necesita comparar valores exactos ("¿En 1990 fue 50 o 52?"), usa un gráfico de líneas multivariable. El Stream Graph es para ver *patrones macro* y *flujo*.

## Origen
Skill desarrollada para Nivel 4 (Avanzado Web) cubriendo visualización orgánica de series temporales.
