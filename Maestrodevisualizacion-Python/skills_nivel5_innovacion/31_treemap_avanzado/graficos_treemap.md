# Skill: Treemap Avanzado (Mapas de Árbol)

## Misión
Visualizar **jerarquías de datos y magnitudes** simultáneamente en un espacio compacto. A diferencia de un gráfico de barras, el Treemap nos permite ver la composición de "el todo" y cómo se dividen sus partes (y las partes de sus partes).

## Guía de Ejes

### Conceptos Clave
-   **Jerarquía (Hierarchy)**: Estructura Padre -> Hijo (ej: Continente -> País -> Ciudad).
-   **Área (Size)**: Representa la magnitud de la variable principal.
-   **Color**: Se usa para:
    -   Codificar una *segunda* variable métrica (ej: Ventas = Tamaño, Rentabilidad = Color).
    -   Diferenciar categorías del nivel superior.

### ¿Cuándo usarlo?
-   Presupuestos gubernamentales (Ministerio -> Proyecto).
-   Inventarios de retail (Categoría -> Producto).
-   Espacio en disco duro (Carpeta -> Archivo).

### ¿Cuándo NO usarlo?
-   Si la jerarquía es temporal (Año/Mes). Usa líneas.
-   Si necesitas comparar magnitudes precisas (el ojo humano juzga mal las áreas de rectángulos de diferentes proporciones).

---

## Implementación

### 1. Plotly Express (Interactivo y Potente)
Plotly maneja la navegación (drill-down) automáticamente. Al hacer clic en una categoría, esta se expande.

```python
import plotly.express as px
import pandas as pd

# Datos de ejemplo
df = px.data.gapminder().query("year == 2007")

# Crear Treemap
fig = px.treemap(
    df, 
    path=[px.Constant("Mundo"), 'continent', 'country'], # Jerarquía definida
    values='pop',       # Tamaño del rectángulo = Población
    color='lifeExp',    # Color = Esperanza de Vida
    color_continuous_scale='RdBu',
    hover_data=['iso_alpha']
)

# Estética
fig.update_traces(root_color="lightgrey") # Color del nodo raíz
fig.update_layout(margin = dict(t=50, l=25, r=25, b=25))
fig.show()
```

### 2. Squarify (Matplotlib Fijo)
Para reportes estáticos donde controlas el layout exacto. `squarify` calcula los rectángulos para que sean lo más cuadrados posible.

```python
import matplotlib.pyplot as plt
import squarify

# Datos
sizes = [50, 25, 12, 6]
label = ["A", "B", "C", "D"]
color = ['red', 'blue', 'green', 'grey']

plt.figure(figsize=(10, 8))
squarify.plot(sizes=sizes, label=label, color=color, alpha=0.6)
plt.axis('off')
plt.show()
```

---

## Reglas de Diseño

1.  **Etiquetas Inteligentes**: Si el rectángulo es muy pequeño, oculta la etiqueta para evitar ruido visual.
2.  **Color Divergente**: Si usas color para una métrica de desempeño (ej: Ganancia/Pérdida), usa una escala divergente (Rojo-Blanco-Verde/Azul).
3.  **Proporción**: Evita rectángulos extremadamente delgados ("fideos"), ya que son difíciles de comparar y etiquetar. Los algoritmos como "squarified" intentan evitar esto.
4.  **Profundidad**: No muestres más de 2 o 3 niveles de profundidad a la vez, o se volverá ilegible. Aprovecha la interactividad para clickear y bajar de nivel.

## Origen
Skill basada en Nivel 5 (Innovación) del curso Data Viz, enfocada en visualización jerárquica rectangular.
