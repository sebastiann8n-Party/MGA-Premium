# Skill: Sunburst (Gráfico Solar)

## Misión
Visualizar **jerarquías de datos radiales** y proporciones. Similar al Treemap, pero proyectado en coordenadas polares. Es ideal para mostrar cómo la *totalidad* se distribuye en sus partes de manera concéntrica, donde cada anillo es un nivel de profundidad.

## Guía de Ejes

### Conceptos Clave
-   **Centro (Root)**: El nivel superior de la jerarquía (El "Todo").
-   **Anillos (Levels)**: Cada circunferencia representa un nivel (Continente -> País -> Ciudad).
-   **Sector (Slice)**: El ángulo del sector es proporcional al valor.

### ¿Cuándo usarlo?
-   Estructura organizacional de empresas.
-   Taxonomía biológica (Reino -> Filo -> Clase).
-   Desglose de ingresos por región y producto.

### ¿Cuándo NO usarlo?
-   Si necesitas comparar magnitudes precisas (los ángulos son difíciles de comparar, especialmente en los anillos externos).
-   Si la jerarquía es muy profunda (> 4 niveles se vuelve confuso).

---

## Implementación

### 1. Plotly Express (Interactivo y Potente)
Permite navegación drill-down al hacer clic en un sector, este toma el centro y expande sus hijos.

```python
import plotly.express as px
import pandas as pd

# Datos de ejemplo
df = px.data.gapminder().query("year == 2007")

# Crear Sunburst
fig = px.sunburst(
    df, 
    path=[px.Constant("Mundo"), 'continent', 'country'], # Jerarquía
    values='pop',       # Ángulo del sector = Población
    color='lifeExp',    # Color = Esperanza de Vida
    color_continuous_scale='RdBu',
    hover_data=['iso_alpha']
)

# Estética
fig.update_layout(margin = dict(t=50, l=25, r=25, b=25))
fig.show()
```

### 2. D3.js (Nativo o via Wrapper)
Para visualizaciones web altamente personalizadas, Sunburst es un clásico de D3.js. En Python, Plotly es la mejor opción.

---

## Reglas de Diseño

1.  **Etiquetas Curvas**: Si usas D3.js, adapta el texto a la curva del anillo para mejorar la legibilidad.
2.  **Color Consistente**: Mantén la misma paleta de colores para las ramas principales a través de todos los niveles. Si "América" es azul en el centro, sus países deben ser tonos de azul.
3.  **Interactividad**: Es crucial. El gráfico estático suele ser difícil de leer en los niveles más profundos. El tooltip (hover) debe mostrar el valor y el porcentaje del total.
4.  **Centro Vacío o Donut**: Puedes dejar el centro vacío o colocar el total global.

## Origen
Skill basada en Nivel 5 (Innovación) del curso Data Viz, enfocada en visualización jerárquica radial.
