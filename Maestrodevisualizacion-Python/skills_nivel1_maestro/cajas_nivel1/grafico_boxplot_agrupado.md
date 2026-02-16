# Skill: Gráfico de Cajas Agrupado / Grouped Box Plot (Maestro de Visualización)

Esta skill extiende el Box Plot básico para permitir la comparación de múltiples categorías cruzadas (ej. Edad por Sexo y por Clase de pasajero), facilitando la detección de interacciones complejas en los datos.

## 1. Misión
Visualizar la variabilidad de una variable numérica a través de dos niveles de categorización, manteniendo el rigor estadístico y la claridad visual.

## 2. Guía de Uso

### ¿Cuándo usarlo?
- **Análisis de Interacción**: Cuando quieres ver cómo una subcategoría influye en la distribución de un grupo principal.
- **Segmentación Detallada**: Para reportes que requieren comparar segmentos específicos (ej. Mujeres en 1ra Clase vs Mujeres en 3ra Clase).

### ¿Cuándo NO usarlo?
- **Demasiadas Subcategorías**: Si el parámetro `hue` tiene más de 3-4 niveles, el gráfico se vuelve saturado y pierde efectividad.

### Tipos de Variables por Eje
- **Eje X (Categoría Principal)**: Variable **Cualitativa Nominal** u **Ordinal** (ej: Pclass en Titanic).
- **Eje Y (Métrica)**: Variable **Cuantitativa Continua** (ej: Age, Fare).
- **Hue (Subcategoría)**: Variable **Cualitativa Nominal** (ej: Sex). Máximo 3-4 niveles recomendados.

### Consejos de Diseño Premium
- **Leyendas Claras**: La leyenda debe estar fuera del área de trazado o en un lugar que no obstruya.
- **Paletas Contrastantes**: Usar colores que se diferencien bien entre sí pero que mantengan la armonía.

## 3. Implementación Python (Estándar Premium)

```python
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def plot_grouped_boxplot_premium(data, x, y, hue, title, palette='Set2'):
    """
    Genera un Box Plot agrupado con tres dimensiones de datos (X, Y, Hue).
    """
    plt.figure(figsize=(12, 7))
    
    # DAMA: Limpieza proactiva
    clean_data = data.dropna(subset=[y, x, hue])
    
    # Gráfico Agrupado
    ax = sns.boxplot(
        data=clean_data, 
        x=x, 
        y=y, 
        hue=hue,
        palette=palette,
        linewidth=1.5,
        fliersize=4,
        gap=0.1 # Pequeño espacio entre grupos para claridad
    )
    
    # Estética
    plt.title(title, fontsize=18, fontweight='bold', pad=25)
    plt.xlabel(x.capitalize(), fontsize=13)
    plt.ylabel(y.capitalize(), fontsize=13)
    
    # Mover leyenda fuera
    plt.legend(title=hue.capitalize(), bbox_to_anchor=(1.05, 1), loc='upper left')
    
    sns.despine(offset=10, trim=True)
    plt.grid(axis='y', alpha=0.3)
    plt.tight_layout()
    
    return plt
```

## 4. Ejemplo de Aplicación: Titanic (Edad por Clase y Sexo)

```python
# Comparación de Edad (Y) por Pclass (X) segmentado por Sexo (Hue)
plot_grouped_boxplot_premium(
    data=df_clean, 
    x='Pclass', 
    y='Age', 
    hue='Sex',
    title='Interacción de Edad: Clase y Sexo (Titanic)',
    palette='pastel'
)
plt.show()
```
