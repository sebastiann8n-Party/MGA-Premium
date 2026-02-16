# 🌐 GLOBAL.md — Sistema de Gestión Documental Premium
> **Jurisdicción:** `x:\skills-analista` | **Nivel:** Estratégico | **Versión:** 1.0.0

Este archivo es la **Constitución del Proyecto**. Define las reglas, roles y estándares para la orquestación de `generador_apa` y `Producto_1_Premium`.

---

## 1. Misión y Visión
**Misión:** Proveer herramientas de software de élite para la generación y gestión de documentos profesionales, asegurando estándares académicos (APA) y financieros con precisión matemática.
**Visión:** Convertirse en el estándar "Premium" de referencia para la automatización documental en el entorno `skills-analista`.

---

## 2. Arquitectura del Sistema
El sistema se compone de dos dominios federados bajo este Gobierno Central:

### 📂 Estructura de Carpetas
```
x:\skills-analista\
├── GLOBAL.md                 # (Este archivo) Orquestador Maestro
├── generador_apa/            # [Dominio Académico]
│   ├── .agent/               # Agente Local (Investigador)
│   ├── src/                  # Código Fuente (Core Python)
│   └── tests/                # Pruebas Unitarias
└── Producto_1_Premium/       # [Dominio Financiero]
    ├── .agent/               # Agente Local (Analista Financiero)
    ├── Documentosprofesionales/ # Motor Financiero y Templates
    └── PLAN_MAESTRO.md       # Plan específico del producto
```

---

## 3. Roles y Agentes (Workflow Agéntico)
Para la ejecución de tareas, se asignan los siguientes roles virtuales:

| Rol | Agente Asignado | Responsabilidad |
| :--- | :--- | :--- |
| **Director** | `Sistema` | Gobernanza, aprobación de planes y arquitectura global. |
| **Investigador** | `generador_apa/.agent` | Investigación de normas APA, validación de referencias. |
| **Desarrollador** | `Producto_1_Premium/.agent` | Implementación de lógica financiera, optimización de código. |
| **QA/Tester** | `Coordinador de Calidad` | Pruebas cruzadas y validación de entregables. |

---

## 4. Gobernanza Técnica (Estándares DAMA, DevOps & MGA)

### 4.1 Metodología General Ajustada (MGA)
El `Producto_1_Premium` debe alinearse estrictamente con los 4 módulos de la MGA:
1.  **Identificación:** Problemática, población y alternativas.
2.  **Preparación:** Estudios técnicos, legales y de mercado.
3.  **Evaluación:** Indicadores financieros (VPN, TIR) y económicos (Precios Cuenta).
4.  **Programación:** Cronograma y matriz de financiación.

### 4.2 Calidad del Dato (Data Quality)
- **Exactitud Financiera:** Cálculos de VPN y TIR con precisión `Decimal`. Flujos de caja proyectados a 10+ años.
- **Consistencia Académica:** Citas APA 7ma Edición generadas automáticamente por `generador_apa`.
- **Trazabilidad:** Cada dato financiero debe tener una fuente auditable (e.g., "Fuente: Tabla 3 - DNP").

### 4.3 Estándares de Código
- **Python:** PEP8 estricto. Type hinting obligatorio.
- **Estructura:** Arquitectura modular (Inputs -> Processing -> Outputs).
- **Documentación:** Docstrings estilo Google.

### 4.4 Seguridad
- **Cero Hardcoding:** No credenciales en código.
- **Validación de Entradas:** Sanitización de datos numéricos y de texto.

---

## 5. Protocolo de Comunicación
1. **Lectura:** Los agentes deben leer este `GLOBAL.md` antes de iniciar cualquier sprint.
2. **Escritura:** Los cambios en arquitectura requieren aprobación del Director (Usuario).
3. **Reporte:** Actualizar `task.md` al finalizar cada unidad de trabajo.
