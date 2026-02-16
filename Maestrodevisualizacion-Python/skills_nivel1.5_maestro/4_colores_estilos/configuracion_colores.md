# Skill Transversal: Configuración de Colores y Estilos

## Misión
Dominar la personalización de colores para mejorar la legibilidad, estética y semántica de los gráficos. El color debe usarse con propósito (destacar, agrupar, diferenciar), no solo por decoración.

## 1. Matplotlib (Control Manual)
Matplotlib acepta colores en múltiples formatos: nombres (ej. 'red'), códigos HEX ('#FF5733'), RGB/RGBA, y mapas de colores (colormaps).

### Colores Individuales
```python
import matplotlib.pyplot as plt

# Usando nombres y HEX
plt.bar(['A', 'B'], [10, 20], color=['royalblue', '#FF5733'])
plt.show()
```

### Mapas de Color (Colormaps)
Para datos continuos o categorías secuenciales.
```python
import numpy as np

x = np.random.rand(50)
y = np.random.rand(50)
colors = np.random.rand(50)

# cmap: define el mapa de color (ej. 'viridis', 'plasma', 'inferno', 'magma', 'cividis')
plt.scatter(x, y, c=colors, cmap='viridis')
plt.colorbar(label='Escala de Valor')
plt.show()
```

## 2. Seaborn (Paletas Semánticas)
Seaborn facilita el uso de paletas armónicas.
- `palette`: Argumento principal para gráficos categóricos.
- `sn.color_palette()`: Para generar o visualizar paletas.

### Tipos de Paletas
1.  **Cualitativas:** Para categorías sin orden (ej. 'deep', 'muted', 'pastel', 'bright', 'dark', 'colorblind').
2.  **Secuenciales:** Para datos numéricos ordenados (ej. 'Rocket', 'Mako', 'Blues').
3.  **Divergentes:** Para datos con un punto medio neutro (ej. 'vlag', 'icefire').

```python
import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("penguins")

# Uso de palette en gráfico categórico
sns.barplot(data=df, x="species", y="body_mass_g", palette="viridis")
plt.title("Paleta 'viridis' (Secuencial/Perceptual)")
plt.show()

# Configuración Global de Estilo y Paleta
sns.set_theme(style="whitegrid", palette="pastel")
sns.boxplot(data=df, x="island", y="body_mass_g")
plt.show()
```

## 3. Plotly (Interactivo)
Plotly distingue entre colores discretos (categorías) y continuos (escalas).

### Colores Discretos (Sequence)
Para variables categóricas (`color="..."`).
```python
import plotly.express as px

df = px.data.iris()

fig = px.scatter(
    df, x="sepal_width", y="sepal_length", 
    color="species",
    # Secuencia personalizada
    color_discrete_sequence=["#FF5733", "#33FF57", "#3357FF"] 
    # O usar predefinidos: px.colors.qualitative.G10
)
fig.show()
```

### Colores Continuos (Scale)
Para variables numéricas en `color`.
```python
fig = px.scatter(
    df, x="sepal_width", y="sepal_length", 
    color="petal_length",
    # Escala continua
    color_continuous_scale=px.colors.sequential.Viridis
)
fig.show()
```

## Resumen de Argumentos Clave
| Librería | Argumento Color Fijo | Argumento Mapeo (Variable) | Argumento Paleta/Escala |
|---|---|---|---|
| **Matplotlib** | `color='r'` | `c=variable` | `cmap='viridis'` |
| **Seaborn** | `color='b'` (raro) | `hue=variable` | `palette='deep'` |
| **Plotly Express** | `color_discrete_sequence=['red']`* | `color='variable'` | `color_continuous_scale` / `color_discrete_sequence` |

*Nota: En Plotly, para un color fijo en todos los elementos sin mapear variable, se usa `update_traces(marker_color='red')`.
