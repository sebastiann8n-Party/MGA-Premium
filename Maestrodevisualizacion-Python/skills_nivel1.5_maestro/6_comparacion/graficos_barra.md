# Skill: Gráficos de Comparación (Barras)

## Misión
Comparar la magnitud de una variable numérica a través de categorías discretas. Ideal para rankings y comparaciones nominales.

## Reglas de Diseño
1.  **Orden:** Ordena las barras de mayor a menor (o viceversa) para facilitar la lectura, a menos que la categoría tenga un orden natural intrínseco (ej. días de la semana, meses).
2.  **Etiquetas:** Si las etiquetas de categoría son largas, usa **barras horizontales** para evitar inclinar el texto.
3.  **Base Cero:** El eje numérico DEBE comenzar en cero.

## 1. Matplotlib (Control Manual)
```python
import matplotlib.pyplot as plt

categorias = ['A', 'B', 'C', 'D']
valores = [10, 25, 15, 30]

# Barras Verticales
plt.bar(categorias, valores, color='skyblue')
plt.title("Comparación Simple (Vertical)")
plt.show()

# Barras Horizontales (Recomendado para etiquetas largas)
plt.barh(categorias, valores, color='salmon')
plt.title("Comparación Simple (Horizontal)")
plt.show()
```

## 2. Seaborn (Agregación Automática)
Seaborn puede agregar datos crudos (promedio por defecto) o contar frecuencias.

### Barplot (Con Agregación)
Calcula el promedio (u otra métrica) con intervalo de confianza.
```python
import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("tips")

# Promedio de propina por día, ordenado por magnitud
# 'order' permite definir el orden manualmente o dinámicamente
order = df.groupby('day')['tip'].mean().sort_values(ascending=False).index

sns.barplot(data=df, x='tip', y='day', order=order, palette='Blues_r')
plt.title("Promedio de Propina por Día (Ordenado)")
plt.show()
```

### Countplot (Frecuencia)
Cuenta ocurrencias de cada categoría.
```python
sns.countplot(data=df, x='sex', palette='Set2')
plt.title("Cantidad de Registros por Sexo")
plt.show()
```

## 3. Plotly (Interactivo)
Ideal para tooltips informativos.

### Barras Simples
```python
import plotly.express as px

# Si los datos ya están agregados/resumidos
df_resumen = px.data.medals_long()

fig = px.bar(
    df_resumen, 
    x="nation", 
    y="count", 
    color="medal", # Barras apiladas por defecto
    title="Medallas por Nación",
    barmode='group' # 'group' para agrupar, 'relative' o 'stack' para apilar
)
fig.show()
```

### Orientación Horizontal
Plotly detecta automáticamente la orientación si mapeas una variable numérica a X y una categórica a Y.
```python
fig = px.bar(
    df_resumen, 
    x="count", 
    y="nation", 
    color="medal",
    orientation='h',
    title="Medallas (Horizontal)"
)
fig.show()
```

## Tips Avanzados
- **Barras Apiladas (Stacked):** Útiles para ver el total y la composición (Plotly `barmode='stack'`, Matplotlib `bottom=...`).
- **Valores en Barras:** Agrega el valor numérico al final de la barra para precisión.
    - Matplotlib: `ax.bar_label(container)`
    - Plotly: `text='valor', text_auto=True`
