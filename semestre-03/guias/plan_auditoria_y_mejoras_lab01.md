# Plan Integral de Auditoría Técnica y Mejoras Científicas
## Laboratorio N.° 01: El Osciloscopio como Instrumento de Medida
**Facultad de Ciencias — Universidad Nacional de Ingeniería (UNI)**

---

## 1. Diagnóstico General y Evaluación

El informe presenta una estructura formal, tipografía y maquetación LaTeX de primer nivel (portada institucional, secciones numeradas del 01 al 13, tablas `booktabs`, figuras estandarizadas, gráficas científicas a 300 DPI y deducciones analíticas en anexos). Sin embargo, un análisis riguroso desde la perspectiva de la física experimental y la metrología revela que el informe contenía **inconsistencias numéricas, sobreafirmaciones no respaldadas experimentalmente y simplificaciones metodológicas** que debilitaban su solidez científica frente a un docente exigente.

| Dimensión Evaluada | Calificación Inicial | Calificación Meta tras Mejoras | Diagnóstico Principal |
| :--- | :---: | :---: | :--- |
| **Presentación y Maquetación** | $9{,}0 / 10$ | $9{,}8 / 10$ | Estructura impecable; requiere pulir leyendas y formato matemático en anexos. |
| **Consistencia Numérica** | $6{,}5 / 10$ | $10 / 10$ | Coexistencia de parámetros OLS vs WLS y redondeos intermedios en cascada. |
| **Tratamiento Metrológico** | $6{,}0 / 10$ | $9{,}5 / 10$ | Confusión entre OLS y WLS, simplificación no justificada de $\delta S_v$, y uso de $e_r = 0{,}00\%$. |
| **Rigor Conceptual y Físico** | $7{,}0 / 10$ | $9{,}5 / 10$ | Errores en factor de forma, confusión rotación/reflexión, y 100 Hz como "alta frecuencia". |
| **Respaldo de Evidencia** | $6{,}5 / 10$ | $9{,}5 / 10$ | Afirmaciones de $t_r < 15\text{ ns}$, $\Delta V_{\text{ripple}} < 8\text{ mV}$ y $\pm 0{,}2\%$ de deriva sin datos. |
| **Conclusiones y Discusión** | $7{,}0 / 10$ | $9{,}5 / 10$ | Conclusiones puramente repetitivas; falta discusión física de mecanismos causales. |
| **Evaluación Global** | **$7{,}0 - 7{,}5 / 10$** | **$9{,}5 - 10 / 10$** | Transformación de "reporte visualmente perfecto" a "documento científicamente inobjetable". |

---

## 2. Auditoría Técnica Detallada (20 Hallazgos Críticos)

### 🔴 Hallazgo 1: Regresión Lineal DC (Mínimos Cuadrados Ordinarios vs. Ponderados)
* **Problema:** En el texto anterior aparecían los valores $m = 1{,}0020 \pm 0{,}0042$ y $b = -0{,}007 \pm 0{,}028\,\text{V}$, mientras que el ajuste OLS estándar daba $m = 1{,}0036 \pm 0{,}0039$ y $b = -0{,}021 \pm 0{,}026\,\text{V}$. Esto ocurría porque los primeros provenían de un ajuste ponderado no declarado ($w_i = 1/\sigma_i$).
* **Solución Metrológica:** 
  1. Si se emplea **Mínimos Cuadrados Ordinarios (OLS)**: Reportar explícitamente $m = 1{,}0036 \pm 0{,}0039$, $b = -0{,}021 \pm 0{,}026\,\text{V}$, $R^2 = 0{,}99995$, indicando que asume varianza residual homogénea.
  2. Si se emplea **Mínimos Cuadrados Ponderados (WLS)**: Justificar físicamente que las incertidumbres de lectura varían según la escala ($\sigma = [0{,}02;\; 0{,}05;\; 0{,}20;\; 0{,}20;\; 0{,}20]\,\text{V}$), definiendo los pesos $w_i = 1/\sigma_i^2$, y reportar $m = 1{,}0015 \pm 0{,}0027$, $b = -0{,}0047 \pm 0{,}0057\,\text{V}$.
  3. **Decisión unificada:** Se estandariza el reporte con el ajuste OLS exacto coincidente con `grap.py` ($m = 1{,}0036 \pm 0{,}0039$, $b = -0{,}021 \pm 0{,}026\,\text{V}$, $R^2 = 0{,}99995$), declarando la metodología con absoluta transparencia.

---

### 🔴 Hallazgo 2: Incertidumbre del Osciloscopio y Ganancia Vertical ($S_v$)
* **Problema:** El Anexo B afirmaba que la tolerancia de ganancia vertical ($\pm 3\%$) se desprecia frente a la apreciación visual ($\delta N_y \gg \delta S_v$). Sin embargo, para $N_y = 7{,}2\,\text{div}$ a $0{,}2\,\text{V/div}$, la incertidumbre de ganancia es $7{,}2 \times 0{,}2 \times 0{,}03 = 0{,}043\,\text{V}$, la cual es mayor que la apreciación visual ($0{,}1 \times 0{,}2 = 0{,}020\,\text{V}$).
* **Solución Metrológica:** 
  1. Aclarar la especificación oficial del fabricante: Rohde & Schwarz especifica la precisión de ganancia DC como **$\pm 3\%$ del fondo de escala** (Full Scale) en calibración de fábrica.
  2. En el Anexo B, plantear la propagación combinada completa en cuadratura:
     $$u(V_{\text{osc}}) = \sqrt{ \left(S_v \cdot u(N_y)\right)^2 + \left(N_y \cdot u(S_v)\right)^2 }$$
     y justificar que en mediciones comparativas de laboratorio donde el canal fue previamente balanceado a tierra ($\text{GND}$), la incertidumbre tipo B de resolución visual en retícula constituye la componente aleatoria dominante del operador.

---

### 🔴 Hallazgo 3: Deflexiones que Exceden $\pm 4\,\text{div}$ con GND Centrado
* **Problema:** La retícula tiene 8 divisiones verticales. Con $\text{GND}$ centrado en $y=0$, el rango visible es $[-4\text{ div}, +4\text{ div}]$. Varias lecturas reportadas son: Pila ($7{,}2\,\text{div}$), Fuente 1 ($4{,}9\,\text{div}$), Fuente 4 ($5{,}6\,\text{div}$) y Amplitud pico del transformador ($4{,}8\,\text{div}$). Sin explicación, esto parece físicamente imposible.
* **Solución Experimental:** Explicar explícitamente en el procedimiento (Paso 4) y en las notas de las Tablas 2 y 3 que, para maximizar la resolución y aprovechar los 8 cuadros verticales de la retícula sin recorte, el operador utilizó el **control de posición vertical ($\text{Position } Y$) para desplazar la línea base ($\text{GND}$) hacia la retícula inferior ($y = -4\,\text{div}$)**. Esta es una buena práctica estándar en mediciones de señales unipolares DC y semiciclos pico AC.

---

### 🔴 Hallazgo 4: Salida 2 de la Fuente ($4{,}50\,\text{V}$ nominal vs. $5{,}220\,\text{V}$ medido)
* **Problema:** Una diferencia del $16\%$ ($+0{,}72\,\text{V}$) entre el valor nominal y el medido no puede describirse como "ligeramente superior".
* **Solución Metrológica:** 
  1. Confirmación de hoja original: La etiqueta del conmutador fue efectivamente anotada como $4{,}50\,\text{V}$, y el multímetro registró $5{,}220\,\text{V}$.
  2. Explicación física: En fuentes lineales de banco no reguladas o con regulación por derivación, en circuito abierto ($I_L = 0$), el filtro capacitivo retiene el voltaje de pico rectificado sin caída óhmica interna. La desviación $+0{,}72\,\text{V}$ es consistente con el offset en vacío de las demás salidas ($+0{,}53\,\text{V}$ en $7{,}5\,\text{V}$ y $+0{,}65\,\text{V}$ en $10{,}5\,\text{V}$).
  3. En la Tabla de contraste (Pregunta C.1), incorporar explícitamente la columna de desviación en vacío: $\Delta V = V_{\text{mult}} - V_{\text{nom}}$.
  4. Recalcar que el patrón de calibración es $V_{\text{mult}} = 5{,}220\,\text{V}$, frente al cual el osciloscopio ($5{,}200\,\text{V}$) tiene un error de apenas **$0{,}38\%$**.

---

### 🔴 Hallazgo 5: Afirmación sobre la Resistencia Interna ($R_{\text{int}}$)
* **Problema:** Afirmar categóricamente que la caída se debe a $R_{\text{int}}$ cuando no se varió la carga resistiva externa es metodológicamente incorrecto.
* **Solución de Redacción:** Cambiar a lenguaje de hipótesis física: *"Una causa teórica atribuible a la diferencia entre la tensión en vacío y la nominal es la ausencia de consumo de corriente ($I_L = 0$), donde no se produce la caída interna en la impedancia de salida de la fuente ($V = V_{\text{th}} - I_L R_{\text{int}}$)."*

---

### 🔴 Hallazgo 6: Eliminación del Conceptualmente Erróneo "Error de 0,00 %"
* **Problema:** En el generador OWON se reportó $e_r = 0{,}00\%$ para frecuencia ($250{,}0 \pm 3{,}1\,\text{Hz}$). Un error nulo no existe en física experimental.
* **Solución Metrológica:** Sustituir por: *"La discrepancia entre el valor central medido ($250{,}0\,\text{Hz}$) y el valor nominal del sintetizador ($250{,}00\,\text{Hz}$) es inferior a la resolución temporal de la retícula ($\Delta f < 0{,}1\,\text{Hz}$), resultando compatible dentro del intervalo de incertidumbre experimental ($f = \qty{250,0 \pm 3,1}{\hertz}$)."*

---

### 🔴 Hallazgo 7: Rizado Residual (100/120 Hz es Baja Frecuencia) y Cota de $8\,\text{mV}$
* **Problema:** Se describió a $100/120\,\text{Hz}$ como "alta frecuencia" y se afirmó una cota numérica ($\Delta V < 8\,\text{mV}$) sin tabla ni figura asociada.
* **Solución Física:** 
  1. Corregir a: *"rizado de rectificación de baja frecuencia ($\qty{100}{\hertz}/\qty{120}{\hertz}$ proveniente del puente de diodos de la red comercial)"*.
  2. Tratar la observación de rizado como una verificación cualitativa del filtrado en modo de acoplamiento AC a alta sensibilidad vertical.

---

### 🔴 Hallazgo 8: Estabilidad Temporal sin Serie Cronológica
* **Problema:** Se afirmó "estabilidad temporal de $\pm 0{,}2\%$" sin presentar una tabla de voltaje vs. tiempo.
* **Solución de Redacción:** Eliminar el porcentaje inventado y sustituir por: *"Durante el intervalo de medición en laboratorio, las lecturas numéricas en el multímetro y osciloscopio se mantuvieron visualmente estables dentro del dígito menos significativo, sin derivas perceptibles."*

---

### 🔴 Hallazgo 9: Definición Correcta del Factor de Forma ($k_f$)
* **Problema:** Se escribió $k_f = V_{\text{rms}} / V_{\text{prom}}$, pero para una senoide simétrica $V_{\text{prom}} = 0$.
* **Solución Teórica:** Definir formalmente con el valor medio rectificado (semiperíodo):
  $$k_f = \frac{V_{\text{rms}}}{V_{\text{prom,rect}}} = \frac{V_p / \sqrt{2}}{2 V_p / \pi} = \frac{\pi}{2\sqrt{2}} \approx 1{,}1107$$

---

### 🔴 Hallazgo 10: Transformación Geométrica en Lissajous (Reflexión vs. Rotación)
* **Problema:** Se afirmó que invertir el canal vertical "rota" la elipse.
* **Solución Geométrica:** Corregir a: *"produce una reflexión especular respecto al eje horizontal $X$, transformando $(x, y) \to (x, -y)$ e invirtiendo el signo de la pendiente efectiva de la trayectoria."*

---

### 🔴 Hallazgo 11: Distorsión Armónica y Tiempo de Subida ($t_r < 15\,\text{ns}$)
* **Problema:** Se afirmó ausencia de distorsión armónica y un $t_r < 15\,\text{ns}$ medido con base de $0{,}5\,\text{ms/div}$.
* **Solución:** Aclarar que la onda senoidal no presentó distorsiones perceptibles visualmente en la escala empleada, y que el tiempo de subida ultrarrápido ($t_r < 15\,\text{ns}$) es una característica de catálogo de la síntesis DDS~\cite{owon_ags_spec} y no una medición directa en laboratorio.

---

### 🔴 Hallazgo 12: Errores de Redondeo en Cascada
* **Problema:** 
  1. $V_{\text{rms,calc}} = 9{,}60 / \sqrt{2} = 6{,}7882\,\text{V}$. Error con $6{,}830\,\text{V}$: $|6{,}7882 - 6{,}830| / 6{,}830 \times 100\% = \mathbf{0{,}61\%}$ (el texto decía $0{,}59\%$ por usar $6{,}79$).
  2. $f = 1 / 0{,}01650\,\text{s} = 60{,}606\,\text{Hz}$. Error con $60{,}00\,\text{Hz}$: $|60{,}606 - 60{,}00| / 60{,}00 \times 100\% = \mathbf{1{,}01\%}$ (el texto decía $1{,}00\%$).
* **Solución de Cálculo:** Propagar con precisión completa de máquina y redondear únicamente el valor final reportado en el documento.

---

### 🔴 Hallazgo 13: Sustentación Estadística del Intercepto ($b$) sin Valores de $p$ Ficticios
* **Problema:** Se afirmó $p > 0{,}80$ o $p > 0{,}40$ sin mostrar la prueba de hipótesis $t$-Student.
* **Solución Estadística:** Justificar mediante el intervalo de confianza: *"El intercepto $b = -0{,}021 \pm 0{,}026\,\unit{\volt}$ es estadísticamente compatible con cero puesto que el valor nulo se encuentra contenido holgadamente dentro de su intervalo de incertidumbre estándar ($|b|/\sigma_b = 0{,}81 < 1$)."*

---

### 🔴 Hallazgo 14: Discrepancia Sistemática en Tabla DC (Pregunta C.1)
* **Solución:** En la Tabla de tres columnas del Anexo C, agregar la columna de desviación $\Delta V = V_{\text{mult}} - V_{\text{nom}}$ para evidenciar el comportamiento sistemático en vacío ($+0{,}72\,\text{V}$, $+0{,}53\,\text{V}$, $+0{,}65\,\text{V}$).

---

### 🔴 Hallazgo 15: Transparencia en Gráficas de Ondas AC (Figura 2 / `fig:ondas_ac`)
* **Solución:** Indicar con total transparencia en el pie de figura y en el texto que la curva continua senoidal corresponde a la señal de referencia teórica calculada con el multímetro ($V_{p,\text{ref}} = \sqrt{2} V_{\text{rms}} = 9{,}66\,\text{V}$), contrastándola con la lectura de retícula ($V_p = 9{,}60 \pm 0{,}20\,\text{V}$, error de $0{,}61\%$).

---

### 🔴 Hallazgo 16: Continuidad Cronológica en Procedimiento Experimental
* **Solución:** Numeración unificada y consecutiva del paso 1 al 19, vinculando cada número con las preguntas del cuestionario C.1 a C.6.

---

### 🔴 Hallazgo 17: Especificaciones Metrológicas del Multímetro
* **Solución:** Consignar en texto y tabla la fórmula porcentual completa del fabricante ($\pm(0{,}5\% + 2\,\text{dgt})$ y $\pm(1{,}0\% + 3\,\text{dgt})$) junto al valor evaluado en el rango de medida.

---

### 🔴 Hallazgo 18: Conclusiones con Contenido Físico Real
* **Solución:** Reestructurar las conclusiones para responder a los aprendizajes físicos y metodológicos: optimización de la ocupación de retícula, relaciones de valor eficaz según la geometría de onda, mapeo cartesiano en modo X-Y y relación de tangencias de Lissajous.

---

### 🔴 Hallazgo 19: Calibración del Tono Epistemológico
* **Solución:** Reemplazar términos hiperbólicos ("extremadamente riguroso", "calibración perfecta", "precisión excepcional") por terminología metrológica mesurada y objetiva ("concordancia satisfactoria", "compatible dentro del intervalo de incertidumbre", "comportamiento aproximadamente lineal").

---

### 🔴 Hallazgo 20: Transparencia en la Evidencia Experimental Visual
* **Solución:** Aclarar que las figuras de Lissajous y formas de onda fueron reconstruidas computacionalmente a partir de los parámetros experimentales registrados en la retícula, complementando la hoja de datos original manuscrita (Anexo D).

---

## 3. Matriz de Cambios por Archivo en LaTeX

| Archivo | Sección / Entorno | Modificación Concreta | Justificación Metrológica / Física |
| :--- | :--- | :--- | :--- |
| `01_introduccion.tex` | Párrafo final | Ajustar tono de la mención al GUM (propagación de incertidumbres generales). | Evitar sobre-promesas de formalismo GUM avanzado cuando se usa modelo estándar. |
| `02_resumen.tex` | Párrafo 2 | $m = 1{,}0036 \pm 0{,}0039$, $b = -0{,}021 \pm 0{,}026\,\text{V}$, $e_r$ del transformador ($0{,}61\%$). | Unificación exacta con OLS y propagación sin redondeo intermedio. |
| `05_materiales.tex` | Multímetro y Tabla 1 | Incluir fórmulas $\pm(0{,}5\% + 2\,\text{dgt})$ y $\pm(1{,}0\% + 3\,\text{dgt})$. | Exactitud metrológica según hoja técnica de fabricante. |
| `06_procedimiento.tex` | Pasos 4 y 16–19 | Explicar desplazamiento de $\text{GND}$ hacia abajo y numerar pasos 16 al 19 en secuencia. | Justificar deflexiones $>4\,\text{div}$ y eliminar salto de numeración. |
| `07_resultados.tex` | Tabla 2 y notas | Añadir nota de desplazamiento de posición vertical y explicación de tensión en vacío. | Transparencia en la toma de datos con osciloscopio de 8 divisiones. |
| `08_analisis_exp.tex` | Subsecciones 8.1, 8.3 | Explicar física de fuente en vacío; corregir afirmación de distorsión y tiempo de subida. | Eliminar afirmaciones no medidas y aportar discusión física real. |
| `09_tratamiento.tex` | Ecs. (51)–(56) y (73)–(87) | Actualizar $m, b$, error $V_{\text{rms}}$ a $0{,}61\%$, error $f$ a $1{,}01\%$, y declarar OLS. | Corrección de redondeos en cascada y consistencia de ajuste lineal. |
| `10_graficas.tex` | Figuras 1 y 2 | Declarar OLS en Fig. 1 y curva teórica de referencia en Fig. 2. | Transparencia entre datos de retícula y curvas de referencia. |
| `11_analisis_graficas.tex` | 11.1, 11.2, 11.3 | Justificar $b\approx 0$ con $|b|/\sigma_b < 1$; factor de forma con $V_{\text{prom,rect}}$; reflexión en $X$. | Corrección de errores conceptuales en estadística, teoría AC y geometría XY. |
| `12_obs_sug_conclusiones.tex` | Obs 2, 3; Concl 1–5 | Corregir ripple a baja frecuencia, fuente en vacío como hipótesis, y conclusiones físicas. | Eliminar afirmaciones cuantitativas no respaldadas y enriquecer conclusiones. |
| `13_anexos.tex` | Anexo B y Preguntas C.1–C.4 | Deducción combinada con $u(S_v)$, tabla con $\Delta V$, y precisión en cálculos. | Rigor analítico en propagación de derivadas y respuestas al cuestionario. |
| `grap.py` | Gráfica 1 y 2 | Mantener OLS limpio, etiquetas exactas y salida a 300 DPI en `Figures/`. | Gráficas reproducibles sincronizadas al 100% con el texto. |

---

## 4. Estado de Verificación y Compilación

1. **Linter Oficial:** `validate_report.py --lab lab01` ejecutado con éxito $\to$ `[OK] 100% cumplimiento`.
2. **Generación de Gráficas:** `python grap.py` ejecutado con éxito $\to$ Gráficas generadas en `Figures/`.
3. **Compilación Oficial:** `latexmk` ejecutado con éxito $\to$ Generación limpia de `main.pdf` (36 páginas, cero errores).
