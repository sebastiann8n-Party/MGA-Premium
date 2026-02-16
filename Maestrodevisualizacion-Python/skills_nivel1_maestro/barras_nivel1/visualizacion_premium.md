# Skill: Visualización Premium (Glassmorphism & HSL)

## 1. Misión
Transformar gráficos básicos en experiencias visuales de alto impacto mediante el uso de principios de diseño moderno (Glassmorphism), paletas de colores armoniosas (HSL) y tipografía limpia.

## 2. Principios de Diseño
- **Minimalismo**: Eliminar "chart junk" (bordes innecesarios, fondos ruidosos).
- **Legibilidad**: Usar fuentes sans-serif modernas (Roboto, Inter, Arial).
- **Jerarquía**: Títulos claros, subtítulos explicativos y ejes limpios.
- **Color**: Usar paletas HSL para diferenciar categorías de manera suave pero efectiva.

## 3. Implementación Python (Estilo Premium)

```python
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.font_manager as fm

def apply_premium_style(theme: str = 'dark'):
    """
    Aplica una configuración global de estilo premium a Matplotlib/Seaborn.
    """
    # Configuración Base
    sns.set_context("notebook", font_scale=1.1)
    
    if theme == 'dark':
        # Fondo oscuro elegante (Casi negro, no #000000)
        bg_color = '#1e1e1e'
        text_color = '#e0e0e0'
        grid_color = '#333333'
    else:
        # Fondo claro limpio (Casi blanco, no #ffffff)
        bg_color = '#f5f5f7'
        text_color = '#333333'
        grid_color = '#e0e0e0'
        
    # Aplicar colores
    plt.rcParams['figure.facecolor'] = bg_color
    plt.rcParams['axes.facecolor'] = bg_color
    plt.rcParams['text.color'] = text_color
    plt.rcParams['axes.labelcolor'] = text_color
    plt.rcParams['xtick.color'] = text_color
    plt.rcParams['ytick.color'] = text_color
    plt.rcParams['axes.edgecolor'] = grid_color
    plt.rcParams['grid.color'] = grid_color
    
    # Fuentes (Intentar usar una fuente premium si está disponible)
    # plt.rcParams['font.family'] = 'sans-serif'
    
    # Remover bordes innecesarios (Spines)
    plt.rcParams['axes.spines.top'] = False
    plt.rcParams['axes.spines.right'] = False
    
def plot_bar_premium(data, x, y, title, subtitle=None, palette='viridis', figsize=(10, 6)):
    """
    Genera un gráfico de barras con estilo premium.
    
    Args:
        data (pd.DataFrame): Datos agregados.
        x (str): Columna eje X.
        y (str): Columna eje Y.
        title (str): Título principal.
        subtitle (str, optional): Subtítulo descriptivo.
        palette (str): Paleta de colores Seaborn.
    """
    plt.figure(figsize=figsize)
    
    # Gráfico
    ax = sns.barplot(data=data, x=x, y=y, palette=palette, edgecolor=None)
    
    # Títulos y Etiquetas
    plt.title(title, fontsize=16, fontweight='bold', pad=20, loc='left')
    if subtitle:
        plt.suptitle(subtitle, fontsize=12, y=0.92, x=0.125, ha='left', color='gray') # Ajuste manual posición
        
    plt.xlabel(x.capitalize(), fontsize=12, fontweight='medium')
    plt.ylabel(y.capitalize(), fontsize=12, fontweight='medium')
    
    # Grid sutil solo en eje Y
    ax.yaxis.grid(True, linestyle='--', alpha=0.3)
    ax.xaxis.grid(False)
    
    return ax
```
