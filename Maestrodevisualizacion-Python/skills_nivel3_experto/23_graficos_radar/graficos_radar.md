# Skill: Gráfico de Radar (Spider Chart)

## Misión
Visualizar el **perfil de desempeño o características** de una o varias entidades a través de múltiples variables cuantitativas. Permite identificar fortalezas y debilidades de un vistazo al comparar la forma del polígono resultante.

## Guía de Ejes

### Conceptos Clave
-   **Variables (Radios)**: Cada eje radial representa una métrica distinta (ej: Velocidad, Fuerza, Resistencia).
-   **Escala**: Todos los ejes deben estar normalizados a la misma escala (ej: 0-10, 0-100%) para que la forma sea interpretable.
-   **Área**: El área cubierta por el polígono da una idea del desempeño general.

### ¿Cuándo usarlo?
-   **Perfiles de Habilidades**: Jugadores de videojuegos (Ataque, Defensa, Magia), Empleados (Liderazgo, Técnico, Comunicación).
-   **Comparación de Productos**: Teléfonos (Cámara, Batería, Pantalla, Precio).
-   **Benchmarking**: Comparar una entidad contra el promedio del sector.

---

## Implementación

### 1. Plotly (Radar Interactivo)
Plotly ofrece la mejor implementación moderna con `scatterpolar`. El truco es repetir el primer punto al final para cerrar el polígono.

```python
import plotly.graph_objects as go

# Variables
categories = ['Procesamiento', 'Memoria', 'Almacenamiento', 'Batería', 'Pantalla']

# Datos (Nótese que el primer valor se repite al final para cerrar el ciclo)
r_modelo_a = [4, 3, 5, 2, 4, 4] 
r_modelo_b = [3, 4, 3, 5, 3, 3]
theta = categories + [categories[0]]

fig = go.Figure()

# Añadir Modelo A
fig.add_trace(go.Scatterpolar(
      r=r_modelo_a,
      theta=theta,
      fill='toself',
      name='Modelo A'
))

# Añadir Modelo B
fig.add_trace(go.Scatterpolar(
      r=r_modelo_b,
      theta=theta,
      fill='toself',
      name='Modelo B'
))

fig.update_layout(
  polar=dict(
    radialaxis=dict(
      visible=True,
      range=[0, 5] # Escala fija importante
    )),
  showlegend=True,
  title="Comparación de Smartphones"
)

fig.show()
```

### 2. Matplotlib (Proyección Polar)
Más complejo de configurar manualmente pero flexible.

```python
import numpy as np
import matplotlib.pyplot as plt

# Datos
labels=np.array(['Ataque', 'Defensa', 'Velocidad', 'Agilidad', 'Stamina'])
stats=np.array([90, 65, 88, 72, 80])

# Ángulos para cada eje
angles=np.linspace(0, 2*np.pi, len(labels), endpoint=False).tolist()

# Cerrar el plot
stats=np.concatenate((stats,[stats[0]]))
angles+=angles[:1]

fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))

ax.fill(angles, stats, color='red', alpha=0.25)
ax.plot(angles, stats, color='red', linewidth=2)

ax.set_yticks([20, 40, 60, 80, 100])
ax.set_yticklabels(["20", "40", "60", "80", "100"], color="grey", size=7)
ax.set_xticks(angles[:-1])
ax.set_xticklabels(labels)

plt.title("Perfil del Jugador")
plt.show()
```

---

## Reglas de Diseño

1.  **Escala Común**: NUNCA uses escalas diferentes en cada eje (ej: precio en miles y rating en 1-5) sin normalizar primero. La distorsión visual inducirá a error.
2.  **Límite de Variables**: No uses más de 7-8 variables, se vuelve un círculo ilegible. Ideal entre 3 y 6.
3.  **Comparación**: Si comparas muchas entidades (más de 3), usa "small multiples" (varios gráficos pequeños) en lugar de encimarlos todos en uno solo ("spaghetti polar").
4.  **Orden**: Si las variables tienen un orden lógico (ej: Pasado -> Presente -> Futuro, o Fases de un proceso), respétalo en sentido horario. Si son independientes, agrúpalas por afinidad.

## Origen
Skill desarrollada siguiendo estándares de Nivel 3 (Experto) para visualización multivariable de perfiles.
