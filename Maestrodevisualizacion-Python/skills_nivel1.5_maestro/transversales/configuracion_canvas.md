# Skill Transversal: Configuración de Canvas (Lienzo)

## Misión
Controlar y personalizar el "lienzo" (Canvas) de nuestras visualizaciones, definiendo **dimensiones** precisas y aplicando **estilos visuales (temas)** coherentes a través de las diferentes librerías gráficas (Matplotlib, Seaborn, Plotly).

## Conceptos Clave
- **Canvas (Lienzo):** El área rectangular donde se dibuja el gráfico.
- **Dimensiones:** Ancho y alto del área de dibujo (generalmente en pulgadas o píxeles).
- **Temas/Estilos:** Configuraciones predefinidas de colores, fuentes, fondos y líneas de cuadrícula para dar una estética consistente.
- **Jerarquía:** Seaborn y Pandas 'envuelven' a Matplotlib, por lo que muchas configuraciones globales de Matplotlib les afectan. Plotly es independiente y tiene su propia configuración.

## Matplotlib & Pandas (Configuración Global)

Las configuraciones hechas aquí afectarán a todos los gráficos generados posteriormente con `.plot()` de Pandas.

```python
import matplotlib.pyplot as plt

# 1. DIMENSIONES (Global)
# Define el tamaño por defecto de todas las figuras (ancho, alto) en pulgadas
plt.rcParams["figure.figsize"] = (12, 6)

# 2. ESTILOS POR TEMA (Global)
# Aplica un estilo predefinido a todos los gráficos
# Ver estilos disponibles: plt.style.available
plt.style.use('Solarize_Light2')  # Otros ejemplos: 'ggplot', 'seaborn-v0_8', 'bmh'

# Ejemplo de uso con Pandas:
df['columna'].plot(
    figsize=(10, 5),  # Sobrescribe la config global para este gráfico específico
    title="Gráfico con estilo Solarize_Light2"
)
plt.show()
```

## Seaborn (Configuración Avanzada)

Seaborn ofrece un control más fino sobre la estética y el contexto (escalado de elementos).

```python
import seaborn as sns
import matplotlib.pyplot as plt

# 1. DIMENSIONES
# Seaborn usa la infraestructura de Matplotlib, por lo que se inicia la figura igual
plt.figure(figsize=(10, 6))

# 2. TEMA Y ESTILO (Set Theme)
# sns.set_theme() es la función maestra que configura estilo, paleta y contexto a la vez
sns.set_theme(
    style="whitegrid",   # Fondo: white, dark, whitegrid, darkgrid, ticks
    palette="pastel",    # Paleta de colores: deep, muted, bright, pastel, dark, colorblind
    context="notebook"   # Escala: paper, notebook, talk, poster (ajusta grosor de líneas y fuentes)
)

# Configuración individual de estilo (alternativa)
# sns.set_style("darkgrid")

# Ejemplo:
sns.lineplot(data=df, x='fecha', y='valor')
plt.show()
```

## Plotly (Configuración Web/Interactiva)

Plotly es independiente de Matplotlib y usa píxeles para dimensionar. Sus temas se llaman "templates".

```python
import plotly.express as px

# 1. Crear el gráfico con configuración inicial
fig = px.line(
    df, 
    x='fecha', 
    y='valor',
    width=800,        # Ancho en píxeles (no pulgadas)
    height=400,       # Alto en píxeles
    template='plotly_white', # Temas disponibles: 'ggplot2', 'seaborn', 'simple_white', 'plotly', 'plotly_dark', etc.
    title="Gráfico Interactivo con Plotly"
)

# 2. Actualizar configuración después de crear (Update Layout)
# Útil si queremos modificar un gráfico existente
fig.update_layout(
    width=1000,
    height=500,
    template='ggplot2',
    # Márgenes (l=left, r=right, t=top, b=bottom)
    margin=dict(l=20, r=20, t=40, b=20)
)

fig.show()
```

## Guía de Estilos Recomendados (Best Practices)

| Librería | Estilo "Limpio" (Publicación/Reporte) | Estilo "Oscuro" (Presentación/Pantalla) | Estilo "Técnico" (Análisis) |
|---|---|---|---|
| **Matplotlib** | `seaborn-v0_8-whitegrid` | `dark_background` | `bmh` o `ggplot` |
| **Seaborn** | `style="whitegrid"` | `style="dark"`, `palette="bright"` | `style="ticks"` |
| **Plotly** | `template="plotly_white"` | `template="plotly_dark"` | `template="ggplot2"` |

## Errores Comunes
- **Confundir unidades:** Matplotlib usa pulgadas (`figsize=(10,5)`), Plotly usa píxeles (`width=1000`).
- **Olvidar el contexto:** Usar un estilo de "poster" (letras gigantes) en un reporte impreso.
- **Mezclar configuraciones:** Intentar usar `plt.style.use()` para cambiar un gráfico de Plotly (no funcionará).
- **Sobreescritura:** `sns.set_theme()` restaura los valores por defecto de matplotlib, pudiendo anular configuraciones previas de `plt.rcParams`.

## Referencias
- [Matplotlib Style Sheets](https://matplotlib.org/stable/gallery/style_sheets/style_sheets_reference.html)
- [Seaborn Aesthetics](https://seaborn.pydata.org/tutorial/aesthetics.html)
- [Plotly Templates](https://plotly.com/python/templates/)
