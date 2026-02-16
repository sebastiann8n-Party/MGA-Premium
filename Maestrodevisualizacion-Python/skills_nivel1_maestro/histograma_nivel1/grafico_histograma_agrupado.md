# Skill: Histograma Agrupado / Grouped Histogram (Maestro de Visualización)

El histograma agrupado permite comparar las distribuciones de una variable numérica entre diferentes grupos o categorías, visualizando múltiples distribuciones en un mismo gráfico.

## 1. Misión
Comparar la distribución de una variable numérica entre diferentes grupos categóricos, permitiendo identificar diferencias en la forma, dispersión y concentración de los datos entre categorías.

## 2. Guía de Uso

### ¿Cuándo usarlo?
- **Comparación entre Grupos**: Para ver cómo se distribuye una variable continua en diferentes categorías (ej: Edad por Sexo).
- **Identificar Patrones**: Detectar si diferentes grupos tienen distribuciones similares o distintas.
- **Análisis Exploratorio**: Entender diferencias demográficas o de comportamiento entre segmentos.

### ¿Cuándo NO usarlo?
- **Muchas Categorías**: Con más de 3-4 grupos, el gráfico se vuelve confuso y difícil de interpretar.
- **Datos Escasos**: Si algún grupo tiene muy pocos datos, la distribución será poco representativa.

### Tipos de Variables por Eje
- **Eje X (Variable)**: Variable **Cuantitativa Continua** (ej: Age, Fare) agrupada en **Bins**.
- **Eje Y (Frecuencia)**: **Frecuencia Absoluta** o **Relativa** por categoría.
- **Hue/By (Agrupación)**: Variable **Cualitativa Nominal** (ej: Sex, Pclass). Máximo 3-4 categorías.

### Diseño Premium
- **Colores Diferenciados**: Usar paletas que distingan claramente cada grupo.
- **Transparencia (Alpha)**: Aplicar alpha < 1 para evitar superposición visual y permitir comparación.
- **Leyenda Clara**: Posicionar la leyenda de forma que no obstruya los datos.

## 3. Implementación Python (Estándar Premium)

```python
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def plot_grouped_histogram_premium(data, x, hue, title, bins=None, palette='Set2'):
    """
    Genera un Histograma Agrupado con estética premium para comparar distribuciones entre grupos.
    """
    plt.figure(figsize=(12, 6))
    
    # DAMA: Limpieza de nulos
    clean_data = data.dropna(subset=[x, hue])
    
    # Gráfico con Seaborn
    ax = sns.histplot(
        data=clean_data,
        x=x,
        hue=hue,
        bins=bins if bins else 'auto',
        kde=False,
        element="bars",
        palette=palette,
        alpha=0.6,
        edgecolor="white",
        linewidth=1.2,
        multiple="layer"  # 'layer', 'dodge', 'stack'
    )
    
    # Personalización
    plt.title(title, fontsize=18, fontweight='bold', pad=20)
    plt.xlabel(x.capitalize(), fontsize=13)
    plt.ylabel("Frecuencia", fontsize=13)
    plt.legend(title=hue.capitalize(), loc='upper right')
    
    sns.despine(trim=True)
    plt.grid(axis='y', linestyle=':', alpha=0.5)
    plt.tight_layout()
    
    return plt

```

## 4. Ejemplo de Aplicación: Titanic (Distribución de Edades por Sexo)

### Comparación de Edades entre Hombres y Mujeres
```python
# Limpieza de datos
df_clean = df.dropna(subset=['Age', 'Sex'])

# Visualización usando la Skill
plot_grouped_histogram_premium(
    data=df_clean,
    x='Age',
    hue='Sex',
    title='Distribución de Edades por Sexo (Titanic)',
    bins=15,
    palette='magma'
)
plt.show()

# Análisis:
# - Observar si hay diferencias en las distribuciones de edad entre sexos
# - Identificar picos de concentración distintos entre grupos
```

### Variación: Histograma Dodged (Barras Lado a Lado)
```python
# Para mejor separación visual, usar 'dodge'
sns.histplot(
    data=df_clean,
    x='Age',
    hue='Sex',
    bins=15,
    multiple="dodge",  # Barras lado a lado
    palette='viridis',
    alpha=0.7,
    edgecolor="white"
)
plt.title('Distribución de Edades por Sexo (Modo Dodge)', fontsize=16, fontweight='bold')
plt.tight_layout()
plt.show()
```
