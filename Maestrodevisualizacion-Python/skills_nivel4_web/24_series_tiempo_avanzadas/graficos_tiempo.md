# Skill: Series de Tiempo Avanzadas (Time Series)

## Misión
Analizar y visualizar **datos que cambian en el tiempo** para detectar tendencias, estacionalidad y anomalías. A diferencia de un gráfico de líneas simple, esta skill se enfoca en herramientas financieras y estadísticas avanzadas como velas, bandas de Bollinger y descomposición de series.

## Guía de Ejes

### Conceptos Clave
-   **Tendencia (Trend)**: Dirección general de la serie a largo plazo.
-   **Estacionalidad (Seasonality)**: Patrones repetitivos (ej: ventas aumentan en diciembre).
-   **Ruido (Noise)**: Variaciones aleatorias impredecibles.
-   **Resampling**: Cambiar la frecuencia de los datos (ej: de minutos a días).

### ¿Cuándo usarlo?
-   Análisis bursátil (Stock prices).
-   Predicción de demanda (Forecasting).
-   Monitoreo de servidores (CPU usage).
-   Estudios climáticos (Temperatura anual).

---

## Implementación

### 1. Plotly (Interactivo con Range Slider)
Plotly brilla aquí por sus herramientas nativas de zoom y selección de rangos temporales.

```python
import plotly.express as px

df = px.data.stocks() # Datos de ejemplo

fig = px.line(df, x='date', y='GOOG', title='Precio de Acción Google')

# Añadir Range Slider y Botones de Selección Rápida
fig.update_xaxes(
    rangeslider_visible=True,
    rangeselector=dict(
        buttons=list([
            dict(count=1, label="1m", step="month", stepmode="backward"),
            dict(count=6, label="6m", step="month", stepmode="backward"),
            dict(count=1, label="YTD", step="year", stepmode="todate"),
            dict(count=1, label="1y", step="year", stepmode="backward"),
            dict(step="all")
        ])
    )
)
fig.show()
```

### 2. Candlestick (Velas Japonesas) - Financiero
Fundamental para trading. Muestra Apertura, Máximo, Mínimo y Cierre (OHLC).

```python
import plotly.graph_objects as go
import pandas as pd

# Simular datos
df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv')

fig = go.Figure(data=[go.Candlestick(x=df['Date'],
                open=df['AAPL.Open'],
                high=df['AAPL.High'],
                low=df['AAPL.Low'],
                close=df['AAPL.Close'])])

fig.update_layout(title="Apple Stock Price (Candlestick)")
fig.show()
```

### 3. Seaborn + Pandas (Resampling y Descomposición)
Para análisis estadístico rápido.

```python
import matplotlib.pyplot as plt
import seaborn as sns

# Resampling: Promedio mensual
df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date', inplace=True)
monthly_avg = df['AAPL.Close'].resample('M').mean()

plt.figure(figsize=(12, 6))
sns.lineplot(data=monthly_avg, color="purple", label="Promedio Mensual")
plt.title("Tendencia Mensual Suavizada")
plt.show()
```

---

## Reglas de Diseño

1.  **Eje X Continuo**: Asegúrate de que tu eje X sea de tipo `datetime`. Si usas strings ("Jan", "Feb"), perderás la escala temporal real si faltan datos intermedios.
2.  **Contexto**: Usa anotaciones para eventos clave (ej: "Lanzamiento de producto" o "Caída del mercado 2020") que expliquen picos o valles.
3.  **Comparación Relativa**: Si comparas series con escalas muy diferentes (ej: Bitcoin vs Euro), usa dos ejes Y o normaliza los datos (porcentaje de cambio desde el inicio) para ver la correlación real.
4.  **No unir puntos faltantes**: Si hay un hueco en los datos, deja el espacio en blanco (gap) en lugar de interpolar una línea recta falsa, a menos que la interpolación sea intencional.

## Origen
Skill desarrollada para Nivel 4 (Avanzado Web) cubriendo visualización financiera y temporal.
