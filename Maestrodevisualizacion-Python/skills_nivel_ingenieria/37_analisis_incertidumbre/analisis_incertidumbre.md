# Skill Ingenieria: Análisis de Incertidumbre y Errores

## Misión
En ingeniería y ciencia, un dato sin su incertidumbre asociada está incompleto. Esta skill permite visualizar el margen de error, la desviación estándar o los intervalos de confianza para dar fiabilidad a los resultados.

## Reglas de Oro
1.  **Claridad:** Las barras de error no deben ocultar el dato principal.
2.  **Especificidad:** Indica siempre en la leyenda o título qué representa el error (SD, SE, CI 95%).
3.  **Simetría vs Asimetría:** Usa barras asimétricas si el error positivo es diferente al negativo.

## 1. Barras de Error en Plotly (Interactivo)
Plotly permite añadir barras de error a casi cualquier tipo de gráfico (scatter, bar, line) usando los argumentos `error_x` y `error_y`.

```python
import plotly.express as px
import pandas as pd

# Datos de ejemplo: Resistencia de materiales
df = pd.DataFrame({
    "Material": ["Acero A", "Acero B", "Aleación C"],
    "Resistencia_Media": [450, 320, 510],
    "Desviacion_Estandar": [20, 15, 35] # Incertidumbre simétrica
})

# Gráfico de Barras con Error
fig = px.bar(df, x="Material", y="Resistencia_Media",
             error_y="Desviacion_Estandar", # Columna con el valor del error
             title="Resistencia a la Tracción con Desviación Estándar",
             labels={"Resistencia_Media": "Resistencia (MPa)"},
             template="plotly_white")

fig.show()
```

### Barras de Error Asimétricas
Para errores que no son iguales hacia arriba y abajo, usa `error_y_minus`.

```python
import plotly.graph_objects as go

# Datos simulados
x = [1, 2, 3, 4]
y = [2.1, 3.5, 5.7, 8.2]
error_pos = [0.1, 0.2, 0.3, 0.1]
error_neg = [0.2, 0.4, 0.1, 0.5]

fig = go.Figure(data=go.Scatter(
    x=x,
    y=y,
    error_y=dict(
        type='data', # valores explicitos
        symmetric=False,
        array=error_pos, # Error hacia arriba (+)
        arrayminus=error_neg # Error hacia abajo (-)
    )
))
fig.update_layout(title="Mediciones Experimentales con Error Asimétrico")
fig.show()
```

## 2. Bandas de Confianza Continuas (Plotly)
Ideal para series de tiempo o regresiones donde la incertidumbre varía continuamente.

```python
import plotly.graph_objects as go
import numpy as np

# Generar datos sintéticos
x = np.linspace(0, 10, 100)
y = np.sin(x)
y_upper = y + 0.2 # Limite superior
y_lower = y - 0.2 # Limite inferior

fig = go.Figure()

# Banda de confianza (relleno)
fig.add_trace(go.Scatter(
    x=np.concatenate([x, x[::-1]]), # Ida y vuelta en X para cerrar el polígono
    y=np.concatenate([y_upper, y_lower[::-1]]), # Upper y luego Lower invertido
    fill='toself',
    fillcolor='rgba(0,100,80,0.2)',
    line=dict(color='rgba(255,255,255,0)'),
    hoverinfo="skip",
    showlegend=False,
    name='Intervalo de Confianza'
))

# Línea principal
fig.add_trace(go.Scatter(
    x=x,
    y=y,
    line=dict(color='rgb(0,100,80)'),
    mode='lines',
    name='Señal Nominal'
))

fig.update_layout(title="Señal con Banda de Confianza (Confidence Interval)")
fig.show()
```

## 3. Matplotlib (Estático)
Para reportes impresos o papers, Matplotlib es el estándar.

```python
import matplotlib.pyplot as plt

x = ["Muestra 1", "Muestra 2", "Muestra 3"]
y = [10, 15, 7]
y_err = [1, 2, 0.5]

plt.figure(figsize=(8, 5))
plt.errorbar(x, y, yerr=y_err, fmt='o', capsize=5, color='black', label='Datos')
plt.title("Mediciones con Barras de Error (Capsize)")
plt.grid(True, alpha=0.3)
plt.show()
```

## Resumen
| Tipo de Error | Plotly Express | Plotly GO | Matplotlib |
|---|---|---|---|
| Simétrico | `error_y="col"` | `error_y=dict(type='data', array=...)` | `plt.errorbar(yerr=...)` |
| Asimétrico | `error_y="pos", error_y_minus="neg"` | `symmetric=False, array=..., arrayminus=...` | `yerr=[neg, pos]` |
| Banda Continua | (Difícil, usar GO) | `fill='toself'` o `fill='tonexty'` | `plt.fill_between()` |
