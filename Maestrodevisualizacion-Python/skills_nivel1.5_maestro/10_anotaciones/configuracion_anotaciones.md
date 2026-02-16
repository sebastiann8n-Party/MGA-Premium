# Skill: Anotaciones y Marcas de Referencia

## Misión
Guiar la atención del usuario hacia puntos clave del gráfico utilizando texto descriptivo, flechas y líneas de referencia (umbrales). Las anotaciones transforman un gráfico simple en una narrativa de datos (Storytelling).

## 1. Matplotlib y Seaborn (Uso de `annotate`, `axhline` y `axvline`)
Matplotlib ofrece un control granular sobre las flechas y la posición del texto.

### Anotaciones con Flecha
```python
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(10, 5))
ax.plot([1, 2, 3, 4], [1, 4, 2, 3], marker='o')

# xy: coordenadas del punto a señalar
# xytext: coordenadas de donde estará el texto
# arrowprops: estilo de la flecha
ax.annotate('Punto de Interés', 
            xy=(2, 4), xytext=(3, 4),
            arrowprops=dict(facecolor='black', shrink=0.05, width=2, headwidth=8),
            fontsize=12, fontweight='bold')

plt.show()
```

### Líneas de Referencia (Umbrales)
```python
# Línea horizontal (ej: promedio o meta)
ax.axhline(y=2.5, color='r', linestyle='--', label='Meta')

# Línea vertical (ej: fecha de lanzamiento)
ax.axvline(x=2, color='green', alpha=0.5)

# Rellenar área (ej: zona crítica)
ax.axhspan(0, 1.5, color='red', alpha=0.1)
```

## 2. Plotly (Uso de `add_annotation` y `add_hline/vline`)
Plotly facilita la creación de anotaciones interactivas que se mantienen legibles al hacer zoom.

### Anotación de Texto
```python
import plotly.express as px
fig = px.line(x=[1, 2, 3, 4], y=[1, 4, 9, 16], title="Crecimiento Exponencial")

fig.add_annotation(x=3, y=9,
            text="Punto de Quiebre",
            showarrow=True,
            arrowhead=1)
```

### Líneas Proyectadas (Mejora: Etiquetas integradas)
```python
fig.add_hline(y=10, line_dash="dot", 
              annotation_text="Límite de Seguridad", 
              annotation_position="bottom right")
```

## Reglas de Oro para Mejores Anotaciones
1.  **Menos es más:** No satures el gráfico. Anota solo lo que no es obvio a primera vista.
2.  **Contraste:** Usa colores que resalten sobre los datos pero que no compitan con el título principal.
3.  **Alineación:** Asegúrate de que el texto de la anotación no tape puntos de datos importantes.
4.  **Contexto:** Las líneas de referencia deben tener una etiqueta que explique *qué* representan (ej: "Promedio Histórico").

## Resumen de Comandos
| Función | Matplotlib/Seaborn | Plotly |
|---|---|---|
| **Anotación con flecha** | `ax.annotate()` | `fig.add_annotation()` |
| **Texto suelto** | `ax.text()` | `fig.add_annotation(showarrow=False)` |
| **Línea Horizontal** | `ax.axhline()` | `fig.add_hline()` |
| **Línea Vertical** | `ax.axvline()` | `fig.add_vline()` |
| **Rango de Área** | `ax.axhspan()` / `ax.axvspan()` | `fig.add_hrect()` / `fig.add_vrect()` |
