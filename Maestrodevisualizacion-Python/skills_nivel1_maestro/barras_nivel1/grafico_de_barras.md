# Skill: Gráfico de Barras (Maestro de Visualización)

Esta skill orquesta el uso de `Analítica DAMA` y `Visualización Premium` para generar gráficos de barras de alta calidad, resolviendo problemas específicos como el *Titanic Gender Count*.

## 1. Flujo de Trabajo (Workflow)
1.  **Carga Segura**: Usar `analitica_dama.data_loader_secure`.
2.  **Transformación**: Usar `analitica_dama.validated_aggregation`.
3.  **Estilizado**: Aplicar `visualizacion_premium.apply_premium_style`.
4.  **Generación**: Usar `visualizacion_premium.plot_bar_premium`.

## 2. Guía de Uso del Gráfico de Barras

### ¿Cuándo usarlo?
- **Comparación de Categorías**: Ideal para mostrar diferencias de magnitud entre grupos discretos (ej: Sexo, Supervivencia, Clase).
- **Enfatizar Cambios**: Permite visualizar claramente las diferencias absolutas o relativas.
- **Pocas Categorías**: Funciona mejor cuando el número de barras es manejable (menos de 15) y las etiquetas son legibles.

### ¿Cuándo NO usarlo?
- **Muchas Categorías**: Si hay demasiadas barras, el gráfico se vuelve denso y difícil de leer.
- **Distribuciones Continuas**: Para ver la forma de una distribución de datos numéricos (usar Histograma o KDE).
- **Relación Parte-Todo**: Si el objetivo es mostrar proporciones porcentuales de un total (considerar un gráfico de barras apiladas al 100% o, con cautela, de pastel).
- **Análisis de Tendencias**: Si el eje X es tiempo continuo (usar gráfico de líneas).

### Tipos de Variables por Eje
- **Eje X (Categoría)**: Variable **Cualitativa Nominal** (ej: Hombre/Mujer) o **Ordinal** (ej: 1ra Clase, 2da Clase, 3ra Clase).
- **Eje Y (Métrica)**: Variable **Cuantitativa Discreta** (conteo) o **Continua** (promedio, suma) que represente la magnitud.

## 3. Ejemplo de Aplicación (Titanic)

```python
# Importar skills (asumiendo que están disponibles como módulos o copiando el código)
# from skills_nivel1_maestro import analitica_dama, visualizacion_premium

# 1. Definir Ruta y Columnas (Gobernanza)
FILE_PATH = '../data/titanic.csv' # Parametrizar esto en producción
REQUIRED_COLS = ['Sex', 'PassengerId']

try:
    # 2. Carga (DAMA)
    # df = analitica_dama.data_loader_secure(FILE_PATH, REQUIRED_COLS)
    # Simulación de carga para este ejemplo:
    df = pd.read_csv(FILE_PATH) 
    
    # 3. Transformación (DAMA)
    # conteo = analitica_dama.validated_aggregation(df, 'Sex')
    # Transformación a DataFrame para Seaborn
    conteo_df = df['Sex'].value_counts().reset_index()
    conteo_df.columns = ['Sex', 'Count']
    
    # 4. Configurar Estilo (Premium)
    # visualizacion_premium.apply_premium_style(theme='dark')
    
    # 5. Generar Gráfico
    # visualizacion_premium.plot_bar_premium(
    #    data=conteo_df, 
    #    x='Sex', 
    #    y='Count', 
    #    title='Distribución de Pasajeros por Sexo',
    #    subtitle='Análisis de demografía a bordo del Titanic',
    #    palette='mako'
    # )
    
    # plt.show()
    
except Exception as e:
    print(f"Error en el proceso de visualización: {e}")
```

## 3. Checklist de Calidad
- [ ] ¿Los datos fueron validados antes de graficar?
- [ ] ¿El gráfico tiene título y ejes claros?
- [ ] ¿Se eliminó el "ruido visual" (chart junk)?
- [ ] ¿La paleta de colores es accesible y agradable?
