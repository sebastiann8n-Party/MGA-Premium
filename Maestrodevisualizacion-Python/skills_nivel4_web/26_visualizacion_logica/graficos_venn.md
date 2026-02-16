# Skill: Visualización Lógica (Proporciones y Relaciones)

## Misión
Mostrar visualmente cómo se **superponen y agrupan** los conjuntos de datos. A diferencia de un radar chart que compara características independientes, el diagrama de Venn muestra la *intersección* (elementos comunes).

## Guía de Ejes

### Conceptos Clave
-   **Conjunto (Set)**: Grupo de elementos únicos (A, B, C).
-   **Unión (A ∪ B)**: Todos los elementos en A o en B.
-   **Intersección (A ∩ B)**: Elementos que están en AMBOS.
-   **Complemento (A' o ¬A)**: Elementos que NO están en A.

### ¿Cuándo usarlo?
-   Clientes que compran Producto A Y Producto B ( Cross-selling ).
-   Pacientes con Síntoma X Y Síntoma Y Y Síntoma Z (Venn 3 círculos).
-   Genes comunes entre especies.
-   Análisis de Cohortes (Usuarios activos vs Retenidos vs Nuevos).

---

## Implementación

### 1. Matplotlib-Venn (Simple y Estático)
La librería `matplotlib-venn` es la solución directa para diagramas de 2 o 3 círculos.

```python
from matplotlib_venn import venn2, venn3
import matplotlib.pyplot as plt

# A. Venn de 2 círculos (Conjuntos A y B)
# Subsets = (Solo A, Solo B, Intersección A&B)
venn2(subsets = (10, 5, 2), set_labels = ('Grupo A', 'Grupo B'))
plt.title("Intersección Simple")
plt.show()

# B. Venn de 3 círculos
# Subsets sigue el orden binario: (100, 010, 110, 001, 101, 011, 111)
# 100: Solo A, 010: Solo B, 110: A&B, 001: Solo C, etc.
venn3(subsets = (20, 10, 12, 10, 9, 4, 3), set_labels = ('Set 1', 'Set 2', 'Set 3'))
plt.title("Intersección Compleja")
plt.show()
```

### 2. UpSet Plot (Para > 3 Conjuntos) - Moderno
El diagrama de Venn colapsa visualmente con más de 3 conjuntos. **UpSet Plot** es la alternativa moderna recomendada para visualización de muchas intersecciones.
Requiere `pip install upsetplot`.

```python
from upsetplot import plot
from matplotlib import pyplot as plt
import pandas as pd

# Datos de ejemplo (Multinivel)
example = generate_counts() # upsetplot tiene generador de datos dummy

# Generar gráfico UpSet
plot(example)
plt.show()
```

---

## Reglas de Diseño

1.  **Etiquetado Claro**: Las áreas de intersección a veces son pequeñas. Usa líneas de llamada (callouts) si el texto no cabe.
2.  **Color Significativo**: Usa colores semitransparentes (alpha < 0.5) para que la intersección de Rojo y Azul se vea Morada, reforzando la idea de mezcla.
3.  **Límite de Complejidad**: NUNCA uses un diagrama de Venn de 4 o más elipses/círculos "simétricos", es ilegible. Pásate a **UpSet Plot** inmediatamente.
4.  **Proporcionalidad**: Intenta que el área del círculo sea proporcional al tamaño del conjunto (Area-proportional Venn). `matplotlib-venn` lo intenta por defecto, pero a veces es matemáticamente imposible con 3 círculos. Acéptalo o usa un Euler diagram relajado.

## Origen
Skill desarrollada para Nivel 4 (Avanzado Web) cubriendo teoría de conjuntos visual.
