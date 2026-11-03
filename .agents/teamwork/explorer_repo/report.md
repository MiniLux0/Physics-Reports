# Reporte de Investigación: Estructura del Repositorio, Convenciones y Estado para Lab 04

**Fecha:** 2026-11-03  
**Investigador:** `explorer_repo` (Teamwork Explorer)  
**Repositorio Base:** `C:\Users\jrvv9\OneDrive\Desktop\Physics-Reports`  
**Destino de Reporte:** `.agents/teamwork/explorer_repo/report.md`

---

## 1. Resumen Ejecutivo

Se investigó exhaustivamente la arquitectura del repositorio `Physics-Reports`, las directrices de la cátedra de Física III (CF2B1, Sección A, Facultad de Ciencias de la Universidad Nacional de Ingeniería - UNI), la plantilla base `template/`, los informes previos en `semestre-03/` (`lab01`, `lab03`) y `semestre-02/` (`lab03`, `lab04`, `lab05`), y el estado del entorno para `semestre-03/lab04`.

**Hallazgo Clave Principal:** El directorio `semestre-03/lab04` **no existe actualmente**. Debe ser inicializado a partir de `template/` (preferiblemente mediante el script automatizado `.agents/skills/physics-reports/scripts/new_lab.py --semester 3 --lab 4 ...`). Toda la estructura de 13 secciones, configuración de `latexmk`, scripts de Python para graficado a 300 DPI, unidades de `siunitx` y directrices de estilo UNI se encuentran plenamente especificadas y documentadas en el repositorio.

---

## 2. Arquitectura de `template/` y Configuración LaTeX

### 2.1. Estructura de Directorios y Archivos de `template/`
El directorio `template/` contiene la plantilla estándar modular del repositorio:
```text
template/
├── .latexmkrc          # Configuración para compilación automática con latexmk
├── main.tex            # Documento raíz, preámbulo, metadatos y llamada a secciones
├── refs.bib            # Base bibliográfica en formato BibLaTeX / Biber
├── Figures/            # Directorio de recursos gráficos y logos
│   └── uni_logo.jpg    # Logo institucional de la UNI
├── scripts/            # Directorio para scripts numéricos y de graficado (Python)
├── sections/           # Los 13 archivos modulares de sección (01 a 13)
└── out/                # Directorio para archivos auxiliares generados durante la compilación
```

### 2.2. Método de Compilación (`.latexmkrc`)
El repositorio tiene una **Regla de Oro de Build**: nunca invocar `pdflatex` directamente de forma manual; siempre se compila mediante `latexmk`.

El archivo `template/.latexmkrc` (líneas 1 a 8) especifica:
```perl
$pdf_mode   = 1;        # Compilación mediante pdflatex
$bibtex_use = 2;        # Uso de biber para la gestión de citas BibLaTeX
$out_dir    = 'out';    # Colocación de archivos auxiliares (.aux, .bcf, .log, .out) en out/

# Copia automática del PDF generado a la raíz del laboratorio
$success_cmd = 'powershell -Command "Copy-Item \'%D\' \'%R.pdf\'"';
```
Comandos de compilación y mantenimiento:
- Compilación normal: `latexmk`
- Limpieza y recompilación tras interrupción o `.aux` corrupto: `latexmk -C; latexmk`
- Limpieza de auxiliares preservando el PDF final: `latexmk -c`

### 2.3. Preámbulo de `main.tex` y Paquetes de Formato
Analizado en `template/main.tex` (líneas 9 a 144):
1. **Clase y Geometría:**
   - `\documentclass[a4paper, 11pt, oneside]{article}`
   - `\usepackage[top=2.5cm, bottom=2.5cm, left=3.0cm, right=2.5cm]{geometry}`
2. **Idioma y Tipografía:**
   - `\usepackage[utf8]{inputenc}`, `\usepackage[T1]{fontenc}`, `\usepackage[spanish, es-tabla]{babel}`
   - `\usepackage{csquotes}`, `\usepackage{lmodern}`
   - `\usepackage[nopatch={toc,footnote}]{microtype}` cargado al final del preámbulo.
3. **Matemáticas:**
   - `\usepackage{amsmath}`, `\usepackage{amssymb}`, `\usepackage{mathtools}`
4. **Metrología y Unidades SI (`siunitx` v3):**
   - Configuración:
     ```latex
     \sisetup{
         output-decimal-marker = {,},
         separate-uncertainty  = true,
         per-mode              = symbol,
     }
     ```
   - Unidades personalizadas obligatorias declaradas en el preámbulo:
     ```latex
     \DeclareSIUnit{\sample}{Sa}           % Muestras (GSa/s, MSa/s)
     \DeclareSIUnit{\division}{div}        % Divisiones de retícula (V/div, s/div)
     \DeclareSIUnit{\ppm}{ppm}             % Partes por millón
     \DeclareSIUnit{\inch}{in}             % Pulgadas
     \DeclareSIUnit{\voltpp}{V_{pp}}       % Tensión pico a pico
     \DeclareSIUnit{\voltrms}{V_{rms}}     % Tensión eficaz True-RMS
     \DeclareSIUnit{\millivoltpp}{mV_{pp}} % Milivoltios pico a pico
     ```
5. **Figuras y Tablas:**
   - `\usepackage{graphicx}` con `\graphicspath{{Figures/}}` (permite referenciar imágenes sin ruta ni extensión).
   - `\usepackage{float}` para fijar posición estricta con especificador `[H]`.
   - `\usepackage{caption}`, `\usepackage{subcaption}`.
   - `\usepackage{booktabs}`, `\usepackage{multirow}`, `\usepackage{array}`.
   - Prohibición estricta de `\hline` y líneas verticales `|`. Tablas con 4+ columnas deben envolverse obligatoriamente en `\resizebox{\linewidth}{!}{% ... %}`.
6. **Colores e Hipervínculos:**
   - `\usepackage[dvipsnames]{xcolor}`, con color institucional `\definecolor{uni-blue}{RGB}{0, 56, 101}`.
   - `\usepackage[hypertexnames=false, colorlinks=true, linkcolor=uni-blue, citecolor=uni-blue, urlcolor=uni-blue]{hyperref}`.
7. **Encabezados y Pies (`fancyhdr`):**
   - `\fancyhead[L]{\small\textit{\labcurso}}`
   - `\fancyhead[R]{\small\textit{Lab \labnumero\ --- \labtitulo}}`
   - `\fancyfoot[C]{\small\thepage}`
   - `\renewcommand{\headrulewidth}{0.4pt}`
8. **Estructura y Títulos (`titlesec`):**
   - `\newcommand{\sectionbreak}{\clearpage}`: cada sección principal inicia en página nueva.
   - Formato formal con barra horizontal:
     ```latex
     \titleformat{\section}[block]{\Large\bfseries}{\thesection.}{0.6em}{}[\vspace{2pt}\titlerule\vspace{4pt}]
     \titleformat{\subsection}[block]{\large\bfseries}{\thesubsection}{0.6em}{}
     \titleformat{\subsubsection}[runin]{\normalsize\bfseries\itshape}{\thesubsubsection}{0.5em}{}[.\quad]
     ```
   - Profundidad de numeración: `\setcounter{secnumdepth}{3}`.
9. **Espaciado y Paginación:**
   - `\setstretch{1.15}`, `\setlength{\parskip}{0.4em}`, `\setlength{\parindent}{0pt}`.
   - Paginación romana (`\pagenumbering{roman}`) para portada e índice (`\tableofcontents`), y arábiga (`\pagenumbering{arabic}`) para el cuerpo.
10. **Bibliografía y Anexos:**
    - `\usepackage[backend=biber, style=numeric, sorting=none]{biblatex}` y `\addbibresource{refs.bib}`.
    - `\usepackage[toc, page]{appendix}` con redefinición a español (`Anexo`, `Anexos`).

---

## 3. Las 13 Secciones Canónicas de `Physics-Reports`

En el repositorio, todo informe consta exactamente de 13 secciones numeradas e integradas modularmente mediante `\input{sections/NN_nombre}`:

| N° | Archivo | Nombre Canónico | Requisitos de Contenido y Estructura |
| :---: | :--- | :--- | :--- |
| **01** | `01_introduccion.tex` | **Introducción** (`\label{sec:introduccion}`) | 3 a 5 párrafos: Fenómeno físico (microscópico $\to$ macroscópico), magnitudes fundamentales SI, referencias bibliográficas (\cite{serway}, \cite{halliday}), sistema experimental y anticipación de fuentes de error. |
| **02** | `02_resumen.tex` | **Resumen** | 2 a 3 párrafos ejecutivos: Propósito del experimento, rango de parámetros, metodología, resultados cuantitativos con incertidumbre ($x \pm \delta x$), parámetros OLS ($m, b, R^2$), errores relativos porcentuales ($E_r \le 10\%$, idealmente $< 1\%$) y conclusión sintética. |
| **03** | `03_objetivos.tex` | **Objetivos** (`\label{sec:objetivos}`) | Subdividido en `\subsection{Objetivo general}` y `\subsection{Objetivos específicos}` con lista numerada `\begin{enumerate}` (4 a 5 objetivos medibles y concisos). |
| **04** | `04_fundamento.tex` | **Fundamento Teórico** | Modelos físico-matemáticos, deducción analítica de ecuaciones de trabajo, ecuaciones numeradas con `\begin{equation}\label{eq:...}\end{equation}`, uso de `\texorpdfstring` en títulos con símbolos matemáticos, diagramas y factores geométricos. |
| **05** | `05_materiales.tex` | **Materiales y Equipos** (`\label{sec:materiales}`) | Bloques estandarizados por instrumento (`\subsection{...}`) con descripción y función, especificaciones del fabricante, incertidumbres instrumentales y operativas ($\delta N = \pm 0{,}1\,\text{div}$), precauciones operativas, imágenes con dimensión uniforme `width=0.50\linewidth, height=5.5cm` y tabla metrológica de resumen (`tab:especificaciones_equipos`). |
| **06** | `06_procedimiento.tex` | **Procedimiento Experimental** (`\label{sec:procedimiento}`) | Pasos secuenciales y cronológicos en `\begin{enumerate}` con continuidad mediante `\setcounter{enumi}{...}`. Documentación de adquisición digital vía osciloscopio / USB y advertencias explícitas de seguridad eléctrica/térmica. |
| **07** | `07_resultados.tex` | **Resultados Experimentales** (`\label{sec:resultados}`) | Tablas construidas exclusivamente con `booktabs`, encabezados con unidades `\unit{...}`, datos numéricos con `\num{...}` o `\qty{...}`, parámetros constantes en tabla inicial (`tab:parametros_constantes`), y tablas de mediciones crudas envueltas en `\resizebox{\linewidth}{!}{%...%}`. |
| **08** | `08_analisis_exp.tex` | **Análisis Experimental** (`\label{sec:analisis_exp}`) | Análisis **estrictamente cualitativo y fenomenológico**: evaluación de tendencias, linealidad vs no linealidad, morfología de ondas/curvas, hipótesis físicas tentativas, remitiendo explícitamente el cálculo numérico formal a la Sección 09. |
| **09** | `09_tratamiento.tex` | **Tratamiento de Datos y Resultados** (`\label{sec:tratamiento}`) | Sustitución paso a paso, regresión por mínimos cuadrados ordinarios (MCO/OLS) con pendiente $m$, intercepto $b$, errores estándar $s_m, s_b$, coeficiente $R^2$, propagación formal de errores en cuadratura (GUM / JCGM 100:2008), resultados finales enmarcados y error relativo porcentual respecto a la teoría. |
| **10** | `10_graficas.tex` | **Gráficas** (`\label{sec:graficas}`) | Figuras en bloque `[H]` con `width=0.85\linewidth`. Captions exhaustivos detallando colores, barras de error, líneas de ajuste, citas al script `\cite{script_graficas}` y librerías científicas (`\cite{numpy}`, `\cite{scipy}`, `\cite{matplotlib}`). **Párrafo de cierre obligatorio de transición** hacia la Sección 11. |
| **11** | `11_analisis_graficas.tex` | **Análisis de Gráficas** (`\label{sec:analisis_graficas}`) | Evaluación cuantitativa y estadística: dispersión respecto a la curva teórica, validación de pendiente e intercepto ($|b|/s_b < 1$), análisis de residuos (distribución aleatoria vs sesgo sistemático), concordancia con constantes físicas. |
| **12** | `12_obs_sug_conclusiones.tex` | **Observaciones, Sugerencias y Conclusiones** (`\label{sec:conclusiones}`) | Tres subsecciones obligatorias: `\subsection{Observaciones}` (fuentes de error sistemático y operativo), `\subsection{Sugerencias}` (recomendaciones técnicas factibles) y `\subsection{Conclusiones Cuantitativas}` (respuestas 1 a 1 a los objetivos con valores numéricos $\pm \delta x$ y errores relativos). |
| **13** | `13_anexos.tex` | **Anexos** (`\begin{appendices} ... \end{appendices}`) | Estructurado en secciones independientes: **Anexo A** (Deducciones analíticas formales de modelos matemáticos), **Anexo B** (Propagación analítica de incertidumbres con derivadas parciales y `\boxed{...}`), **Anexo C** (Cuestionario oficial de la guía resuelto detalladamente) y **Anexo D** (Hoja de datos original escaneada o test facsimilar). |

---

## 4. Tono y Estilo Narrativo: Voz Estudiantil de la UNI

El examen de los informes en `semestre-03/lab01`, `semestre-03/lab03` y las directrices en `GEMINI.md` evidencia un perfil de redacción distintivo y consistente:

1. **Primera Persona del Plural Activa y Colaborativa:**
   - La redacción adopta la voz de los estudiantes de la mesa de trabajo: *"conectamos"*, *"ajustamos el divisor de tensión"*, *"observamos en la pantalla del osciloscopio"*, *"registramos simultáneamente"*, *"constatamos la estabilidad térmica"*, *"verificamos que para tensiones inferiores a 0,50 V la corriente fuera despreciable"*.
   - Se evita tanto el tono impersonal frío o autómata (*"se procedió a la realización de..."* repetido mecánicamente) como el estilo excesivamente pomposo o de paper doctoral consagrado.
2. **Pedagógico, Explicativo y Honesto:**
   - El estudiante de la UNI razona físicamente lo que ve: explica el puente entre el concepto teórico (ej. efecto Drude, barrera de potencial, constante de tiempo $\tau = RC$) y la respuesta experimental observada en el banco de trabajo.
   - Transparencia experimental total: si un componente no estuvo disponible, se documenta con naturalidad (*"el elemento nicrón fue formalmente omitido por indicación del docente de mesa debido a indisponibilidad de la muestra patronada"*); si un punto experimental se desvía, se identifica como dato atípico y se razona la causa instrumental (ej. resolución del voltímetro o inestabilidad transitoria de contacto del cursor).
3. **Rigurosidad Metrológica y Física Innegociable:**
   - A pesar de la frescura en el tono, la formalidad matemática y física es máxima:
     - Cada magnitud lleva sus unidades SI con macro `siunitx` (`\qty{...}{...}`).
     - Separador decimal con coma (`output-decimal-marker = {,}`).
     - Cada cálculo indirecto incluye su deducción analítica de propagación por derivadas parciales.
     - Errores porcentuales evaluados explícitamente y acotados ($E_r \le 10\%$, idealmente $< 1\%$).

---

## 5. Estructura de Scripts en Python y Gráficas Científicas

Analizado a partir de `semestre-03/lab03/scripts/grap.py` y `.agents/skills/physics-reports/references/python_plotting.md`:

1. **Ubicación y Entorno de Ejecución:**
   - Script central en `semestre-XX/labNN/scripts/grap.py`.
   - Backend gráfico no interactivo al inicio: `plt.switch_backend('Agg')`.
   - Exportación directa a `semestre-XX/labNN/Figures/` en resolución de publicación de **300 DPI**:
     ```python
     figures_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Figures'))
     plt.savefig(output_path, dpi=300, bbox_inches='tight')
     ```
2. **Estilo Gráfico Científico:**
   - Fondo blanco puro: `fig.patch.set_facecolor('white')`, `ax.set_facecolor('white')`.
   - Paleta de colores sobria: Azul UNI (`#003865`), Rojo carmín para ajustes (`#D9534F`), Gris para referencias teóricas (`gray`).
   - Formateador de coma decimal en ambos ejes mediante `matplotlib.ticker.FuncFormatter`:
     ```python
     def format_coma_1dec(val, pos):
         return f"{val:.1f}".replace('.', ',')
     ax.xaxis.set_major_formatter(FuncFormatter(format_coma_1dec))
     ```
3. **Composición de Doble Panel (Gridspec):**
   - Panel superior (75% altura): Datos experimentales con barras de error bidireccionales (`errorbar`), curva de ajuste analítico (MCO o no lineal) y curva teórica ideal.
   - Panel inferior (25% altura): Residuos $e_i = y_i - \hat{y}_i$ con línea de cero punteada, permitiendo verificar visualmente si los residuos son aleatorios (ajuste adecuado) o sistemáticos.
4. **Referencia en LaTeX:**
   - No se incluye la extensión `.png` ni la ruta: `\includegraphics[width=0.85\linewidth]{fig_nombre}`.
   - Caption exhaustivo explicando cada trazo y citando a los paquetes: `\cite{script_graficas}`, `\cite{numpy}`, `\cite{scipy}`, `\cite{matplotlib}`.

---

## 6. Macros, Entornos y Reglas del Linter

El linter oficial `.agents/skills/physics-reports/scripts/validate_report.py` impone 14 reglas estrictas que deben cumplirse:

1. **Comas Decimales en Modo Matemático:** Prohibido escribir `$2,46$`. Usar `\qty{2,46}{\volt}`, `\num{2,46}` o encierre entre llaves `$2{,}46$`.
2. **Símbolos Unicode Sueltos:** Prohibido usar `°` o `℃`. Usar `\qty{25,0}{\celsius}`, `\unit{\degree}` o `^{\circ}\text{C}`.
3. **Subíndices en `siunitx`:** Prohibido escribir `\qty{20}{\volt}_{\text{pp}}` en modo texto (produce error `Missing $ inserted`). Usar la macro declarada `\qty{20}{\voltpp}` o `\qty{20}{\voltrms}`.
4. **Rangos con `\qtyrange`:** Solo acepta `{val1}{val2}{unidad}`. Si los extremos tienen prefijos distintos (ej. $1\,\text{mV}$ a $10\,\text{V}$), escribir: `$\qty{1}{\milli\volt}\text{ a }\qty{10}{\volt}$`.
5. **Reglas `booktabs`:** Prohibido terminantemente el uso de `\hline` y barras verticales `|`. Tablas $\ge 4$ columnas obligatoriamente con `\resizebox{\linewidth}{!}{%...%}`.
6. **Consistencia de `\label{}` y `\ref{}`:** No admitir etiquetas duplicadas ni referencias rotas.
7. **Citas Bibliográficas:** Toda cita `\cite{clave}` debe existir obligatoriamente en `refs.bib`.
8. **Figuras de Materiales (Sección 05):** Dimensiones estándar obligatorias: `[width=0.50\linewidth, height=5.5cm]`.
9. **Modo Matemático en Encabezados:** Obligatorio usar `\texorpdfstring{$math$}{texto}` para prevenir avisos en marcadores PDF.
10. **Prohibición de Markdown en `.tex`:** Prohibido `**negrita**`, `*cursiva*`, `# Título`.
11. **Delimitadores de Ecuación:** Prohibido el uso de `$$ ... $$`; usar `\[ ... \]` o `\begin{equation} ... \end{equation}`.
12. **Etiquetas Huérfanas:** Toda figura o tabla declarada debe estar citada en el cuerpo del texto (salvo `fig:mat_` en materiales).
13. **Párrafo de Transición en Sección 10:** La Sección 10 debe culminar obligatoriamente con un párrafo de cierre que referencie a la Sección 11 (`\ref{sec:analisis_graficas}`).
14. **Terminología Física Precisa:** Detección de fallos léxicos (ej. *deflectar* en vez de *deflactar*; *reflexión especular* en vez de *rotación* en Lissajous).

---

## 7. Estado de `semestre-03/lab04` y Requerimientos de Inicialización

### 7.1. Situación Actual
- **Existencia:** El directorio `C:\Users\jrvv9\OneDrive\Desktop\Physics-Reports\semestre-03\lab04` **NO EXISTE**.
- **Guías previas en repo:** En `semestre-03/guias/` solo existen carpetas para `lab01` y `lab03`.
- **Materiales disponibles fuera del repo:**
  - Guía oficial impresa fotografiada: 5 imágenes en `.user_uploaded/` de la conversación Antigravity.
  - Datos experimentales tomados por compañeros: `C:\Users\jrvv9\Downloads\WhatsApp Unknown 2026-11-02 at 7.33.38 PM`.
  - Carpeta de cátedra local: `C:\Users\jrvv9\OneDrive\Documentos\UNI\03_Cursos\2026-2_Ciclo3_Actual\CF2B1_Fisica_III`.

### 7.2. Procedimiento de Inicialización Requerido
Para inicializar `semestre-03/lab04` cumpliendo los estándares del repositorio:
1. **Ejecutar el script oficial de creación:**
   ```powershell
   python .agents/skills/physics-reports/scripts/new_lab.py --semester 3 --lab 4 --title "Circuitos RC --- Carga y descarga de un condensador" --date "Lima, 03 de noviembre de 2026" --teacher "Cortez R., Gregorio" --course "Física General / Física III --- Sección A"
   ```
2. **Estructura que generará:**
   - `semestre-03/lab04/main.tex` (con metadatos actualizados).
   - `semestre-03/lab04/.latexmkrc`.
   - `semestre-03/lab04/Figures/uni_logo.jpg`.
   - `semestre-03/lab04/scripts/`.
   - `semestre-03/lab04/sections/` (01 a 13).
   - `semestre-03/lab04/refs.bib`.
3. **Ajuste de Integrantes de Mesa:**
   Verificar en `main.tex` la inclusión del grupo habitual de mesa:
   ```latex
   \newcommand{\labintegrantes}{%
       \begin{enumerate}
           \item Vera Vivanco, Jesús Rodolfo \quad (20252703K)
           \item Casañe Ramírez, Gerald Giordano \quad (20251368C)
           \item Sánchez Feril, Piero Alejandro \quad (20251629A)
       \end{enumerate}
   }
   ```
4. **Archivos a Incorporar para el Lab 04:**
   - `semestre-03/lab04/PLAN_TRABAJO.md`: Plan maestro de 13 secciones, delimitación de datos reales vs simulados y respuestas al cuestionario (a, b, c, d).
   - `semestre-03/lab04/scripts/grap.py` (y scripts auxiliares de modelado): Procesamiento de datos de WhatsApp, cálculo de $\tau = RC$, capacitancias experimentales $C = \tau / R$, propagación de errores y modelado con dispersión instrumental para datos faltantes.

---

## 8. Conclusiones y Próximos Pasos para el Equipo

1. **Plantilla Lista y Comprobada:** La infraestructura de LaTeX y Python del repositorio está perfectamente estandarizada y es directamente extensible para el Laboratorio 4.
2. **Inicialización Inmediata:** La creación de `semestre-03/lab04` mediante `new_lab.py` es el primer paso ejecutable para el implementador.
3. **Hoja de Ruta de Cumplimiento:**
   - Redacción del plan detallado en `semestre-03/lab04/PLAN_TRABAJO.md`.
   - Implementación de scripts en `semestre-03/lab04/scripts/`.
   - Ejecución del validador `validate_report.py --lab lab04`.
   - Compilación oficial con `latexmk` dentro de `semestre-03/lab04/`.
