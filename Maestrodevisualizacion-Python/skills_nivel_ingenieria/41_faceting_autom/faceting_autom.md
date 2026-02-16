# Skill Ingenieria: Faceting Automático (Small Multiples)

## Misión
Comparar subconjuntos de datos lado a lado (Trellis Plots / Small Multiples). En lugar de superponer todo en un solo gráfico confuso, el faceting crea una cuadrícula de gráficos idénticos, uno para cada categoría.

## Reglas de Oro
1.  **Comparabilidad:** Todos los subgráficos deben compartir la misma escala de ejes (o una lógica consistente) para facilitar la comparación visual.
2.  **Sobrecarga:** Evita demasiadas filas/columnas. Si hay muchas categorías, usa `facet_col_wrap`.
3.  **Dimensiones:** Puedes usar `facet_row` y `facet_col` simultáneamente para cruzar dos variables categóricas.

## 1. Faceting Básico (Columnas)
Separa el gráfico en columnas según una variable categórica.

```python
import plotly.express as px

df = px.data.tips()

fig = px.scatter(df, x="total_bill", y="tip", color="smoker",
                 facet_col="sex", # Una columna para cada sexo
                 title="Propinas por Cuenta: Separado por Sexo")

fig.show()
```

## 2. Faceting Cruzado (Filas y Columnas)
Crea una matriz de gráficos cruzando dos variables.

```python
import plotly.express as px

df = px.data.tips()

fig = px.histogram(df, x="total_bill",
                   facet_row="time", # Filas: Lunch / Dinner
                   facet_col="day",  # Columnas: Thur, Fri, Sat, Sun
                   category_orders={"day": ["Thur", "Fri", "Sat", "Sun"]}, # Orden personalizado
                   title="Distribución de Cuentas: Hora vs Día")

fig.show()
```

## 3. Faceting con Wrap (Ajuste de Línea)
Si tienes una variable con muchas categorías (ej. 12 meses, 50 estados), usa `facet_col_wrap` para que no se haga un gráfico muy ancho.

```python
import plotly.express as px

# Supongamos un dataset con muchas categorías
df = px.data.gapminder().query("year == 2007")

# Filtrar solo continente Americas para el ejemplo
df_americas = df[df['continent'] == 'Americas']

fig = px.bar(df_americas, y="country", x="lifeExp",
             facet_col="country", # Queremos un gráfico por país (muchos)
             facet_col_wrap=5,    # Máximo 5 columnas, luego baja a la siguiente fila
             color="lifeExp",
             title="Esperanza de Vida en América (Faceting con Wrap)")

# Ocultar etiquetas repetitivas si es necesario
fig.update_yaxes(matches=None, showticklabels=True) 
fig.update_xaxes(matches=None, showticklabels=True)

fig.show()
```

## Resumen
| Argumento | Acción |
|---|---|
| `facet_col="var"` | Crea subgráficos en horizontal (columnas) por cada valor de `var`. |
| `facet_row="var"` | Crea subgráficos en vertical (filas). |
| `facet_col_wrap=N` | Limita el número de columnas a N y continúa abajo. Útil para "muchos múltiplos". |
| `category_orders={}` | Controla el orden de aparición de los subgráficos. |
