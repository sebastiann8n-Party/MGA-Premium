# Skill: Diagrama de Coordenadas Paralelas (Parallel Coordinates)

## Misión
Comparar **observaciones individuales** a través de los valores de múltiples variables simultáneamente, descubriendo patrones, agrupaciones y relaciones entre dimensiones que serían invisibles en gráficos bidimensionales convencionales.

## Guía de Ejes

### Ejes — Múltiples Ejes Y Verticales (Numéricos o Categóricos)
A diferencia de la mayoría de los gráficos, las Coordenadas Paralelas **no tienen un Eje X convencional**. En su lugar, consisten en **múltiples ejes verticales paralelos**, donde cada eje representa el rango de una variable diferente.

- **¿Qué representa cada eje?**: Cada eje vertical es una **variable de interés** del dataset. Los valores de una misma observación en cada variable se conectan con líneas que cruzan todos los ejes.
- **¿Cuándo usarlo?**:
  - Cuando necesitas comparar **3 o más variables numéricas** para cada observación.
  - Para detectar **clusters o grupos** naturales en los datos.
  - Para identificar **patrones de comportamiento** entre variables (ej: cuando una variable sube, ¿las demás suben o bajan?).
  - Para análisis exploratorio **multidimensional** sin reducción de dimensionalidad.
  - Para comparar **perfiles** de entidades (productos, personas, regiones).
- **¿Cuándo NO usarlo?**:
  - Con **pocas variables** (2 o menos) — usa Scatter Plot en su lugar.
  - Con **demasiadas observaciones** sin filtro — las líneas se sobreponen y el gráfico se vuelve ilegible ("spaghetti plot").
  - Cuando las variables tienen **escalas muy diferentes** y no se normalizan — los ejes con rangos grandes dominarán visualmente.
  - Para mostrar **distribuciones** de una sola variable — usa histograma o boxplot.
  - Para mostrar **relaciones causales** — este gráfico muestra correlaciones, no causalidad.

### Variable de Color (Categórica o Numérica)
- **¿Qué representa?**: Una variable **diferenciadora** que colorea las líneas para identificar grupos o gradientes.
- **¿Cuándo usarla?**: Siempre que tengas una variable categórica (especie, tipo, clase) que permita distinguir subgrupos.
- **¿Cuándo NO usarla?**: Si el color no aporta información adicional o si la variable categórica tiene demasiadas categorías (>7), el color pierde utilidad.

## Reglas de Diseño

1. **Normalización**: Si las variables tienen escalas muy diferentes (ej: 0-50 vs 0-5000), considera normalizar los datos para que cada eje tenga un rango comparable.
2. **Orden de ejes**: El orden en que se disponen los ejes afecta la legibilidad. Coloca variables correlacionadas de forma adyacente para facilitar la detección de patrones.
3. **Opacidad**: Con muchas observaciones, reduce la opacidad de las líneas (`opacity=0.5` o menos) para evitar saturación visual.
4. **Muestreo**: Si tienes miles de observaciones, muestra un subconjunto representativo.
5. **Color significativo**: Usa la variable de color para representar una categoría que aporte valor al análisis, no de forma decorativa.

## Implementación en Plotly Express (Interactivo)

### Preparación de Datos
```python
import pandas as pd
import plotly.express as px

# Cargar datos (ejemplo: dataset de pingüinos)
df = pd.read_csv('data/pinguinos.csv')
df = df.dropna()  # Eliminar valores nulos para evitar errores

# Para usar color con variable categórica, convertir a códigos numéricos
df['species_id'] = df['species'].astype('category').cat.codes
```

### Gráfico Básico de Coordenadas Paralelas
```python
fig = px.parallel_coordinates(
    df,
    color="species_id",
    dimensions=['culmen_length_mm', 'culmen_depth_mm', 
                'flipper_length_mm', 'body_mass_g'],
    color_continuous_scale=px.colors.diverging.Tealrose
)
fig.show()
```

### Parámetros Principales de `px.parallel_coordinates()`
| Parámetro | Tipo | Descripción |
|---|---|---|
| `data_frame` | DataFrame | Dataset con las observaciones |
| `dimensions` | list[str] | Lista de columnas numéricas a representar como ejes |
| `color` | str | Columna numérica para colorear las líneas (gradiente) |
| `color_continuous_scale` | str/list | Escala de colores para el gradiente |
| `labels` | dict | Diccionario para renombrar etiquetas de ejes |
| `title` | str | Título del gráfico |

### Personalización Avanzada
```python
fig = px.parallel_coordinates(
    df,
    color="species_id",
    dimensions=['culmen_length_mm', 'culmen_depth_mm', 
                'flipper_length_mm', 'body_mass_g'],
    color_continuous_scale=px.colors.diverging.Tealrose,
    labels={
        'culmen_length_mm': 'Largo Pico (mm)',
        'culmen_depth_mm': 'Profundidad Pico (mm)',
        'flipper_length_mm': 'Largo Aleta (mm)',
        'body_mass_g': 'Masa Corporal (g)',
        'species_id': 'Especie'
    },
    title='Comparación Multidimensional de Especies de Pingüinos'
)

# Personalizar el layout
fig.update_layout(
    font=dict(size=12),
    margin=dict(l=80, r=80, t=60, b=40),
    paper_bgcolor='white',
    plot_bgcolor='white'
)

fig.show()
```

### Filtrado Interactivo de Rangos
Una ventaja clave de Plotly es que el usuario puede **arrastrar rangos en cada eje** para filtrar observaciones interactivamente. Esto permite:
- Seleccionar un subconjunto de datos en un eje y ver cómo se comportan en los demás.
- Descubrir clusters de forma visual e interactiva.

### Reordenación de Ejes
En Plotly, los ejes se pueden **arrastrar y reordenar** interactivamente. Esto permite explorar diferentes combinaciones de variables adyacentes para descubrir correlaciones.

## Mejores Prácticas

1. **Limpieza de datos**: Eliminar valores nulos (`dropna()`) antes de graficar. Los `NaN` rompen las líneas y distorsionan el gráfico.
2. **Conversión categórica → numérica**: `px.parallel_coordinates()` requiere que la variable de color sea numérica. Usa `.astype('category').cat.codes` para convertir.
3. **Escalas de color**: Usa escalas divergentes (`Tealrose`, `RdYlGn`, `Spectral`) para distinguir mejor los grupos.
4. **Alternativa categórica**: Si tus ejes incluyen variables categóricas, usa `px.parallel_categories()` en lugar de `px.parallel_coordinates()`.
5. **Exportación**: Guarda como HTML interactivo con `fig.write_html('coordenadas.html')` para compartir la interactividad.

## Tabla Resumen de Comandos

| Acción | Comando |
|---|---|
| Coordenadas Paralelas (numérico) | `px.parallel_coordinates(df, color='var', dimensions=[...])` |
| Coordenadas Paralelas (categórico) | `px.parallel_categories(df, color='var', dimensions=[...])` |
| Escala de color divergente | `color_continuous_scale=px.colors.diverging.Tealrose` |
| Escala de color secuencial | `color_continuous_scale=px.colors.sequential.Viridis` |
| Renombrar ejes | `labels={'col_original': 'Etiqueta Nueva'}` |
| Guardar como HTML interactivo | `fig.write_html('archivo.html')` |
| Guardar como imagen estática | `fig.write_image('archivo.png', width=1200, height=600, scale=2)` |

## Origen
Código extraído y documentado a partir de: `contexto/nivel2/10coordenas.ipynb`
