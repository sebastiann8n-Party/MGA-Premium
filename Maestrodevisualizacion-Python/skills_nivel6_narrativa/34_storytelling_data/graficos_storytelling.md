# Skill: Data Storytelling (Narrativa con Datos)

## Misión
Trascender la simple visualización de datos para **contar una historia**. Esto implica guiar la atención del espectador, resaltar insights clave y provocar una acción o decisión. No es solo "mostrar el gráfico", es "explicar el porqué".

## Guía de Ejes

### Conceptos Clave
-   **Contexto**: Título declarativo (ej: "Las ventas cayeron un 20%"), no descriptivo (ej: "Ventas Q1").
-   **Enfasis**: Usar color *solo* para resaltar lo importante (el dato anómalo, la tendencia ganadora). El resto debe ser gris.
-   **Anotaciones**: Texto directo en el gráfico que explica picos o valles (ej: "Lanzamiento de producto X").
-   **Flujo**: Ordenar los gráficos lógicamente (Situación -> Complicación -> Resolución).

### ¿Cuándo usarlo?
-   Presentaciones a directivos (Pitch Decks).
-   Artículos periodísticos o blogs.
-   Reportes finales donde se requiere persuasión.

---

## Implementación

### 1. Matplotlib + Seaborn (Estilo Editorial)
Crear gráficos limpios, sin bordes innecesarios, con tipografía clara y anotaciones estratégicas.

```python
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Datos
data = pd.DataFrame({
    'Año': [2018, 2019, 2020, 2021, 2022],
    'Ventas': [100, 120, 90, 150, 180]
})

# Configuración Estética (Minimalista)
sns.set_style("white") 
plt.figure(figsize=(10, 6))

# Gráfico principal (Línea gris, Puntos destacados)
plt.plot(data['Año'], data['Ventas'], color='lightgrey', linewidth=3)
plt.plot(data['Año'].iloc[-1], data['Ventas'].iloc[-1], marker='o', color='firebrick', markersize=10)

# Título Declarativo (Izquierda, Grande)
plt.text(x=2017.5, y=200, s="Las ventas alcanzaron un récord en 2022", fontsize=16, weight='bold', color='firebrick')
plt.text(x=2017.5, y=190, s="A pesar de la caída en 2020, la recuperación fue sólida.", fontsize=12, color='grey')

# Anotación Directa
plt.annotate(
    'Impacto Pandemia', 
    xy=(2020, 90), 
    xytext=(2020, 130), 
    arrowprops=dict(facecolor='grey', shrink=0.05)
)

# Eliminar bordes (Spines)
sns.despine(left=True, bottom=False)
plt.grid(axis='y', linestyle='--', alpha=0.3)
plt.show()
```

### 2. Plotly (Narrativa Interactiva)
Usar animaciones (`animation_frame`) para mostrar la evolución temporal como una película.

```python
import plotly.express as px
df = px.data.gapminder()

fig = px.scatter(
    df, x="gdpPercap", y="lifeExp", animation_frame="year", 
    size="pop", color="continent", hover_name="country",
    log_x=True, size_max=55, range_x=[100,100000], range_y=[25,90]
)

fig.update_layout(title="La Evolución de la Salud y Riqueza Mundial (1952-2007)")
fig.show()
```

---

## Reglas de Diseño (Gestalt)
1.  **Simplicidad**: Elimina todo lo que no aporte (gridlines fuertes, fondos de color, bordes).
2.  **Proximidad**: Agrupa visualmente los elementos relacionados (etiquetas cerca de las líneas, no en una leyenda lejana).
3.  **Contraste**: El ojo va a donde hay contraste. Si todo es colorido, nada destaca.

## Origen
Skill basada en Nivel 6 (Narrativa) enfocada en comunicación efectiva de datos.
