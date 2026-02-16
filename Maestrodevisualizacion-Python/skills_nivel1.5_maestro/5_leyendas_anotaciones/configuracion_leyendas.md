# Skill Transversal: Configuración de Leyendas y Anotaciones

## Misión
Guiar la atención del usuario mediante leyendas claras y anotaciones estratégicas que expliquen el "¿Qué es esto?" y el "¿Por qué importa?" de los datos. La leyenda no solo identifica colores, sino que organiza la jerarquía visual.

## 1. Matplotlib y Seaborn (Control Total)
Para gráficos profesionales, no basta con la ubicación por defecto. Debemos controlar el estilo del contenedor.

### Estilo y Bordes (`legend`)
```python
import matplotlib.pyplot as plt
import seaborn as sns

# Configuración estética avanzada
plt.legend(
    title='Categorías',        # Título de la leyenda
    loc='upper left',          # Ubicación relativa
    bbox_to_anchor=(1.05, 1),  # Ubicación absoluta (fuera del eje)
    ncol=1,                    # Número de columnas
    frameon=True,              # Mostrar u ocultar el borde (marco)
    edgecolor='gray',          # Color del borde
    facecolor='white',         # Color de fondo
    framealpha=0.8,            # Transparencia del fondo
    fontsize='small',          # Tamaño de la fuente
    shadow=True                # Sombra proyectada para profundidad
)
```

### Ejemplo de Narrativa (Anotaciones)
Usa flechas para señalar hitos o valores atípicos (outliers).
```python
# Anotar el punto máximo con estilo premium
plt.annotate('Punto de Quiebre', 
             xy=(x_val, y_val), 
             xytext=(x_val+1, y_val+5),
             arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=.2', color='red'),
             fontsize=10, 
             bbox=dict(boxstyle="round,pad=0.3", fc="yellow", ec="darkgoldenrod", lw=2))
```

## 2. Plotly (Interactividad y Layout)
En Plotly, la leyenda es un elemento dinámico que permite filtrar series con un clic. Su diseño debe ser fluido.

### Leyenda Horizontal vs Vertical
```python
import plotly.express as px

fig.update_layout(
    legend=dict(
        title="Filtros",
        orientation="h",        # "h" para horizontal, "v" para vertical
        yanchor="bottom",
        y=1.02,                 # Posición por encima del gráfico
        xanchor="right",
        x=1,
        bgcolor="LightSteelBlue", # Fondo personalizado
        bordercolor="Black",     # Borde
        borderwidth=2
    )
)
```

## 3. Mejores Prácticas de Legibilidad
1.  **Eliminar Leyendas Redundantes:** Si el gráfico solo tiene una serie, el título del gráfico es suficiente.
2.  **Ubicación:** Si hay muchas categorías, coloca la leyenda a la derecha (`bbox_to_anchor`). Si hay pocas, prueba ponerla arriba de forma horizontal.
3.  **Títulos:** Dale un título descriptivo a la leyenda si el nombre de la columna no es claro.
4.  **Anotaciones Selectivas:** Anota solo aquello que requiera explicación adicional o que sea el "insight" principal de la visualización.

## Resumen de Propiedades Estéticas
| Propiedad | Matplotlib | Plotly |
|---|---|---|
| **Borde** | `frameon`, `edgecolor` | `borderwidth`, `bordercolor` |
| **Fondo** | `facecolor`, `framealpha` | `bgcolor` |
| **Columnas** | `ncol=N` | N/A (usa `orientation`) |
| **Título** | `title='Txt'` | `title=dict(text='Txt')` |
| **Sombra** | `shadow=True` | N/A |

