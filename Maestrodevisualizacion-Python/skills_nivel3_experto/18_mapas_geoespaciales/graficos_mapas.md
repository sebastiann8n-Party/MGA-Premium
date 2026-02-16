# Skill: Visualización Geoespacial (Mapas)

## Misión
Visualizar la **distribución espacial** de los datos. Esta habilidad es fundamental cuando la posición geográfica (Latitud/Longitud, Zona, País) es un factor crítico en el análisis. Permite responder preguntas sobre *dónde* ocurren los eventos y *cómo* se distribuyen las métricas en un territorio.

## Guía de Ejes

### Tipos de Mapas
Existen diversas formas de visualizar datos sobre un mapa:

1.  **Mapas de Puntos (Scatter Map)**:
    -   Ideal para: Ubicaciones exactas (Lat/Lon) de eventos o tiendas.
    -   Codificación: Tamaño (cantidad) y Color (categoría/tipo).
    -   Herramientas: `folium`, `plotly.express`.

2.  **Mapas Coropléticos (Choropleth)**:
    -   Ideal para: Datos agregados por regiones (Países, Estados, Municipios).
    -   Codificación: Intensidad de Color en el polígono del área.
    -   Requiere: Archivos GeoJSON o fronteras definidas.
    -   Herramientas: `geopandas`, `plotly.express`.

3.  **Mapas de Calor (Heatmap)**:
    -   Ideal para: Ver densidad de puntos e intensidad sin importar fronteras.
    -   Codificación: Gradiente de color suave sobre el mapa base.
    -   Herramientas: `folium.plugins.HeatMap`.

### ¿Cuándo usarlo?
- Comparar ventas por región/país.
- Visualizar rutas o flujos de transporte.
- Entender la densidad poblacional o densidad de eventos.
- Identificar clústeres geográficos.

---

## Implementación

### 1. Folium (Mapas Interactivos basados en Leaflet)
Folium es excelente para mapas interactivos ligeros que se pueden incrustar en HTML.

```python
import folium
from folium.plugins import HeatMap
import pandas as pd

# Datos de ejemplo: Latitud, Longitud, Intensidad
data = [
    [40.7128, -74.0060, 10], # NY
    [34.0522, -118.2437, 8], # LA
    [41.8781, -87.6298, 5]   # Chicago
]

# Crear mapa base centrado
m = folium.Map(location=[39.8283, -98.5795], zoom_start=4, tiles="CartoDB positron")

# Opción A: Marcadores Individuales con Popup
for lat, lon, val in data:
    folium.CircleMarker(
        location=[lat, lon],
        radius=val,
        color="crimson",
        fill=True,
        fill_color="crimson",
        popup=f"Valor: {val}"
    ).add_to(m)

# Opción B: Mapa de Calor (Density)
HeatMap(data, radius=15).add_to(m)

# Guardar o Visualizar
m.save("mapa_interactivo.html")
m
```

### 2. Plotly (Mapas Modernos y Dashboards)
Plotly es ideal si necesitas integrar el mapa en un dashboard o requieres interacción avanzada con tooltips.

#### A. Scatter Geo (Puntos en el Mapa)
```python
import plotly.express as px

df = px.data.gapminder().query("year == 2007")

fig = px.scatter_geo(
    df,
    locations="iso_alpha",  # Código ISO de país
    color="continent",
    hover_name="country",
    size="pop",
    projection="natural earth",
    title="Población Mundial 2007"
)
fig.show()
```

#### B. Choropleth (Mapas de Regiones)
```python
fig = px.choropleth(
    df,
    locations="iso_alpha",
    color="lifeExp", # Variable a colorear
    hover_name="country",
    color_continuous_scale=px.colors.sequential.Plasma,
    title="Esperanza de Vida por País"
)
fig.show()
```

### 3. Geopandas (Mapas Estáticos de Alta Precisión)
Basado en Matplotlib, permite manipular geometrías complejas y hacer operaciones espaciales.

```python
import geopandas as gpd
import matplotlib.pyplot as plt

# Cargar dataset de países incluido en Geopandas
world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

# Filtrar continente
sudamerica = world[world.continent == 'South America']

# Plot básico
sudamerica.plot(
    column='pop_est',
    legend=True,
    cmap='OrRd',
    figsize=(10, 8),
    legend_kwds={'label': "Población Estimada"}
)
plt.title("Población en Sudamérica")
plt.show()
```

---

## Reglas de Diseño

1.  **Elección de Proyección**: La proyección Mercator (cilíndrica) distorsiona áreas cerca de los polos. Para mapas mundiales temáticos, prefiere proyecciones como "Natural Earth" o "Robinson".
2.  **Color con Significado**: Usa paletas secuenciales (claro a oscuro) para métricas numéricas (población) y cualitativas (distintos colores) para categorías (continentes).
3.  **Contexto**: Los mapas base (tiles) deben ser sutiles. Si tus datos son coloridos, usa un mapa base en escala de grises (Ej: CartoDB Positron) para que resalten los datos.
4.  **Normalización**: En mapas coropléticos, *siempre* normaliza los datos (ej: "casos por 100k habitantes" en lugar de "casos totales") para evitar simplemente mostrar qué áreas tienen más población.

## Origen
Skill desarrollada siguiendo estándares de Nivel 3 (Experto) para visualización geoespacial avanzada.
