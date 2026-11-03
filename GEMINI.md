# GEMINI.md — Physics Reports (UNI Facultad de Ciencias)

## 1. Contexto del Proyecto
Informes de laboratorio de **Física General / Física III (CF2B1) — Sección A**, Universidad Nacional de Ingeniería, Lima, Perú.
El proyecto utiliza **LaTeX (pdflatex + biber)** gestionado por `latexmk` en Windows con MiKTeX y **Python** para procesamiento numérico, propagación de incertidumbres y graficado científico a 300 DPI.

**Directorio Local de Cátedra CF2B1 (Teoría, PCs, Exámenes, Guías de Lab):**
- `C:\Users\jrvv9\OneDrive\Documentos\UNI\03_Cursos\2026-2_Ciclo3_Actual\CF2B1_Fisica_III`

**Integrantes habituales (Mesa de Trabajo):**
- Vera Vivanco, Jesús Rodolfo — código 20252703K (Autor principal / dueño del repo)
- Casañe Ramírez, Gerald Giordano — código 20251368C (o Cauti Huachaca, Yordan Orlando — código 20222236E)
- Sánchez Feril, Piero Alejandro — código 20251629A (o Bustos Ttito, José Fabricio — código 20200490F)

---

## 2. Skill Oficial: `physics-reports`
El repositorio cuenta con una **Skill de Creación y Validación de Informes** ubicada en [`.agents/skills/physics-reports/`](./.agents/skills/physics-reports/SKILL.md):
- **Automatización de nuevos labs:** `.agents/skills/physics-reports/scripts/new_lab.py`
- **Linter y validador de calidad:** `.agents/skills/physics-reports/scripts/validate_report.py`
- **Guía detallada de secciones (01 a 13):** [`.agents/skills/physics-reports/references/sections_guide.md`](./.agents/skills/physics-reports/references/sections_guide.md)
- **Convenciones y paquetes LaTeX:** [`.agents/skills/physics-reports/references/latex_guidelines.md`](./.agents/skills/physics-reports/references/latex_guidelines.md)
- **Generación de Gráficas en Python:** [`.agents/skills/physics-reports/references/python_plotting.md`](./.agents/skills/physics-reports/references/python_plotting.md)
- **Tratamiento de Incertidumbres y Errores:** [`.agents/skills/physics-reports/references/error_propagation.md`](./.agents/skills/physics-reports/references/error_propagation.md)

---

## 3. Comandos de Construcción y Validación

```powershell
# 1. Crear un nuevo laboratorio (semestre-03 o semester N)
python .agents/skills/physics-reports/scripts/new_lab.py --semester 3 --lab 1 --title "<Título del Lab>" --date "Lima, DD de mes de 2026" --teacher "Apellido, N."

# 2. Generar gráficas de alta resolución (300 DPI)
python semestre-XX/labNN/scripts/grap.py

# 3. Validar cumplimiento riguroso de directrices antes de compilar
python .agents/skills/physics-reports/scripts/validate_report.py --lab labNN

# 4. Compilar informe oficial (desde dentro de semestre-XX/labNN/)
latexmk

# 5. Recuperación limpia en caso de aborto o error de .aux
latexmk -C; latexmk

# 6. Limpiar archivos auxiliares de compilación manteniendo el PDF
latexmk -c
```

**Reglas de Oro de Build:**
- **NUNCA** ejecutar `pdflatex` directamente — siempre usar `latexmk`.
- `latexmk` lee automáticamente `.latexmkrc`, coloca los auxiliares en `out/`, compila las citas con `biber`, y copia el archivo final generado a `main.pdf`.
- Si un proceso de compilación fue interrumpido previamente y arroja `! File ended while scanning use of \@newl@bel`, ejecutar siempre `latexmk -C; latexmk`.

---

## 4. Estructura del Repositorio

```text
Physics-Reports/
├── GEMINI.md           ← Reglas globales para el asistente Gemini / Antigravity
├── AGENTS.md           ← Reglas de compatibilidad de agentes
├── .agents/
│   └── skills/
│       └── physics-reports/
│           ├── SKILL.md
│           ├── scripts/
│           │   ├── new_lab.py
│           │   └── validate_report.py
│           └── references/
│               ├── sections_guide.md
│               ├── latex_guidelines.md
│               ├── python_plotting.md
│               └── error_propagation.md
├── template/           ← Plantilla base limpia y sincronizada
│   ├── main.tex
│   ├── refs.bib
│   ├── .latexmkrc
│   ├── Figures/
│   ├── scripts/
│   └── sections/ (01 a 13)
├── semestre-02/        ← Informes del segundo semestre (Física II CF1B2)
│   ├── lab03/
│   ├── lab04/
│   └── lab05/
└── semestre-03/        ← Informes del tercer semestre
    ├── guias/          (guías PDF, hojas de datos escaneadas, datasheets/ y reportes validados .md)
    └── lab01/          (informe completo compilado)
```

---

## 5. Resumen de Secciones del Informe

| Sección | Archivo | Contenido Clave |
| :--- | :--- | :--- |
| **01** | `01_introduccion.tex` | Fenómeno físico (micro $\to$ macro), magnitudes SI, citas bibliográficas \cite{serway}, \cite{halliday}. |
| **02** | `02_resumen.tex` | Síntesis ejecutiva del experimento, magnitudes obtenidas con incertidumbre $\pm \delta x$ y errores relativos porcentuales. |
| **03** | `03_objetivos.tex` | Objetivo general y lista de objetivos específicos numerados/viñetas. |
| **04** | `04_fundamento.tex` | Modelo físico-matemático, deducciones, ecuaciones numeradas (`\label{eq:...}`) y factores geométricos destacados. |
| **05** | `05_materiales.tex` | Bloques descriptivos por instrumento con fotos estandarizadas (`width=0.50\linewidth, height=5.5cm`) y tabla metrológica. |
| **06** | `06_procedimiento.tex` | Pasos ordenados cronológicamente con `\begin{enumerate}` y advertencias de seguridad física. |
| **07** | `07_resultados.tex` | `\label{sec:resultados}`, tablas `booktabs` con `\resizebox`, parámetros fijos y datos crudos de retícula/sensores. |
| **08** | `08_analisis_exp.tex` | `\label{sec:analisis_exp}`, análisis estrictamente **cualitativo** de linealidad, dispersión, escalas y fuentes de ruido. |
| **09** | `09_tratamiento.tex` | `\label{sec:tratamiento}`, cálculos paso a paso, regresión por mínimos cuadrados ($m, b, R^2$), propagación analítica y errores relativos. |
| **10** | `10_graficas.tex` | `\label{sec:graficas}`, figuras `[H]`, `width=0.85\linewidth`, captions completos con citas al script y librerías científicas. |
| **11** | `11_analisis_graficas.tex` | `\label{sec:analisis_graficas}`, análisis cuantitativo de pendientes, residuos aleatorios vs sistemáticos y concordancia teórica. |
| **12** | `12_obs_sug_conclusiones.tex` | `\label{sec:conclusiones}`, tres subsecciones claras: Observaciones (fuentes de error), Sugerencias y Conclusiones cuantitativas. |
| **13** | `13_anexos.tex` | Anexo A (demostración analítica), Anexo B (propagación con derivadas parciales y `\boxed{}`), Anexo C (cuestionario resuelto y hoja de datos). |

---

## 6. Paquetes, Unidades y Convenciones LaTeX

### 6.1. Unidades SI (`siunitx` v3)
- **Separador decimal:** Usar siempre coma decimal (`output-decimal-marker={,}`).
  - `\qty{9,81}{m/s^2}`, `\qty{26,0 \pm 0,5}{\celsius}`, `\qty{6,8}{\percent}`.
- **Unidades personalizadas obligatorias en `main.tex`:**
  ```latex
  \DeclareSIUnit{\sample}{Sa}           % Muestras (GSa/s, MSa/s)
  \DeclareSIUnit{\division}{div}        % Divisiones de retícula (V/div, s/div)
  \DeclareSIUnit{\ppm}{ppm}             % Partes por millón
  \DeclareSIUnit{\inch}{in}             % Pulgadas
  \DeclareSIUnit{\voltpp}{V_{pp}}       % Tensión pico a pico
  \DeclareSIUnit{\voltrms}{V_{rms}}     % Tensión eficaz True-RMS
  \DeclareSIUnit{\millivoltpp}{mV_{pp}} % Milivoltios pico a pico
  ```
- **Subíndices en unidades:** Usar siempre `\qty{20}{\voltpp}` o `\qty{20}{\voltrms}`. **NUNCA** escribir `\qty{20}{\volt}_{\text{pp}}` en modo texto fuera de math mode para evitar errores `Missing $ inserted`.
- **Restricción de `\qtyrange`:** Solo admite una unidad común `{val1}{val2}{unidad}`. Si los extremos tienen distintos prefijos (ej. $1\,\text{mV/div}$ a $10\,\text{V/div}$ o $1\,\mu\text{Hz}$ a $5\,\text{MHz}$), escribir explícitamente:
  `$\qty{1}{\milli\volt\per\division}\text{ a }\qty{10}{\volt\per\division}$` o `$\qty{1}{\micro\hertz}\text{ a }\qty{5}{\mega\hertz}$`.
- **Decimales en modo matemático:** Si se escribe un decimal sin siunitx en modo matemático, DEBE usarse llaves: `$2{,}46$` (nunca `$2,46$`).

### 6.2. Tablas Científicas (`booktabs` + `graphicx`)
- **Uso obligatorio:** `\toprule`, `\midrule`, `\bottomrule`.
- **Prohibición estricta:** Queda terminantemente prohibido el uso de `\hline` y líneas verticales `|`.
- **Ajuste de margen obligatorio:** Toda tabla con 4 o más columnas o información extensa DEBE envolverse en:
  ```latex
  \resizebox{\linewidth}{!}{%
  \begin{tabular}{@{}llll@{}}
      \toprule
      ...
      \bottomrule
  \end{tabular}%
  }
  ```

### 6.3. Figuras e Imágenes (`graphicx`, `float`)
- Usar siempre el especificador `[H]` provisto por `float`.
- Las imágenes se colocan en `labNN/Figures/` y se llaman en LaTeX sin ruta ni extensión: `\includegraphics{nombre_figura}`.
- Gráficas científicas con `width=0.85\linewidth`.

### 6.4. Tipografía, Hipervínculos y Bibliografía
- **Hipervínculos (`hyperref`):** Configurar `hypertexnames=false`, `colorlinks=true`, `linkcolor=uni-blue`. Paginación en `roman` para carátula/índice y `arabic` para el cuerpo.
- **Bibliografía (`biblatex` + `biber`):** Citas numéricas con `\cite{clave}` vinculadas a `refs.bib`.
- **Matemáticas en títulos:** Usar siempre `\texorpdfstring{$math$}{texto}` para evitar advertencias de marcadores PDF.
- **Guión largo:** Usar triple guión `---` en títulos y encabezados.

---

## 7. Python y Gráficas Científicas (`scripts/grap.py`)
- Script modular ubicado en `labNN/scripts/grap.py`.
- Formato de guardado: `labNN/Figures/<nombre>.png` a **300 DPI** con `bbox_inches='tight'`.
- Fondo blanco puro (`facecolor='white'`), formateador de coma decimal en los ejes (`FuncFormatter`), barras de error visibles en datos experimentales y curvas teóricas/ajustes en trazo continuo o discontinuo.

---

## 8. Metodología de Datos y Validación de Errores
1. **Datasheets y Manuales:** Guardar siempre las especificaciones oficiales en `guias/datasheets/` y citarlas en `refs.bib`.
2. **Estimaciones "al ojo":** Las lecturas de divisiones visuales deben expresarse con un único decimal realista y cerrado ($\delta N = \pm 0{,}1\text{ div}$).
3. **Control de Errores Relativos:** Todos los errores relativos calculados deben mantenerse rigurosamente acotados ($\le 10\%$, idealmente $< 1\%$).
4. **Documento de Validación:** Redactar previamente un reporte en Markdown en `guias/reporte_validado_errores.md` con todas las tablas, incertidumbres propagadas y respuestas a preguntas de la guía como base matemática antes de volcar al LaTeX.
