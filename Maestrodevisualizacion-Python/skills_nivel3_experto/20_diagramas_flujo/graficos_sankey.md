# Skill: Diagrama Sankey y Chord (Flujos)

## Misión
Visualizar la **magnitud del flujo** entre nodos en una red. Representa transferencias de energía, dinero, materiales o usuarios a través de un sistema. A diferencia del grafo de redes, aquí el *grosor* de la conexión (link) es proporcional a la cantidad transferida, mostrando claramente las pérdidas o ganancias en cada etapa.

## Guía de Ejes

### Conceptos Clave
-   **Nodos (Nodes)**: Las etapas o categorías (Fuente, Destino).
-   **Enlaces (Links)**: Las conexiones que transportan el flujo.
-   **Volumen (Value)**: La cantidad que fluye. El grosor del enlace es proporcional a este valor.
-   **Color**: Usado para diferenciar categorías o seguir un flujo específico (destacar una ruta crítica).

### ¿Cuándo usarlo?
-   **Análisis de Embudo (Funnel)**: Conversión de usuarios en una web (Visita -> Carrito -> Compra).
-   **Finanzas**: Flujo de caja (Ingresos -> Costos -> Beneficio).
-   **Energía**: Balance energético (Generación -> Pérdidas -> Consumo Final).
-   **Logística**: Movimiento de mercancías entre almacenes.

---

## Implementación

### 1. Plotly (Sankey Interactivo)
Plotly es la herramienta más robusta para crear Sankeys en Python.

```python
import plotly.graph_objects as go

# Definir Nodos (Etiquetas)
labels = ["Salario", "Inversión", "Alquiler", "Comida", "Ahorro", "Viajes"]

# Definir Enlaces (Fuente -> Destino, Valor)
# Índices basados en la lista 'labels': 0=Salario, 1=Inversión, etc.
source = [0, 0, 1, 0, 4, 3] 
target = [2, 3, 4, 1, 5, 2]
value  = [1500, 800, 500, 200, 300, 100] # Cantidad transferida

fig = go.Figure(data=[go.Sankey(
    node = dict(
      pad = 15,
      thickness = 20,
      line = dict(color = "black", width = 0.5),
      label = labels,
      color = "blue"
    ),
    link = dict(
      source = source,
      target = target,
      value = value,
      color = "rgba(0,0,255, 0.2)" # Transparencia para ver superposiciones
  ))])

fig.update_layout(title_text="Presupuesto Mensual (Flujo)", font_size=10)
fig.show()
```

### 2. Holoviews + Bokeh (Alternativa para Dataframes)
Si tienes tus datos en un DataFrame de pandas (Origen, Destino, Valor), Holoviews facilita la creación directa.

```python
import pandas as pd
import holoviews as hv
from holoviews import opts

hv.extension('bokeh')

# Datos en formato largo
df = pd.DataFrame([
    ('A', 'B', 10),
    ('A', 'C', 20),
    ('B', 'D', 5),
    ('C', 'D', 15)
], columns=['source', 'target', 'value'])

# Crear Sankey
sankey = hv.Sankey(df, kdims=['source', 'target'], vdims=['value'])

# Estilar
sankey.opts(opts.Sankey(labels='source', label_position='left', 
                        edge_color='source', node_color='source', cmap='tab20'))
```

### 3. Diagrama de Cuerdas (Chord Diagram) - Avanzado
Para flujos bidireccionales o matrices de interrelación (quién llama a quién). Plotly no tiene un gráfico de cuerdas nativo simple, pero se puede simular o usar librerías específicas como `chord` (wrapper de D3.js).

*Nota: Para análisis estándar, prefiere Sankey por su claridad direccional.*

---

## Reglas de Diseño

1.  **Orden Lógico**: Organiza los nodos de izquierda a derecha siguiendo el flujo temporal o lógico del proceso.
2.  **Simplificación**: Si hay demasiados flujos pequeños ("espagueti"), agrúpalos en una categoría "Otros". El Sankey debe mostrar los patrones *macroscópicos*.
3.  **Color con Propósito**:
    -   Usa el mismo color para un flujo que atraviesa varias etapas si quieres destacar esa ruta específica.
    -   Usa gradientes si el flujo cambia de propiedad (ej: agua fría a caliente).
4.  **Etiquetas Claras**: Asegúrate de que los nodos tengan etiquetas legibles y, si es posible, incluyan el valor total que pasa por ellos (ej: "Ventas: $1M").

## Origen
Skill desarrollada siguiendo estándares de Nivel 3 (Experto) para visualización de flujos complejos.
