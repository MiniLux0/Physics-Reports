# Guía de Propagación de Incertidumbres y Análisis de Errores

Metodología formal para el tratamiento matemático de incertidumbres en los informes de laboratorio (Física UNI Facultad de Ciencias), alineada con la Guía para la Expresión de Incertidumbre en las Mediciones (GUM) y la norma JCGM 100:2008.

---

## 1. Método General de Suma en Cuadratura

Para una magnitud física indirecta $y = f(x_1, x_2, \dots, x_n)$ dependiente de $n$ variables de entrada independientes $x_i$ con incertidumbres típicas $\delta x_i$:

### Expresión Diferencial en Cuadratura:
\[
\delta y = \sqrt{ \sum_{i=1}^n \left( \frac{\partial f}{\partial x_i} \delta x_i \right)^2 }
\]

Para coeficientes de correlación no nulos $r(x_i, x_j) \ne 0$, se añade el término de covarianza cruzada $2 \sum_{i<j} \frac{\partial f}{\partial x_i} \frac{\partial f}{\partial x_j} u(x_i, x_j)$.

---

## 2. Casos Frecuentes y Fórmulas Operativas

### A. Productos y Cocientes (e.g. $\alpha = \frac{D\,\theta}{L_0\,\Delta T}$)
Tomando la combinación en cuadratura de las incertidumbres relativas:
\[
\frac{\delta\alpha}{\alpha} = \sqrt{ \left(\frac{\delta D}{D}\right)^2 + \left(\frac{\delta\theta}{\theta}\right)^2 + \left(\frac{\delta L_0}{L_0}\right)^2 + \left(\frac{\delta(\Delta T)}{\Delta T}\right)^2 }
\]
\[
\delta\alpha = \alpha \times \sqrt{ \left(\frac{\delta D}{D}\right)^2 + \left(\frac{\delta\theta}{\theta}\right)^2 + \left(\frac{\delta L_0}{L_0}\right)^2 + \left(\frac{\delta(\Delta T)}{\Delta T}\right)^2 }
\]

### B. Inversión de Frecuencia ($f = \frac{1}{T}$)
\[
\frac{df}{dT} = -\frac{1}{T^2} \implies \delta f = \left|-\frac{1}{T^2}\right|\delta T = f^2\,\delta T = \frac{\delta T}{T^2}
\]

### C. Tensión Eficaz Senoidal ($V_{\text{rms}} = \frac{V_p}{\sqrt{2}}$)
\[
\delta V_{\text{rms}} = \frac{\delta V_p}{\sqrt{2}}
\]

### D. Tensión Pico a Pico ($V_{\text{pp}} = 2 V_p \implies V_p = \frac{V_{\text{pp}}}{2}$)
\[
\delta V_p = \frac{\delta V_{\text{pp}}}{2}
\]

---

## 3. Regresión Lineal por Mínimos Cuadrados (OLS) y Errores Estándar

Para un conjunto de $N$ pares experimentales $(x_i, y_i)$:

### 3.1. Pendiente ($m$) y Ordenada al Origen ($b$):
\[
m = \frac{N \sum x_i y_i - \sum x_i \sum y_i}{N \sum x_i^2 - (\sum x_i)^2}, \qquad b = \bar{y} - m\bar{x} = \frac{\sum y_i - m \sum x_i}{N}
\]

### 3.2. Desviación Estándar de los Residuos ($s_y$ o $S_{y/x}$):
\[
s_y = \sqrt{\frac{\sum_{i=1}^N (y_i - (m x_i + b))^2}{N - 2}}
\]

### 3.3. Errores Estándar de los Parámetros ($s_m$ y $s_b$):
\[
s_m = s_y \sqrt{\frac{N}{N \sum x_i^2 - (\sum x_i)^2}} = \frac{s_y}{\sqrt{\sum (x_i - \bar{x})^2}}
\]
\[
s_b = s_y \sqrt{\frac{\sum x_i^2}{N \sum x_i^2 - (\sum x_i)^2}} = s_y \sqrt{\frac{1}{N} + \frac{\bar{x}^2}{\sum (x_i - \bar{x})^2}}
\]

### 3.4. Coeficiente de Determinación ($R^2$):
\[
R^2 = 1 - \frac{\sum (y_i - \hat{y}_i)^2}{\sum (y_i - \bar{y})^2}
\]

### 3.5. Pruebas de Compatibilidad de Hipótesis:
1. **Pendiente teórica ($m_{\text{teo}} = 1$):**
   Verificar si $|m - 1| \le 2 s_m$ (intervalo de confianza al 95\% con $k=2$).
2. **Intercepto nulo ($b_{\text{teo}} = 0$):**
   Verificar si el estadístico ratio satisface:
   \[
   \frac{|b|}{s_b} < 1 \quad\text{o}\quad |b| \le 2 s_b
   \]
   lo que certifica que el intercepto es estadísticamente indistinguible de cero al nivel de significancia del 95\%.

---

## 4. Incertidumbre Operativa vs. Combinada Instrumental

En mediciones con osciloscopio o instrumentos analógicos:
1. **Incertidumbre operativa (de apreciación visual):**
   Al fijar la referencia de cero ($\text{GND}$) en el centro de la retícula antes de cada medición, el sesgo de cero se anula y la incertidumbre dominante en la lectura viene dada por la resolución visual del operador:
   \[
   \delta V_{\text{osc}} = S_v \cdot \delta N_y, \qquad \delta t = S_t \cdot \delta N_x
   \]
   con $\delta N_y = \pm 0{,}1\,\text{div}$ y $\delta N_x = \pm 0{,}05\,\text{a}\,0{,}1\,\text{div}$.
2. **Incertidumbre combinada (GUM):**
   Incluye la tolerancia del fabricante en la ganancia vertical $u(S_v)$:
   \[
   u_c(V) = \sqrt{(S_v \cdot \delta N_y)^2 + (N_y \cdot u(S_v))^2}
   \]

---

## 5. Discrepancia y Error Relativo Porcentual

El error relativo porcentual respecto a la referencia aceptada se calcula mediante:
\[
E_r = \frac{|y_{\text{exp}} - y_{\text{ref}}|}{y_{\text{ref}}} \times \qty{100}{\percent}
\]

**Criterios de Calidad Metrológica:**
1. **Límite superior:** Todos los errores relativos deben ser estrictamente $\le 10\%$ (idealmente $< 1\%$).
2. **Apreciación visual:** Registrar siempre lecturas con un solo decimal cerrado ($\pm 0{,}1\,\text{div}$).
3. **Escala óptima:** Elegir la escala vertical y base de tiempo que ocupe la mayor porción posible de la pantalla para minimizar el error relativo propagado.

---

## 6. Estándar de Redacción en LaTeX

1. **En la Sección 09 (Tratamiento de Datos):**
   - Presentar la fórmula general de propagación.
   - Detallar los valores numéricos de entrada con sus incertidumbres.
   - Mostrar el valor de cada sumando dentro de la raíz cuadrada.
   - Reportar el resultado final en formato:
     ```latex
     \begin{equation}
         \alpha_{\text{Al}} = \qty{2,46 \pm 0,11 e-5}{\per\celsius}
         \label{eq:res_alfa_al}
     \end{equation}
     ```

2. **En el Anexo B (`sections/13_anexos.tex`):**
   - Demostración paso a paso: función base, derivadas parciales analíticas, sustitución en la raíz, factorización y expresión final.
   - Resultados finales enmarcados con `\boxed{...}`:
     ```latex
     \begin{equation}
         \boxed{\alpha_{\text{Al}} = \qty{2,46 \pm 0,11 e-5}{\per\celsius}}
     \end{equation}
     ```
