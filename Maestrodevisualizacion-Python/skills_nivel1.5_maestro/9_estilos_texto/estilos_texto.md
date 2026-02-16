# Skill: Estilos de Texto y Tipografías

## Misión
Personalizar la fuente, el tamaño y el estilo de los textos para mejorar la jerarquía visual y la legibilidad, adaptando el diseño a requerimientos estéticos o corporativos.

## 1. Matplotlib y Seaborn (Uso de `fontdict` y `rcParams`)
En Matplotlib, la mayoría de los métodos de texto (`set_title`, `set_xlabel`, `set_ylabel`, `text`) aceptan un argumento `fontdict`.

### Configuración por elemento
```python
import matplotlib.pyplot as plt
import numpy as np

# Datos de ejemplo
x = np.linspace(0, 10, 100)
y = np.sin(x)

fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(x, y)

# Diccionario de estilos para el título
title_style = {
    'family': 'serif',
    'color':  'darkblue',
    'weight': 'bold',
    'size': 20,
}

ax.set_title('Análisis de Oscilación Senoidal', fontdict=title_style, pad=20)

# Estilo para los ejes
label_style = {'family': 'sans-serif', 'color': 'black', 'size': 14}
ax.set_xlabel('Tiempo (s)', fontdict=label_style)
ax.set_ylabel('Amplitud', fontdict=label_style)

# Rotación y estilo de los Ticks (Marcas de los ejes)
plt.xticks(fontsize=12, rotation=45, family='monospace')
plt.show()
```

### Configuración Global (rcParams)
Ideal para mantener la consistencia en todo el proyecto.
```python
plt.rcParams.update({
    'font.family': 'sans-serif',
    'font.sans-serif': ['Arial'],
    'axes.titlesize': 18,
    'axes.labelsize': 14,
    'xtick.labelsize': 12
})
```

## 2. Plotly (Uso de `update_layout`)
Plotly centraliza el estilo del texto en el atributo `font` del layout o de elementos específicos.

```python
import plotly.express as px

df = px.data.gapminder().query("country == 'Canada'")
fig = px.line(df, x='year', y='lifeExp', title='Experiencia de Vida en Canadá')

fig.update_layout(
    title={
        'text': "Análisis Temporal de Longevidad",
        'y': 0.9,
        'x': 0.5,
        'xanchor': 'center',
        'yanchor': 'top',
        'font': dict(family="Courier New, monospace", size=24, color="RebeccaPurple")
    },
    font=dict(
        family="Arial, sans-serif",
        size=14,
        color="black"
    )
)
fig.show()
```

## Reglas de Oro
1.  **Consistencia:** Usa el mismo tipo de letra en todos los gráficos de un mismo reporte.
2.  **Jerarquía:** El título siempre debe ser más grande y pesado (bold) que las etiquetas de los ejes.
3.  **Legibilidad:** Evita fuentes excesivamente decorativas. Las fuentes *San Serif* (Arial, Helvetica) funcionan mejor en pantallas.
4.  **Contrastes:** El color del texto debe contrastar fuertemente con el fondo.

## Parámetros Comunes
| Propiedad | Matplotlib | Plotly |
|---|---|---|
| **Tipo de Fuente** | `family` | `family` |
| **Tamaño** | `size` | `size` |
| **Peso** | `weight` (bold, light, normal) | N/A (se define en la fuente) |
| **Color** | `color` | `color` |
| **Estilo** | `style` (italic, oblique) | N/A |
| **Rotación** | `rotation` | `tickangle` |
