# Guía de Estilo y Convenciones LaTeX

Reglas y buenas prácticas para la redacción de informes de laboratorio en LaTeX en este repositorio (Física UNI Facultad de Ciencias).

---

## 1. Unidades SI y Números (`siunitx` v3)

El preámbulo está configurado con:
```latex
\usepackage{siunitx}
\sisetup{
    output-decimal-marker = {,},
    separate-uncertainty  = true,
    per-mode              = symbol,
}
```

### 1.1. Declaración de Unidades Personalizadas Obligatorias:
En `main.tex` y en la plantilla base se deben declarar las siguientes unidades especializadas para instrumentación y laboratorio:
```latex
\DeclareSIUnit{\sample}{Sa}           % Muestras (GSa/s, MSa/s)
\DeclareSIUnit{\division}{div}        % Divisiones de retícula (V/div, s/div)
\DeclareSIUnit{\ppm}{ppm}             % Partes por millón
\DeclareSIUnit{\inch}{in}             % Pulgadas
\DeclareSIUnit{\voltpp}{V_{pp}}       % Tensión pico a pico
\DeclareSIUnit{\voltrms}{V_{rms}}     % Tensión eficaz True-RMS
\DeclareSIUnit{\millivoltpp}{mV_{pp}} % Milivoltios pico a pico
```

### 1.2. Reglas de uso y sintaxis estricta:
- **Separador decimal:** Usar siempre coma decimal `,` (`output-decimal-marker = {,}`).
- **Valores con unidad:** Preferir `\qty{valor}{unidad}` o `\qty{valor \pm incert}{unidad}`.
  - Correcto: `\qty{26,0 \pm 0,5}{\celsius}`, `\qty{0,600}{\milli\meter}`, `\qty{6,8}{\percent}`, `\qty{20}{\voltpp}`, `\qty{2}{\giga\sample\per\second}`.
- **Subíndices en unidades:** NUNCA escribir `\qty{20}{\volt}_{\text{pp}}` en modo texto (produce error de compilación `Missing $ inserted`). Usar siempre la unidad declarada `\qty{20}{\voltpp}` o `\qty{20}{\voltrms}`.
- **Valores puros / Incertidumbres:** Usar `\num{1,5184 \pm 0,0087}`.
- **Solo unidades:** `\unit{\per\kelvin}` o `\si{\milli\newton\per\meter}`.
- **Rangos (`\qtyrange`):** Solo acepta una unidad común `{val1}{val2}{unidad}`.
  - Correcto: `\qtyrange{2,5}{10,5}{\volt}` o `\qtyrange{12,0}{129,0}{\degree}`.
  - **Diferentes prefijos o unidades:** Si los extremos tienen distintos prefijos (ej. $1\,\text{mV/div}$ a $10\,\text{V/div}$ o $1\,\mu\text{Hz}$ a $5\,\text{MHz}$), NO usar `\qtyrange`; escribir explícitamente:
    `$\qty{1}{\milli\volt\per\division}\text{ a }\qty{10}{\volt\per\division}$` o `$\qty{1}{\micro\hertz}\text{ a }\qty{5}{\mega\hertz}$`.
- **Modo matemático manual:** Si se escribe un decimal sin siunitx en modo matemático, se DEBE encerrar la coma en llaves: `$2{,}46$` (nunca `$2,46$`, ya que LaTeX interpretará la coma como un separador de lista y dejará un espacio indeseado).
- **Símbolos de grados:** Prohibido el uso de caracteres unicode sueltos (`°` o `℃`). Usar `\qty{25,0}{\celsius}`, `\unit{\degree}` o `^{\circ}\text{C}`.

---

## 2. Ecuaciones y Modo Matemático

### 2.1. Delimitadores de Display Math
- Usar siempre `\begin{equation} ... \end{equation}` para ecuaciones numeradas con `\label{eq:...}`.
- Usar `\[ ... \]` o `\begin{equation*} ... \end{equation*}` para ecuaciones en bloque sin numerar.
- **Prohibido:** El uso de las primitivas de TeX `$$ ... $$` está estrictamente desaconsejado en LaTeX moderno.

### 2.2. Puntuación en Ecuaciones
- Las ecuaciones forman parte gramatical de las oraciones. Deben finalizar con coma `,` o punto `.` según corresponda al flujo del párrafo:
  ```latex
  \begin{equation}
      V_{\text{rms}} = \frac{V_p}{\sqrt{2}},
      \label{eq:vrms_seno}
  \end{equation}
  donde $V_p$ representa la tensión de cresta.
  ```

---

## 3. Tablas Científicas (`booktabs` + `graphicx`)

### Reglas obligatorias:
1. **Nunca usar `\hline` ni líneas verticales `|`:** Utilizar exclusivamente las reglas de `booktabs`: `\toprule`, `\midrule` y `\bottomrule`.
2. **`\caption{}` siempre encima de la tabla:** El caption va dentro del entorno `table`, antes de `\begin{tabular}`.
3. **Etiquetas (`\label`):** Inmediatamente después del `\caption{}` con prefijo `tab:`.
4. **Ajuste de ancho obligatorio (`\resizebox`):**
   Toda tabla de 4 o más columnas o con datos extensos debe estar obligatoriamente envuelta en `\resizebox{\linewidth}{!}{% ... %}` para prevenir desbordamientos de márgenes (`Overfull \hbox`):
   ```latex
   \begin{table}[H]
       \centering
       \caption{Título descriptivo de la tabla.}
       \label{tab:nombre_tabla}
       \resizebox{\linewidth}{!}{%
       \begin{tabular}{@{}llll@{}}
           \toprule
           \textbf{Columna 1} & \textbf{Columna 2} & \textbf{Columna 3} & \textbf{Columna 4} \\
           \midrule
           Dato 1 & Dato 2 & Dato 3 & Dato 4 \\
           \bottomrule
       \end{tabular}%
       }
   \end{table}
   ```

---

## 4. Figuras e Imágenes (`graphicx` y `float`)

- **Ruta de figuras:** Las imágenes se ubican en `labNN/Figures/`.
- **Inclusión en LaTeX:** No incluir ruta ni extensión: `\includegraphics[...]{fig_nombre}`.
- **Figuras de Materiales (Sección 05):** Estandarizadas con `\includegraphics[width=0.50\linewidth, height=5.5cm]{fig_nombre}`.
- **Gráficas principales (Sección 10):** `width=0.85\linewidth`.
- **Posicionamiento:** Usar siempre el especificador `[H]` provisto por el paquete `float`.

---

## 5. Estilo de Secciones, Títulos e Hipervínculos (`titlesec` y `hyperref`)

- **Separador de sección:** Las secciones principales inician en página nueva (`\newcommand{\sectionbreak}{\clearpage}`).
- **Matemáticas en encabezados:** Usar siempre `\texorpdfstring{$math$}{texto}` en títulos de sección o subsección para evitar advertencias de marcadores PDF:
  ```latex
  \subsection{Comparativa del coeficiente \texorpdfstring{$\alpha$}{alpha} experimental}
  ```
- **Guiones en títulos:** Usar triple guión `---` (em-dash) con espacios:
  ```latex
  \subsection{Aluminio --- Tabla~\ref{tab:datos_dilatacion}}
  ```
- **Paginación:** Configurar `hypertexnames = false` en `hyperref`, usar `\pagenumbering{roman}` antes del índice y `\pagenumbering{arabic}` al iniciar el cuerpo del informe.

---

## 6. Prohibición de Sintaxis Markdown en Archivos LaTeX

- **Negrita:** Usar `\textbf{texto}` (NUNCA `**texto**`).
- **Cursiva:** Usar `\textit{texto}` (NUNCA `*texto*`).
- **Títulos:** Usar `\section{...}`, `\subsection{...}` (NUNCA `#`, `##`).
- **Listas:** Usar `\begin{enumerate} ... \end{enumerate}` o `\begin{itemize} ... \end{itemize}` (NUNCA `- item` ni `1. item` en texto plano).

---

## 7. Bibliografía (`biblatex` + `biber`)

- **Estilo:** Numérico secuencial (`style=numeric, sorting=none`).
- **Archivo:** `refs.bib` en la raíz de cada carpeta de lab.
- **Inclusión:** `\addbibresource{refs.bib}` en el preámbulo y `\printbibliography[heading=none]` dentro de la sección Bibliografía.
- **Citas en texto:** Siempre con `\cite{clave}` vinculada a una entrada existente en `refs.bib`.
