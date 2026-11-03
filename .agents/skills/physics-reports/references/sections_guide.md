# Guía Estructurada de Secciones (01 a 13)

Esta guía detalla el contenido, estructura, estilo y requisitos de cada una de las 13 secciones de un informe de laboratorio de Física II en la Facultad de Ciencias de la Universidad Nacional de Ingeniería (UNI).

---

## 01 — Introducción (`01_introduccion.tex`)
- **Extensión:** 3 a 5 párrafos.
- **Estructura obligatoria:**
  1. *Fenómeno físico fundamental:* Descripción desde el nivel microscópico/molecular hasta su manifestación macroscópica. Citar literatura base (\cite{serway}, \cite{halliday}).
  2. *Definición de magnitudes principales:* Definir las variables clave con ecuaciones inline y unidades SI (usando `\unit{...}` o `\qty{...}`). Introducir los valores bibliográficos de referencia (ej. $V_{\text{rms}}$, frecuencias patrón).
  3. *Influencia de variables externas o principios de transducción:* Explicar cómo el campo eléctrico, la desviación por placas deflectoras, el calentamiento o las señales AC/DC modifican la magnitud estudiada.
  4. *Descripción del instrumental y métodos:* Explicar el principio de operación del equipo (ej. deflexión electrostática en TRC, muestreo digital DSO, generador DDS, multímetro True-RMS) con sus relaciones analíticas.
  5. *Resultados anticipados y fuentes de error esperadas:* Conectar con las expectativas cuantitativas y anticipar limitaciones experimentales (apreciación visual de retícula, rizado de rectificación, ruido parásito).

---

## 02 — Resumen (`02_resumen.tex`)
- **Extensión:** 2 a 3 párrafos concisos y de alto impacto.
- **Estructura obligatoria:**
  1. *Propósito y sistema experimental:* Qué se investigó, rango de parámetros de operación (ej. voltajes DC de $\qty{1,442}{\volt}$ a $\qty{11,150}{\volt}$, señales AC a $\qty{60}{\hertz}$ y $\qty{250}{\hertz}$).
  2. *Metodología y principio de medición:* Cómo se tradujeron las magnitudes físicas (ej. calibración vertical en modo Y-t, cálculo de valores eficaces $V_{\text{rms}}$, barrido de tiempo y figuras de Lissajous en modo X-Y).
  3. *Resultados cuantitativos y errores:* Lista exhaustiva de resultados con incertidumbre $(\text{valor} \pm \delta x)\ \text{unidad}$, parámetros de ajuste OLS ($m \pm s_m$, $b \pm s_b$, $R^2$), y errores relativos porcentuales $E_r \le 10\%$ (idealmente $< 1\%$).
  4. *Conclusión sintética:* Validación del método, linealidad observada y concordancia con los modelos teóricos.

---

## 03 — Objetivos (`03_objetivos.tex`)
```latex
\section{Objetivos}
\label{sec:objetivos}

\subsection{Objetivo general}
Estudiar y caracterizar experimentalmente el comportamiento de ... mediante ...

\subsection{Objetivos específicos}
\begin{enumerate}
    \item Calibrar y verificar la linealidad de la escala de deflexión vertical ...
    \item Determinar la amplitud pico, tensión eficaz y frecuencia de ondas senoidales, triangulares y cuadradas ...
    \item Sintetizar y analizar figuras de Lissajous en modo X-Y para determinar relaciones de frecuencia enteras ...
    \item Propagar rigurosamente las incertidumbres instrumentales y operativas mediante derivadas parciales en cuadratura.
    \item Comparar los resultados con las referencias bibliográficas y especificaciones de fabricante.
\end{enumerate}
```

---

## 04 — Fundamento Teórico (`04_fundamento.tex`)
- Cada concepto se organiza como una `\subsection{}` independiente.
- Todas las ecuaciones deben estar numeradas con `\begin{equation} \label{eq:...} \end{equation}`.
- Citas con `\cite{...}` y referencias cruzadas con `\eqref{eq:...}`.
- Usar siempre `\texorpdfstring{$math$}{texto}` en los títulos de subsección que contengan expresiones matemáticas.
- **Deducciones completas:** Incluir las integrales de definición (ej. valor eficaz $V_{\text{rms}} = \sqrt{\frac{1}{T}\int_0^T v^2(t)\,dt}$ para ondas senoidales, triangulares y cuadradas). Si el desarrollo matemático es extenso, presentar la ecuación clave y remitir su desarrollo al Anexo A (`\ref{sec:anexo_deducciones}`).
- **Figuras y factores geométricos:** Resaltar factores geométricos relevantes y remitir a diagramas explicativos.
- Separar ecuaciones inline o dobles con `\qquad`.

---

## 05 — Materiales y Equipos (`05_materiales.tex`)
Bloque estandarizado por instrumento:
```latex
\subsection{Nombre del instrumento}
\begin{itemize}
    \item \textbf{Descripción y función:} Texto descriptivo detallando su principio de funcionamiento y rol experimental.
    \item \textbf{Especificaciones del fabricante:}
    \begin{itemize}
        \item Modelo / Marca: R\&S RTC1002 / OWON AG 051F
        \item Ancho de banda / Rango: $\qty{50}{\mega\hertz}$, $\qty{0}{\volt}$ a $\qty{30}{\volt}$
        \item Incertidumbre del catálogo: $\pm (\qty{3}{\percent} + \qty{0,1}{\division})$
    \end{itemize}
    \item \textbf{Incertidumbre operativa / apreciación:} $\delta N = \pm\qty{0,1}{\division}$ en retícula visual.
    \item \textbf{Precauciones:} Calibración de cero en GND, acoplamiento DC/AC, compensación de sonda $1\times/10\times$.
\end{itemize}
\begin{figure}[H]
    \centering
    \includegraphics[width=0.50\linewidth, height=5.5cm]{fig_instrumento}
    \caption{Fotografía o esquema del instrumento utilizado en el laboratorio.}
    \label{fig:mat_instrumento}
\end{figure}
```
*Reglas:*
- Todas las imágenes de materiales deben tener exactamente `width=0.50\linewidth, height=5.5cm`.
- Incluir siempre una tabla metrológica resumen (`tab:especificaciones_equipos`) con todos los instrumentos, sus rangos, resoluciones y fórmulas de tolerancia.

---

## 06 — Procedimiento Experimental (`06_procedimiento.tex`)
- Pasos numerados con `\begin{enumerate}` en riguroso orden cronológico, divididos por partes lógicas (Parte A, B, C...).
- Si se interrumpe la lista con texto o subsecciones, mantener la numeración continua mediante `\setcounter{enumi}{N}`.
- Mencionar los controles del instrumento (escala $S_v$, base de tiempo $S_t$, trigger, modo X-Y, nivel de GND).
- **Registro digital USB:** Cuando no se disponga de cámaras fotográficas físicas en el laboratorio, documentar explícitamente el almacenamiento digital de parámetros y formas de onda en memoria masiva USB (`USB Flash Drive`) y la reconstrucción vectorial a 300 DPI mediante scripts de Python.
- Advertencias de seguridad física y eléctrica claras (límites de tensión, disipación de calor).

---

## 07 — Resultados Experimentales (`07_resultados.tex`)
- Lleva `\label{sec:resultados}` al inicio.
- Breve párrafo introductorio antes de las tablas.
- Tablas construidas exclusivamente con `booktabs` (`\toprule`, `\midrule`, `\bottomrule`), sin `\hline` ni barras verticales `|`.
- **Ajuste de margen obligatorio:** Envolver toda tabla de 4 o más columnas en `\resizebox{\linewidth}{!}{% ... %}`.
- Encabezados claros con unidades SI mediante `\unit{...}` y datos numéricos con `\num{...}` o `\qty{...}`.
- Separar parámetros constantes del sistema en una tabla inicial (`tab:parametros_constantes`) y datos medidos en tablas posteriores.

---

## 08 — Análisis Experimental (`08_analisis_exp.tex`)
- Lleva `\label{sec:analisis_exp}` al inicio.
- **Enfoque estrictamente CUALITATIVO:** Evaluar linealidad, morfología de ondas, simetría de Lissajous, fuentes de ruido y sensibilidad instrumental.
- **Importante:** Indicar explícitamente al inicio que el cálculo cuantitativo y la propagación analítica de errores se realiza en la Sección 09.
- **Epistemología y matización de hipótesis:** Cuando un comportamiento físico no haya sido sometido a un barrido exhaustivo con carga variable o ciclos bidireccionales, formular las interpretaciones como *hipótesis tentativas plausibles* (ej. "el aumento de tensión podría atribuirse al comportamiento de la fuente en vacío $V_{\text{out}} \approx V_{\text{th}}$").
- Cerrar la sección enlazando con el tratamiento numérico formal de la Sección~\ref{sec:tratamiento}.

---

## 09 — Tratamiento de Datos y Resultados (`09_tratamiento.tex`)
- Lleva `\label{sec:tratamiento}` al inicio.
- Presenta la ecuación de trabajo general (`\label{eq:trabajo_calculo}`) y la fórmula de suma en cuadratura (`\label{eq:propagacion_cuadratura}`).
- **Ajuste Lineal por Mínimos Cuadrados (OLS):** Presentar $m$, $b$, sus errores estándar $s_m, s_b$, y el coeficiente $R^2$.
- **Incertidumbre operativa:** Justificar cuándo la incertidumbre de apreciación visual $\delta N = \pm 0{,}1\,\text{div}$ domina la medición ($\delta V = S_v \cdot \delta N$) tras la calibración de cero en modo GND.
- Sustitución numérica paso a paso:
  1. Valores de entrada con sus incertidumbres.
  2. Sustitución en la fórmula base.
  3. Sustitución en la fórmula de propagación mostrando sumandos cuadráticos.
  4. Resultado final con `\begin{equation} y = (valor \pm inc) \times 10^{-N}\ \text{unidad} \label{eq:res_...} \end{equation}`.
  5. Cálculo explícito del error relativo porcentual $E_r = \frac{|y - y_{\text{ref}}|}{y_{\text{ref}}} \times \qty{100}{\percent}$.

---

## 10 — Gráficas (`10_graficas.tex`)
- Lleva `\label{sec:graficas}` al inicio.
- Figuras con entorno `\begin{figure}[H]`, ancho `width=0.85\linewidth`.
- `\caption{}` exhaustivo: describir detalladamente qué representa cada color, marcadores experimentales con barras de error ($\pm \delta y$), línea de ajuste o teórica, citas al script (`\cite{script_graficas}`) y librerías científicas (`\cite{numpy}`, `\cite{matplotlib}`, `\cite{scipy}`).
- Documentar en el texto que los gráficos fueron generados a partir de los datos registrados vía USB en alta resolución (300 DPI).
- **Párrafo de cierre obligatorio:** Incluir un párrafo final de transición que sintetice la representación visual y enlace directamente al análisis cuantitativo de la Sección 11 (`\ref{sec:analisis_graficas}`).

---

## 11 — Análisis de Gráficas (`11_analisis_graficas.tex`)
- Lleva `\label{sec:analisis_graficas}` al inicio.
- Subsecciones con `\texorpdfstring{$math$}{texto}` en los encabezados.
- Evaluación cuantitativa y metrológica:
  - Dispersión y consistencia de las barras de error respecto a la curva teórica.
  - Validación del intercepto OLS: verificar si $b$ es compatible con cero ($|b|/s_b < 1$ o intervalo al 95\% cubre $0$).
  - Validación de la pendiente OLS: verificar si $m$ es estadísticamente compatible con el valor ideal ($m = 1$).
  - Residuos: evaluar si la distribución de residuos $e_i = y_i - \hat{y}_i$ es aleatoria sin sesgo sistemático evidente.
  - Factores de forma en ondas AC ($k_f = \frac{V_{\text{rms}}}{V_{\text{prom,rect}}} \approx 1{,}11$ para senoides con media rectificada).
  - Figuras de Lissajous: verificación de relaciones de frecuencia por número de tangencias y simetría de inversión de canal.

---

## 12 — Observaciones, Sugerencias y Conclusiones (`12_obs_sug_conclusiones.tex`)
Contiene tres secciones numeradas independientes en el mismo archivo:
1. `\section{Observaciones}`: Análisis de causas físicas y metrológicas de incertidumbre (apreciación visual de $\pm 0{,}1\,\text{div}$, rizado de rectificación, ruido térmico, hipótesis de funcionamiento en vacío, adquisición digital por USB).
2. `\section{Sugerencias}`: Recomendaciones técnicas viables para mitigar cada observación (empleo de cursores digitales automáticos, optimización de base de tiempo para abarcar 2–3 ciclos, acoplamiento de impedancias $50\,\Omega$ vs High-Z, promediado de señal *Averaging*).
3. `\section{Conclusiones}` (`\label{sec:conclusiones}`):
   - Responder punto por punto y en orden a todos los objetivos planteados.
   - Listar todos los resultados cuantitativos con sus incertidumbres y errores relativos.
   - Conclusiones con contenido físico real, validando las leyes físicas y el comportamiento del instrumental.

---

## 13 — Anexos (`13_anexos.tex`)
Encapsulado en `\begin{appendices} ... \end{appendices}`:
- **Anexo A:** Deducciones matemáticas formales (e.g. valores eficaces True-RMS para ondas senoidales, triangulares y cuadradas con límites integrales correctos, ecuación paramétrica y cartesiana de elipses de Lissajous).
- **Anexo B:** Deducción analítica completa de la propagación de errores mediante derivadas parciales y suma en cuadratura, distinguiendo la incertidumbre instrumental combinada de la operativa, y concluyendo con los resultados finales enmarcados en `\boxed{...}`.
- **Anexo C:** Cuestionario oficial de la guía de laboratorio completamente resuelto con respuestas detalladas y tablas comparativas.
- **Anexo D (o final de C):** Hoja de recolección de datos original escaneada (`fig_hoja_datos`).
