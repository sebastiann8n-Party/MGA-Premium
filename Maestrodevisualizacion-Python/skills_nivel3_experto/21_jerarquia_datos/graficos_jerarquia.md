# Skill: Gráfico de Jerarquía (Treemap & Sunburst)

## Misión
Visualizar la composición de un todo cuando existen múltiples niveles de anidamiento. A diferencia del gráfico de pastel (pie chart) que solo muestra un nivel (Partes del total), los Treemaps y Sunbursts muestran la estructura organizativa (ej: Directorio de archivos, Categorías de productos, Geografía mundial) y el tamaño relativo de cada componente.

## Guía de Ejes

### Tipos de Gráficos
1.  **Treemap (Mapa de Árbol)**: Divide un rectángulo en sub-rectángulos anidados.
    -   Ideal para: Jerarquías profundas (muchos niveles) y comparar el tamaño total de áreas.
    -   Lectura: Área = Valor cuantitativo. Color = Categoría o Valor de rendimiento (ej: % cambio).
    -   Ventaja: Aprovecha todo el espacio disponible (eficiente).

2.  **Sunburst (Estallido Solar)**: Versión radial del Treemap.
    -   Ideal para: Jerarquías donde el recorrido desde el centro hacia afuera es importante (Estructura radial).
    -   Lectura: Ángulo/Arco = Valor cuantitativo. Anillos concéntricos = Niveles de jerarquía.
    -   Desventaja: Menos eficiente en espacio, etiquetas difíciles de leer en el centro.

### ¿Cuándo usarlo?
-   Presupuesto nacional desglosado por ministerios y programas.
-   Ventas por Región > País > Ciudad > Tienda.
-   Portafolio de inversión por Sector > Industria > Compañía.
-   Estructura de archivos en disco (WinDirStat).

---

## Implementación

### 1. Treemap con Plotly Express
Plotly simplifica la creación de Treemaps interactivos donde puedes hacer click para "entrar" (drill-down) en una categoría.

```python
import plotly.express as px

# Datos jerárquicos de ejemplo (Gapminder)
df = px.data.gapminder().query("year == 2007")

fig = px.treemap(
    df,
    path=[px.Constant("Mundo"), 'continent', 'country'], # Jerarquía
    values='pop',       # Tamaño del rectángulo = Población
    color='lifeExp',    # Color = Esperanza de Vida
    color_continuous_scale='RdBu',
    hover_name='country',
    title='Población Mundial y Esperanza de Vida (Treemap)'
)
fig.update_traces(root_color="lightgrey")
fig.show()
```

### 2. Sunburst con Plotly Express
Misma lógica, diferente visualización radial. Mejor para mostrar la proporción del nivel "padre" ocupada por cada "hijo".

```python
fig = px.sunburst(
    df,
    path=['continent', 'country'],
    values='pop',
    color='lifeExp',
    color_continuous_scale='RdBu',
    title='Población Mundial (Sunburst)'
)
fig.show()
```

### 3. Personalización con Graph Objects
Si necesitas control total sobre etiquetas y colores específicos.

```python
import plotly.graph_objects as go

labels = ["Eve", "Cain", "Seth", "Enos", "Noam", "Abel", "Awan", "Enoch", "Azura"]
parents = ["", "Eve", "Eve", "Seth", "Seth", "Eve", "Eve", "Awan", "Eve"]
values = [10, 14, 12, 10, 2, 6, 6, 4, 4]

fig = go.Figure(go.Treemap(
    labels = labels,
    parents = parents,
    values =  values,
    textinfo = "label+value+percent parent", # Muestra valor y % del padre
    marker_colors = ["pink", "royalblue", "lightgray", "purple", "cyan", "lightgray", "lightblue", "lightgreen", "gold"]
))

fig.show()
```

---

## Reglas de Diseño

1.  **Etiquetas Inteligentes**: En Treemaps, si el rectángulo es muy pequeño, oculta la etiqueta para evitar ruido visual. Plotly lo hace automáticamente, pero verifica.
2.  **Color Significativo**:
    -   Usa color categórico para distinguir ramas principales (ej: Continentes).
    -   Usa color divergente (Rojo-Azul) para métricas de rendimiento (ej: Ganancia/Pérdida) dentro de cada caja.
3.  **No abusar de la profundidad**: Más de 3-4 niveles de jerarquía pueden hacer que el gráfico sea ilegible. Si tienes muchos niveles, considera usar un gráfico interactivo con *drill-down*.
4.  **Treemap vs Sunburst**: Si el espacio es cuadrado/rectangular (monitor), usa Treemap. Si es circular o el diseño es radial, usa Sunburst. El Treemap es generalmente más fácil de comparar áreas.

## Origen
Skill desarrollada siguiendo estándares de Nivel 3 (Experto) para visualización de jerarquías de datos.
