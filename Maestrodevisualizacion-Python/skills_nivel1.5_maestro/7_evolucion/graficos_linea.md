# Skill: Gráficos de Evolución (Líneas)

## Misión
Visualizar cambios a lo largo del tiempo o de una variable continua. Es fundamental para detectar tendencias, ciclos y patrones temporales.

## Reglas de Diseño
1.  **Eje X Continuo:** El eje X debe representar una variable continua (tiempo, distancia, secuencias).
2.  **Conectividad:** Las líneas implican conexión entre puntos. No las uses para categorías discretas sin orden.
3.  **Múltiples Series:** Limita el número de líneas (spaghetti chart). Si hay muchas, usa "small multiples" (Grillas) o destaca solo una.

## 1. Matplotlib (Control Manual)
```python
import matplotlib.pyplot as plt
import numpy as np

# Datos simulados (Tiempo)
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

plt.figure(figsize=(10, 5))

# Serie 1
plt.plot(x, y1, label='Seno', color='blue', linestyle='-')

# Serie 2
plt.plot(x, y2, label='Coseno', color='red', linestyle='--')

plt.title("Evolución Temporal de Funciones")
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud")
plt.legend()
plt.grid(True, alpha=0.3) # Una grilla suave ayuda a leer valores
plt.show()
```

## 2. Seaborn (Series Temporales y Agregación)
Seaborn es excelente para series temporales porque maneja intervalos de confianza automáticamente si hay múltiples observaciones por punto de tiempo.

```python
import seaborn as sns
import matplotlib.pyplot as plt

# Dataset de vuelos (Time Series)
flights = sns.load_dataset("flights")

# Lineplot agrega automáticamente si hay múltiples valores para un mismo x
# Aquí, como hay un valor único por mes/año, dibuja la línea directa.
sns.lineplot(data=flights, x="year", y="passengers", hue="month") 
plt.title("Pasajeros por Año (Segmentado por Mes)")
plt.show()

# Agregación: Promedio anual con intervalo de confianza (sombra)
sns.lineplot(data=flights, x="year", y="passengers")
plt.title("Tendencia General de Pasajeros (Promedio Anual)")
plt.show()
```

## 3. Plotly (Interactivo y Zoom)
El zoom interactivo es crucial para series temporales largas.

```python
import plotly.express as px

df = px.data.stocks()

# Plotly maneja fechas automáticamente en el eje X
fig = px.line(
    df, 
    x='date', 
    y=['GOOG', 'AAPL', 'AMZN'], # Múltiples columnas a la vez
    title='Precio de Acciones (Tech)',
    labels={'value': 'Precio', 'variable': 'Empresa'}
)

# Range Slider: Herramienta útil para navegar en el tiempo
fig.update_xaxes(rangeslider_visible=True)

fig.show()
```

## Tips Avanzados
- **Área (Area Chart):** Útil para mostrar volumen acumulado.
    - Matplotlib: `fill_between()`
    - Plotly: `px.area()`
- **Suavizado:** Si la señal es muy ruidosa, considera graficar una media móvil.
- **Marcadores:** Usa marcadores (`marker='o'` en mpl, `mode='lines+markers'` en plotly) si los puntos de datos son escasos y quieres enfatizar la medición real vs la interpolación.
