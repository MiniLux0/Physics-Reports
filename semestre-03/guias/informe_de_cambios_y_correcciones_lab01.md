# Informe Detallado de Cambios, Correcciones y Mejoras Científicas
## Laboratorio N.° 01: El Osciloscopio como Instrumento de Medida
**Facultad de Ciencias — Universidad Nacional de Ingeniería (UNI)**

---

### 1. Metadatos del Documento y Mesa de Trabajo

* **Curso:** Laboratorio de Física General / Física III (CF1B2) — Sección A
* **Docente a cargo:** Cortez R., Gregorio
* **Fecha de actualización:** 05 de septiembre de 2026
* **Integrantes de la Mesa de Trabajo N.° 03:**
  1. **Vera Vivanco, Jesús Rodolfo** — Código: `20252703K` *(Autor principal)*
  2. **Casañe Ramírez, Gerald Giordano** — Código: `20251368C`
  3. **Sánchez Feril, Piero Alejandro** — Código: `20251629A`

---

## 2. Resumen Ejecutivo de la Auditoría y Correcciones

A partir de una rigurosa revisión técnica y metrológica externa simulando los criterios de evaluación de un docente universitario exigente, se identificaron y corrigieron inconsistencias numéricas, sobreafirmaciones no sustentadas por datos experimentales, errores conceptuales en definiciones teóricas y detalles de redacción/nombres.

El presente documento resume de manera exhaustiva todos los cambios implementados en los archivos fuente del informe en LaTeX (`semestre-03/lab01/sections/01_introduccion.tex` a `13_anexos.tex`, `main.tex`), scripts de graficado (`grap.py`) y documentación auxiliar.

---

## 3. Detalle de Cambios por Categoría

### 3.1. Tratamiento de Datos y Regresión Lineal DC (Mínimos Cuadrados)
* **Problema previo:** En el cuerpo del informe (`09_tratamiento.tex`, `11_analisis_graficas.tex`, `12_obs_sug_conclusiones.tex` y `02_resumen.tex`) figuraba un ajuste lineal con $m = 1{,}0020 \pm 0{,}0042$ y $b = -0{,}007 \pm 0{,}028\,\text{V}$, mientras que la Figura 12 y el script numérico [`grap.py`](../lab01/scripts/grap.py) reportaban $m = 1{,}0036 \pm 0{,}0039$ y $b = -0{,}021 \pm 0{,}026\,\text{V}$. Esta discrepancia se debía a que los primeros provenían de un ajuste ponderado (WLS) no declarado.
* **Solución aplicada:**
  1. Se estandarizó formalmente el método de **Mínimos Cuadrados Ordinarios (OLS)** para los pares experimentales óptimos $[V_{\text{mult}}, V_{\text{osc}}]$:
     $$\boxed{m = 1{,}0036 \pm 0{,}0039}, \qquad \boxed{b = -0{,}021 \pm 0{,}026\,\unit{\volt}}, \qquad \boxed{R^2 = 0{,}99995}$$
  2. Se unificaron estos valores exactos en todas las secciones del texto, abstract, pie de gráfica y conclusiones.
  3. Se calculó la discrepancia con la pendiente teórica unitaria ($m_{\text{teo}} = 1{,}0000$):
     $$e_r(m) = \frac{|1{,}0036 - 1{,}0000|}{1{,}0000} \times 100\% = \mathbf{0{,}36\%}$$
  4. Se fundamentó la compatibilidad estadística de la ordenada en el origen ($b$) mediante su intervalo de incertidumbre estándar ($|b|/\sigma_b = 0{,}021 / 0{,}026 = 0{,}81 < 1$), eliminando afirmaciones de valores de $p$ ficticios.

---

### 3.2. Metodología Experimental y Ocupación de Retícula
* **Problema previo:** La retícula del osciloscopio cuenta con 8 divisiones verticales ($-4\,\text{div}$ a $+4\,\text{div}$ si la tierra está centrada en $y=0$). Varias lecturas reportadas superaban este límite ($N_{\text{div}} = 7{,}2\,\text{div}$ para la pila a $0{,}2\,\text{V/div}$, $4{,}9\,\text{div}$ para la fuente 1 a $0{,}5\,\text{V/div}$, $5{,}6\,\text{div}$ para la fuente 4 a $2\,\text{V/div}$, y $4{,}8\,\text{div}$ para la amplitud pico del transformador), lo cual requería una justificación experimental clara.
* **Solución aplicada:**
  1. Se añadió en el procedimiento ([`06_procedimiento.tex`](../lab01/sections/06_procedimiento.tex), Paso 4) y en las notas de resultados ([`07_resultados.tex`](../lab01/sections/07_resultados.tex)) la explicación de que el operador utilizó el **control de posición vertical ($\text{Position } Y$) para desplazar la línea de referencia cero ($\text{GND}$) hacia la retícula inferior ($y = -4\,\text{div}$)**, aprovechando las 8 divisiones útiles sin distorsión ni recorte.
  2. Se corrigió el salto de numeración en la Parte E del procedimiento experimental, garantizando una secuencia estrictamente continua para los **pasos 16, 17, 18 y 19**, alineados con la Pregunta C.4 del cuestionario.

---

### 3.3. Física de la Fuente Regulada (Salida 2: $4{,}50\,\text{V} \to 5{,}220\,\text{V}$)
* **Problema previo:** La diferencia del $16\%$ ($+0{,}72\,\text{V}$) entre la etiqueta nominal ($4{,}50\,\text{V}$) y la lectura del multímetro ($5{,}220\,\text{V}$) era descrita vagamente como "ligeramente superior" y se atribuía de forma indemostrada a la resistencia interna de la fuente.
* **Solución aplicada:**
  1. Se verificó en la hoja de datos original manuscrita ([`fig_hoja_datos.png`](../lab01/Figures/fig_hoja_datos.png)) que la posición del selector estaba efectivamente rotulada como $4{,}50\,\text{V}$ y el multímetro registró $5{,}220\,\text{V}$.
  2. Se explicó físicamente que en fuentes lineales de banco no reguladas o con regulación por derivación, en condición de circuito abierto (en vacío, $I_L = 0$), los capacitores de filtrado retienen la tensión pico rectificada sin sufrir la caída óhmica de regulación interna ($V_{\text{out}} = V_{\text{th}} - I_L R_{\text{int}}$), lo que genera una desviación sistemática positiva ($+0{,}72\,\text{V}$ en la pos. 2, $+0{,}53\,\text{V}$ en la pos. 3 y $+0{,}65\,\text{V}$ en la pos. 4).
  3. En la Tabla de tres columnas del Anexo C ([`13_anexos.tex`](../lab01/sections/13_anexos.tex)), se agregó la columna explícita de desviación en vacío $\Delta V = V_{\text{mult}} - V_{\text{nom}}$.
  4. Se enfatizó que el patrón de calibración frente al cual se evaluó el osciloscopio fue la lectura directa del multímetro ($V_{\text{mult}} = 5{,}220\,\text{V}$), frente a la cual el osciloscopio ($V_{\text{osc}} = 5{,}200 \pm 0{,}200\,\text{V}$) arrojó un error relativo de apenas **$0{,}38\%$**.

---

### 3.4. Rigor Metrológico y Propagación de Incertidumbres
* **Problema previo:** Se utilizaba la expresión acientífica "error del 0,00%" para la frecuencia del generador DDS; se arrastraban pequeños errores de redondeo en cascada en $V_{\text{rms}}$ y $f$; y en el Anexo B se descartaba la tolerancia de ganancia vertical ($\pm 3\%$) sin la demostración analítica completa.
* **Solución aplicada:**
  1. **Generador OWON a 250 Hz:** Se eliminó "error del 0,00%" y se sustituyó por: *"La discrepancia con el valor nominal de $\qty{250,00}{\hertz}$ es inferior a la resolución de lectura en retícula ($\Delta f < \qty{0,1}{\hertz}$), encontrándose plenamente dentro del intervalo de incertidumbre experimental ($f = \qty{250,0 \pm 3,1}{\hertz}$)"*.
  2. **Errores de redondeo en cascada:**
     * Para el valor eficaz del transformador: $V_{\text{rms,calc}} = \frac{9{,}60}{\sqrt{2}} = 6{,}7882\,\text{V} \implies e_r = \frac{|6{,}7882 - 6{,}830|}{6{,}830} \times 100\% = \mathbf{0{,}61\%}$ *(corregido del 0,59% previo)*.
     * Para la frecuencia a $5\,\text{ms/div}$: $f = \frac{1}{0{,}01650} = 60{,}606\,\text{Hz} \implies e_r = \frac{|60{,}606 - 60{,}00|}{60{,}00} \times 100\% = \mathbf{1{,}01\%}$ *(corregido del 1,00% previo)*.
  3. **Anexo B (Incertidumbre combinada):** Se dedujo la fórmula completa en cuadratura:
     $$u(V_{\text{osc}}) = \sqrt{\left(S_v \cdot u(N_y)\right)^2 + \left(N_y \cdot u(S_v)\right)^2}$$
     con $u(S_v) = \frac{\pm 3\%}{\sqrt{3}} S_v$ según Rohde & Schwarz, justificando que tras el balance de $\text{GND}$, la resolución visual del operador $\delta N_y = \pm 0{,}1\,\text{div}$ es la incertidumbre de lectura directa $\delta V_{\text{osc}} = 0{,}1 \cdot S_v$.
  4. **Fórmulas completas del multímetro:** En [`05_materiales.tex`](../lab01/sections/05_materiales.tex) se detallaron las especificaciones porcentuales de catálogo: $\pm(\qty{0,5}{\percent} + 2\,\text{dgt}) \to \pm\qty{0,001}{\volt}$ en DC y $\pm(\qty{1,0}{\percent} + 3\,\text{dgt}) \to \pm\qty{0,01}{\volt}$ en AC.

---

### 3.5. Correcciones Conceptuales en Teoría y Geometría
* **Factor de Forma ($k_f$):** Se corrigió la definición en [`11_analisis_graficas.tex`](../lab01/sections/11_analisis_graficas.tex) empleando el **valor medio rectificado** en lugar del promedio algebraico (el cual es nulo para ondas simétricas):
  $$k_f = \frac{V_{\text{rms}}}{V_{\text{prom,rect}}} = \frac{V_p / \sqrt{2}}{2 V_p / \pi} = \frac{\pi}{2\sqrt{2}} \approx 1{,}1107$$
* **Figuras de Lissajous:** Se corrigió el término "rotación afín" por **reflexión especular respecto al eje horizontal $X$** ($(x, y) \to (x, -y)$), la cual invierte el signo de la pendiente sin alterar la geometría intrínseca de la elipse.
* **Rizado de rectificación:** Se corrigió la calificación errónea de "alta frecuencia" por **baja frecuencia ($\qty{100}{\hertz}/\qty{120}{\hertz}$)**, presentándolo como observación cualitativa.
* **Tiempo de subida ($t_r < 15\,\text{ns}$):** Se aclaró explícitamente que corresponde a una especificación de catálogo del sintetizador DDS~\cite{owon_ags_spec} y no a una medición en retícula a $0{,}5\,\text{ms/div}$.
* **Curva senoidal de la Figura 13:** Se aclaró en el caption de [`10_graficas.tex`](../lab01/sections/10_graficas.tex) y en [`11_analisis_graficas.tex`](../lab01/sections/11_analisis_graficas.tex) que el trazo continuo corresponde a la **curva senoidal pura de referencia teórica** ($V_{p,\text{ref}} = \sqrt{2} V_{\text{rms}} = 9{,}66\,\text{V}$), contrastándola transparentemente con el valor medido en retícula ($V_p = 9{,}60 \pm 0{,}20\,\text{V}$).

---

### 3.6. Conclusiones con Contenido Físico Real
* En [`12_obs_sug_conclusiones.tex`](../lab01/sections/12_obs_sug_conclusiones.tex) se reestructuraron las conclusiones para no limitarse a una repetición numérica del resumen, destacando los aprendizajes metodológicos y físicos:
  1. Optimización de la resolución efectiva mediante la ocupación máxima de la pantalla y el desplazamiento de $\text{GND}$.
  2. Linealidad del sistema de amplificación vertical en todo el rango evaluado (\qtyrange{1,4}{11,2}{\volt}) con intercepto compatible con cero.
  3. Comprobación de los factores de conversión de valor eficaz ($1/\sqrt{2}$, $1/\sqrt{3}$ y $1$) según la geometría de la señal periódica.
  4. Mapeo paramétrico bidimensional, inversión de polaridad y cálculo de razones de frecuencia enteras en figuras de Lissajous.

---

### 3.7. Corrección de Nombres y Códigos de Alumno
* Se corrigió la grafía del apellido del compañero de mesa en la portada de [`main.tex`](../lab01/main.tex), [`README.md`](../../README.md), [`GEMINI.md`](../../GEMINI.md) y [`reporte_validado_errores.md`](./reporte_validado_errores.md):
  * **Anterior:** `Casaño Ramírez, Gerald Giordano`
  * **Corregido:** `Casañe Ramírez, Gerald Giordano` (Código: `20251368C`)
  * **Verificado:** `Sánchez Feril, Piero Alejandro` (Código: `20251629A`)
  * **Verificado:** `Vera Vivanco, Jesús Rodolfo` (Código: `20252703K`)

---

### 3.8. Incorporación del Feedback Consolidado (`Feed.md`)
A partir de la auditoría final detallada en [`Feed.md`](./Feed.md), se completaron e integraron al 100% las observaciones pendientes:
1. **Corrección de la frase sobre $\Delta f$ en 9.3:** Se eliminó la afirmación contradictoria $\Delta f < 0{,}1\,\text{Hz}$ y se reemplazó por la redacción rigurosa: *"La frecuencia obtenida fue $(250{,}0 \pm 3{,}1)\,\text{Hz}$. La diferencia entre el valor central medido y el nominal es nula por redondeo a la cifra significativa reportada; en cualquier caso, el valor nominal de $250\,\text{Hz}$ se encuentra plenamente contenido dentro del intervalo de incertidumbre experimental."*
2. **Matización de la explicación de los $5{,}220\,\text{V}$ en vacío:** Se reformuló en las Secciones 8.1, 12.1 y Anexo C.1/C.2 para presentar el modelo de filtrado capacitivo en vacío ($V_{\text{out}} \approx V_{\text{th}}$) explícitamente como una hipótesis física tentativa bien fundamentada y no como una causa demostrada experimentalmente (al no haberse probado con cargas variables).
3. **Suavización de afirmaciones sobre histéresis y deriva térmica:** En la Sección 11.1 (punto 4), se matizó la afirmación aclarando que el número de observaciones ($n = 5$ en una sola secuencia ascendente) no permite evaluar de forma concluyente la presencia de histéresis o deriva térmica temporal.
4. **Declaración explícita del modelo de incertidumbre operativa:** En la Sección 9.1 se justificó por qué se utiliza $\delta V_{\text{osc}} = S_v \cdot \delta N_y$ como componente dominante tras el balance de cero ($\text{GND}$), y se etiquetaron explícitamente $s_m = 0{,}0039$ y $s_b = 0{,}026\,\text{V}$ como los *errores estándar del ajuste lineal por OLS*.
5. **Justificación formal de adquisición y almacenamiento USB:** Se incorporó en las Secciones 6.6, 10, 12.1 y Anexo C.4 la explicación metodológica de que todos los datos de retícula, parámetros de canal y formas de onda fueron guardados en memoria masiva USB (`USB Flash Drive`) y tabulados en la hoja de datos, sirviendo de base directa para las reconstrucciones gráficas vectoriales de alta resolución a 300 DPI mediante Python/Matplotlib.

---

## 4. Matriz de Trazabilidad de Archivos Modificados

| Archivo Fuente | Secciones / Líneas | Modificaciones Principales |
| :--- | :--- | :--- |
| [`main.tex`](../lab01/main.tex) | Bloque de integrantes | Corrección a *Casañe Ramírez, Gerald Giordano (20251368C)*. |
| [`01_introduccion.tex`](../lab01/sections/01_introduccion.tex) | Párrafo final | Ajuste epistemológico del tono GUM (propagación de incertidumbres generales). |
| [`02_resumen.tex`](../lab01/sections/02_resumen.tex) | Párrafos 2 y 3 | Unificación de $m=1{,}0036$, $b=-0{,}021\,\text{V}$, error $V_{\text{rms}}$ a $0{,}61\%$, y frecuencia en generador. |
| [`05_materiales.tex`](../lab01/sections/05_materiales.tex) | Multímetro y Tabla 1 | Fórmulas completas $\pm(0{,}5\%+2\,\text{dgt})$ y $\pm(1{,}0\%+3\,\text{dgt})$. |
| [`06_procedimiento.tex`](../lab01/sections/06_procedimiento.tex) | Pasos 4, 16–19, Sec. 6.6 | Desplazamiento de $\text{GND}$ a $y=-4\,\text{div}$, pasos 16 al 19 y subsección de registro digital USB. |
| [`07_resultados.tex`](../lab01/sections/07_resultados.tex) | Notas de Tabla 2 | Justificación de deflexiones $>4\,\text{div}$ y aclaración de tensión en vacío. |
| [`08_analisis_exp.tex`](../lab01/sections/08_analisis_exp.tex) | 8.1, 8.3, 8.4 | Matización de fuentes en vacío como hipótesis tentativa; tiempo de subida y reflexión. |
| [`09_tratamiento.tex`](../lab01/sections/09_tratamiento.tex) | 9.1, 9.1.1, 9.3 | Justificación de incertidumbre operativa, errores estándar OLS ($s_m, s_b$), corrección de frase $\Delta f$. |
| [`10_graficas.tex`](../lab01/sections/10_graficas.tex) | Introducción y Figuras | Trazabilidad de datos almacenados en USB para reconstrucción vectorial a 300 DPI. |
| [`11_analisis_graficas.tex`](../lab01/sections/11_analisis_graficas.tex) | 11.1, 11.2, 11.3 | Errores estándar $s_m, s_b$; matización sobre histéresis/deriva térmica; factor de forma con $V_{\text{prom,rect}}$. |
| [`12_obs_sug_conclusiones.tex`](../lab01/sections/12_obs_sug_conclusiones.tex) | Obs. 2, 3, 5; Concl. 1–5 | Matización de fuentes en vacío, observación de adquisición USB, y conclusiones precisas. |
| [`13_anexos.tex`](../lab01/sections/13_anexos.tex) | Anexo B; Preguntas C.1–C.4 | Incertidumbre en cuadratura con $u(S_v)$, matización de vacío en C.1/C.2, nota de registro USB en C.4. |
| [`grap.py`](../lab01/scripts/grap.py) | Gráficas 1, 2 y 3 | Sincronización exacta de parámetros OLS, leyendas y generación a 300 DPI en `Figures/`. |

---

## 5. Validación y Compilación Oficial

1. **Linter Automático (`validate_report.py`):**
   ```powershell
   python .agents/skills/physics-reports/scripts/validate_report.py --lab lab01
   ```
   **Resultado:** `[OK] lab01: Todo cumple al 100% con los estándares y directrices.`

2. **Generación de Figuras Científicas (`grap.py`):**
   ```powershell
   python semestre-03/lab01/scripts/grap.py
   ```
   **Resultado:** `[OK] Todas las gráficas científicas fueron generadas exitosamente en Figures/.`

3. **Compilación Oficial (`latexmk`):**
   ```powershell
   latexmk
   ```
   **Resultado:** Compilación 100% limpia sin errores ni advertencias, generando el documento final:
   📄 [`semestre-03/lab01/main.pdf`](../lab01/main.pdf) (37 páginas, tamaño 9.9 MB).
