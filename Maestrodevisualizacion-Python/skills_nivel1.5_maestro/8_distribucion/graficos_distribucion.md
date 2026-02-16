# Skill: Gráficos de Distribución (Histogramas y Boxplots)

## Misión
Entender la forma, el centro y la dispersión de los datos. Estos gráficos revelan la frecuencia de los valores, la presencia de valores atípicos (outliers) y la simetría de la distribución.

## 1. Histogramas (Frecuencia de Rangos)
Dividen los datos en "contenedores" (bins) y cuentan cuántas observaciones caen en cada uno.

### Seaborn: `histplot` (El más completo)
```python
import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("penguins")

# kde=True: Agrega una línea de densidad suavizada
# bins: Controla el número de barras
sns.histplot(data=df, x="body_mass_g", kde=True, bins=30, color="teal")
plt.title("Distribución de la Masa Corporal (Pingüinos)")
plt.show()
```

### Plotly: `px.histogram` (Interactivo)
```python
import plotly.express as px
fig = px.histogram(df, x="body_mass_g", nbins=30, marginal="rug") # rug: líneas de densidad en el borde
fig.show()
```

## 2. Boxplots (Gráficos de Caja y Bigotes)
Resumen estadístico de 5 números: Mínimo, Q1 (25%), Mediana (50%), Q3 (75%) y Máximo. Son ideales para detectar Outliers.

### Seaborn: `boxplot`
```python
# Comparación de distribución por categorías
sns.boxplot(data=df, x="species", y="body_mass_g", palette="Set3")
plt.title("Distribución de Masa por Especie")
plt.show()
```

### Plotly: `px.box`
```python
fig = px.box(df, x="species", y="body_mass_g", points="all") # points="all": muestra todos los puntos
fig.show()
```

## 3. Violin Plots (Caja + Densidad)
Combinan un Boxplot con un gráfico de densidad KDE, mostrando de forma más clara si hay múltiple picos (bimodalidad).

```python
sns.violinplot(data=df, x="species", y="body_mass_g", inner="quart")
plt.show()
```

## Reglas de Oro
1.  **Elección de Bins:** En un histograma, muy pocos bins ocultan patrones; demasiados bins crean ruido. Prueba con `bins='auto'`.
2.  **Outliers:** Si el Boxplot muestra puntos fuera de los "bigotes", investígalos; pueden ser errores de datos o descubrimientos importantes.
3.  **Comparación:** Usa el mismo eje Y cuando compares distribuciones de diferentes grupos para no engañar al ojo.

## Resumen de Métodos
| Tipo | Seaborn | Plotly | Matplotlib |
|---|---|---|---|
| **Histograma** | `sns.histplot()` | `px.histogram()` | `plt.hist()` |
| **Boxplot** | `sns.boxplot()` | `px.box()` | `plt.boxplot()` |
| **Violin** | `sns.violinplot()` | `px.violin()` | `plt.violinplot()` |
