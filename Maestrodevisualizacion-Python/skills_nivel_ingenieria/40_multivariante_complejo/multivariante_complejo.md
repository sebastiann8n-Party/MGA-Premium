# Skill Ingenieria: Análisis Multivariante Complejo (SPLOM, Parallel Categories)

## Misión
Explorar relaciones entre **múltiples variables** (> 3) simultáneamente. Es fundamental para el análisis exploratorio de datos (EDA) y para entender la estructura de datasets complejos antes de modelar.

## Reglas de Oro
1.  **Dimensionalidad:** Usa SPLOM para variables numéricas (correlaciones cruzadas).
2.  **Flujo Categórico:** Usa Parallel Categories para variables categóricas.
3.  **Interactividad:** La selección (brushing) en Plotly es clave: seleccionar datos en un panel resalta los mismos datos en todos los demás.

## 1. SPLOM (Scatter Plot Matrix)
Una matriz de n x n gráficos de dispersión. Cada celda muestra la relación entre dos variables. La diagonal suele mostrar el histograma de la variable.

```python
import plotly.express as px

df = px.data.iris()

fig = px.scatter_matrix(df,
    dimensions=["sepal_width", "sepal_length", "petal_width", "petal_length"], # Variables a comparar
    color="species", # Color por categoría
    title="Matriz de Dispersión (SPLOM) - Dataset Iris",
    labels={col:col.replace('_', ' ').title() for col in df.columns} # Etiquetas limpias
)

# Ajustes visuales para claridad
fig.update_traces(diagonal_visible=False) # Ocultar diagonal (opcional)
fig.show()
```

## 2. Parallel Categories (Categorías Paralelas)
Visualiza cómo los elementos fluyen a través de diferentes categorías. Similar a un diagrama de Sankey pero para datos individuales. Distinto a Parallel Coordinates (numérico).

```python
import plotly.express as px

df = px.data.tips()

# Convertir variables numéricas discretas a string si se quieren tratar como categorías
df["size_str"] = df["size"].astype(str)

fig = px.parallel_categories(df, color="total_bill", color_continuous_scale=px.colors.sequential.Inferno,
    dimensions=['sex', 'smoker', 'day', 'time', 'size_str'],
    title="Flujo de Clientes: Sexo -> Fumador -> Día -> Hora -> Tamaño Grupo",
    labels={'sex':'Sexo', 'smoker':'Fumador', 'day':'Día', 'time':'Hora', 'size_str':'Tamaño Mesa'}
)

fig.show()
```

## 3. Parallel Coordinates (Coordenadas Paralelas - Numérico)
Para comparar perfiles multivariables numéricos. Cada línea es una observación.

```python
import plotly.express as px

df = px.data.iris()

fig = px.parallel_coordinates(df, color="species_id", labels={"species_id": "Species",
                  "sepal_width": "Sepal Width", "sepal_length": "Sepal Length",
                  "petal_width": "Petal Width", "petal_length": "Petal Length", },
                    color_continuous_scale=px.colors.diverging.Tealrose,
                    color_continuous_midpoint=2)
fig.show()
```

## Resumen
| Tipo de Dato | Gráfico Recomendado | Función Plotly |
|---|---|---|
| Todo Numérico | SPLOM | `px.scatter_matrix` |
| Todo Categórico | Parallel Categories | `px.parallel_categories` |
| Perfiles Numéricos | Parallel Coordinates | `px.parallel_coordinates` |
