# Skill: Gráfico de Línea Simple

## Misión
Crear visualizaciones que muestren la tendencia de una variable numérica a lo largo de una secuencia ordenada (generalmente temporal), conectando puntos con líneas rectas para facilitar la identificación de patrones de cambio.

## Guía de Uso

### Cuándo usar
- Analizar tendencias de subida o bajada en variables numéricas
- Visualizar cambios en magnitud a lo largo del tiempo (días, meses, años, etc.)
- Mostrar progresión de datos en una variable categórica ordinal
- Cuando la cantidad de puntos es alta y se quiere ver la tendencia general

### Cuándo NO usar
- Si la variable en el Eje X no tiene una progresión ordenada (usar Gráfico de Barras)
- Si tienes menos de 3 puntos para graficar
- Si quieres comparar proporciones (usar Gráfico Circular)
- Si quieres obtener información sobre distribuciones (usar Histograma o Boxplot)
- Si el único objetivo es comparar magnitudes con pocos puntos (usar Gráfico de Barras)

## Tipos de Variables por Eje

| Eje | Tipo de Variable | Descripción |
|-----|------------------|-------------|
| X | Categórica Ordinal | Variable con orden natural (tiempo, categorías ordenadas) |
| Y | Numérica | Variable cuantitativa continua |

## Implementación Python (con principios DAMA y estética premium)

```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Configuración de estilo premium
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (12, 6)
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['axes.labelsize'] = 13
plt.rcParams['axes.titlesize'] = 18
plt.rcParams['xtick.labelsize'] = 11
plt.rcParams['ytick.labelsize'] = 11

def grafico_linea_simple(data, x, y, title="Gráfico de Línea", 
                         xlabel=None, ylabel=None, color='#2E86AB', 
                         marker='o', linewidth=2.5):
    """
    Crea un gráfico de línea simple con diseño premium
    
    Parámetros DAMA:
    ---------------
    data : DataFrame
        Datos limpios y validados
    x : str
        Nombre de la columna para el eje X (variable ordenada)
    y : str
        Nombre de la columna para el eje Y (variable numérica)
    title : str
        Título descriptivo del gráfico
    xlabel : str, opcional
        Etiqueta del eje X
    ylabel : str, opcional
        Etiqueta del eje Y
    color : str
        Color de la línea (usar paleta curada)
    marker : str
        Símbolo para marcar cada punto
    linewidth : float
        Grosor de la línea
    """
    
    # DAMA: Limpiar datos nulos
    clean_data = data.dropna(subset=[x, y])
    
    # DAMA: Ordenar por variable X para asegurar progresión correcta
    clean_data = clean_data.sort_values(by=x)
    
    # Crear figura con estética premium
    fig, ax = plt.subplots(figsize=(14, 7))
    
    # Trazar línea
    ax.plot(clean_data[x], clean_data[y], 
            color=color, 
            linewidth=linewidth, 
            marker=marker, 
            markersize=7,
            markerfacecolor='white',
            markeredgewidth=2,
            markeredgecolor=color,
            label=ylabel if ylabel else y)
    
    # Configuración de ejes y título
    ax.set_xlabel(xlabel if xlabel else x.capitalize(), fontsize=14, fontweight='600')
    ax.set_ylabel(ylabel if ylabel else y.capitalize(), fontsize=14, fontweight='600')
    ax.set_title(title, fontsize=18, fontweight='bold', pad=20)
    
    # Estética premium
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.grid(axis='y', linestyle=':', alpha=0.4, color='gray')
    
    # Rotar etiquetas del eje X si son muchas
    if len(clean_data) > 10:
        plt.xticks(rotation=45, ha='right')
    
    plt.tight_layout()
    plt.show()

# Ejemplo 1: Ventas mensuales
# Preparar datos agregados por mes
df_mensual = df.groupby('fecha')['sales'].sum().reset_index()
df_mensual.columns = ['Mes', 'Ventas']

grafico_linea_simple(
    data=df_mensual,
    x='Mes',
    y='Ventas',
    title='Evolución de Ventas Mensuales (2013-2016)',
    xlabel='Periodo',
    ylabel='Ventas Totales ($)',
    color='#06AED5'
)
```

## Ejemplo de Aplicación: Dataset Titanic

```python
# Analizar tendencia de edad promedio por clase de pasajero
edad_por_clase = df.groupby('Pclass')['Age'].mean().reset_index()

grafico_linea_simple(
    data=edad_por_clase,
    x='Pclass',
    y='Age',
    title='Edad Promedio por Clase de Pasajero',
    xlabel='Clase',
    ylabel='Edad Promedio',
    color='#DD1C1A'
)
```

## Consejos de Diseño

### Principios DAMA
1. **Limpieza**: Remover valores nulos antes de graficar
2. **Ordenamiento**: Asegurar que los datos estén ordenados por la variable X
3. **Validación**: Verificar que la variable Y sea numérica
4. **Documentación**: Títulos y etiquetas claros y descriptivos

### Estética Premium
1. **No inicies el eje Y en cero** - A diferencia de gráficos de barras, permite ver mejor las variaciones
2. **Usa líneas rectas** - No interpoles o suavices la curva
3. **Marca los puntos** - Si hay pocos datos, usa marcadores visibles
4. **Colores curados** - Evita colores básicos (rojo, azul, verde planos)
5. **Grid sutil** - Solo en el eje Y con líneas punteadas y baja opacidad
6. **Elimina elementos innecesarios** - Bordes superior y derecho

## Otros Nombres
- Line Chart
- Line Graph
- Serie de Tiempo (cuando X es temporal con muchos puntos)
- Gráfico de Tendencia

## Referencias
- Principios DAMA para calidad de datos
- Normas APA 7ma edición para visualización científica
- Tufte, E. R. (2001). The Visual Display of Quantitative Information
