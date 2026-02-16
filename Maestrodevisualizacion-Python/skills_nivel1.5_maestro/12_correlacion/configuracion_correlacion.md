# Skill: Análisis de Correlación (Scatter Plots y Heatmaps)

## Misión
Identificar y visualizar la fuerza y dirección de la relación entre dos o más variables numéricas, permitiendo descubrir patrones, dependencias y causalidades potenciales en los datos.

## 1. El Concepto: ¿Están Conectadas las Variables?
*   **Scatter Plot (Gráfico de Dispersión):** Ideal para visualizar la relación entre *dos* variables continuas. Permite ver si hay una tendencia lineal, agrupaciones (clusters) o valores atípicos.
*   **Heatmap (Mapa de Calor):** Ideal para visualizar la **matriz de correlación** de *múltiples* variables a la vez, usando colores para representar la intensidad de la relación (índice de Pearson).

## 2. Implementación en Seaborn (Estadística Rápida)

### Scatter Plot con Línea de Regresión
Seaborn facilita ver la tendencia automáticamente con `regplot` o `lmplot`.
```python
import seaborn as sns
import matplotlib.pyplot as plt

# Visualizar relación entre Ventas y Gastos de Marketing
plt.figure(figsize=(10, 6))
sns.regplot(data=df, x='marketing_spend', y='sales', 
            scatter_kws={'alpha':0.5}, line_kws={'color':'red'})
plt.title('Relación Gastos Marketing vs Ventas')
plt.show()
```

### Heatmap de Correlación
```python
# Calcular la matriz de correlación numérica
corr_matrix = df.corr()

plt.figure(figsize=(12, 8))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
plt.title('Matriz de Correlación de Variables')
plt.show()
```

## 3. Implementación en Plotly (Exploración Interactiva)

### Scatter Plot Interactivo
Permite identificar puntos específicos al pasar el mouse.
```python
import plotly.express as px

fig = px.scatter(df, x="marketing_spend", y="sales", 
                 color="category", size="profit",
                 hover_data=['product_id'],
                 title="Análisis Interactivo de Ventas")
fig.show()
```

## 4. Interpretación Matemática (Coeficiente de Pearson)
*   **+1:** Correlación positiva perfecta (si una sube, la otra también en proporción constante).
*   **0:** No hay correlación lineal evidente.
*   **-1:** Correlación negativa perfecta (si una sube, la otra baja).

## 5. Mejores Prácticas
1.  **Causas vs. Correlación:** Recuerda que la correlación no implica causalidad.
2.  **Limpieza de Datos:** Los valores atípicos (outliers) pueden distorsionar gravemente la línea de tendencia. Identifícalos con el scatter plot antes de concluir.
3.  **Variables Categóricas:** En scatter plots, usa el parámetro `hue` (color) para ver si la relación cambia según la categoría.
4.  **Escalado:** Si las variables tienen escalas muy diferentes (ej: 0-1 y 1M-10M), considera normalizar para el Heatmap si usas otros algoritmos, aunque para Pearson no es estrictamente necesario.

## 6. Exportación y Guardado Profesional

### Guardado en Alta Resolución (PNG)
Para presentaciones y reportes, es crucial guardar con calidad profesional:
```python
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(10, 6))
sns.regplot(data=df, x='marketing_spend', y='sales', ax=ax)

# Guardado en alta resolución
plt.savefig('correlacion_marketing.png', 
            dpi=300,              # Resolución mínima para impresión
            bbox_inches='tight',  # Elimina espacios en blanco
            transparent=False,    # Fondo blanco (cambiar a True si necesitas transparencia)
            facecolor='white')
```

### Exportación a PDF (Formato Vectorial)
Ideal para documentos académicos y reportes técnicos:
```python
# PDF simple
plt.savefig('correlacion_marketing.pdf', bbox_inches='tight')

# PDF con metadatos
from matplotlib.backends.backend_pdf import PdfPages

metadata = {
    'Title': 'Análisis de Correlación - Marketing vs Ventas',
    'Author': 'Analista de Datos',
    'Subject': 'Correlación de Pearson',
    'Keywords': 'correlación, marketing, ventas'
}

with PdfPages('reporte_correlacion.pdf', metadata=metadata) as pdf:
    # Gráfico 1: Scatter Plot
    fig1, ax1 = plt.subplots(figsize=(10, 6))
    sns.regplot(data=df, x='marketing_spend', y='sales')
    ax1.set_title('Relación Marketing-Ventas')
    pdf.savefig(fig1, bbox_inches='tight')
    plt.close(fig1)
    
    # Gráfico 2: Heatmap
    fig2, ax2 = plt.subplots(figsize=(8, 6))
    corr_matrix = df.corr()
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', ax=ax2)
    ax2.set_title('Matriz de Correlación')
    pdf.savefig(fig2, bbox_inches='tight')
    plt.close(fig2)
```

### Automatización con Timestamp
Para guardar múltiples versiones sin sobreescribir:
```python
from datetime import datetime
import os

def guardar_grafico_auto(figura, nombre_base, carpeta='analisis_correlacion'):
    """
    Guarda gráfico con timestamp automático.
    
    Args:
        figura: objeto Figure de matplotlib
        nombre_base: nombre base del archivo (sin extensión)
        carpeta: carpeta de destino
    """
    # Crear carpeta si no existe
    if not os.path.exists(carpeta):
        os.makedirs(carpeta)
    
    # Generar timestamp
    fecha_hora = datetime.now().strftime("%Y%m%d_%H%M%S")
    nombre_completo = f"{carpeta}/{nombre_base}_{fecha_hora}"
    
    # Guardar en múltiples formatos
    figura.savefig(f"{nombre_completo}.png", dpi=300, bbox_inches='tight')
    figura.savefig(f"{nombre_completo}.pdf", bbox_inches='tight')
    
    print(f"✅ Gráfico guardado: {nombre_completo}")
    return nombre_completo

# Uso:
fig, ax = plt.subplots(figsize=(10, 6))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm', ax=ax)
guardar_grafico_auto(fig, 'matriz_correlacion')
```

### Botones Interactivos (Plotly)
Para dashboards interactivos con opciones de descarga:
```python
import plotly.express as px

# Configurar botones de descarga personalizados
config = {
    'toImageButtonOptions': {
        'format': 'png',              # Formato: 'png', 'svg', 'jpeg'
        'filename': 'correlacion_interactiva',
        'height': 1080,
        'width': 1920,
        'scale': 2                    # Multiplica la resolución
    },
    'displayModeBar': True,           # Mostrar barra de herramientas
    'displaylogo': False,             # Ocultar logo de Plotly
    'modeBarButtonsToRemove': ['pan2d', 'lasso2d']  # Remover botones específicos
}

fig = px.scatter(df, x="marketing_spend", y="sales", 
                 trendline="ols",
                 title="Análisis de Correlación Interactivo")

fig.show(config=config)

# Guardado programático de Plotly
fig.write_html("correlacion_interactiva.html")
fig.write_image("correlacion_estatica.png", width=1920, height=1080, scale=2)
```

### Reporte PDF Completo Automatizado
```python
from matplotlib.backends.backend_pdf import PdfPages
import numpy as np

def crear_reporte_correlacion(dataframe, archivo_salida='reporte_correlacion.pdf'):
    """
    Crea un reporte PDF completo con todos los análisis de correlación.
    """
    with PdfPages(archivo_salida) as pdf:
        # Página 1: Matriz de Correlación
        fig = plt.figure(figsize=(11, 8.5))
        
        corr = dataframe.corr()
        sns.heatmap(corr, annot=True, fmt='.2f', cmap='RdYlGn', 
                   center=0, linewidths=1, cbar_kws={'label': 'Correlación'})
        
        plt.title('Matriz de Correlación Dataset Completo', 
                 fontsize=16, fontweight='bold', pad=20)
        plt.tight_layout()
        pdf.savefig(fig, bbox_inches='tight')
        plt.close()
        
        # Página 2-N: Scatter plots de correlaciones fuertes
        correlaciones_fuertes = []
        columnas = corr.columns
        
        for i in range(len(columnas)):
            for j in range(i+1, len(columnas)):
                valor_corr = corr.iloc[i, j]
                if abs(valor_corr) > 0.5:  # Umbral de correlación fuerte
                    correlaciones_fuertes.append((columnas[i], columnas[j], valor_corr))
        
        for var1, var2, valor in correlaciones_fuertes:
            fig, ax = plt.subplots(figsize=(10, 6))
            
            sns.regplot(data=dataframe, x=var1, y=var2, ax=ax,
                       scatter_kws={'alpha':0.5}, 
                       line_kws={'color':'red', 'linewidth':2})
            
            ax.set_title(f'Correlación: {var1} vs {var2}\nr = {valor:.3f}',
                        fontsize=14, fontweight='bold')
            ax.set_xlabel(var1, fontsize=12)
            ax.set_ylabel(var2, fontsize=12)
            ax.grid(True, alpha=0.3)
            
            plt.tight_layout()
            pdf.savefig(fig, bbox_inches='tight')
            plt.close()
        
        # Agregar metadata
        d = pdf.infodict()
        d['Title'] = 'Reporte de Análisis de Correlación'
        d['Author'] = 'Sistema de Análisis Automatizado'
        d['Subject'] = 'Análisis Estadístico de Correlaciones'
        d['CreationDate'] = datetime.now()
    
    print(f"📄 Reporte completo guardado en: {archivo_salida}")

# Uso:
crear_reporte_correlacion(df, 'reporte_correlacion_completo.pdf')
```

## Resumen de Comandos
| Acción | Comando (Seaborn) |
|---|---|
| Dispersión con Regresión | `sns.regplot(x, y)` |
| Matriz de Correlación | `df.corr()` |
| Mapa de Calor | `sns.heatmap(data, annot=True)` |
| Scatter Plot por Grupos | `sns.scatterplot(x, y, hue='category')` |
| Guardar PNG Alta Resolución | `plt.savefig('archivo.png', dpi=300, bbox_inches='tight')` |
| Guardar PDF | `plt.savefig('archivo.pdf', bbox_inches='tight')` |
| PDF Multipágina | `PdfPages('reporte.pdf')` |
| Guardar Plotly Interactivo | `fig.write_html('grafico.html')` |
