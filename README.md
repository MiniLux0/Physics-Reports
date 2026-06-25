<meta name="google-site-verification" content="sbLIiXRMiteN8G0VM4I5a_Rlk48VGQ2etw8kN5FCrGE" />

# Physics Reports — Física II (CF1B2)
<p align="center">
  <b>Universidad Nacional de Ingeniería (UNI)</b><br>
  Facultad de Ciencias · Escuela de Física
</p>

Repositorio de informes de laboratorio del curso **Física II (CF1B2), Sección A**.  
Los informes incluidos están redactados en **LaTeX** y compilados con `latexmk` + `biber`.  
El tratamiento de datos experimentales se realiza con **Python** (NumPy, SciPy, Matplotlib).

**Notas:**
- Los laboratorios L1 y L2 fueron redactados originalmente en Word y no forman parte de este repositorio.
- L6 no fue realizado: el curso permite eliminar un laboratorio, y este fue el elegido. Adicionalmente, hubo inconvenientes logísticos en la sesión (falta de gas en el laboratorio) que imposibilitaron la toma de datos.
---

## 📋 Estado de los laboratorios

| Lab | Título | Estado |
| :---: | :--- | :---: |
| L1 | Dinámica de Rotación | — |
| L2 | Péndulo Físico y Teorema de Steiner | — |
| L3 | Ley de Hooke | ✅ |
| L4 | Tensión Superficial | ✅ |
| L5 | Coeficiente de Dilatación Lineal | ✅ |
| L6 | Calor Específico | ❌ No realizado |

---

## 🔬 Laboratorios en este repositorio

### L3 — Ley de Hooke
Análisis del comportamiento elástico de un **resorte helicoidal** y un **polímero viscoelástico** (tira de jebe).  
Se determinó la constante elástica, el módulo de Young y la energía disipada por histéresis mediante integración numérica sobre el ciclo carga–descarga.

### L4 — Tensión Superficial
Determinación del coeficiente de tensión superficial γ del agua por dos métodos de equilibrio estático:
- **Balanza de Mohr–Westphal** (torques) — agua pura: γ₁ = 39,73 ± 0,88 mN/m
- **Película jabonosa sobre dispositivo de hilo** (fuerzas) — γ₂ = 12,21 ± 1,10 mN/m

Se verificó la reducción de γ por acción de surfactantes y se realizó propagación analítica de incertidumbres con derivadas parciales.

### L5 — Coeficiente de Dilatación Lineal
Determinación experimental de α para tres materiales mediante el **método de la aguja giratoria** (ΔL = D·Δθ), calentando las muestras por flujo continuo de vapor de agua.

| Material | α (°C⁻¹) |
| :--- | :--- |
| Aluminio | (2,46 ± 0,11) × 10⁻⁵ |
| Cobre | (1,60 ± 0,07) × 10⁻⁵ |
| Vidrio borosilicato | (2,43 ± 0,14) × 10⁻⁶ |

Las incertidumbres fueron propagadas en cuadratura. Se analizó el deslizamiento mecánico y la transferencia convectiva como principales fuentes de desviación.

---

## 📁 Estructura del repositorio

```
Physics-Reports/
├── template/          ← Plantilla base reutilizable para nuevos labs
│   ├── main.tex
│   ├── refs.bib
│   ├── _latexmkrc     (renombrar a .latexmkrc al copiar)
│   └── sections/
├── lab03/
├── lab04/
├── lab05/
│   ├── main.tex
│   ├── refs.bib
│   ├── sections/
│   ├── Figures/
│   └── scripts/
└── AGENTS.md          ← Convenciones para agentes de código
```

Cada carpeta `labNN/` es autónoma: contiene su propio `main.tex`, `refs.bib`, secciones, figuras y scripts de Python.

---

## ⚙️ Compilación

```powershell
cd labNN
latexmk        # compila con pdflatex + biber
latexmk -c     # limpia archivos auxiliares
```

Requiere **MiKTeX** (Windows) con `latexmk` y `biber` disponibles en el PATH.

---

## 🛠️ Stack técnico

| Herramienta | Uso |
| :--- | :--- |
| LaTeX (`article`) + MiKTeX | Redacción y tipografía del informe |
| `latexmk` + `biber` | Compilación automática |
| `siunitx` | Unidades SI con coma decimal (`{,}`) |
| `biblatex` (estilo IEEE) | Referencias bibliográficas |
| Python · NumPy · SciPy | Tratamiento de datos e incertidumbres |
| Matplotlib | Gráficas exportadas a `Figures/` |

---

<p align="center">
  <i>Física II · UNI · 2025–2026</i>
</p>
