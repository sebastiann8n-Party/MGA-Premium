# Skill: Gráfico de Cajas / Box Plot (Maestro de Visualización)

Esta skill permite analizar y visualizar la distribución de datos numéricos a través de sus cuartiles, identificando la mediana, el rango intercuartílico y los datos atípicos (outliers).

## 1. Misión
Extraer información estadística visual sobre la dispersión y centralidad de los datos, permitiendo comparaciones entre grupos (ej. Edad por Sexo) de manera robusta.

## 2. Guía de Uso

### ¿Cuándo usarlo?
- **Comparación de Grupos**: Para ver diferencias en media, mediana y variabilidad entre categorías.
- **Detección de Outliers**: Identificar valores "aberrantes" que se alejan del comportamiento normal.
- **Análisis de Distribución**: Entender la simetría y el sesgo de los datos.

### ¿Cuándo NO usarlo?
- **Forma Exacta**: Si necesitas ver la multimodalidad o la forma precisa de la densidad, usa un Histograma o un gráfico de Violín.
- **Puntos Individuales**: Si el interés principal son los valores específicos de cada registro.

### Tipos de Variables por Eje
- **Eje X (Categoría)**: Variable **Cualitativa Nominal** u **Ordinal** (ej: Sex, Pclass en Titanic).
- **Eje Y (Métrica)**: Variable **Cuantitativa Continua** (ej: Age, Fare).

### Anatomía del Box Plot (Maestro)
- **Caja**: Contiene el 50% central de los datos (Q1 a Q3).
- **Línea Central**: Representa la Mediana.
- **Bigotes**: Representan los límites de la distribución "normal" (generalmente 1.5 * IQR).
- **Puntos (Outliers)**: Datos fuera de los bigotes.

## 3. Implementación Python (Estándar Premium)

```python
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def plot_boxplot_premium(data, x, y, title, palette='magma', orient='v'):
    """
    Genera un Box Plot con estética premium centrada en la legibilidad estadística.
    """
    plt.figure(figsize=(10, 6))
    
    # Limpieza de datos (DAMA: Calidad de datos)
    # Es crítico eliminar o tratar NaNs en la variable numérica (Age)
    clean_data = data.dropna(subset=[y])
    
    # Gráfico con Seaborn para estética superior
    ax = sns.boxplot(
        data=clean_data, 
        x=x, 
        y=y, 
        palette=palette,
        hue=x,
        legend=False,
        width=0.6,
        linewidth=2.5,
        fliersize=5,
        showmeans=True,
        meanprops={"marker":"o", "markerfacecolor":"white", "markeredgecolor":"black", "markersize":"8"}
    )
    
    # Personalización Premium (Aesthetics)
    plt.title(title, fontsize=16, fontweight='bold', pad=20)
    plt.xlabel(x.capitalize(), fontsize=12)
    plt.ylabel(y.capitalize(), fontsize=12)
    
    # Quitar bordes innecesarios
    sns.despine(trim=True, left=True)
    
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    return plt
```

## 4. Ejemplo de Aplicación: Titanic (Edad por Sexo)

El objetivo es determinar si existe una diferencia significativa en la edad de los pasajeros según su sexo.

```python
# 1. Carga y Limpieza (DAMA)
df = pd.read_csv('../data/titanic.csv')
# dropna es fundamental para evitar distorsiones matemáticas
df_clean = df.dropna(subset=['Age'])

# 2. Visualización usando la Skill
plot_boxplot_premium(
    data=df_clean, 
    x='Sex', 
    y='Age', 
    title='Distribución de Edad por Sexo (Pasajeros Titanic)',
    palette='muted'
)
plt.show()

# 3. Análisis rápido:
# - La mediana de edad suele ser similar, pero los hombres presentan 
#   una mayor cantidad de outliers en edades avanzadas.
```
