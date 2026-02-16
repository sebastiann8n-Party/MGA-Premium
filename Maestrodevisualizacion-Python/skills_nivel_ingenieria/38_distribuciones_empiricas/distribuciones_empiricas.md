# Skill Ingenieria: Distribuciones Empíricas (ECDF y Strip)

## Misión
Entender la distribución real de los datos sin asumir normalidad. A diferencia de los histogramas que agrupan y ocultan detalles, los Strip Charts y ECDF (Empirical Cumulative Distribution Function) muestran cada punto o la probabilidad acumulada exacta.

## Reglas de Oro
1.  **Datos Crudos:** Prefiere Strip Charts para muestras pequeñas (< 1000) donde cada punto importa.
2.  **Probabilidad:** Usa ECDF para responder preguntas tipo "¿Qué porcentaje de mis datos es menor a X?".
3.  **Comparación:** Ambos gráficos son excelentes para comparar distribuciones entre categorías.

## 1. Strip Charts (Datos Crudos con Jitter)
Evita el solapamiento de puntos usando "jitter" (ruido aleatorio en el eje categórico).

```python
import plotly.express as px

df = px.data.tips()

# Strip Chart básico
fig = px.strip(df, x="total_bill", y="day", 
               color="sex", # Color por categoría
               stripmode="overlay", # Puntos superpuestos
               title="Distribución de Cuentas por Día (Strip Chart)")

fig.show()
```

## 2. ECDF (Función de Distribución Acumulada Empírica)
Muestra la proporción de datos que son menores o iguales a un valor dado. Es robusto y no depende de "bins" como el histograma.

```python
import plotly.express as px

df = px.data.tips()

# ECDF
fig = px.ecdf(df, x="total_bill", color="time",
              title="Probabilidad Acumulada del Total de la Cuenta",
              ecdfnorm='percent') # Eje Y en porcentaje (0-100)

# Añadir líneas guía
fig.add_hline(y=50, line_dash="dash", annotation_text="Mediana (50%)")
fig.add_vline(x=20, line_dash="dot", annotation_text="Umbral $20")

fig.show()
```

## 3. Comparación Visual: Histograma vs ECDF
El ECDF permite ver diferencias sutiles en colas y medianas que el histograma podría ocultar.

```python
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np

# Datos simulados: Dos distribuciones normales
d1 = np.random.normal(0, 1, 1000)
d2 = np.random.normal(0.5, 1.2, 1000)

fig = make_subplots(rows=1, cols=2, subplot_titles=("Histograma", "ECDF"))

# Histograma
fig.add_trace(go.Histogram(x=d1, name='D1', opacity=0.7), row=1, col=1)
fig.add_trace(go.Histogram(x=d2, name='D2', opacity=0.7), row=1, col=1)

# ECDF (Implementación manual rápida para GO, o usar px y convertir)
# Usaremos una aproximación simple ordenando
fig.add_trace(go.Scatter(x=np.sort(d1), y=np.linspace(0, 1, len(d1)), name='D1 ECDF'), row=1, col=2)
fig.add_trace(go.Scatter(x=np.sort(d2), y=np.linspace(0, 1, len(d2)), name='D2 ECDF'), row=1, col=2)

fig.update_layout(title="Comparativa: Densidad vs Acumulada", barmode='overlay')
fig.show()
```

## Resumen
| Pregunta | Gráfico Recomendado | Función Plotly |
|---|---|---|
| ¿Cómo se dispersan los datos individuales? | Strip Chart | `px.strip()` |
| ¿Cuál es la probabilidad de que X < valor? | ECDF | `px.ecdf()` |
| ¿Qué porcentaje de datos supera un umbral? | ECDF (Complementario) | `px.ecdf(ecdfmode='complementary')` |
