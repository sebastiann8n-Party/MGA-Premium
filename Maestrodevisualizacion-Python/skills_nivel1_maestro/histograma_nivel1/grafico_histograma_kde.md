# Skill: Histograma con KDE / Histogram + KDE (Maestro de Visualización)

El histograma con KDE (Kernel Density Estimation) combina barras de frecuencia con una curva de densidad suavizada, proporcionando una visión más clara de la distribución continua de los datos.

## 1. Misión
Visualizar la distribución de datos numéricos mediante barras de frecuencia y una curva de densidad estimada, facilitando la identificación de modas, asimetrías y la forma general de la distribución.

## 2. Guía de Uso

### ¿Cuándo usarlo?
- **Ver Forma de Distribución**: La curva KDE muestra suavemente la forma de la distribución sin los "saltos" de las barras.
- **Identificar Modas**: Detectar fácilmente picos de concentración (distribuciones unimodales, bimodales, multimodales).
- **Complementar Información**: Las barras muestran frecuencias exactas, la curva KDE muestra la tendencia.

### ¿Cuándo NO usarlo?
- **Pocos Datos**: Con muestras pequeñas, la curva KDE puede ser engañosa y mostrar patrones inexistentes.
- **Datos Discretos**: Si la variable tiene pocos valores discretos, la curva KDE puede suavizar en exceso.

### Tipos de Variables por Eje
- **Eje X (Variable)**: Variable **Cuantitativa Continua** (ej: Age, Fare).
- **Eje Y Izquierdo (Frecuencia)**: **Frecuencia Absoluta** (barras).
- **Eje Y Derecho (Densidad)**: **Densidad de Probabilidad** (curva KDE).

### Ventajas del KDE
- **Suavizado**: Elimina el "ruido" visual de las barras individuales.
- **Interpretación**: Facilita ver si los datos siguen una distribución normal, sesgada, etc.
- **Comparación**: Más fácil comparar formas de distribución entre grupos.

## 3. Implementación Python (Estándar Premium)

```python
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def plot_histogram_kde_premium(data, x, title, bins=None, palette="Blues", kde_color="darkblue"):
    """
    Genera un Histograma con curva KDE superpuesta con estética premium.
    """
    plt.figure(figsize=(12, 6))
    
    # DAMA: Limpieza de nulos
    clean_data = data.dropna(subset=[x])
    
    # Gráfico con Seaborn (Histograma + KDE)
    ax = sns.histplot(
        data=clean_data,
        x=x,
        bins=bins if bins else 'auto',
        kde=True,  # Activar curva KDE
        color=palette,
        alpha=0.6,
        edgecolor="white",
        linewidth=1.2,
        line_kws={'linewidth': 2.5, 'color': kde_color}  # Estilo de la curva KDE
    )
    
    # Personalización
    plt.title(title, fontsize=18, fontweight='bold', pad=20)
    plt.xlabel(x.capitalize(), fontsize=13)
    plt.ylabel("Frecuencia / Densidad", fontsize=13)
    
    # Añadir línea vertical en la media
    mean_val = clean_data[x].mean()
    plt.axvline(mean_val, color='red', linestyle='--', linewidth=2, alpha=0.7, label=f'Media: {mean_val:.2f}')
    
    plt.legend()
    sns.despine(trim=True)
    plt.grid(axis='y', linestyle=':', alpha=0.5)
    plt.tight_layout()
    
    return plt

```

## 4. Ejemplo de Aplicación: Titanic (Distribución de Edades con KDE)

### Histograma + KDE de Edades
```python
# Limpieza de datos
df_clean = df.dropna(subset=['Age'])

# Visualización usando la Skill
plot_histogram_kde_premium(
    data=df_clean,
    x='Age',
    title='Distribución de Edades con KDE (Titanic)',
    bins=20,
    palette='steelblue',
    kde_color='navy'
)
plt.show()

# Análisis:
# - La curva KDE muestra una distribución aproximadamente normal con sesgo
# - Se observa un pico principal alrededor de 20-30 años
# - La línea roja indica la edad media de los pasajeros
```

### Variación: KDE Agrupado por Categoría
```python
# Comparar distribuciones de edad por sexo con KDE
sns.histplot(
    data=df_clean,
    x='Age',
    hue='Sex',
    bins=20,
    kde=True,
    palette='Set1',
    alpha=0.5,
    edgecolor="white",
    line_kws={'linewidth': 2}
)
plt.title('Distribución de Edades por Sexo (KDE)', fontsize=16, fontweight='bold')
plt.tight_layout()
plt.show()

# Las curvas KDE permiten comparar fácilmente las formas de distribución entre hombres y mujeres
```

## 5. Parámetros Avanzados KDE

### Ajustar el Ancho de Banda (Bandwidth)
```python
# Mayor bandwidth = curva más suave
# Menor bandwidth = curva más detallada (puede capturar ruido)
sns.kdeplot(data=df_clean, x='Age', bw_adjust=0.5, color='purple', linewidth=2.5)
plt.title('KDE con Bandwidth Ajustado', fontsize=14)
plt.show()
```
