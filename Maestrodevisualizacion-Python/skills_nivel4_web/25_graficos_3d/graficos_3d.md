# Skill: Visualización 3D (Scatter & Surface)

## Misión
Agregar un **tercer eje espacial (Z)** para estudiar relaciones complejas en modelos, terreno o simulaciones físicas. A diferencia de un mapa de calor 2D (que usa color para Z), este gráfico usa profundidad real interactiva.

## Guía de Ejes

### Tipos de Gráficos 3D
1.  **Scatter 3D**: Nubes de puntos en el espacio.
    -   Ideal para: Ver agrupamientos (clusters) que no son visibles en 2D.
    -   Ejemplo: Segmentación de clientes (Edad, Gasto, Frecuencia).

2.  **Surface 3D**: Superficies continuas (terreno, modelos matemáticos).
    -   Ideal para: Topografía, funciones de pérdida en ML.
    -   Ejemplo: Mapa de elevación de un volcán.

3.  **Mesh 3D**: Mallas triangulares o poligonales.
    -   Ideal para: Modelado 3D (BIM), visualización arquitectónica.

### ¿Cuándo usarlo?
-   Visualizar la frontera de decisión de un SVM en 3 dimensiones.
-   Estudios topográficos o geológicos.
-   Simulaciones de fluidos o temperatura.

---

## Implementación

### 1. Plotly (Interactivo es Obligatorio)
NUNCA uses Matplotlib estático para 3D si puedes evitarlo, ya que la percepción de profundidad requiere rotación interactiva. Plotly es el rey aquí.

```python
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import numpy as np

# A. Scatter 3D (Iris dataset)
df = px.data.iris()
fig = px.scatter_3d(df, x='sepal_length', y='sepal_width', z='petal_width',
              color='species')
fig.show()

# B. Surface (Superficie Volcán)
# Cargar datos de elevación
z_data = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/api_docs/mt_bruno_elevation.csv')

fig = go.Figure(data=[go.Surface(z=z_data.values)])

fig.update_layout(title='Monte Bruno (Elevación)', autosize=False,
                  width=500, height=500,
                  margin=dict(l=65, r=50, b=65, t=90))

fig.show()
```

### 2. PyVista (Ingeniería Avanzada - Opcional)
Para mallas complejas (archivos `.stl`, `.vtk`), PyVista es una librería poderosa que envuelve VTK.

*Nota: Requiere instalación adicional y backend gráfico compatible.*

```python
# Ejemplo conceptual (PyVista)
# import pyvista as pv
# mesh = pv.read("pieza_mecanica.stl")
# mesh.plot(color='orange')
```

---

## Reglas de Diseño

1.  **Interactividad Obligatoria**: Un gráfico 3D estático es confuso. El usuario DEBE poder rotar y hacer zoom para entender la estructura.
2.  **Proyección Perspectiva vs Ortográfica**:
    -   *Perspectiva*: Más realista (objetos lejanos se ven pequeños). Bueno para visualización general.
    -   *Ortográfica*: Conserva las medidas (objetos lejanos mantienen tamaño). Crucial para ingeniería y arquitectura.
3.  **Iluminación**: Usa sombreado ("lighting effects") para resaltar la curvatura de las superficies. Plotly lo hace por defecto.
4.  **No abusar**: Si puedes mostrar lo mismo con un Scatter 2D + Color/Tamaño, HAZLO. El cerebro humano procesa 2D mucho mejor que 3D en pantallas planas.

## Origen
Skill desarrollada para Nivel 4 (Avanzado Web) cubriendo técnicas de visualización espacial.
