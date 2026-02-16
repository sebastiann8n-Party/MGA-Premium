# Skill Transversal: Configuración de Títulos y Etiquetas de Ejes

## Misión
Comunicar claramente el mensaje del gráfico mediante títulos descriptivos y etiquetas precisas en los ejes. Un gráfico sin etiquetas es un gráfico mudo.

## Reglas de Oro (Según Best Practices)
1.  **Título Principal:** Debe ser conciso (ideamente < 10 palabras).
2.  **Subtítulo:** Úsalo para dar contexto adicional (10-15 palabras), como la fuente de datos o una conclusión clave.
3.  **Etiquetas de Ejes:** Obligatorias. Deben indicar la variable y la unidad de medida (ej: "Ventas (Millones USD)").

## 1. Matplotlib (La Base)
Matplotlib ofrece control total sobre la posición y estilo del texto. Se recomienda usar la API orientada a objetos (`ax`).

```python
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(10, 5))

# Gráfico
ax.plot([1, 2, 3], [10, 20, 15])

# Título Principal
# loc: 'left', 'center', 'right' (alineación)
# pad: espacio entre título y gráfico
ax.set_title("Evolución de Ventas Trimestrales", loc='left', fontsize=14, fontweight='bold', pad=20)

# Subtítulo (Usando text o title con menor jerarquía)
# Una forma común es usar suptitle para el título general y set_title para el específico,
# o usar fig.text()
fig.text(0.125, 0.9, "Comparativa 2023 vs 2024 - Fuente: CRM Interno", fontsize=10, color='gray')

# Etiquetas de Ejes
ax.set_xlabel("Trimestre", loc='right', fontsize=10) # loc alinea la etiqueta al final del eje
ax.set_ylabel("Ventas (k$)", loc='top', fontsize=10) # loc alinea la etiqueta al tope del eje

plt.show()
```

## 2. Pandas (Rápido y Directo)
Pandas permite definir el título directamente en el método de ploteo, y retorna el objeto `Axes` para personalización posterior.

```python
import pandas as pd

df = pd.DataFrame({'Ventas': [100, 120, 150]}, index=['Ene', 'Feb', 'Mar'])

# El parámetro 'title' asigna el título principal
ax = df.plot(kind='line', title='Ventas del Primer Trimestre')

# Usamos el objeto 'ax' retornado para ajustar detalles de Matplotlib
ax.set_xlabel("Mes")
ax.set_ylabel("Unidades Vendidas")
```

## 3. Seaborn (Interfaz de Alto Nivel)
Seaborn hereda de Matplotlib, pero ofrece el método `.set()` para configurar múltiples propiedades en una línea.

```python
import seaborn as sns

# Crear gráfico
g = sns.barplot(x=['A', 'B'], y=[50, 80])

# Configuración compacta con .set()
g.set(
    title='Rendimiento por Grupo (Seaborn)',
    xlabel='Grupo Experimental',
    ylabel='Puntaje Promedio'
)

# Para mayor control, se pueden usar los métodos de matplotlib sobre 'g' (que es un Axes)
# g.set_title("Nuevo Título", loc='left')
```

## 4. Plotly (Interactivo y Declarativo)
En Plotly, todo el layout se configura mediante `update_layout` o diccionarios.

```python
import plotly.express as px

df = px.data.tips()

fig = px.scatter(df, x="total_bill", y="tip", color="sex")

# Configuración global del layout
fig.update_layout(
    title={
        'text': "Relación Propina vs Total Cuenta",
        'y':0.95, # Posición vertical
        'x':0.5,  # Posición horizontal (centrado)
        'xanchor': 'center',
        'yanchor': 'top'
    },
    xaxis_title="Total de la Cuenta ($)",
    yaxis_title="Propina ($)",
    font=dict(
        family="Courier New, monospace",
        size=12,
        color="RebeccaPurple"
    )
)

fig.show()
```

## Resumen de Métodos
| Librería | Título | Etiqueta X | Etiqueta Y |
|---|---|---|---|
| **Matplotlib** | `ax.set_title("txt")` | `ax.set_xlabel("txt")` | `ax.set_ylabel("txt")` |
| **Pandas** | `df.plot(title="txt")` | (vía Matplotlib) | (vía Matplotlib) |
| **Seaborn** | `g.set(title="txt")` | `g.set(xlabel="txt")` | `g.set(ylabel="txt")` |
| **Plotly** | `layout(title_text="txt")` | `layout(xaxis_title="txt")` | `layout(yaxis_title="txt")` |
