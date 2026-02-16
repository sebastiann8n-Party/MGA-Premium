# Skill: Circle Packing (Empaquetado de Círculos)

## Misión
Visualizar **jerarquías de datos anidadas** usando círculos dentro de círculos. Es una alternativa orgánica y visualmente atractiva al Treemap. Aunque menos eficiente en espacio (hay huecos entre círculos), muestra la profundidad de la jerarquía de una manera más intuitiva.

## Guía de Ejes

### Conceptos Clave
-   **Círculo Padre**: El nivel superior (Continente).
-   **Círculos Hijos**: Los niveles inferiores (Países) *contenidos* dentro del padre.
-   **Tamaño (Radius)**: Proporcional al valor de la métrica (Población).
-   **Color**: Codifica la categoría del nivel superior o una métrica secundaria.

### ¿Cuándo usarlo?
-   Exploración de datos cualitativos (temas, categorías).
-   Estructuras organizacionales donde los *grupos* importan más que los valores exactos.
-   Visualizaciones artísticas o de impacto.

---

## Implementación

### 1. D3.js (Nativo - La Mejor Opción)
Circle Packing es nativo de D3.js y se ve increíble. En Python puro es difícil de lograr con la misma calidad interactiva.

### 2. Plotly (Simulación o Wrapper)
Plotly no tiene `go.CirclePacking` directo. Se suele usar un Treemap o Sunburst como alternativa.
Sin embargo, se puede simular o usar librerías como `circlify`.

```python
import circlify
import matplotlib.pyplot as plt

# Datos: Lista de diccionarios {id, datum}
data = [
    {'id': 'World', 'datum': 100, 'children': [
        {'id': "Asia", 'datum': 60, 'children': [
            {'id': "China", 'datum': 30},
            {'id': "India", 'datum': 30}
        ]},
        {'id': "Europe", 'datum': 40, 'children': [
            {'id': "UK", 'datum': 10},
            {'id': "Germany", 'datum': 30}
        ]}
    ]}
]

# Calcular Círculos
circles = circlify.circlify(
    data, 
    show_enclosure=False, 
    target_enclosure=circlify.Circle(x=0, y=0, r=1)
)

# Plotear
fig, ax = plt.subplots(figsize=(10, 10))
ax.axis('off')
lim = max(
    max(
        abs(circle.x) + circle.r,
        abs(circle.y) + circle.r,
    )
    for circle in circles
)
plt.xlim(-lim, lim)
plt.ylim(-lim, lim)

for circle in circles:
    x, y, r = circle.x, circle.y, circle.r
    ax.add_patch(plt.Circle((x, y), r, alpha=0.2, linewidth=2))
    plt.annotate(
        circle.ex['id'], 
        (x,y),
        va='center',
        ha='center'
    )
```

---

## Reglas de Diseño

1.  **Zoomable**: Al igual que el Treemap, debe permitir hacer zoom (entrar en un círculo) para ver los detalles.
2.  **Etiquetas Claras**: Solo etiqueta los círculos grandes. Los pequeños deben mostrarse solo al hacer hover.
3.  **Espacio Negativo**: Acepta que habrá espacio vacío. Úsalo para respirar visualmente.
4.  **Profundidad Limitada**: Muestra 1 o 2 niveles a la vez.

## Origen
Skill basada en Nivel 5 (Innovación) del curso Data Viz, enfocada en visualización jerárquica orgánica.
