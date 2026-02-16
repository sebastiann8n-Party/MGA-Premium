# Skill: Histograma (Maestro de Visualización)

El histograma es la herramienta fundamental para representar la distribución de una variable numérica, permitiendo observar la frecuencia, la forma (normal, sesgada, bimodal) y la dispersión de los datos.

## 1. Misión
Identificar patrones de distribución y frecuencias en datos continuos, facilitando la toma de decisiones estadísticas (ej. validación de normalidad).

## 2. Guía de Uso

### ¿Cuándo usarlo?
- **Distribución de Valores**: Para ver cómo se reparten los datos a lo largo de un rango.
- **Forma de la Curva**: Identificar si los datos siguen una campana de Gauss, si tienen sesgo o si hay múltiples modas (picos).
- **Rangos de Concentración**: Ver en qué intervalos se encuentra la mayor cantidad de registros.

### ¿Cuándo NO usarlo?
- **Variables Categóricas**: Para categorías puras, usa un gráfico de barras.
- **Pocos Datos**: Con muestras muy pequeñas, las barras pueden ser engañosas.

### Tipos de Variables por Eje
- **Eje X (Variable)**: Variable **Cuantitativa Continua** (ej: Age, Fare en Titanic) agrupada en **Bins** (rangos iguales).
- **Eje Y (Frecuencia)**: **Frecuencia Absoluta** o **Relativa** (conteo automático, no requiere variable de entrada del usuario).

### Parámetros Críticos (Bins)
- **Bins (Contenedores)**: El número de barras es vital. Muy pocos ocultan la forma; demasiados crean "ruido". La regla de Sturges (`log2(n) + 1`) es un buen punto de partida.

## 3. Implementación Python (Estilo Premium)

```python
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def plot_histogram_premium(data, x, title, bins=None, hue=None, element="bars", palette="viridis"):
    """
    Genera un histograma con estética premium, incluyendo KDE (densidad) opcional.
    """
    plt.figure(figsize=(12, 6))
    
    # DAMA: Limpieza de nulos para exactitud matemática
    clean_data = data.dropna(subset=[x])
    
    # Gráfico con Seaborn
    ax = sns.histplot(
        data=clean_data,
        x=x,
        hue=hue,
        bins=bins if bins else 'auto',
        kde=True, # Línea de densidad para suavizado
        element=element,
        palette=palette,
        alpha=0.6,
        edgecolor="white",
        linewidth=1.2
    )
    
    # Personalización
    plt.title(title, fontsize=18, fontweight='bold', pad=20)
    plt.xlabel(x.capitalize(), fontsize=13)
    plt.ylabel("Frecuencia", fontsize=13)
    
    sns.despine(trim=True)
    plt.grid(axis='y', linestyle=':', alpha=0.5)
    plt.tight_layout()
    
    return plt
```

## 4. Ejemplo de Aplicación: Titanic (Distribución de Edades y Tarifas)

### Reto 1: Frecuencia de Edades por Sexo
```python
# Ver si las edades de hombres y mujeres se distribuyen igual
plot_histogram_premium(
    data=df_clean,
    x='Age',
    hue='Sex',
    title='Distribución de Edades por Sexo (Titanic)',
    palette='magma'
)
plt.show()
```

### Reto 2: Distribución de Tarifas (Fare)
```python
# Los precios pagados suelen tener un sesgo positivo fuerte
plot_histogram_premium(
    data=df_clean,
    x='Fare',
    title='Concentración de Precios de Pasajes (Fare)',
    bins=30,
    palette='Blues_r'
)
plt.show()
```
