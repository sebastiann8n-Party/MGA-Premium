# Skill: Mapa de Conexiones (Connection Map / Route Map)

## Misión
Mostrar las trayectorias reales o abstractas que conectan puntos geográficos. Útil para entender **patrones de movimiento, rutas logísticas o vuelos**. A diferencia de un mapa de puntos, aquí la línea (arco) que conecta A y B es el protagonista.

## Guía de Ejes

### Conceptos Clave
-   **Arco Geodésico (Great Circle)**: En un mapa global, la ruta más corta entre dos puntos es una curva, no una línea recta. Si no usas arcos geodésicos en proyecciones globales, tus líneas cruzarán el mapa incorrectamente.
-   **Volumen del Flujo**: Grosor de la línea.
-   **Dirección**: Color o Flecha indicando el sentido (A -> B).

### ¿Cuándo usarlo?
-   Rutas de aerolíneas (Hub and Spoke).
-   Cables submarinos de internet.
-   Envíos de mercancías internacionales.
-   Migración de aves o personas.

---

## Implementación

### 1. Plotly (Mapas Interactivos)
Plotly maneja excelente las líneas geográficas (Flight paths).

```python
import plotly.graph_objects as go
import pandas as pd

df_airports = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/2011_february_us_airport_traffic.csv')
df_flight_paths = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/2011_february_aa_flight_paths.csv')

fig = go.Figure()

# Añadir Vuelos (Líneas)
for i in range(len(df_flight_paths)):
    fig.add_trace(
        go.Scattergeo(
            locationmode = 'USA-states',
            lon = [df_flight_paths['start_lon'][i], df_flight_paths['end_lon'][i]],
            lat = [df_flight_paths['start_lat'][i], df_flight_paths['end_lat'][i]],
            mode = 'lines',
            line = dict(width = 1,color = 'red'),
            opacity = float(df_flight_paths['cnt'][i]) / float(df_flight_paths['cnt'].max()),
        )
    )

# Añadir Aeropuertos (Puntos)
fig.add_trace(go.Scattergeo(
    locationmode = 'USA-states',
    lon = df_airports['long'],
    lat = df_airports['lat'],
    hoverinfo = 'text',
    text = df_airports['airport'],
    mode = 'markers',
    marker = dict(
        size = 2,
        color = 'rgb(255, 0, 0)',
        line = dict(
            width = 3,
            color = 'rgba(68, 68, 68, 0)'
        )
    )))

fig.update_layout(
    title_text = 'Feb. 2011 American Airline Flight Paths',
    showlegend = False,
    geo = dict(
        scope = 'north america',
        projection_type = 'azimuthal equal area',
        showland = True,
        landcolor = 'rgb(243, 243, 243)',
        countrycolor = 'rgb(204, 204, 204)',
    ),
)
fig.show()
```

### 2. Folium (Plugins.AntPath)
Para animaciones de rutas (líneas que "caminan").

```python
import folium
from folium import plugins

m = folium.Map(location=[41.5025, -72.699997], zoom_start=4)

# Coordenadas de la ruta
route_lats_longs = [[40.7128, -74.0060], [34.0522, -118.2437]]

# Añadir AntPath (Línea animada tipo hormiga)
plugins.AntPath(
    locations=route_lats_longs,
    dash_array=[10, 20],
    delay=1000,
    color='blue',
    pulse_color='white'
).add_to(m)

m
```

---

## Reglas de Diseño

1.  **Opacidad**: Cuando tienes miles de líneas superpuestas, usa transparencias altas (alpha=0.1). Las rutas más transitadas se verán más oscuras naturalmente por la acumulación de capas.
2.  **Curvatura**: Evita líneas rectas en mapas mundiales si es posible. La curvatura ayuda a separar rutas que van y vienen.
3.  **Animación**: En mapas digitales, usa un efecto sutil de movimiento (como `AntPath` o partículas fluyendo) para indicar la dirección, ya que las flechas estáticas ensucian el mapa.
4.  **Mapa Base**: Minimalista excesivo. Si tu mapa está lleno de líneas rojas, el fondo debe ser gris muy claro o muy oscuro, sin etiquetas de ciudades innecesarias.

## Origen
Skill desarrollada para Nivel 4 (Avanzado Web) enfocada en rutas y conexiones geográficas.
