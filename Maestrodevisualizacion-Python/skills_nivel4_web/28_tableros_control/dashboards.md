# Skill: Tableros de Control Web (Streamlit Dashboard)

## Misión
Orquestar tus visualizaciones en una **aplicación web interactiva**. Permite que el usuario final *filtre, explore y comparta* los resultados sin necesidad de ejecutar código. Transforma los scripts sueltos en un **producto de datos**.

## Guía de Ejes

### Conceptos Clave
-   **Widget**: Elemento de control (Slider, Dropdown, Checkbox).
-   **State**: Variable que persiste entre interacciones (ej: filtro actual).
-   **Layout**: Distribución visual (Columnas, Sidebar, Tabs).
-   **Reactividad**: El gráfico se actualiza SOLO cuando cambia su input.

### ¿Cuándo usarlo?
-   Reportes mensuales automatizados.
-   Exploración de datos para stakeholders no técnicos.
-   Prototipado rápido de aplicaciones ML (demo de modelo).
-   Monitoreo en tiempo real.

---

## Implementación

### 1. Estructura Básica (`app.py`)
Streamlit convierte scripts de Python en web apps mágicamente.
Ejecutar con: `streamlit run app.py`

```python
import streamlit as st
import pandas as pd
import plotly.express as px

# Configuración de Página (Siempre al inicio)
st.set_page_config(layout="wide", page_title="Dashboard Demo")

# Título y Descripción
st.title("📊 Panel de Control Maestro")
st.markdown("Exploración interactiva de datos de ventas.")

# Sidebar (Barra lateral de controles)
with st.sidebar:
    st.header("Filtros")
    year = st.slider("Año", 2020, 2025, 2023)
    category = st.multiselect("Categoría", ["Tech", "Fashion", "Home"], default=["Tech"])

# Cargar Datos (Simulados o Reales)
@st.cache_data # Decorador para optimizar carga (Cache)
def load_data():
    return pd.DataFrame({
        'Year': [2022, 2023, 2024]*3,
        'Category': ['Tech']*3 + ['Fashion']*3 + ['Home']*3,
        'Sales': [100, 150, 200, 80, 120, 160, 50, 70, 90]
    })

df = load_data()

# Filtrar Datos (Reactividad)
df_filtered = df[(df['Year'] == year) & (df['Category'].isin(category))]

# Layout Principal (Columnas)
col1, col2 = st.columns([2, 1]) # Proporción 2:1

with col1:
    st.subheader("Tendencia de Ventas")
    fig = px.bar(df_filtered, x='Category', y='Sales', color='Category', 
                 title=f"Ventas en {year}")
    st.plotly_chart(fig, use_container_width=True)

with col2:
    st.subheader("Métricas Clave")
    total_sales = df_filtered['Sales'].sum()
    delta = total_sales - 100 # Comparación dummy
    st.metric(label="Ventas Totales", value=f"${total_sales}", delta=f"{delta}")
    
    st.subheader("Datos Crudos")
    st.dataframe(df_filtered, use_container_width=True)

# Expander (Acordeón para detalles ocultos)
with st.expander("Ver notas técnicas"):
    st.write("Datos extraídos del sistema SAP el 12/10/2025.")
```

### 2. Elementos Avanzados y Consejos

#### A. Session State (Memoria)
Para guardar variables entre recargas (ej: contador de clicks).
```python
if 'count' not in st.session_state:
    st.session_state.count = 0

if st.button('Click me'):
    st.session_state.count += 1

st.write(f'Clicks: {st.session_state.count}')
```

#### B. Pestañas (Tabs)
Organiza contenido denso.
```python
tab1, tab2 = st.tabs(["Gráficos", "Mapa"])
with tab1:
    st.line_chart(df['Sales'])
with tab2:
    st.map(pd.DataFrame({'lat': [40], 'lon': [-74]}))
```

---

## Reglas de Diseño

1.  **Carga Perezosa (Lazy Loading)**: Usa `@st.cache_data` para funciones pesadas (cargar CSV, queries SQL). Si no lo haces, la app recargará TODO cada vez que muevas un slider.
2.  **Jerarquía Visual**:
    -   Lo más importante arriba a la izquierda (KPIs).
    -   Gráficos complejos en el centro.
    -   Tablas de detalle abajo o en Tabs secundarios.
3.  **Feedback al Usuario**: Si una operación tarda, usa `with st.spinner('Cargando...'):` para que el usuario no crea que se colgó.
4.  **Responsive**: Usa `use_container_width=True` en los gráficos de Plotly/Altair para que se adapten al ancho de la columna o móvil.

## Origen
Skill desarrollada para Nivel 4 (Avanzado Web) integrando visualización en productos interactivos.
