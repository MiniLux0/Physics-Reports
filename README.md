# 🔬 Physics Reports — Física II (CF1B2)

**Universidad Nacional de Ingeniería (UNI) — Facultad de Ciencias**

Este repositorio sirve como portafolio y archivo central de los informes de laboratorio del curso de Física II. Todos los documentos están redactados con alto rigor académico utilizando **LaTeX** (`article` estándar), y el tratamiento de datos experimentales, ajustes de curvas e integración numérica se realizan mediante **Python** (`NumPy`, `SciPy`, `Matplotlib`).

## 👥 Equipo de Trabajo
* **Vera Vivanco, Jesús Rodolfo**
* **Cauti Huachaca, Yordan Orlando**
* **Marín Quispe, Joel Gabriel**

---

## 📊 Estado de los Laboratorios

A continuación se presenta la relación de experiencias del curso y el estado actual de nuestros informes:

| Lab | Título del Experimento | Docente | Estado | Carpeta |
| :---: | :--- | :--- | :---: | :--- |
| **L1** | **Dinámica de Rotación** | Prof. G. Cortez | 🟢 Completado | [`/lab01`](./lab01) |
| **L2** | **Péndulo Físico y Teorema de Steiner** | Prof. R. Salazar | 🟢 Completado | [`/lab02`](./lab02) |
| **L3** | **Ley de Hooke** | Prof. G. Cortez | 🟢 Completado | [`/lab03`](./lab03) |
| **L4** | **Tensión Superficial** | Prof. R. Salazar | 🟢 Completado | [`/lab04`](./lab04) |
| **L5** | **Coeficiente de Dilatación Lineal** | Prof. G. Cortez | ⚪ Pendiente | `-` |
| **L6** | **Calor Específico** | Prof. R. Salazar | ⚪ Pendiente | `-` |

---

## 🔬 Resumen de Experiencias Completadas

### 📌 [Laboratorio 01] Dinámica de Rotación
Estudio experimental de las variables cinemáticas y dinámicas en sistemas rotacionales. Análisis de la conservación del momento angular, cálculo de momentos de inercia de diferentes geometrías y validación experimental de las leyes de Newton aplicadas a la rotación.

### 📌 [Laboratorio 02] Péndulo Físico y Teorema de Steiner
Determinación de la aceleración de la gravedad y análisis del comportamiento oscilatorio de un cuerpo rígido. Comprobación experimental del Teorema de Ejes Paralelos (Steiner) midiendo el periodo de oscilación al variar la distancia entre el centro de masa y el eje de rotación.

### 📌 [Laboratorio 03] Ley de Hooke
Análisis contrastado del comportamiento elástico de un metal (resorte helicoidal) y un polímero viscoelástico (tira de jebe). La experiencia incluyó:
* Verificación del límite elástico y cálculo del módulo de Young.
* Análisis de esfuerzos reales frente a la reducción del área transversal (Efecto de Poisson).
* Cuantificación de la energía mecánica disipada térmica a través de la integración numérica de lazos de histéresis.

### 📌 [Laboratorio 04] Tensión Superficial
Determinación experimental del coeficiente de tensión superficial ($\gamma$) del agua mediante métodos basados en el equilibrio estático. La experiencia incluyó:
* Cálculo de $\gamma$ para el agua pura aplicando equilibrio de torques mediante una balanza de Mohr-Westphal.
* Análisis de una película jabonosa mediante un dispositivo de tubitos e hilo bajo la condición de equilibrio de fuerzas.
* Comprobación cualitativa y cuantitativa de la reducción de las fuerzas de cohesión superficial debido a la acción de moléculas anfifílicas (surfactantes).
* Evaluación de sensibilidad geométrica y propagación de incertidumbres analíticas mediante derivadas parciales.

---

## 📂 Estructura del Repositorio

El repositorio está organizado en carpetas independientes para cada sesión de laboratorio, garantizando que el código y las figuras no se mezclen:

```text
physics-reports/
├── lab01/             ← Informe 1: Dinámica de Rotación
├── lab02/             ← Informe 2: Péndulo Físico
├── lab03/             ← Informe 3: Ley de Hooke
├── lab04/             ← Informe 4: Tensión Superficial
│   ├── main.tex       (Documento principal)
│   ├── sections/      (Secciones modulares del documento)
│   ├── Figures/       (Gráficas y diagramas)
│   └── scripts/       (Código Python para el tratamiento de datos)
│
├── template/          ← Plantilla LaTeX base para futuros informes
└── README.md