# Skill Ingenieria: Densidad 2D y Contornos

## Misión
Visualizar la concentración de datos en dos dimensiones, útil para identificar clústeres, zonas de alta densidad o relaciones no lineales en grandes volúmenes de datos donde un Scatter Plot se satura (overplotting).

## Reglas de Oro
1.  **Overplotting:** Usa Densidad 2D cuando tengas tantos puntos que se solapen y formen una mancha sólida.
2.  **Contornos:** Ideales para visualizar "topografía" de datos y gradientes.
3.  **Color:** Usa escalas de color perceptualmente uniformes (Viridis, Plasma) para representar la densidad.

## 1. Histograma 2D (Heatpmap de Densidad)
Divide el plano 2D en bins rectangulares y cuenta cuántos puntos caen en cada uno.

```python
import plotly.express as px

df = px.data.tips()

fig = px.density_heatmap(df, x="total_bill", y="tip", 
                         nbinsx=20, nbinsy=20, # Resolución de la cuadrícula
                         color_continuous_scale="Viridis",
                         title="Concentración de Propinas vs Cuenta Total",
                         text_auto=True) # Muestra el conteo en cada celda

fig.show()
```

## 2. Gráfico de Contornos de Densidad
Estima la función de densidad de probabilidad (KDE) y dibuja líneas de nivel (isolineas).

```python
import plotly.express as px

df = px.data.iris()

fig = px.density_contour(df, x="sepal_width", y="sepal_length", 
                         color="species", # Contornos separados por categoría
                         marginal_x="histogram", # Histograma marginal arriba
                         marginal_y="histogram", # Histograma marginal derecha
                         title="Densidad de Especies Iris (Contornos)")

fig.show()
```

## 3. Combinación: Scatter + Contornos
Muestra los datos individuales (si no son demasiados) junto con la densidad general.

```python
import plotly.graph_objects as go
import plotly.express as px

df = px.data.iris()
bg_scatter = px.scatter(df, x="sepal_width", y="sepal_length", color="species")
contours = px.density_contour(df, x="sepal_width", y="sepal_length", color="species")

fig = go.Figure()

# Añadir trazas de scatter
for trace in bg_scatter.data:
    fig.add_trace(trace)

# Añadir trazas de contorno (solo líneas)
for trace in contours.data:
    trace.update(line=dict(dash='dot')) # Líneas punteadas para diferenciar
    fig.add_trace(trace)

fig.update_layout(title="Scatter Plot con Contornos de Densidad Superpuestos")
fig.show()
```

## Resumen
| Tipo de Gráfico | Función Plotly | Mejor Uso |
|---|---|---|
| Histograma 2D | `px.density_heatmap` | Datos discretos o conteo exacto por zonas. |
| Contornos | `px.density_contour` | Datos continuos, visualizar gradientes suaves. |
| Hexbin (Similar) | (Usar Matplotlib/Seaborn `jointplot(kind='hex')`) | Alternativa estética al cuadrado. |
