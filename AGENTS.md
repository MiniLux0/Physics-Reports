# AGENTS.md — Physics Reports (UNI Facultad de Ciencias)

## Proyecto
Informes de laboratorio de **Física II (CF1B2) — Sección A**, Universidad Nacional de Ingeniería, Lima, Perú.
Compilados con LaTeX (pdflatex + biber) en Windows con MiKTeX.

**Integrantes:**
- Vera Vivanco, Jesus Rodolfo — código 20252703K ← autor principal / dueño del repo
- Bustos Ttito, Jose Fabricio — código 20200490F
- Cauti Huachaca, Yordan Orlando — código 20222236E

---

## Build

```powershell
# Desde dentro de la carpeta del lab (e.g. lab04/)
latexmk
```

- Lee `.latexmkrc` automáticamente (pdflatex + biber, auxiliares en `out/`)
- Al terminar copia el PDF a la raíz del lab (`labNN/main.pdf`) vía PowerShell
- **NUNCA** correr `pdflatex` directamente — siempre `latexmk`
- Para limpiar auxiliares: `latexmk -c`

---

## Estructura del repositorio

```
Physics-Reports/
├── template/           ← plantilla base (copiar para nuevo lab)
│   ├── main.tex
│   ├── refs.bib
│   ├── .latexmkrc      (en disco como _latexmkrc, renombrar al copiar)
│   └── sections/
│       ├── 01_introduccion.tex
│       ├── 02_resumen.tex
│       ├── 03_objetivos.tex
│       ├── 04_fundamento.tex
│       ├── 05_materiales.tex
│       ├── 06_procedimiento.tex
│       ├── 07_resultados.tex
│       ├── 08_analisis_exp.tex
│       ├── 09_tratamiento.tex
│       ├── 10_graficas.tex
│       ├── 11_analisis_graficas.tex
│       ├── 12_obs_sug_conclusiones.tex
│       └── 13_anexos.tex
├── lab03/
├── lab04/
└── labNN/
```

**Nota:** `lab01/` y `lab02/` aparecen en el README pero no existen en disco.

---

## Nuevo lab

1. Copiar `template/` → `labNN/`
2. Renombrar `_latexmkrc` → `.latexmkrc` dentro del nuevo lab
3. En `main.tex`, editar **SOLO** el bloque `DATOS DEL INFORME`:
   ```latex
   \newcommand{\labcurso}{Fisica II (CF1B2) --- Seccion A}
   \newcommand{\labnumero}{NN}
   \newcommand{\labtitulo}{Título del laboratorio}
   \newcommand{\labfecha}{Lima, DD de mes de 2026}
   \newcommand{\labdocente}{Apellido, Nombre}
   ```
4. Los integrantes ya están fijos en `main.tex` — no modificar
5. Correr `latexmk` desde `labNN/`

---

## Asignación de secciones por persona

| Secciones | Archivo(s) | Persona |
|-----------|------------|---------|
| 01–04 | introduccion, resumen, objetivos, fundamento | Persona 1 (Vera Vivanco) |
| 05–07 | materiales, procedimiento, resultados | Persona 2 (Bustos Ttito) |
| 08–12 | analisis_exp, tratamiento, graficas, analisis_graficas, obs_sug_conclusiones | Persona 3 (Cauti Huachaca) |
| 13 | anexos | Todos |

---

## Contenido y convenciones de cada sección

### 01 — Introducción
- Contexto físico, principio central con `\cite{}`, sistema experimental, magnitudes a determinar
- Extensión: 3–5 párrafos
- Estructura real observada en lab04:
  1. Fenómeno físico desde nivel molecular → manifestación macroscópica
  2. Definición de la magnitud principal con ecuación inline y unidades SI
  3. Efecto de variables externas relevantes (temperatura, surfactantes, etc.)
  4. Descripción de los dos métodos del experimento (comparación entre ellos)
  5. Párrafo final anticipando resultados esperados y su comparación con el valor bibliográfico
- Citar `\cite{serway}` y `\cite{halliday}` en los puntos de definición y método
- Valores de referencia bibliográfica se introducen aquí con `\SI{}{}`, ej: `$\gamma_{\text{ref}} = \SI{72.8e-3}{\newton\per\meter}$`

### 02 — Resumen
- Síntesis: qué se estudió, cómo, qué se obtuvo
- Incluir resultado principal con incertidumbre y error relativo
- Extensión: 2–3 párrafos

### 03 — Objetivos
```latex
\subsection{Objetivo general}
Texto.
\subsection{Objetivos específicos}
\begin{itemize}
    \item Objetivo 1.
\end{itemize}
```

### 04 — Fundamento Teórico
- Cada concepto como `\subsection{}`
- Todas las ecuaciones numeradas con `\label{eq:nombre}` y referenciadas con `\eqref{}`
- Citar siempre con `\cite{clave}`
- Estructura real observada en lab04:
  1. Subsección de fenómeno base (nivel molecular → macroscópico)
  2. Subsección de definición formal de la magnitud principal con ecuación central `\label{eq:def}`
  3. Subsección por cada método experimental (desarrollo del modelo físico-matemático)
  4. Subsección de efectos externos relevantes (surfactantes, temperatura, etc.)
- Patrón de referencia cruzada entre ecuaciones: `combinando las Ecs.~\eqref{eq:a}, \eqref{eq:b} y \eqref{eq:c}:`
- Patrón con `\textbf{}` para destacar factores clave dentro del texto: `\textbf{el factor 2} que multiplica...`
- Derivaciones largas se remiten al Anexo: `La demostración detallada se desarrolla en el Anexo~A.`
- Usar `\qquad` para separar ecuaciones dobles en una misma línea:
  ```latex
  \begin{equation}
      a + R\sin\alpha = b + R, \qquad h = R\cos\alpha
      \label{eq:geometria}
  \end{equation}
  ```

### 05 — Materiales y Equipos
Bloque por instrumento:
```latex
\subsection{Nombre del instrumento}
\begin{itemize}
    \item \textbf{Descripción y función:} Texto.
    \item \textbf{Especificaciones:}
    \begin{itemize}
        \item Tipo: digital / analógico
        \item Incertidumbre: \qty{\pm 0.005}{s}
    \end{itemize}
    \item \textbf{Precauciones:} Texto.
\end{itemize}
\begin{figure}[H]
    \centering
    \includegraphics[width=0.50\linewidth]{fig_instrumento1}
    \caption{Nombre del instrumento.}
    \label{fig:instrumento1}
\end{figure}
```

### 06 — Procedimiento Experimental
- Pasos en `\begin{enumerate}` en orden cronológico
- Mencionar instrumentos usados en cada paso

### 07 — Resultados Experimentales
- Datos crudos en tablas con booktabs
- Toda tabla: `\caption{}` arriba, `\label{tab:nombre}`, referenciada en texto con `\ref{}`
- Incertidumbres en todas las mediciones
- La sección lleva `\label{sec:resultados}` para que otras secciones la referencien
- Párrafo introductorio breve antes de las tablas explicando qué se presenta
- Subsecciones por método: `\subsection{Primer método --- Nombre del método}`
- Patrón de tabla con magnitudes (3 columnas: Magnitud / Símbolo / Valor):
```latex
\begin{table}[H]
    \centering
    \caption{Parámetros geométricos del instrumento.}
    \label{tab:param_nombre}
    \begin{tabular}{lcc}
        \toprule
        \textbf{Magnitud} & \textbf{Símbolo} & \textbf{Valor} \\
        \midrule
        Radio externo & $R_{\text{ext}}$ & \qty{5.040 \pm 0.005}{\centi\meter} \\
        \bottomrule
    \end{tabular}
\end{table}
```
- Patrón de tabla con `\multirow` para mediciones repetidas:
```latex
\begin{tabular}{cccc}
    \toprule
    \textbf{Medición} & \textbf{Instrumento} & \textbf{Masa (g)} & \textbf{División $n_i$} \\
    \midrule
    \multirow{2}{*}{1} & $J_1$ & \num{20.2 \pm 0.1} & 1 \\
                       & $J_4$ & \num{1.2 \pm 0.1}  & 3 \\
    \midrule
    \multirow{2}{*}{2} & $J_2$ & \num{18.7 \pm 0.1} & 1 \\
    \bottomrule
\end{tabular}
```
- Usar `\midrule` entre grupos de `\multirow`, no `\hline`
- **Decimales:** preferir `\qty{valor \pm incert}{unidad}` o `\num{valor \pm incert}` sobre `$x{,}xx$`

### Tablas anchas (más de 4 columnas o encabezados largos)
- Si la tabla tiene 4+ columnas o encabezados con unidades largas, usar:
```latex
  \resizebox{\textwidth}{!}{%
  \begin{tabular}{...}
  ...
  \end{tabular}}
```
- Alternativamente, acortar encabezados a notación matemática sola:
  `$L_0$ (mm)` en vez de `Longitud inicial $L_0$ (mm)`
- Nunca poner texto descriptivo largo dentro del `\toprule` — va en el `\caption`

### 08 — Análisis Experimental
- Interpretación **cualitativa** de los datos (no calcular — eso va en sección 09)
- La sección lleva `\label{sec:analisis_exp}` para referencias cruzadas
- Párrafo introductorio que indica explícitamente que no se calculan magnitudes derivadas aún
- Subsecciones: `\subsection{Análisis del primer método --- Tabla~\ref{tab:datos_m1}}`
- Estructura real de cada subsección:
  1. Observación del comportamiento general de los datos (rango, dispersión)
  2. Explicación física de por qué se observa ese comportamiento
  3. Identificación de fuentes de error o limitaciones del método
  4. Si aplica: señalar qué término domina en la ecuación y por qué es sensible a errores
- Usar `\qtyrange{a}{b}{unidad}` para rangos: `\qtyrange{2.38e-3}{2.67e-3}{\kilogram}`
- Referencias a ecuaciones del fundamento teórico: `la Ec.~\eqref{eq:gamma_m2}`
- Al final de cada subsección, anticipar lo que se discutirá en conclusiones: `aspecto que se analiza en detalle en la Sección~\ref{sec:conclusiones}`

### 09 — Tratamiento de Datos y Resultados
- Cálculos con ecuaciones numeradas, sustitución numérica con unidades
- Resultado final: `$(valor \pm error)\ \si{unidad}$`
- Ejemplo:
```latex
\subsection{Magnitud — nombre}
A partir de la relación:
\begin{equation}
    a_G = \frac{2d}{t^2}  \label{eq:aceleracion}
\end{equation}
Sustituyendo $d = \qty{0,40}{m}$ y $t = \qty{15,12}{s}$:
\begin{equation*}
    a_G = \frac{2 \times 0{,}40}{(15{,}12)^2} = \qty{3,51e-3}{m/s^2}
\end{equation*}
```

### 10 — Gráficas
- La sección lleva `\label{sec:graficas}`
- Caption completo: descripción + líneas de referencia + valor promedio + cita del script
```latex
\begin{figure}[H]
    \centering
    \includegraphics[width=0.85\linewidth]{grafica_nombre}
    \caption{Variable $x$ para cada medición. La línea roja punteada indica el promedio
    $\overline{x} = \qty{39.73}{\milli\newton\per\meter}$ y la línea negra el valor
    bibliográfico $x_{\text{ref}} = \qty{72.8}{\milli\newton\per\meter}$ \cite{serway}.
    Figura generada con Python \cite{script_graficas}.}
    \label{fig:grafica_nombre}
\end{figure}
La Fig.~\ref{fig:grafica_nombre} evidencia...
```
- La frase después de la figura resume en 1–2 oraciones lo más visible, remitiendo el análisis a la sección 11

### 11 — Análisis de Gráficas
- La sección lleva `\label{sec:analisis_graficas}`
- Subsección por gráfica con título descriptivo usando `\texorpdfstring` para math en títulos:
  ```latex
  \subsection{Gráfica 1 --- \texorpdfstring{$\gamma_i$}{gamma} vs.\ medición (primer método)}
  ```
- Estructura de cada subsección:
  1. Descripción de la distribución de puntos (tendencia, dispersión, monotonía)
  2. Interpretación física de la distribución (¿error sistemático o aleatorio?)
  3. Relación con las barras de error: ¿son consistentes con la dispersión observada?
  4. Comparación con línea de referencia bibliográfica y señalar discrepancia sistemática
  5. Referenciar sección de conclusiones para discusión de causas: `se discute en la Sección~\ref{sec:conclusiones}`

### 12 — Observaciones / Sugerencias / Conclusiones
Tres secciones en un mismo archivo:
```latex
\section{Observaciones}   % fuentes de error: sistemáticas y aleatorias
\section{Sugerencias}     % recomendaciones para mejorar el experimento
\section{Conclusiones}    % responder a cada objetivo con resultado ± incertidumbre
```

### 13 — Anexos
```latex
\begin{appendices}
\section{Propagación de incertidumbre — nombre}
% Fórmula base, derivadas parciales, sustitución numérica, resultado en \boxed{}
\[\boxed{a_G = (3{,}50 \pm 0{,}07) \times 10^{-3}\ \si{m/s^2}}\]

\section{Hoja de recolección de datos}
\begin{figure}[H]
    \centering
    \includegraphics[width=0.80\linewidth]{fig_hoja_datos}
    \caption{Hoja de recolección de datos original.}
    \label{fig:hoja_datos}
\end{figure}
\end{appendices}
```

---

## Paquetes LaTeX usados (no agregar duplicados)

| Paquete | Propósito |
|---------|-----------|
| `siunitx` | Unidades SI — decimal con coma (`output-decimal-marker={,}`) |
| `booktabs` | Tablas: `\toprule`, `\midrule`, `\bottomrule` — nunca `\hline` |
| `amsmath`, `amssymb`, `mathtools` | Matemáticas |
| `graphicx` | Figuras — ruta: `Figures/` (relativa al lab) |
| `subcaption` | Subfiguras con `\begin{subfigure}` |
| `multirow`, `array` | Tablas complejas |
| `biblatex` + biber | Bibliografía estilo IEEE numérico (`style=numeric, sorting=none`) |
| `appendix` | Anexos con `\begin{appendices}...\end{appendices}` |
| `hyperref` | Links en color `uni-blue` = RGB(0,56,101) |
| `fancyhdr` | Encabezado: curso (izq) y "Lab N — Título" (der) |
| `babel` | Español con `es-tabla` |
| `microtype` | Al final del preámbulo — no mover |
| `float` | Posicionamiento `[H]` para figuras y tablas |

**Convenciones siunitx:**
```latex
\SI{9.81}{m/s^2}           % valor con unidad (forma larga)
\qty{9,81}{m/s^2}          % valor con unidad (forma corta, preferida)
\num{1.23 \pm 0.05}        % valor con incertidumbre
\si{\newton\per\metre}     % solo unidad
```
Usar coma como separador decimal siempre. En math mode sin siunitx: `$7{,}95$`.

---

## Bibliografía (`refs.bib`)

Estilo IEEE numérico. Entradas base ya incluidas:
- `serway` — Serway & Jewett, Physics for Scientists and Engineers, 10th ed.
- `halliday` — Halliday, Resnick & Krane, Physics, 5th ed.
- `numpy`, `matplotlib`, `scipy` — referencias de software Python
- `script_graficas` — script del repo (GitHub MiniLux0/Physics-Reports)

Para citar: `\cite{clave}`. Nunca citar sin referencia previa en `refs.bib`.
La bibliografía se imprime con `\printbibliography[heading=none]`.

---

## Python / Gráficas

- Scripts en `labNN/scripts/grap.py`
- Dependencias: `numpy`, `scipy`, `matplotlib`
- Correr desde `scripts/`:
  ```powershell
  cd labNN/scripts
  python grap.py
  ```
- Las figuras se guardan en `scripts/` → mover manualmente a `labNN/Figures/`
- En LaTeX referenciar como `\includegraphics{nombre_figura}` (sin ruta, solo nombre)

---

## Quirks importantes

- `.gitignore` bloquea `*.pdf` y `out/` — el PDF final del lab se llama `Lab04_Vera_Cauti_Marin.pdf` (no `main.pdf`)
- Line endings: `eol=lf` para `.tex`, `.bib`, `.md`, `.cls`, `.sty`
- `\graphicspath{{Figures/}}` es relativo al lab — las figuras van en `labNN/Figures/`
- El logo de portada es `uni_logo` (sin extensión) — debe estar en `Figures/`
- Secciones numeradas hasta nivel 3 con `\setcounter{secnumdepth}{3}`
- `\subsubsection` usa estilo `runin` (inline con punto) — no usar para bloques grandes
- Todas las etiquetas siguen el patrón: `eq:nombre`, `tab:nombre`, `fig:nombre`
- Todas las referencias usan tilde antes: `Tabla~\ref{}`, `Fig.~\ref{}`, `Ec.~\eqref{}`, `Sección~\ref{}`
- Secciones clave llevan `\label{sec:nombre}` para referencias cruzadas entre archivos:
  - `\label{sec:resultados}` en 07, `\label{sec:analisis_exp}` en 08, `\label{sec:conclusiones}` en 12
- `\qtyrange{a}{b}{unidad}` para rangos numéricos con unidades
- `\texorpdfstring{$math$}{texto}` en títulos de subsección que contienen matemáticas
- Guión largo en títulos: `---` (triple guión), no `--` ni `-`
- **Decimales en modo matemático:** Escribir comas crudas en modo matemático (ej. `$2,46$`) genera espaciado incorrecto en LaTeX. Se debe usar siempre comas con llaves (ej. `$2{,}46$`) o macros de siunitx (`\num{2,46}` o `\qty{2,46}{unidad}`).
- **Evitar advertencias de página duplicada (`hyperref`):** Configurar `hypertexnames=false` en las opciones del paquete `hyperref` en `main.tex`. Además, usar `\pagenumbering{roman}` antes del índice (TOC) y `\pagenumbering{arabic}` antes de la primera sección (Resumen/Introducción) para que el PDF asocie los enlaces correctamente.
- **Estandarización de figuras de materiales:** Las figuras de la sección de Materiales y Equipos (Sección 05) deben tener dimensiones uniformes: `width=0.50\linewidth, height=5.5cm` en el comando `\includegraphics`.
- **Ecuaciones y justificación física en Anexos:** Si la ecuación de trabajo introduce constantes geométricas derivadas del montaje (como el factor 2 en rodadura doble), se debe incluir una subsección cinemática/demostrativa en el Anexo A de `sections/13_anexos.tex` para respaldarla formalmente.
- **Consistencia en Celsius:** Usar consistentemente la macro `\qty{T}{\celsius}` (o en su defecto `T\ ^\circ\text{C}`) para evitar el uso de caracteres unicode sueltos de temperatura (`°C`), garantizando portabilidad en la codificación.