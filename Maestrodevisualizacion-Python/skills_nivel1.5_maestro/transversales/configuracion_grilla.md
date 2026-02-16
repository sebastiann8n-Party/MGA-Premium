# Skill Transversal: Configuración de Grilla (Subplots)

## Misión
Crear composiciones de múltiples gráficos en una sola figura (Canvas), organizándolos en filas y columnas. Esto permite comparar diferentes visualizaciones o variables de un vistazo.

## Imagen de Referencia
El objetivo es lograr una disposición tipo matriz (ej. 2x2) con un título general y títulos individuales para cada sub-gráfico.

## 1. Matplotlib (La Base)
Matplotlib ofrece el control más granular y es la base utilizada también por Seaborn para layouts personalizados.

### Método: `plt.subplots()`
Es la forma más moderna y recomendada de crear grillas.

```python
import matplotlib.pyplot as plt
import numpy as np

# Generar datos de ejemplo
x = np.linspace(0, 10, 100)
y = np.sin(x)

# 1. Crear la figura y la matriz de ejes (2 filas, 2 columnas)
# figsize define el tamaño TOTAL de la figura
fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(12, 10))

# 'axes' es una matriz numpy de objetos Axes.
# Podemos acceder a ellos por índices: axes[0,0], axes[0,1], etc.
# O aplanarlos para iterar: axes.flatten()

# GRÁFICO 1 (Arriba-Izquierda)
axes[0, 0].plot(x, y, color='blue')
axes[0, 0].set_title("Plot 1 - Line")

# GRÁFICO 2 (Arriba-Derecha)
axes[0, 1].scatter(x, y + np.random.normal(0, 0.2, 100), color='green', alpha=0.6)
axes[0, 1].set_title("Plot 2 - Scatter")

# GRÁFICO 3 (Abajo-Izquierda)
axes[1, 0].bar(['A', 'B', 'C'], [10, 20, 15], color='orange')
axes[1, 0].set_title("Plot 3 - Bar")

# GRÁFICO 4 (Abajo-Derecha)
axes[1, 1].hist(np.random.normal(0, 1, 1000), bins=30, color='purple')
axes[1, 1].set_title("Plot 4 - Hist")

# 2. Título General (Suptitle)
fig.suptitle("Grilla de Gráficos (Subplots) con Matplotlib", fontsize=16, fontweight='bold')

# 3. Ajuste Automático (Tight Layout)
# Evita que las etiquetas y títulos se superpongan
plt.tight_layout()

# Opcional: Ajustar espacio superior para el título general
plt.subplots_adjust(top=0.92)

plt.show()
```

## 2. Seaborn (Integración)
Seaborn tiene dos formas de manejar grillas:
1.  **Grillas de Datos (`FacetGrid`, `PairGrid`):** Para cuando quieres separar **el mismo tipo de gráfico** por una variable categórica.
2.  **Grillas Personalizadas (Subplots):** Para mezclar **diferentes tipos de gráficos** (como en la imagen). Usamos `plt.subplots` y pasamos el eje con `ax=`.

### Método: Grilla Personalizada (Mezcla de tipos)

```python
import seaborn as sns
import matplotlib.pyplot as plt

# Datos de ejemplo (Dataset Titanic)
df = sns.load_dataset('titanic')

# Crear canvas vacio 2x2
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# Usar el parámetro 'ax' para decirle a Seaborn dónde dibujar

# Gráfico 1: Barras
sns.barplot(data=df, x='class', y='fare', ax=axes[0, 0], palette='viridis')
axes[0, 0].set_title("Tarifa Promedio por Clase")

# Gráfico 2: Histograma (KDE)
sns.histplot(data=df, x='age', kde=True, ax=axes[0, 1], color='salmon')
axes[0, 1].set_title("Distribución de Edad")

# Gráfico 3: Boxplot
sns.boxplot(data=df, x='alive', y='age', ax=axes[1, 0], palette='Set2')
axes[1, 0].set_title("Edad vs Supervivencia")

# Gráfico 4: Scatter (Relplot no soporta 'ax', usamos scatterplot)
sns.scatterplot(data=df, x='age', y='fare', hue='survived', ax=axes[1, 1])
axes[1, 1].set_title("Edad vs Tarifa")

fig.suptitle("Resumen del Titanic con Seaborn", fontsize=16)
plt.tight_layout()
plt.show()
```

## 3. Plotly (Interactivo)
Plotly tiene su propia librería para subplots dentro de `plotly.subplots`. A diferencia de Matplotlib, se agregan "Trazas" (Traces) a filas y columnas específicas.

### Método: `make_subplots()`

```python
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np

# Datos
x = np.linspace(0, 10, 100)

# 1. Crear la figura con subplots
fig = make_subplots(
    rows=2, cols=2,
    subplot_titles=("Plot 1 - Line", "Plot 2 - Scatter", "Plot 3 - Bar", "Plot 4 - Hist"),
    # Opcional: Tipos de especificaciones si mezclamos 3D o mapas
    # specs=[[{"type": "xy"}, {"type": "xy"}], [{"type": "xy"}, {"type": "xy"}]]
)

# 2. Agregar Trazas indicando fila y columna (row, col)

# Arriba-Izquierda
fig.add_trace(go.Scatter(x=x, y=np.sin(x), mode='lines', name='Seno'), row=1, col=1)

# Arriba-Derecha
fig.add_trace(go.Scatter(x=x, y=np.sin(x) + np.random.normal(0, 0.2, 100), mode='markers', name='Ruido'), row=1, col=2)

# Abajo-Izquierda
fig.add_trace(go.Bar(x=['A', 'B', 'C'], y=[10, 20, 15], name='Categorías'), row=2, col=1)

# Abajo-Derecha
fig.add_trace(go.Histogram(x=np.random.normal(0, 1, 500), name='Dist'), row=2, col=2)

# 3. Actualizar Layout Global
fig.update_layout(
    height=700, 
    width=900, 
    title_text="Grilla Interactiva con Plotly",
    showlegend=False  # Ocultar leyenda si satura
)

fig.show()
```

## Comparativa y Consejos
| Característica | Matplotlib/Seaborn | Plotly |
|---|---|---|
| **Estructura** | `plt.subplots(filas, cols)` | `make_subplots(rows=..., cols=...)` |
| **Ubicación** | `axes[fila, col].plot(...)` | `fig.add_trace(..., row=f, col=c)` |
| **Tamaño** | `figsize=(ancho, alto)` en pulgadas | `height=px, width=px` en píxeles |
| **Títulos** | `ax.set_title()` (individual), `fig.suptitle()` (global) | `subplot_titles=(...)` (lista), `title_text` (global) |
| **Complejidad** | Media. Control manual total. | Alta (si mezclas tipos). Muy potente. |

### Consejos de Diseño
1.  **Consistencia:** Intenta que los gráficos compartan escalas en los ejes si muestran datos comparables (`sharex=True`, `sharey=True` en `plt.subplots`).
2.  **Espaciado:** Siempre usa `plt.tight_layout()` en Matplotlib para evitar textos montados.
3.  **No Abusar:** Más de 2x3 o 3x3 gráficos suelen ser ilegibles en una pantalla normal.
