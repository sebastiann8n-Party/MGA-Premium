# Skill: Gráfico de Áreas

## Misión
Crear visualizaciones que muestren la magnitud de cambio a lo largo del tiempo mediante el relleno del área bajo la línea, permitiendo enfatizar el volumen total y facilitar la comparación de contribuciones cuando se utilizan áreas apiladas.

## Guía de Uso

### Cuándo usar
- Mostrar el volumen o magnitud total de una variable a lo largo del tiempo
- Visualizar la contribución de diferentes categorías a un total (áreas apiladas)
- Enfatizar la acumulación o depleción de valores
- Comparar la proporción de componentes en una serie temporal

### Cuándo NO usar
- Si las áreas se superponen mucho y dificultan la lectura (considerar líneas simples)
- Cuando la precisión de valores individuales es crítica (usar gráfico de líneas)
- Si hay muchas categorías (max 5-6 para áreas apiladas)
- Cuando los valores son negativos (puede causar confusión visual)

## Tipos de Variables por Eje

| Elemento | Tipo de Variable | Descripción |
|----------|------------------|-------------|
| X | Categórica Ordinal | Variable con orden natural (tiempo, categorías ordenadas) |
| Y | Numérica (positiva) | Variable cuantitativa continua no negativa |
| Áreas | Categórica Nominal (opcional) | Cada área representa un grupo/categoría |

## Implementación Python (con principios DAMA y estética premium)

### 1. Gráfico de Área Simple

```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Configuración de estilo premium
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (14, 7)
plt.rcParams['font.family'] = 'sans-serif'

def grafico_area_simple(data, x, y, title="Gráfico de Área",
                        xlabel=None, ylabel=None, color='#2E86AB',
                        alpha=0.6):
    """
    Crea un gráfico de área simple con diseño premium
    
    Parámetros DAMA:
    ---------------
    data : DataFrame
        Datos limpios y validados
    x : str
        Nombre de la columna para el eje X (variable ordenada)
    y : str
        Nombre de la columna para el eje Y (variable numérica positiva)
    title : str
        Título descriptivo del gráfico
    xlabel : str, opcional
        Etiqueta del eje X
    ylabel : str, opcional
        Etiqueta del eje Y
    color : str
        Color del área
    alpha : float
        Transparencia del relleno (0-1)
    """
    
    # DAMA: Limpiar datos nulos
    clean_data = data.dropna(subset=[x, y])
    
    # DAMA: Verificar que los valores sean no negativos
    if (clean_data[y] < 0).any():
        print("⚠️ Advertencia: Hay valores negativos. El gráfico de área funciona mejor con valores positivos.")
    
    # DAMA: Ordenar por variable X
    clean_data = clean_data.sort_values(by=x)
    
    # Crear figura con estética premium
    fig, ax = plt.subplots(figsize=(14, 7))
    
    # Crear área rellena
    ax.fill_between(clean_data[x], clean_data[y], 
                    color=color, alpha=alpha, 
                    linewidth=0)
    
    # Agregar línea del borde superior
    ax.plot(clean_data[x], clean_data[y],
            color=color, linewidth=2.5, alpha=1)
    
    # Configuración de ejes y título
    ax.set_xlabel(xlabel if xlabel else x.capitalize(), fontsize=14, fontweight='600')
    ax.set_ylabel(ylabel if ylabel else y.capitalize(), fontsize=14, fontweight='600')
    ax.set_title(title, fontsize=18, fontweight='bold', pad=20)
    
    # Estética premium
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.grid(axis='y', linestyle=':', alpha=0.3, color='gray')
    ax.set_ylim(bottom=0)  # Comenzar desde 0 para enfatizar el área
    
    # Rotar etiquetas del eje X si son muchas
    if len(clean_data) > 10:
        plt.xticks(rotation=45, ha='right')
    
    plt.tight_layout()
    plt.show()

# Ejemplo: Ventas totales mensuales
df_mensual = df.groupby('fecha')['sales'].sum().reset_index()
df_mensual.columns = ['Mes', 'Ventas']

grafico_area_simple(
    data=df_mensual,
    x='Mes',
    y='Ventas',
    title='Evolución del Volumen de Ventas Mensuales',
    xlabel='Periodo',
    ylabel='Ventas Totales ($)',
    color='#06AED5',
    alpha=0.4
)
```

### 2. Gráfico de Áreas Apiladas (Stacked Area Chart)

```python
def grafico_areas_apiladas(data, x, y, hue, title="Distribución de Componentes",
                          xlabel=None, ylabel=None, palette='Set2',
                          alpha=0.7):
    """
    Crea un gráfico de áreas apiladas para mostrar contribución de categorías
    
    Parámetros DAMA:
    ---------------
    data : DataFrame
        Datos limpios y validados
    x : str
        Nombre de la columna para el eje X (variable ordenada)
    y : str
        Nombre de la columna para el eje Y (variable numérica positiva)
    hue : str
        Columna que diferencia las áreas (categorías)
    title : str
        Título descriptivo del gráfico
    xlabel : str, opcional
        Etiqueta del eje X
    ylabel : str, opcional
        Etiqueta del eje Y
    palette : str or list
        Paleta de colores curada
    alpha : float
        Transparencia del relleno
    """
    
    # DAMA: Limpiar datos nulos
    clean_data = data.dropna(subset=[x, y, hue])
    
    # DAMA: Verificar número de categorías
    n_categories = clean_data[hue].nunique()
    if n_categories > 6:
        print(f"⚠️ Advertencia: {n_categories} categorías. Considere reducir a máximo 6 para mejor legibilidad.")
    
    # Pivotar datos para formato de áreas apiladas
    pivot_data = clean_data.pivot_table(index=x, columns=hue, values=y, aggfunc='sum', fill_value=0)
    pivot_data = pivot_data.sort_index()
    
    # Crear figura con estética premium
    fig, ax = plt.subplots(figsize=(14, 7))
    
    # Obtener colores
    if isinstance(palette, str):
        colors = sns.color_palette(palette, n_colors=len(pivot_data.columns))
    else:
        colors = palette
    
    # Crear áreas apiladas
    ax.stackplot(pivot_data.index, 
                 *[pivot_data[col] for col in pivot_data.columns],
                 labels=pivot_data.columns,
                 colors=colors,
                 alpha=alpha)
    
    # Configuración de ejes y título
    ax.set_xlabel(xlabel if xlabel else x.capitalize(), fontsize=14, fontweight='600')
    ax.set_ylabel(ylabel if ylabel else y.capitalize(), fontsize=14, fontweight='600')
    ax.set_title(title, fontsize=18, fontweight='bold', pad=20)
    
    # Estética premium
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.grid(axis='y', linestyle=':', alpha=0.3, color='gray')
    
    # Leyenda profesional
    ax.legend(title=hue.capitalize(),
             loc='upper left',
             frameon=True,
             fancybox=True,
             shadow=True,
             fontsize=11)
    
    # Rotar etiquetas del eje X si son muchas
    if len(pivot_data.index) > 10:
        plt.xticks(rotation=45, ha='right')
    
    plt.tight_layout()
    plt.show()

# Ejemplo: Distribución de ventas por familia de productos en 2015
df_2015 = df[df['fecha'].str.startswith('2015')]
familias = ['SEAFOOD', 'DAIRY', 'MEATS']
df_filtered = df_2015[df_2015['family'].isin(familias)]

df_apilado = df_filtered.groupby(['fecha', 'family'])['sales'].sum().reset_index()
df_apilado.columns = ['Mes', 'Familia', 'Ventas']

grafico_areas_apiladas(
    data=df_apilado,
    x='Mes',
    y='Ventas',
    hue='Familia',
    title='Contribución de Familias al Total de Ventas (2015)',
    xlabel='Periodo',
    ylabel='Ventas Acumuladas ($)',
    palette=['#06AED5', '#F37748', '#87C38F'],
    alpha=0.7
)
```

### 3. Gráfico de Áreas con Porcentaje (100% Stacked)

```python
def grafico_areas_porcentaje(data, x, y, hue, title="Distribución Porcentual",
                             xlabel=None, ylabel="Porcentaje (%)", 
                             palette='Set2', alpha=0.7):
    """
    Crea un gráfico de áreas apiladas al 100% para mostrar proporciones
    """
    
    # DAMA: Limpiar datos nulos
    clean_data = data.dropna(subset=[x, y, hue])
    
    # Pivotar y calcular porcentajes
    pivot_data = clean_data.pivot_table(index=x, columns=hue, values=y, aggfunc='sum', fill_value=0)
    pivot_data = pivot_data.sort_index()
    
    # Convertir a porcentajes
    pivot_pct = pivot_data.div(pivot_data.sum(axis=1), axis=0) * 100
    
    # Crear figura con estética premium
    fig, ax = plt.subplots(figsize=(14, 7))
    
    # Obtener colores
    if isinstance(palette, str):
        colors = sns.color_palette(palette, n_colors=len(pivot_pct.columns))
    else:
        colors = palette
    
    # Crear áreas apiladas al 100%
    ax.stackplot(pivot_pct.index,
                 *[pivot_pct[col] for col in pivot_pct.columns],
                 labels=pivot_pct.columns,
                 colors=colors,
                 alpha=alpha)
    
    # Configuración de ejes y título
    ax.set_xlabel(xlabel if xlabel else x.capitalize(), fontsize=14, fontweight='600')
    ax.set_ylabel(ylabel, fontsize=14, fontweight='600')
    ax.set_title(title, fontsize=18, fontweight='bold', pad=20)
    ax.set_ylim(0, 100)
    
    # Estética premium
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.grid(axis='y', linestyle=':', alpha=0.3, color='gray')
    
    # Leyenda profesional
    ax.legend(title=hue.capitalize(),
             loc='best',
             frameon=True,
             fancybox=True,
             shadow=True,
             fontsize=11)
    
    # Rotar etiquetas del eje X si son muchas
    if len(pivot_pct.index) > 10:
        plt.xticks(rotation=45, ha='right')
    
    plt.tight_layout()
    plt.show()

# Ejemplo: Distribución porcentual de ventas
grafico_areas_porcentaje(
    data=df_apilado,
    x='Mes',
    y='Ventas',
    hue='Familia',
    title='Distribución Porcentual de Ventas por Familia (2015)',
    xlabel='Periodo',
    palette=['#06AED5', '#F37748', '#87C38F']
)
```

## Ejemplo de Aplicación: Dataset Titanic

```python
# Analizar supervivencia por clase a lo largo de las edades
# Crear grupos de edad
df['AgeGroup'] = pd.cut(df['Age'], bins=[0, 18, 35, 50, 100], 
                        labels=['0-18', '19-35', '36-50', '50+'])

supervivencia_edad = df.groupby(['AgeGroup', 'Pclass'])['Survived'].sum().reset_index()

grafico_areas_apiladas(
    data=supervivencia_edad,
    x='AgeGroup',
    y='Survived',
    hue='Pclass',
    title='Supervivientes por Grupo de Edad y Clase',
    xlabel='Grupo de Edad',
    ylabel='Número de Supervivientes',
    palette=['#DD1C1A', '#F37748', '#87C38F']
)
```

## Consejos de Diseño

### Principios DAMA
1. **Valores no negativos**: Verificar que los datos sean ≥ 0
2. **Agregación correcta**: Asegurar que las sumas sean coherentes
3. **Orden de categorías**: En áreas apiladas, ordenar por relevancia (categoría más grande abajo)
4. **Normalización**: Para comparaciones, considerar usar porcentajes

### Estética Premium
1. **Transparencia adecuada**: Alpha entre 0.6-0.8 para evitar áreas demasiado oscuras
2. **Límite del eje Y**: Comenzar en 0 para enfatizar el volumen
3. **Colores armoniosos**: Usar paletas que no causen fatiga visual
4. **Máximo 5-6 áreas**: En gráficos apilados, más categorías dificultan la lectura
5. **Líneas de borde**: Agregar línea superior para delimitar el área

## Comparación: Área vs. Línea

| Característica | Gráfico de Área | Gráfico de Línea |
|---------------|-----------------|------------------|
| **Énfasis** | Volumen/Magnitud | Tendencia/Cambio |
| **Inicio en 0** | Sí (recomendado) | No necesario |
| **Comparación** | Total acumulado | Valores individuales |
| **Precisión** | Menor | Mayor |
| **Uso típico** | Series de tiempo con volumen | Cualquier serie ordenada |

## Errores Comunes a Evitar

❌ **Demasiadas áreas apiladas** - Dificulta identificar contribuciones individuales
❌ **Valores negativos** - Causa confusión visual en el área rellena
❌ **Colores muy saturados** - Con transparencia, se vuelven difíciles de leer
❌ **Sin ordenar categorías** - En apiladas, la categoría más importante debe estar abajo
❌ **Escalas inconsistentes** - Al comparar múltiples gráficos de área

## Variantes del Gráfico de Área

1. **Área Simple**: Una sola serie de datos
2. **Áreas Apiladas**: Múltiples series sumadas
3. **100% Apiladas**: Muestra proporciones que suman 100%
4. **Áreas Solapadas**: Áreas transparentes superpuestas (usar con cuidado)
5. **Stream Graph**: Áreas apiladas simétricas alrededor de un eje central

## Otros Nombres
- Area Chart
- Area Graph
- Stacked Area Chart (apilado)
- Stream Graph (variante)
- Gráfico de Área Temporal

## Referencias
- Tufte, E. R. (2001). The Visual Display of Quantitative Information
- Cleveland, W. S. (1993). Visualizing Data
- Few, S. (2012). Show Me the Numbers: Designing Tables and Graphs
- Principios DAMA-DMBOK para visualización de datos
