# Skill: Gráfico de Violín / Violin Plot (Maestro de Visualización)

El gráfico de violín combina el Box Plot con una estimación de densidad de kernel (KDE), permitiendo ver no solo los cuartiles sino también la "forma" o distribución de densidad de los datos.

## 1. Misión
Proporcionar una visión integral de la distribución de datos, revelando picos de frecuencia, multimodalidad y anomalías que un Box Plot convencional podría ocultar.

## 2. Guía de Uso

### ¿Cuándo usarlo?
- **Distribuciones Complejas**: Cuando sospechas que tus datos son multimodales (tienen más de un pico).
- **Grandes Datasets**: Funciona mejor que un Box Plot simple cuando tienes suficientes datos para estimar la densidad con precisión.

### ¿Cuándo NO usarlo?
- **Pocos Datos**: Con muestras pequeñas, la estimación de densidad puede ser engañosa y ruidosa.
- **Audiencia no Técnica**: Algunos usuarios pueden encontrarlo difícil de interpretar inicialmente; en esos casos, prefiere Box Plots.

### Tipos de Variables por Eje
- **Eje X (Categoría)**: Variable **Cualitativa Nominal** u **Ordinal** (ej: Sex en Titanic).
- **Eje Y (Métrica)**: Variable **Cuantitativa Continua** (ej: Age, Fare). Requiere suficientes datos para estimación KDE confiable.

### Elementos Clave
- **Ancho del Violín**: Densidad de probabilidad de los datos en ese valor.
- **Caja Interna**: Generalmente incluye un mini-boxplot que muestra la mediana y el IQR.

## 3. Implementación Python (Estándar Premium)

```python
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def plot_violin_premium(data, x, y, title, palette='coolwarm', split=False, hue=None):
    """
    Genera un Violin Plot con integración de Box Plot interno y estética refinada.
    """
    plt.figure(figsize=(11, 7))
    
    # DAMA: Asegurar integridad numérica
    clean_data = data.dropna(subset=[y])
    
    # Gráfico de Violín
    ax = sns.violinplot(
        data=clean_data, 
        x=x, 
        y=y, 
        hue=hue,
        split=split, # Permite ver densidades encontradas (ej. hombre a la izq, mujer a la der)
        palette=palette,
        inner="quart", # Mostrar cuartiles internamente
        linewidth=1.8,
        cut=0 # No extender la densidad más allá de los datos reales
    )
    
    # Pulido Visual
    plt.title(title, fontsize=18, fontweight='bold', pad=25)
    plt.xlabel(x.capitalize(), fontsize=12)
    plt.ylabel(y.capitalize(), fontsize=12)
    
    sns.despine(left=True, bottom=True)
    plt.tight_layout()
    
    return plt
```

## 4. Ejemplo de Aplicación: Titanic (Distribución de Edad por Sexo)

```python
# Ver la "forma" de las edades por sexo
plot_violin_premium(
    data=df_clean, 
    x='Sex', 
    y='Age', 
    title='Densidad de Edad por Sexo (Titanic)',
    palette='viridis'
)
plt.show()
```
