# Skill: Gráfico Conjunto (Joint Plot)

## Misión
Fusionar dos visiones en una: la **relación** entre dos variables (Scatter Plot) y la **distribución** individual de cada una (Histograma/KDE). Permite entender no solo *cómo se relacionan* las variables, sino *cómo se concentran* los datos en cada dimensión.

## Guía de Ejes

### Estructura de Ejes (Crucial)
Al igual que el Scatter Plot, este gráfico compara dos magnitudes continuas.

-   **Eje X (Variable 1)**: Variable **NUMÉRICA CONTINUA**. Muestra su dispersión horizontal y su distribución en el margen superior.
-   **Eje Y (Variable 2)**: Variable **NUMÉRICA CONTINUA**. Muestra su dispersión vertical y su distribución en el margen derecho.
-   **Márgenes**: Son los "bordes" del gráfico donde se proyecta la densidad de los datos de cada eje por separado.

### ¿Cuándo usarlo?
- Cuando un Scatter Plot simple esconde la densidad de puntos (overplotting).
- Para detectar si una correlación se debe a la distribución de los datos (ej: bimodalidad).
- Para reportes compactos donde el espacio es limitado y quieres mostrar distribución + relación.

## Implementación

### 1. Seaborn (`jointplot`) — El Estándar
Es la herramienta más directa para generar este gráfico compuesto.

```python
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('../data/pinguinos.csv').dropna()

# Gráfico Básico: Scatter + Histogramas
sns.jointplot(
    data=df,
    x='flipper_length_mm',
    y='culmen_length_mm',
    height=7,
    ratio=5,       # Proporción centro vs márgenes
    color="#4CB391"
)
plt.show()
```

### 2. Variaciones de Estilo (`kind`)
Seaborn permite cambiar la representación central y marginal.

*   `kind="reg"`: Añade regresión lineal y KDE.
*   `kind="hex"`: Hexbin plot (bueno para muchos datos).
*   `kind="kde"`: Curvas de nivel (densidad 2D).

```python
# Estilo Hexbin (Panales) - Ideal para datasets grandes
sns.jointplot(
    data=df,
    x='flipper_length_mm',
    y='culmen_length_mm',
    kind="hex",
    color="#E74C3C"
)
```

### 3. Diferenciación por Grupos (Hue)
Si añades una variable categórica, tanto el scatter como las densidades marginales se separan por color.

```python
# Scatter + KDE marginal por Especie
sns.jointplot(
    data=df,
    x='flipper_length_mm',
    y='culmen_length_mm',
    hue='species',
    palette='viridis'
)
```

### 4. Plotly (Interactivo)
Plotly permite añadir gráficos marginales a un scatter normal.

```python
import plotly.express as px

fig = px.scatter(
    df,
    x="flipper_length_mm",
    y="culmen_length_mm",
    color="species",
    marginal_x="box",     # Margen superior: Boxplot
    marginal_y="violin",  # Margen derecho: Violin Plot
    title="Análisis Conjunto: Distribución y Relación"
)
fig.show()
```

## Reglas de Diseño

1.  **No saturar**: Este gráfico ya es complejo visualmente. Evita añadir demasiados elementos extra (como muchas categorías en `hue`).
2.  **Consistencia**: Asegura que el tipo de gráfico marginal (histograma, boxplot, kde) tenga sentido para la cantidad de datos.
    -   *Pocos datos* → Boxplot o Rug plot.
    -   *Muchos datos* → Histograma o KDE.
3.  **Proporción**: El gráfico central es el protagonista. Los márgenes son contexto. Mantén una relación de tamaño adecuada (ratio 5:1 es buen default en Seaborn).

## Origen
Código analizado y extraído de: `contexto/nivel2/join.ipynb`
