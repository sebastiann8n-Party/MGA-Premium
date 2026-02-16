# Skill: Gráfico Circular / Pie Chart (Maestro de Visualización)

Esta skill orquesta el uso de `Analítica DAMA` y `Visualización Premium` para generar gráficos circulares (tarta) y de dona, ideales para mostrar proporciones y composición.

## 1. Misión
Visualizar la composición porcentual de una variable categórica, siguiendo las mejores prácticas para evitar problemas de legibilidad.

## 2. Guía de Uso

### ¿Cuándo usarlo?
- **Comparación de Partes de un Todo**: Cuando el objetivo es ver cuánto representa cada categoría del total (%).
- **Pocas Categorías**: Ideal para 2 a 5 categorías. Más de esto se vuelve ilegible.
- **Diferencias Evidentes**: Cuando las proporciones son claramente distinguibles a simple vista.

### ¿Cuándo NO usarlo?
- **Muchas Categorías**: Si hay más de 5-6 rebanadas, usa un gráfico de barras.
- **Diferencias Sutiles**: El ojo humano es malo comparando ángulos. Si las categorías son similares (ej: 24% vs 26%), usa barras.
- **Suma no es 100%**: Los datos deben representar un todo completo.

### Tipos de Variables Requeridas
- **Segmentos (Rebanadas)**: Variable **Cualitativa Nominal** (ej: Sex, Embarked en Titanic). Máximo 5-6 categorías.
- **Valores (Tamaño)**: Variable **Cuantitativa Discreta** (conteo) o proporción que sume 100% del total.

### Principios de Diseño Premium
- **Orden**: Ordenar rebanadas de mayor a menor comenzando a las 12 en punto (o 90 grados).
- **Etiquetas Claras**: Usar porcentajes legibles, preferiblemente fuera del gráfico si son pequeños.
- **Dona vs Pie**: El gráfico de Dona (`hole > 0`) suele ser visualmente más ligero y moderno.
- **Evitar 3D**: Nunca usar 3D, distorsiona la percepción de las proporciones.

## 3. Implementación Python (Estilo Premium)

```python
import matplotlib.pyplot as plt
import pandas as pd
# Asumiendo que se tiene acceso a la skill visualizacion_premium para la paleta

def plot_pie_premium(data, labels, values, title, hole=0.5, figsize=(8, 8), palette='viridis'):
    """
    Genera un gráfico de Pie o Dona con estilo premium usando Matplotlib.
    
    Args:
        data (pd.DataFrame): Datos agregados.
        labels (str): Columna con los nombres de las categorías.
        values (str): Columna con los valores numéricos.
        title (str): Título del gráfico.
        hole (float): Tamaño del agujero central (0 para Pie, >0 para Dona).
        figsize (tuple): Tamaño de la figura.
    """
    # Configuración de estilo (reutilizar visualizacion_premium si es posible)
    plt.figure(figsize=figsize)
    
    # Ordenar datos de mayor a menor para mejor lectura
    data = data.sort_values(by=values, ascending=False)
    
    # Colores
    # Se puede usar seaborn para generar la paleta: sns.color_palette(palette, len(data))
    colors = plt.get_cmap(palette)(np.linspace(0.2, 0.7, len(data)))
    
    # Gráfico
    wedges, texts, autotexts = plt.pie(
        data[values], 
        labels=data[labels],
        autopct='%1.1f%%',
        startangle=90,
        counterclock=False, # Sentido reloj
        colors=colors,
        wedgeprops=dict(width=1-hole, edgecolor='w', linewidth=2), # Efecto Dona y borde blanco
        textprops=dict(color="#333333", fontsize=12, fontweight='medium'),
        pctdistance=0.85 if hole > 0 else 0.6
    )
    
    # Ajuste de textos de porcentaje
    plt.setp(autotexts, size=10, weight="bold", color="white")

    # Título
    plt.title(title, fontsize=16, fontweight='bold', pad=20)
    
    # Círculo central si es dona (truco opcional si no se usa wedgeprops width)
    # centre_circle = plt.Circle((0,0), hole, fc='white')
    # fig = plt.gcf()
    # fig.gca().add_artist(centre_circle)
    
    plt.tight_layout()
    return plt

# Ejemplo de uso con Plotly (Interactivo / Web)
import plotly.express as px

def plot_pie_interactive(data, names, values, title, hole=0.5):
    """
    Genera un gráfico de Pie/Dona interactivo con Plotly.
    """
    fig = px.pie(
        data, 
        names=names, 
        values=values, 
        title=title,
        hole=hole,
        color_discrete_sequence=px.colors.sequential.Viridis # Paleta Premium
    )
    fig.update_traces(textposition='inside', textinfo='percent+label')
    fig.update_layout(
        title_font_size=20,
        showlegend=True,
        legend_title_text=None
    )
    return fig

```

## 4. Ejemplo de Aplicación (Titanic - Pasajeros por Sexo)

```python
# Suponiendo carga de datos previa con analitica_dama

# Preparación de datos (DAMA: Agregación validada)
# df_sex = analitica_dama.validated_aggregation(df, 'Sex').reset_index()
# df_sex.columns = ['Sex', 'Count']

# Opción A: Matplotlib (Estático/Reportes)
# plot_pie_premium(
#     data=df_sex, 
#     labels='Sex', 
#     values='Count', 
#     title='Composición de Pasajeros por Sexo', 
#     hole=0.5 # Gráfico de Dona
# )

# Opción B: Plotly (Web/Interactivo)
# fig = plot_pie_interactive(
#    data=df_sex,
#    names='Sex',
#    values='Count',
#    title='Distribución de Pasajeros por Sexo'
# )
# fig.show()
```
