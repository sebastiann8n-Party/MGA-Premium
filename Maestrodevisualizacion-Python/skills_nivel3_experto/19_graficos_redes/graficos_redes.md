# Skill: Gráfico de Redes (Network Graphs)

## Misión
Visualizar la **estructura de relaciones** entre entidades. A diferencia de las tablas, este gráfico se centra en la *conectividad*. Permite identificar nodos centrales (influyentes), comunidades (grupos densamente conectados) y caminos críticos.

## Guía de Ejes

### Conceptos Clave
-   **Nodos (Vertices)**: Representan las entidades (Personas, Aeropuertos, Productos).
-   **Aristas (Edges)**: Representan las conexiones (Amistad, Ruta de vuelo, Co-compra).
-   **Peso (Weight)**: Grosor de la arista que indica la fuerza de la relación.
-   **Dirección**: Si la relación es unidireccional (A sigue a B) o bidireccional (A es amigo de B).

### ¿Cuándo usarlo?
- Análisis de redes sociales (influencia).
- Detección de fraude (anillos de cuentas conectadas).
- Rutas logísticas y transporte.
- Análisis de dependencias de software o biología (interacciones proteína-proteína).

---

## Implementación

### 1. NetworkX + Matplotlib (Base Estática)
NetworkX es la librería estándar de Python para *analizar* grafos, pero su visualización es básica.

```python
import networkx as nx
import matplotlib.pyplot as plt

# Crear un grafo vacío
G = nx.Graph()

# Añadir nodos y aristas
G.add_edge("Alice", "Bob", weight=5)
G.add_edge("Bob", "Charlie", weight=2)
G.add_edge("Alice", "David", weight=1)
G.add_edge("Eve", "Alice", weight=3)

# Calcular posiciones (Layout) - Algoritmo Fruchterman-Reingold (spring)
pos = nx.spring_layout(G, seed=42)

# Dibujar nodos
nx.draw_networkx_nodes(G, pos, node_size=700, node_color="skyblue")

# Dibujar aristas con grosor basado en peso
weights = [G[u][v]['weight'] for u,v in G.edges()]
nx.draw_networkx_edges(G, pos, width=weights, edge_color="gray", alpha=0.5)

# Dibujar etiquetas
nx.draw_networkx_labels(G, pos, font_size=12, font_family="sans-serif")

plt.axis("off")
plt.title("Red Social Simple")
plt.show()
```

### 2. PyVis (Interactivo y Dinámico)
PyVis genera gráficos HTML interactivos donde puedes arrastrar nodos, hacer zoom y filtrar.

```python
from pyvis.network import Network

# Crear red interactiva
net = Network(height="500px", width="100%", bgcolor="#222222", font_color="white")

# Añadir nodos y aristas desde el grafo de NetworkX
net.from_nx(G)

# Personalizar física y opciones
net.barnes_hut() # Algoritmo de física para estabilizar nodos
net.show_buttons(filter_=['physics']) # Mostrar controles de física

# Guardar y mostrar
net.show("red_interactiva.html", notebook=False)
```

### 3. Plotly (Redes Modernas Estáticas/Interactivas)
Plotly permite más control sobre el estilo y los tooltips, pero requiere definir coordenadas manualmente (usando NetworkX para el layout).

```python
import plotly.graph_objects as go

# Obtener posiciones X, Y de los nodos
edge_x = []
edge_y = []
for edge in G.edges():
    x0, y0 = pos[edge[0]]
    x1, y1 = pos[edge[1]]
    edge_x.extend([x0, x1, None])
    edge_y.extend([y0, y1, None])

edge_trace = go.Scatter(
    x=edge_x, y=edge_y,
    line=dict(width=0.5, color='#888'),
    hoverinfo='none',
    mode='lines')

node_x = []
node_y = []
for node in G.nodes():
    x, y = pos[node]
    node_x.append(x)
    node_y.append(y)

node_trace = go.Scatter(
    x=node_x, y=node_y,
    mode='markers+text',
    text=list(G.nodes()),
    textposition="bottom center",
    hoverinfo='text',
    marker=dict(
        showscale=True,
        colorscale='YlGnBu',
        size=10,
        color=[], # Aquí podría ir una medida de centralidad
        line_width=2))

fig = go.Figure(data=[edge_trace, node_trace],
             layout=go.Layout(
                title='Red con Plotly',
                showlegend=False,
                hovermode='closest',
                margin=dict(b=20,l=5,r=5,t=40),
                xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                yaxis=dict(showgrid=False, zeroline=False, showticklabels=False))
                )
fig.show()
```

---

## Reglas de Diseño

1.  **Layout es Clave**: El algoritmo de posición (spring, circular, random) determina si el grafo se ve como una maraña ("hairball") o una estructura clara. `spring_layout` es el estándar para redes orgánicas.
2.  **Filtrado de Ruido**: En redes grandes, elimina nodos con pocas conexiones (grado bajo) o aristas débiles. Intenta visualizar solo el "Core" de la red.
3.  **Tamaño por Importancia**: Usa el tamaño del nodo para representar su importancia (Degree Centrality, PageRank) y el color para su comunidad (Louvain Community Detection).
4.  **No cruzar líneas**: Minimiza el cruce de aristas (edge crossing) ajustando el layout o usando algoritmos que optimicen la legibilidad.

## Origen
Skill desarrollada siguiendo estándares de Nivel 3 (Experto) para visualización de redes complejas.
