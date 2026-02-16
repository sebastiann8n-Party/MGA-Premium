# Skill: Gráfico de Regresión Lineal

## Misión
Visualizar la tendencia y fuerza de la relación entre dos variables numéricas añadiendo un modelo predictivo visual. Permite responder: *"Si X aumenta, ¿cuánto esperamos que cambie Y?"*

## Guía de Ejes

### Estructura de Ejes (Crucial)

Para que una regresión lineal tenga sentido matemático y visual:

-   **Eje X (Variable Independiente)**: Debe ser **NUMÉRICA CONTINUA** (ej: edad, temperatura, precio).
    -   *¿Por qué?* La regresión busca una ecuación matemática basada en la continuidad de X.
    -   *¿Si es categórica?* Entonces NO uses regresión lineal. Usa un Boxplot o Barplot para comparar grupos.
-   **Eje Y (Variable Dependiente)**: Debe ser **NUMÉRICA CONTINUA** (ej: altura, ventas, rendimiento).
    -   *¿Por qué?* Es la magnitud que intentamos predecir.
    -   *¿Si es categórica?* Entonces es un problema de Clasificación (Regresión Logística), no Lineal.

### Elementos Visuales
  - **Puntos**: Observaciones reales (Scatter).
  - **Línea**: El ajuste del modelo (usualmente lineal $y = mx + b$).
  - **Banda**: Intervalo de confianza (usualmente 95%), muestra la incertidumbre de la predicción.

### ¿Cuándo usarlo?
- Para confirmar visualmente una **correlación**.
- Para detectar valores que se desvían del modelo esperado (**residuos**).
- Cuando quieres comunicar una **tendencia** clara, no solo una nube de puntos.

## Implementación

### 1. Preparación y Cálculo Estadístico
Calcular el coeficiente de Pearson (*r*) añade rigor científico al gráfico.

```python
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import scipy.stats as sp

df = pd.read_csv('../data/pinguinos.csv').dropna()

# Calcular correlación de Pearson
x_col = 'flipper_length_mm'
y_col = 'culmen_length_mm'
r, p = sp.pearsonr(df[x_col], df[y_col])

print(f"Coeficiente r: {r:.3f} (p-value: {p:.3e})")
```

### 2. Regresión con Seaborn (`regplot` / `lmplot`)
Seaborn es la herramienta reina para esto. Calcula y dibuja la regresión automáticamente.

```python
# Diseño Premium: Configuración de estilo
sns.set_style("whitegrid")
plt.figure(figsize=(10, 6))

# Gráfico de Regresión
ax = sns.regplot(
    data=df,
    x=x_col,
    y=y_col,
    scatter_kws={'s': 50, 'alpha': 0.6, 'color': '#2E86C1'}, # Puntos semi-transparentes
    line_kws={'color': '#E74C3C', 'linewidth': 2}            # Línea de tendencia destacada
)

# Añadir anotación con el valor r
plt.text(
    x=0.05, y=0.95, 
    s=f'$r = {r:.2f}$', 
    transform=ax.transAxes, 
    fontsize=14, 
    bbox=dict(facecolor='white', alpha=0.8, edgecolor='#cccccc')
)

plt.title('Relación Longitud Aleta vs Pico (con Tendencia Lineal)', fontsize=14)
plt.show()
```

### 3. Regresión por Categorías (`lmplot`)
Si quieres ver si la tendencia cambia según el grupo (ej: especie).

```python
sns.lmplot(
    data=df,
    x="flipper_length_mm",
    y="culmen_length_mm",
    hue="species",    # Una línea de regresión por cada especie
    height=6,
    aspect=1.5,
    scatter_kws={'alpha': 0.5}
)
plt.title("Tendencias Diferenciadas por Especie")
plt.show()
```

### 4. Regresión Interactiva (Plotly)
Para dashboards donde el usuario necesita ver el valor exacto de cada punto.

```python
import plotly.express as px

fig = px.scatter(
    df, 
    x='flipper_length_mm', 
    y='culmen_length_mm', 
    trendline="ols",                 # Ordinary Least Squares (Lineal)
    trendline_color_override="red",
    title="Análisis de Regresión Interactivo"
)
fig.show()
```

## Reglas de Diseño "Maestro"

1.  **Destacar la Línea**: Los puntos son el contexto, la línea es el mensaje. Usa un color contrastante para la línea de regresión (ej: Rojo sobre puntos Azules).
2.  **No ocultar la incertidumbre**: Mantén la banda de confianza visible (es el default en Seaborn). Si es muy ancha, indica que el modelo no es muy preciso.
3.  **Anotar el *r***: Siempre que muestres una regresión linar, escribe el valor de *r* o $R^2$ en el gráfico. Ayuda al espectador a juzgar la fuerza de la relación.
4.  **Menos es más**: Reduce el tamaño (`s`) y opacidad (`alpha`) de los puntos si tienes muchos datos, para que la línea de tendencia no se pierda en el ruido.

## Origen
Código analizado y extraído de: `contexto/nivel2/regresion.ipynb`
