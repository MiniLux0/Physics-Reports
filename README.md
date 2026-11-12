<meta name="google-site-verification" content="sbLIiXRMiteN8G0VM4I5a_Rlk48VGQ2etw8kN5FCrGE" />

# ⚡ Physics Reports — Plataforma de Física Experimental & Metrología Computacional
<p align="center">
  <b>Universidad Nacional de Ingeniería (UNI) · Facultad de Ciencias · Escuela Profesional de Física</b><br>
  <i>Framework reproducible de redacción, análisis numérico, validación metrológica y publicación científica en LaTeX & Python</i>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/LaTeX-pdflatex%20%2B%20biber-blue?logo=latex" alt="LaTeX">
  <img src="https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Engine-latexmk-green" alt="latexmk">
  <img src="https://img.shields.io/badge/Metrology-siunitx%20v3-orange" alt="siunitx">
  <img src="https://img.shields.io/badge/Facultad-UNI%20Ciencias-crimson" alt="UNI Ciencias">
  <img src="https://img.shields.io/badge/License-Academic%20Open%20Access-lightgrey" alt="License">
</p>

---

## 🏛️ Filosofía del Repositorio

Este repositorio constituye una **plataforma integral de ingeniería documental y reproducibilidad científica** para los laboratorios de física de la Universidad Nacional de Ingeniería.

El proyecto se fundamenta en **4 Pilares de Calidad Científica**:

1. **Rigor Metrológico Integral:** Prohibición absoluta de mediciones o cálculos huérfanos. Toda magnitud física experimental calculada se acompaña obligatoriamente de su incertidumbre instrumental y aleatoria propagada analíticamente mediante derivadas parciales en cuadratura ($\delta x$), cotas de error relativo porcentual ($E_r \le 10\%$, idealmente $< 1\%$) y contrastación formal con especificaciones oficiales de hojas de datos (*datasheets*).
2. **Reproducibilidad Total (*Code-as-Paper*):** Ningún resultado numérico ni gráfica es colocado manualmente. Todo dato proviene de pipelines en **Python** (`NumPy`, `SciPy`, `Matplotlib`), exportados a 300 DPI con barras de error bidireccionales, formateador de coma decimal y análisis de regresión por mínimos cuadrados documentado.
3. **Excelencia Tipográfica en LaTeX:** Código fuente modular en 13 secciones conforme al estándar internacional de publicaciones científicas (citas bibliográficas numéricas con `biblatex` + `biber`, maquetación de tablas con `booktabs` + `\resizebox`, unidades del Sistema Internacional con `siunitx` v3).
4. **Evolución Multisemestral y Escalabilidad:** Arquitectura modular organizada por semestres (`semestre-02/`, `semestre-03/`, ...), preservando la trazabilidad de los cursos de Mecánica, Termodinámica, Electromagnetismo, Circuitos y Óptica.

---

## 📋 Catálogo y Estado de Informes de Laboratorio

### Semestre 03 — Física General / Física III (Electricidad y Magnetismo)

> [!NOTE]
> **Directorio Central de Cátedra (Teoría, PCs, Exámenes y Guías de Laboratorio):**  
> [`CF2B1_Fisica_III`](file:///C:/Users/jrvv9/OneDrive/Documentos/UNI/03_Cursos/2026-2_Ciclo3_Actual/CF2B1_Fisica_III) (Semestre Académico 2026-2, Secciones A y B).

| Lab | Título del Experimento | Informe Oficial | Estado |
| :---: | :--- | :---: | :---: |
| **L1** | **El osciloscopio como instrumento de medida** | [📄 `main.pdf`](semestre-03/lab01/main.pdf) | ✅ Publicado (36 págs) |
| **L3** | **Curvas características voltaje–corriente** | [📄 `main.pdf`](semestre-03/lab03/main.pdf) | ✅ Publicado |
| **L4** | **Circuitos RC — Carga y descarga de un condensador** | [📄 `main.pdf`](semestre-03/lab04/main.pdf) | ✅ Publicado (45 págs) |

* **L1 — El osciloscopio como instrumento de medida:**  
  * *Contenido:* Calibración de tensión DC por regresión lineal ($m = 1{,}0000 \pm 0{,}0000$, $R^2 = 1{,}0000$), contraste True-RMS en señales senoidales y cuadradas ($E_r \approx 0{,}57\%$), análisis de desfase y relación de frecuencias mediante curvas de Lissajous ($X$-$Y$), deducción analítica rigurosa del valor eficaz $V_{\text{rms}}$ en Anexo A y resolución exhaustiva de las 6 interrogantes teóricas del cuestionario oficial.
* **L3 — Curvas características voltaje–corriente:**  
  * *Contenido:* Caracterización y modelamiento experimental de tres dipolos: resistor de carbón de $100\,\Omega$ ($R = 100{,}02 \pm 0{,}18\,\Omega$, $E_r = 0{,}02\%$), lámpara incandescente de tungsteno ($I = 0{,}1461 V^{0{,}5726}$, $E_{r,n} = 4{,}5\%$ respecto al modelo térmico de Stefan-Boltzmann), y diodo semiconductor de silicio ($V_u = 0{,}66 \pm 0{,}06\,\text{V}$, $E_r = 1{,}5\%$). Incluye resolución completa del cuestionario de 6 preguntas, deducción analítica y propagación GUM de incertidumbres.
* **L4 — Circuitos RC — Carga y descarga de un condensador:**  
  * *Contenido:* Caracterización experimental de regímenes transitorios en circuitos RC bajo excitación de onda cuadrada periódica ($f = 250\text{ Hz}$, $V = 10\text{ V}_{pp}$) en la Mesa C7. Determinación de constantes de tiempo $\tau$ con cursores digitales en osciloscopio Rohde & Schwarz HMO1202, verificación metrológica de la relación $\tau = RC$ por mínimos cuadrados ordinarios (MCO) con interceptos físicamente nulos ($|b|/s_b \le 1{,}23$), comprobación en tiempo real de la Segunda Ley de Kirchhoff mediante suma de señales (`MATH ADD`) y análisis de red con divisor resistivo aplicando el Teorema de Thévenin.

---

### Semestre 02 — Física II (CF1B2) — Sección A (Mecánica y Fluidos)

| Lab | Título del Experimento | Informe Oficial | Estado |
| :---: | :--- | :---: | :---: |
| **L1** | Dinámica de Rotación | — | 📝 Formato Word (Pre-LaTeX) |
| **L2** | Péndulo Físico y Teorema de Steiner | — | 📝 Formato Word (Pre-LaTeX) |
| **L3** | **Ley de Hooke y Comportamiento Elástico** | [📄 `main.pdf`](semestre-02/lab03/main.pdf) | ✅ Publicado |
| **L4** | **Tensión Superficial de Líquidos** | [📄 `main.pdf`](semestre-02/lab04/main.pdf) | ✅ Publicado |
| **L5** | **Coeficiente de Dilatación Lineal de Sólidos** | [📄 `main.pdf`](semestre-02/lab05/main.pdf) | ✅ Publicado |
| **L6** | Calor Específico | — | ❌ No realizado (Falta de gas en laboratorio) |

* **L3 — Ley de Hooke:** Análisis elástico de resorte helicoidal y polímero viscoelástico (jebe), cálculo del módulo de Young y energía disipada por histéresis mediante integración numérica trapezoidal.
* **L4 — Tensión Superficial:** Coeficiente $\gamma$ del agua pura mediante Balanza de Mohr–Westphal ($\gamma_1 = 39{,}73 \pm 0{,}88\,\text{mN/m}$) y película jabonosa sobre dispositivo de hilo ($\gamma_2 = 12{,}21 \pm 1{,}10\,\text{mN/m}$).
* **L5 — Coeficiente de Dilatación Lineal:** Determinación experimental de $\alpha$ para aluminio ($(2{,}46 \pm 0{,}11) \times 10^{-5}\,^\circ\text{C}^{-1}$), cobre ($(1{,}60 \pm 0{,}07) \times 10^{-5}\,^\circ\text{C}^{-1}$) y vidrio borosilicato ($(2{,}43 \pm 0{,}14) \times 10^{-6}\,^\circ\text{C}^{-1}$) por amplificación geométrica con aguja giratoria ($\Delta L = D \cdot \Delta\theta$).

---

## 📁 Estructura del Repositorio

```text
Physics-Reports/
├── template/                        ← Plantilla base modular oficial (13 secciones)
│   ├── main.tex
│   ├── refs.bib
│   ├── .latexmkrc
│   ├── Figures/
│   ├── scripts/
│   └── sections/ (01 a 13)
├── semestre-02/                     ← Informes del 2.° semestre (Física II CF1B2)
│   ├── lab03/                       (Ley de Hooke)
│   ├── lab04/                       (Tensión Superficial)
│   └── lab05/                       (Dilatación Lineal)
├── semestre-03/                     ← Informes y recursos del 3.° semestre
│   ├── guias/                       (Guías PDF oficiales, datasheets/ y datos crudos)
│   ├── lab01/                       (El osciloscopio como instrumento de medida)
│   └── lab03/                       (Curvas características voltaje–corriente)
└── README.md                        ← Manifiesto y documentación principal
```

Cada carpeta de laboratorio es **completamente autónoma**: incluye su propio código fuente modular `sections/`, figuras vectoriales/raster en `Figures/`, bibliografía `refs.bib`, configuración `.latexmkrc` y scripts de análisis en `scripts/`.

---

## 📑 Arquitectura Modular del Informe (13 Secciones)

Cada informe de laboratorio se estructura de manera estricta en 13 bloques independientes:

| Sección | Archivo | Propósito y Contenido Metodológico |
| :--- | :--- | :--- |
| **01** | `01_introduccion.tex` | Fenomenología física (escala microscópica a macroscópica) y citas bibliográficas fundamentales. |
| **02** | `02_resumen.tex` | Síntesis ejecutiva de magnitudes halladas con incertidumbre $\pm \delta x$ y errores relativos porcentuales. |
| **03** | `03_objetivos.tex` | Objetivo general y objetivos específicos directamente evaluables. |
| **04** | `04_fundamento.tex` | Modelo físico-matemático formal, deducción de ecuaciones de trabajo y parámetros geométricos. |
| **05** | `05_materiales.tex` | Fichas técnicas por instrumento con especificaciones metrológicas, fotos normalizadas y tabla resumen. |
| **06** | `06_procedimiento.tex` | Secuencia cronológica del protocolo experimental y advertencias de seguridad física. |
| **07** | `07_resultados.tex` | Tablas de datos brutos con `booktabs` + `resizebox` y registro de condiciones ambientales de laboratorio. |
| **08** | `08_analisis_exp.tex` | Análisis estrictamente **cualitativo** de linealidad, dispersión, escalas y fuentes de ruido. |
| **09** | `09_tratamiento.tex` | Cálculos numéricos paso a paso, regresión lineal ($m, b, R^2$), propagación de incertidumbres y errores. |
| **10** | `10_graficas.tex` | Figuras de alta resolución (300 DPI) con leyendas descriptivas completas y citas a librerías científicas. |
| **11** | `11_analisis_graficas.tex` | Evaluación cuantitativa de pendientes, análisis de residuos e interpretación física de correlaciones. |
| **12** | `12_obs_sug_conclusiones.tex` | Observaciones (fuentes de error sistemático/aleatorio), Sugerencias técnicas y Conclusiones cuantitativas. |
| **13** | `13_anexos.tex` | Anexo A (Deducción analítica), Anexo B (Propagación con derivadas parciales), Anexo C (Cuestionario) y Anexo D (Hoja de datos original firmada). |

---

## 🛠️ Stack Tecnológico & Compilación

| Herramienta | Versión / Estándar | Propósito en el Proyecto |
| :--- | :--- | :--- |
| **LaTeX (MiKTeX)** | `article` (A4) | Maquetación y tipografía científica del documento |
| **LaTeXmk + Biber** | Motor automatizado | Gestión de compilaciones cruzadas, citas y enlaces |
| **`siunitx`** | v3 (`output-decimal-marker={,}`) | Estandarización de magnitudes y unidades SI con coma decimal |
| **`booktabs`** | Top / Mid / Bottom | Tablas de alta calidad sin líneas verticales |
| **Python 3** | 3.10+ | Procesamiento numérico, propagación matricial y ajustes |
| **NumPy & SciPy** | `numpy`, `scipy.optimize` | Regresión por mínimos cuadrados y cálculo de matrices |
| **Matplotlib** | `matplotlib.pyplot` | Gráficas científicas exportadas a 300 DPI |

### Instrucciones de Compilación:
```powershell
# 1. Posicionarse en el directorio del laboratorio
cd semestre-03/lab01

# 2. Compilar informe completo (pdflatex + biber)
latexmk

# 3. Limpiar archivos auxiliares de compilación manteniendo el PDF
latexmk -c

# 4. Limpieza profunda y recompilación desde cero (si es necesario)
latexmk -C; latexmk
```

---

## 👥 Integrantes y Mesa de Trabajo

**Universidad Nacional de Ingeniería — Facultad de Ciencias**  
*Docente Encargado (Semestre 03):* **Cortez R., Gregorio**

* **Vera Vivanco, Jesús Rodolfo** — Código: `20252703K` *(Autor principal / Administrador del repositorio)*
* **Casañe Ramírez, Gerald Giordano** — Código: `20251368C` *(Semestre 03)*
* **Sánchez Feril, Piero Alejandro** — Código: `20251629A` *(Semestre 03)*

*Colaboradores Históricos (Semestre 02):*
* **Cauti Huachaca, Yordan Orlando** — Código: `20222236E`
* **Bustos Ttito, José Fabricio** — Código: `20200490F`

---

<p align="center">
  <i>Facultad de Ciencias · Universidad Nacional de Ingeniería · Lima, Perú</i><br>
  <b>2025 — 2026</b>
</p>
