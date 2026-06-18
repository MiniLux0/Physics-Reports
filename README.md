# Physics Reports — Física II (CF1B2)

**Universidad Nacional de Ingeniería (UNI) — Facultad de Ciencias — Escuela de Física**

Repositorio de informes de laboratorio del curso **Física II (CF1B2), Sección A**. Los documentos se redactan en **LaTeX** (`article` estándar, compilado con `latexmk` + `biber`) y el tratamiento de datos experimentales se realiza con **Python** (`NumPy`, `SciPy`, `Matplotlib`).

**Autor principal:** Vera Vivanco, Jesús Rodolfo — 20252703K
Los integrantes de cada informe se especifican en la portada del documento correspondiente.

---

## Estado de los laboratorios

| Lab | Título | Docente | Estado |
| :---: | :--- | :--- | :---: |
| L1 | Dinámica de Rotación | Cortez, G. | ✅ Completado |
| L2 | Péndulo Físico y Teorema de Steiner | Salazar, R. | ✅ Completado |
| L3 | Ley de Hooke | Cortez, G. | ✅ Completado |
| L4 | Tensión Superficial | Salazar, R. | ✅ Completado |
| L5 | Coeficiente de Dilatación Lineal | Cortez, G. | ✅ Completado |
| L6 | Calor Específico | Salazar, R. | ⬜ Pendiente |

---

## Laboratorios completados

### L1 — Dinámica de Rotación
Estudio de las variables cinemáticas y dinámicas en sistemas rotacionales. Análisis de la conservación del momento angular, cálculo de momentos de inercia de distintas geometrías y validación de las leyes de Newton aplicadas a la rotación.

### L2 — Péndulo Físico y Teorema de Steiner
Determinación experimental de la aceleración de la gravedad y análisis del comportamiento oscilatorio de un cuerpo rígido. Comprobación del Teorema de Ejes Paralelos (Steiner) midiendo el periodo de oscilación en función de la distancia entre el centro de masa y el eje de rotación.

### L3 — Ley de Hooke
Análisis del comportamiento elástico de un resorte helicoidal y un polímero viscoelástico (tira de jebe). Se determinó la constante elástica, el módulo de Young y la energía disipada por histéresis mediante integración numérica.

### L4 — Tensión Superficial
Determinación del coeficiente de tensión superficial γ del agua por dos métodos de equilibrio estático: torques con balanza de Mohr–Westphal (agua pura, γ₁ = 39,73 ± 0,88 mN/m) y fuerzas con película jabonosa sobre dispositivo de hilo (γ₂ = 12,21 ± 1,10 mN/m). Se verificó cuantitativamente la reducción de γ por acción de surfactantes y se realizó propagación analítica de incertidumbres con derivadas parciales.

### L5 — Coeficiente de Dilatación Lineal
Determinación experimental del coeficiente de dilatación lineal $\alpha$ para cobre, aluminio y vidrio borosilicato mediante el método de la aguja giratoria por rodadura sin deslizamiento ($\Delta L = D\,\Delta\theta$), calentando las muestras por flujo continuo de vapor de agua. Se reportaron los coeficientes con incertidumbres absolutas propagadas en cuadratura: $\alpha_{\text{Al}} = (2{,}46 \pm 0{,}11) \times 10^{-5}\ ^\circ\text{C}^{-1}$, $\alpha_{\text{Cu}} = (1{,}60 \pm 0{,}07) \times 10^{-5}\ ^\circ\text{C}^{-1}$ y $\alpha_{\text{vidrio}} = (2{,}43 \pm 0{,}14) \times 10^{-6}\ ^\circ\text{C}^{-1}$. Se analizó el deslizamiento mecánico y la transferencia de calor convectiva como principales fuentes de desviación.

---

## Estructura del repositorio

```
Physics-Reports/
├── template/          ← Plantilla base para nuevos labs
│   ├── main.tex
│   ├── refs.bib
│   ├── _latexmkrc     (renombrar a .latexmkrc al copiar)
│   └── sections/      (13 archivos .tex)
├── lab01/
├── lab02/
├── lab03/
├── lab04/
├── lab05/             ← Coeficiente de Dilatación Lineal
│   ├── main.tex
│   ├── refs.bib
│   ├── sections/
│   ├── Figures/
│   └── scripts/
├── AGENTS.md          ← convenciones para agentes de código
└── README.md
```

Cada carpeta `labNN/` es autónoma: contiene su propio `main.tex`, `refs.bib`, secciones, figuras y scripts de Python.

---

## Compilación

```powershell
cd labNN
latexmk        # compila con pdflatex + biber
latexmk -c    # limpia auxiliares
```

Requiere **MiKTeX** (Windows) con `latexmk` y `biber` disponibles en el PATH.

---

## Stack técnico

| Herramienta | Uso |
| :--- | :--- |
| LaTeX (`article`) + MiKTeX | Redacción y tipografía del informe |
| `latexmk` + `biber` | Compilación automática |
| `siunitx` | Unidades SI con coma decimal |
| `biblatex` estilo IEEE | Referencias bibliográficas |
| Python + NumPy + SciPy | Tratamiento de datos e incertidumbres |
| Matplotlib | Gráficas exportadas a `Figures/` |