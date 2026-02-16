# Skill: Gráfico Multilinea

## Misión
Crear visualizaciones que comparen múltiples series de datos simultáneamente, mostrando tendencias y relaciones entre diferentes grupos o categorías a lo largo de una variable ordenada.

## Guía de Uso

### Cuándo usar
- Comparar tendencias de múltiples grupos en el mismo periodo
- Analizar la evolución de diferentes categorías de productos/servicios
- Visualizar relaciones entre series de datos relacionadas
- Identificar patrones comunes o divergencias entre grupos

### Cuándo NO usar
- Si tienes más de 5-7 líneas (se vuelve confuso)
- Si las líneas se superponen demasiado (dificulta la lectura)
- Si las variables no tienen una relación lógica entre sí
- Si cada serie merece su propio gráfico para mayor detalle

## Tipos de Variables por Eje

| Elemento | Tipo de Variable | Descripción |
|----------|------------------|-------------|
| X | Categórica Ordinal | Variable con orden natural (tiempo, categorías ordenadas) |
| Y | Numérica | Variable cuantitativa continua |
| Líneas | Categórica Nominal | Cada línea representa un grupo/categoría diferente |

## Implementación Python (con principios DAMA y estética premium)

```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Configuración de estilo premium
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (14, 7)
plt.rcParams['font.family'] = 'sans-serif'

def grafico_multilinea(data, x, y, hue, title="Comparación de Tendencias",
                       xlabel=None, ylabel=None, palette='Set2',
                       linewidth=2.5, markers=True):
    """
    Crea un gráfico multilinea con diseño premium
    
    Parámetros DAMA:
    ---------------
    data : DataFrame
        Datos limpios y validados
    x : str
        Nombre de la columna para el eje X (variable ordenada)
    y : str
        Nombre de la columna para el eje Y (variable numérica)
    hue : str
        Columna que diferencia las líneas (categorías)
    title : str
        Título descriptivo del gráfico
    xlabel : str, opcional
        Etiqueta del eje X
    ylabel : str, opcional
        Etiqueta del eje Y
    palette : str or list
        Paleta de colores curada
    linewidth : float
        Grosor de las líneas
    markers : bool
        Si se deben mostrar marcadores en los puntos
    """
    
    # DAMA: Limpiar datos nulos
    clean_data = data.dropna(subset=[x, y, hue])
    
    # DAMA: Verificar número de categorías
    n_categories = clean_data[hue].nunique()
    if n_categories > 7:
        print(f"⚠️ Advertencia: Visualizando {n_categories} líneas. Considere reducir a máximo 7 para mejor legibilidad.")
    
    # Crear figura con estética premium
    fig, ax = plt.subplots(figsize=(14, 7))
    
    # Obtener categorías únicas
    categories = sorted(clean_data[hue].unique())
    
    # Definir paleta de colores curada
    if isinstance(palette, str):
        colors = sns.color_palette(palette, n_colors=len(categories))
    else:
        colors = palette
    
    # Definir marcadores diferentes para cada línea
    marker_styles = ['o', 's', '^', 'D', 'v', 'p', '*']
    
    # Graficar cada línea
    for idx, category in enumerate(categories):
        data_cat = clean_data[clean_data[hue] == category].sort_values(by=x)
        
        marker = marker_styles[idx % len(marker_styles)] if markers else None
        
        ax.plot(data_cat[x], data_cat[y],
                color=colors[idx],
                linewidth=linewidth,
                marker=marker,
                markersize=8,
                markerfacecolor='white',
                markeredgewidth=2.5,
                markeredgecolor=colors[idx],
                label=category,
                alpha=0.9)
    
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
             loc='best',
             frameon=True,
             fancybox=True,
             shadow=True,
             fontsize=11)
    
    # Rotar etiquetas del eje X si son muchas
    if len(clean_data[x].unique()) > 10:
        plt.xticks(rotation=45, ha='right')
    
    plt.tight_layout()
    plt.show()

# Ejemplo 1: Comparar ventas de 3 familias de productos en 2015
# Filtrar datos para el año 2015 y tres familias específicas
df_2015 = df[df['fecha'].str.startswith('2015')]
familias = ['SEAFOOD', 'DAIRY', 'MEATS']
df_filtered = df_2015[df_2015['family'].isin(familias)]

# Agrupar por mes y familia
df_comparison = df_filtered.groupby(['fecha', 'family'])['sales'].sum().reset_index()
df_comparison.columns = ['Mes', 'Familia', 'Ventas']

grafico_multilinea(
    data=df_comparison,
    x='Mes',
    y='Ventas',
    hue='Familia',
    title='Comparación de Ventas por Familia de Productos (2015)',
    xlabel='Periodo',
    ylabel='Ventas ($)',
    palette=['#06AED5', '#F37748', '#87C38F']
)
```

## Ejemplo Avanzado: Series de Tiempo con Intervalos de Confianza

```python
def grafico_multilinea_con_intervalo(data, x, y, hue, title="Comparación con Intervalos",
                                      xlabel=None, ylabel=None, palette='Set2'):
    """
    Versión avanzada con bandas de confianza
    """
    clean_data = data.dropna(subset=[x, y, hue])
    
    fig, ax = plt.subplots(figsize=(14, 7))
    
    categories = sorted(clean_data[hue].unique())
    colors = sns.color_palette(palette, n_colors=len(categories))
    
    for idx, category in enumerate(categories):
        data_cat = clean_data[clean_data[hue] == category].sort_values(by=x)
        
        # Calcular media y desviación estándar si hay múltiples valores
        grouped = data_cat.groupby(x)[y].agg(['mean', 'std']).reset_index()
        
        # Línea principal
        ax.plot(grouped[x], grouped['mean'],
                color=colors[idx],
                linewidth=2.5,
                marker='o',
                label=category,
                alpha=0.9)
        
        # Banda de confianza (si hay desviación estándar)
        if 'std' in grouped.columns and not grouped['std'].isna().all():
            ax.fill_between(grouped[x],
                           grouped['mean'] - grouped['std'],
                           grouped['mean'] + grouped['std'],
                           color=colors[idx],
                           alpha=0.2)
    
    ax.set_xlabel(xlabel if xlabel else x.capitalize(), fontsize=14, fontweight='600')
    ax.set_ylabel(ylabel if ylabel else y.capitalize(), fontsize=14, fontweight='600')
    ax.set_title(title, fontsize=18, fontweight='bold', pad=20)
    
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.grid(axis='y', linestyle=':', alpha=0.3)
    ax.legend(title=hue.capitalize(), loc='best')
    
    if len(grouped) > 10:
        plt.xticks(rotation=45, ha='right')
    
    plt.tight_layout()
    plt.show()
```

## Consejos de Diseño

### Principios DAMA
1. **Validación de datos**: Verificar que todas las series tengan datos completos
2. **Consistencia**: Asegurar que todas las líneas usen la misma escala
3. **Limpieza**: Remover valores atípicos extremos que distorsionen la visualización
4. **Documentación**: Leyenda clara identificando cada línea

### Estética Premium
1. **Máximo 5-7 líneas**: Más allá de esto, considera múltiples gráficos
2. **Paleta curada**: Usa colores distinguibles pero armoniosos
3. **Marcadores diferentes**: Si hay pocas líneas y pocos puntos
4. **Grosor diferenciado**: Línea principal más gruesa si corresponde
5. **Leyenda estratégica**: Posiciónala donde no oculte datos
6. **Transparencia sutil**: Alpha 0.8-0.9 para permitir ver superposiciones

## Errores Comunes a Evitar

❌ **Demasiadas líneas** - Dificulta la interpretación
❌ **Colores similares** - Las líneas no se distinguen
❌ **Sin leyenda** - No se sabe qué representa cada línea
❌ **Escalas diferentes** - Comparaciones engañosas
❌ **Líneas muy delgadas** - Dificultan la visualización

## Otros Nombres
- Multi-line Chart
- Multiple Line Graph
- Comparative Time Series (cuando X es temporal)
- Gráfico de Líneas Comparativas

## Referencias
- Cleveland, W. S. (1993). Visualizing Data
- Tufte, E. R. (2001). The Visual Display of Quantitative Information
- Principios DAMA-DMBOK para visualización de datos
