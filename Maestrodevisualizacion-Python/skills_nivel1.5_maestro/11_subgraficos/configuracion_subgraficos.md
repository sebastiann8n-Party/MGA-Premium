# Skill: Configuración de Subgráficos (Multi-plot)

## Misión
Organizar múltiples visualizaciones en un solo espacio de trabajo (canvas) de forma coherente, permitiendo la comparación directa entre diferentes variables o dimensiones sin cambiar de contexto.

## 1. El Concepto: Figura vs. Axes
Es fundamental entender la jerarquía en bibliotecas como Matplotlib:
*   **Figura (Figure):** Es el marco o lienzo general. Controla el tamaño total y el título general.
*   **Axes:** Es el gráfico individual dentro de la figura. Cada "Axes" tiene su propio título, etiquetas y escala.

## 2. Implementación en Matplotlib/Seaborn
La forma más eficiente es usar `plt.subplots()`, que devuelve una tupla con la figura y un arreglo de ejes.

### Estructura Básica (Estructura de Cuadrícula)
```python
import matplotlib.pyplot as plt
import seaborn as sns

# Crear una cuadrícula de 2 filas y 2 columnas
fig, axes = plt.subplots(2, 2, figsize=(12, 10), constrained_layout=True)

# Acceder a cada gráfico mediante índices de matriz
sns.lineplot(data=df1, ax=axes[0, 0]).set_title('Serie Temporal')
sns.barplot(data=df2, ax=axes[0, 1]).set_title('Comparación Categorías')
sns.histplot(data=df3, ax=axes[1, 0]).set_title('Distribución')
sns.scatterplot(data=df4, ax=axes[1, 1]).set_title('Correlación')

plt.show()
```

### Configuración de Ejes Compartidos
Útil cuando los gráficos tienen la misma escala para facilitar la comparación visual.
```python
# Compartir el eje Y para que todos los gráficos tengan la misma altura
fig, (ax1, ax2) = plt.subplots(1, 2, sharey=True)
```

## 3. Implementación en Plotly
Plotly requiere el módulo `make_subplots` para manejar múltiples trazos en una sola figura.

```python
from plotly.subplots import make_subplots
import plotly.graph_objects as go

# Definir la estructura
fig = make_subplots(rows=2, cols=1, subplot_titles=("Gráfico A", "Gráfico B"))

# Agregar trazos especificando fila y columna
fig.add_trace(go.Scatter(x=[1, 2, 3], y=[4, 5, 6]), row=1, col=1)
fig.add_trace(go.Bar(x=[1, 2, 3], y=[2, 3, 5]), row=2, col=1)

fig.update_layout(height=600, title_text="Panel de Control")
fig.show()
```

## 4. Mejores Prácticas
1.  **Layout Inteligente:** Usa `constrained_layout=True` o `plt.tight_layout()` para evitar que los títulos y etiquetas se encimen entre sí.
2.  **Consistencia:** Mantén el mismo esquema de colores en todos los subgráficos si representan la misma dimensión.
3.  **Jerarquía:** Si un gráfico es mucho más importante que los otros, considera usar `GridSpec` para que ocupe más espacio (filas/columnas combinadas).
4.  **Menos es más:** No satures el canvas con más de 4-6 subgráficos a menos que sea un dashboard de monitoreo especializado.

## Resumen de Comandos
| Acción | Comando (Matplotlib) |
|---|---|
| Crear cuadrícula | `plt.subplots(rows, cols)` |
| Ajustar espacio | `plt.tight_layout()` |
| Título de Figura | `fig.suptitle('Título General')` |
| Título de Subgráfico | `ax.set_title('Subtítulo')` |
