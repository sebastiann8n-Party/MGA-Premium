# Skill: Gráfico de Dispersión Avanzado (Scatter & Categorical Plots)

## Misión
Visualizar la **relación** entre dos variables para detectar correlaciones, clusters o patrones de distribución. Esta skill cubre tanto la comparación **Numérica vs Numérica** (Scatter clásico) como **Numérica vs Categórica** (Catplot/Strip/Swarm), integrando múltiples dimensiones adicionales mediante color, tamaño y forma.

## Guía de Ejes

### Scatter Plot Clásico (Numérico vs Numérico)
- **Eje X (Numérico)**: Variable independiente o explicativa (ej: Inversión en Marketing).
- **Eje Y (Numérico)**: Variable dependiente o respuesta (ej: Ventas Generadas).
- **Dimensiones Adicionales**:
  - **Color (Hue)**: Tercera variable (categórica o numérica) para agrupar puntos.
  - **Tamaño (Size)**: Cuarta variable (numérica) para ponderar la importancia del punto (Bubble Chart).
  - **Símbolo (Style)**: Variable categórica para distinguir grupos con formas.

### Scatter Categórico (Numérico vs Categórico)
Cuando uno de los ejes es **categórico**, el scatter plot tradicional falla (todos los puntos se solapan en una línea). Para esto usamos variantes avanzadas:
- **Jitter (Ruido)**: Desplaza aleatoriamente los puntos para evitar solapamiento (`stripplot`).
- **Swarm (Enjambre)**: Organiza los puntos para que no se toquen, mostrando la distribución real (`swarmplot`).

### ¿Cuándo usar cuál?
| Objetivo | Tipo de Gráfico | Ejes (X vs Y) |
|---|---|---|
| Correlación entre dos métricas | Scatter Plot | Num vs Num |
| Comparar distribución entre grupos | Strip/Swarm Plot | Cat vs Num |
| Detectar outliers multivariados | Scatter + Color/Size | Num vs Num (+ dims) |

## Reglas de Diseño

1. **Evitar Overplotting**: Si hay demasiados puntos, usa transparencia (`alpha` en Matplotlib/Seaborn, `opacity` en Plotly) o reduce el tamaño del marcador.
2. **Escalas**: Si las variables tienen rangos muy distintos (ej: edad vs salario), las escalas logarítmicas en los ejes pueden revelar patrones ocultos.
3. **Leyenda clara**: Si usas color o tamaño, la leyenda es obligatoria.
4. **Relación de aspecto**: Intenta que el gráfico tienda al cuadrado si ambas variables tienen la misma unidad, para facilitar la comparación de pendientes (45 grados).

## Implementación

### 1. Preparación de Datos
```python
import pandas as pd
import seaborn as sns
import plotly.express as px
import matplotlib.pyplot as plt

# Cargar datos (ejemplo: dataset pingüinos)
df = pd.read_csv('../data/pinguinos.csv').dropna()
```

### 2. Scatter Plot Interactivo (Plotly)
Ideal para exploración, permite tooltips y zoom. Soporta hasta 5 dimensiones (X, Y, Color, Tamaño, Símbolo).

```python
# Gráfico Numérico vs Numérico (con 4 dimensiones)
fig = px.scatter(
    df, 
    x='flipper_length_mm',    # Dimensión 1: X (Num)
    y='culmen_length_mm',     # Dimensión 2: Y (Num)
    color='species',          # Dimensión 3: Color (Cat)
    size='body_mass_g',       # Dimensión 4: Tamaño (Num) -> Bubble Chart
    symbol='sex',             # Dimensión 5: Forma (Cat)
    hover_name='island',      # Tooltip extra
    title='Análisis Multidimensional: Pico vs Aleta (Tam: Masa, Col: Especie)'
)
fig.show()
```

### 3. Scatter Plot Categórico (Seaborn)
Ideal para publicaciones estáticas y análisis estadístico. `catplot` es la interfaz general.

#### Jitter Plot (`stripplot`)
Añade ruido aleatorio para ver la densidad.
```python
sns.catplot(
    data=df,
    x="flipper_length_mm",  # Numérico
    y="species",            # Categórico
    hue="sex",              # Sub-agrupación por color
    kind="strip",           # Tipo de gráfico
    alpha=0.6,              # Transparencia
    height=6, aspect=1.5
)
plt.title("Distribución de Largo de Aleta por Especie (Strip Plot)")
plt.show()
```

#### Swarm Plot (`swarmplot`)
"Enjambre" de puntos que no se solapan. Mejor para ver la distribución exacta (si no hay demasiados datos).
```python
sns.catplot(
    data=df,
    x="flipper_length_mm",
    y="species",
    kind="swarm",           # Tipo: Enjambre
    hue="island",
    height=6, aspect=1.5
)
plt.title("Distribución Detallada por Especie (Swarm Plot)")
plt.show()
```

### 4. Pandas Nativo (Rápido)
Para revisiones rápidas sin formateo complejo.
```python
# Básico
df.plot.scatter(x='flipper_length_mm', y='culmen_length_mm', c='green', alpha=0.5)

# Con mapa de color numérico
df.plot.scatter(
    x='flipper_length_mm', 
    y='culmen_length_mm', 
    c='body_mass_g',        # Variable numérica como color
    colormap='viridis'
)
plt.show()
```

## Mejores Prácticas

1.  **Matrices de Dispersión (Pairplot)**: Cuando tienes muchas variables numéricas, usa `sns.pairplot(df, hue='species')` para ver todos los scatter plots posibles en una cuadrícula. Esto es el paso previo ideal antes de profundizar en un scatter específico.
2.  **Líneas de Tendencia**: En Plotly, añade `trendline="ols"` dentro de `px.scatter` para ver la regresión lineal automáticamente.
3.  **Anotaciones**: Si hay puntos atípicos (outliers) interesantes, etiquétalos manualmente o usa text en Plotly.

## Tabla Resumen de Comandos

| Tipo | Librería | Comando |
|---|---|---|
| Scatter Interactivo | Plotly | `px.scatter(df, x=..., y=..., color=..., size=...)` |
| Scatter con Tendencia | Plotly | `px.scatter(..., trendline="ols")` |
| Strip Plot (Jitter) | Seaborn | `sns.catplot(..., kind="strip")` |
| Swarm Plot (Enjambre) | Seaborn | `sns.catplot(..., kind="swarm")` |
| Pairplot (Matriz) | Seaborn | `sns.pairplot(df, hue='cat_var')` |
| Scatter Rápido | Pandas | `df.plot.scatter(x=..., y=...)` |

## Origen
Código analizado y extraído de: `contexto/nivel2/graficoscaterplot.ipynb`
