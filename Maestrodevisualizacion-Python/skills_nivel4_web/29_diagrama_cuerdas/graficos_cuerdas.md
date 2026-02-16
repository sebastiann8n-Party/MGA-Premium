# Skill: Diagrama de Cuerdas (Chord Diagram)

## Misión
Visualizar las **interrelaciones bidireccionales** entre un conjunto de entidades en forma circular. Es especialmente útil para mostrar flujos de matriz origen-destino (quién envía a quién y cuánto), revelando patrones de dominancia y reciprocidad que un Sankey no siempre captura bien.

## Guía de Ejes

### Conceptos Clave
-   **Arco Exterior**: Representa el tamaño total de la entidad (Nodo).
-   **Cuerda (Chord)**: Banda curva que conecta dos entidades. El grosor en cada extremo representa el flujo saliente.
-   **Auto-lazo**: Flujo que sale y llega a la misma entidad (ej: vuelos domésticos dentro de un mismo país).

### ¿Cuándo usarlo?
-   Migración global (personas moviéndose entre países).
-   Comercio internacional (Exportaciones/Importaciones).
-   Superposición de genes o datos biomédicos.
-   Votos transferidos entre partidos políticos.

---

## Implementación

### 1. Holoviews + Bokeh (Interactivo y Simple)
Python no tiene una librería de Chord Diagram nativa tan fuerte como D3.js, pero Holoviews simplifica mucho la creación.

```python
import holoviews as hv
from holoviews import opts
import pandas as pd

hv.extension('bokeh')

# Datos: Origen, Destino, Valor
data = [
    ('Group A', 'Group B', 10),
    ('Group A', 'Group C', 20),
    ('Group B', 'Group A', 5),
    ('Group B', 'Group C', 15),
    ('Group C', 'Group A', 5),
    ('Group C', 'Group B', 20)
]

# Crear Dataset de Holoviews
chord = hv.Chord(data)

# Estilar
chord.opts(
    opts.Chord(
        cmap='Category20', 
        edge_cmap='Category20', 
        edge_color='source', # Color de la cuerda igual al origen
        labels='source', 
        node_color='index',
        width=600, height=600
    )
)
```

### 2. Plotly (Simulación Avanzada)
Plotly no tiene `go.Chord`. Se suele simular usando un truco complejo de polígonos o bajando a D3.js. Sin embargo, para fines prácticos en Python puro, se recomienda Holoviews o `mne` (librería de neurociencia que tiene buenos plots circulares).

Si necesitas estrictamente Python puro y alta calidad, considera usar `pycirclize`.

```python
from pycirclize import Circos
import pandas as pd

# Matriz de Adyacencia
df = pd.DataFrame(
    [[10, 20, 5], [5, 15, 20], [5, 20, 10]],
    index=["A", "B", "C"],
    columns=["A", "B", "C"],
)

circos = Circos.initialize_from_matrix(
    df,
    space=3,
    r_lim=(93, 100),
    cmap="tab10",
    label_kws=dict(r=104, size=12, color="black"),
    link_kws=dict(ec="black", lw=0.5, direction=1),
)

fig = circos.plotfig()
```

---

## Reglas de Diseño

1.  **Ordenamiento**: Agrupa entidades relacionadas cerca unas de otras en el círculo.
2.  **Color de la Cuerda**: 
    -   *Opción A*: Color del origen (muestra quién envía).
    -   *Opción B*: Gradiente (muestra la transición).
3.  **Filtrado**: El "Hairball" (bola de pelos) es un problema común. Filtra las conexiones con valores muy bajos (<1% del total) para limpiar el gráfico.
4.  **Interactividad**: Dado que las cuerdas se superponen, el `MouseOver` (pasar el mouse) para resaltar una sola entidad y sus conexiones es CRÍTICO para la legibilidad.

## Origen
Skill desarrollada para Nivel 4 (Avanzado Web) cubriendo visualización circular de relaciones complejas.
