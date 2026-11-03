# Laboratorio N°3 — Curvas características Voltaje–Corriente
**Paquete de datos para el informe** (valores medidos tal cual, más cálculos derivados)

Orden pensado para tu formato: Introducción / Resumen / Objetivos → Fundamento teórico → Materiales y equipos → Procedimiento (partes A–D) → Resultados → Tratamiento de datos → Gráficas → Análisis → Observaciones → Bibliografía.

---

## 0. Por confirmar antes de escribir
1. ¿El "RESISTENCIA" de la hoja es la de **100 Ω** o el **E2 (carbón)** de la guía? Los datos dan R ≈ 100 Ω.
2. La guía pide fuente de **6 V** y ustedes usaron **7,5 V**. Dilo así en Equipos y Procedimiento.
3. La guía pide voltímetro y amperímetro separados; ustedes usaron **un medidor que da V e I a la vez**. Anota su marca o modelo si lo tienes.
4. El voltaje en el elemento llegó como máximo a 6,43 V (foquito) y 6,49 V (resistencia), no a 7,5 V. Piensa si hubo un motivo (límite del reóstato, rango, etc.).
5. Fecha en la hoja: 01/10/26. Ojo: la guía dice "Laboratorio N°2" y tu hoja dice "N°3".

---

## 1. Objetivos (según la guía)
- **General:** estudiar las características de elementos resistivos a partir de sus gráficas V–I.
- **Específicos:** medir la corriente a través de un elemento para un voltaje aplicado (pares V–I) y graficar los pares V–I de tres elementos resistivos.

## 2. Fundamento teórico (puntos clave)
- Al aplicar una diferencia de potencial V a un elemento no aislante circula una corriente I que depende de su resistencia.
- **Resistencia:** R = V/I (Ω).
- **Ley de Ohm:** en materiales óhmicos R es constante, así que I es proporcional a V (si se duplica V, se duplica I) y la gráfica I–V es una recta que pasa por el origen.
- **Elementos no óhmicos:** R depende de la corriente.
  - *Foquito (filamento metálico):* al pasar corriente se calienta y su resistencia **aumenta** con la temperatura, así que la curva I–V se aplana.
  - *Diodo:* casi no conduce hasta un voltaje umbral (~0,6–0,7 V en silicio) y luego la corriente crece muy rápido, así que R **disminuye** al aumentar I. Es unidireccional (si no pasa corriente, invertir la polaridad).
- **Potencia:** P = V·I.
- **Propagación de incertidumbre:** ΔR/R = ΔV/V + ΔI/I.

## 3. Materiales y equipos
**Según la guía:** fuente de corriente continua (6 V), reóstato usado como potenciómetro, 8 cables, amperímetro 0–1 A, voltímetro 0–10 V, caja con tres elementos (E1 foquito, E2 carbón, E3 diodo) y dos resistencias (1 Ω y 100 Ω).

**Lo que realmente usaron:** fuente de poder en 7,5 V, medidor que mide V e I automáticamente, caja de elementos, cables. (Completa con lo que falte.)

## 4. Procedimiento (partes)
Circuito de la guía (Fig. 2.1): fuente → reóstato como potenciómetro (divisor de voltaje) → amperímetro en serie con el elemento → voltímetro en paralelo con el elemento (puntos a y b).
- **Parte A — Foquito (E1):** se varió el cursor del reóstato y se registró V e I, de 1 V a ~6,4 V.
- **Parte B — Resistencia:** mismo procedimiento, de 1 V a ~6,5 V.
- **Parte C — Diodo (E3):** mismo procedimiento, de 0,61 V a 0,75 V, cuidando de no pasar de 0,9 A (se quema). La guía pedía tomar el voltaje para corrientes de 0,1; 0,2; … 0,9 A, pero ustedes tomaron la corriente a voltajes elegidos.
- **Parte D — Nicrón:** está tachado en la hoja; no se midió. Indica el motivo si lo recuerdas.

---

## 5. Resultados experimentales (valores medidos)

Incertidumbres supuestas (resolución del último dígito): ΔV = 0,01 V y ΔI = 0,001 A. Ajústalas si conoces la del medidor.

### Tabla 1 — Foquito
| N° | V (V) | I (A) | R = V/I (Ω) | P = V·I (W) |
|----|-------|-------|-------------|-------------|
| 1  | 0,00 | 0,000 | — | 0,000 |
| 2  | 1,00 | 0,148 | 6,76 | 0,148 |
| 3  | 2,02 | 0,218 (*) | 9,27 | 0,440 |
| 4  | 3,04 | 0,272 | 11,18 | 0,827 |
| 5  | 4,01 | 0,318 (*) | 12,61 | 1,275 |
| 6  | 5,01 | 0,366 | 13,69 | 1,834 |
| 7  | 6,01 | 0,412 | 14,59 | 2,476 |
| 8  | 6,43 | 0,432 | 14,88 | 2,778 |

### Tabla 2 — Resistencia
| N° | V (V) | I (A) | R = V/I (Ω) | ΔR (Ω) |
|----|-------|-------|-------------|--------|
| 1  | 0,00 | 0,000 | — | — |
| 2  | 1,00 | 0,010 | 100,0 | ±11,0 |
| 3  | 2,00 | 0,020 | 100,0 | ±5,5 |
| 4  | 3,05 | 0,031 | 98,4 | ±3,5 |
| 5  | 4,03 | 0,040 | 100,8 | ±2,8 |
| 6  | 5,00 | 0,050 | 100,0 | ±2,2 |
| 7  | 6,02 | 0,060 | 100,3 | ±1,8 |
| 8  | 6,49 | 0,065 | 99,8 | ±1,7 |

Todas las R medidas coinciden con 100 Ω dentro de su incertidumbre.

### Tabla 3 — Diodo
| N° | V (V) | I (A) | R = V/I (Ω) | P = V·I (W) |
|----|-------|-------|-------------|-------------|
| 1  | 0,00 | 0,000 | — | 0,000 |
| 2  | 0,61 | 0,050 | 12,2 | 0,031 |
| 3  | 0,69 | 0,215 | 3,21 | 0,148 |
| 4  | 0,70 | 0,230 (*) (?) | 3,04 | 0,161 |
| 5  | 0,71 | 0,411 | 1,73 | 0,292 |
| 6  | 0,72 | 0,537 | 1,34 | 0,387 |
| 7  | 0,73 | 0,690 | 1,06 | 0,504 |
| 8  | 0,75 | 0,783 | 0,96 | 0,587 |

### Tabla 4 — Nicrón
Tachado en la hoja (no se midió).

(*) Dígitos sobrescritos en la hoja original. (?) Punto sospechoso (ver sección 8).

---

## 6. Tratamiento de datos

### 6a. Resistencia de carbón 100 Ω — ajuste lineal por el origen (I = G·V)

Regresión MCO forzada por el origen con 7 puntos (V de 1,00 a 6,49 V):

| Parámetro | Valor experimental | Valor nominal | Error relativo |
|-----------|-------------------|---------------|----------------|
| G = 1/R | 0,009998 S | 0,010000 S | 0,018 % |
| **R_exp** | **100,02 ± 2,55 Ω** | **100 Ω** | **0,02 %** |
| R² | 0,999845 | — | — |

Incertidumbre propagada (ΔR/R = ΔV/V + ΔI/I): δR = ±2,55 Ω. Todos los valores individuales R = V/I ∈ [98,4; 100,8] Ω son compatibles con 100 Ω dentro de su δR.

### 6b. Foquito — ajuste ley de potencias I = k·V^n (regresión log–log, 7 puntos)

I = (0,146 ± 0,003) · V^(0,573 ± 0,014)

| Parámetro | Valor | Referencia bibliográfica | Concordancia |
|-----------|-------|--------------------------|-------------|
| k | 0,1461 A/V^n | — | — |
| **n (exponente)** | **0,573** | **0,50–0,60 (Stefan-Boltzmann + Joule)** | **✅ dentro del rango** |
| R² | 0,9987 | — | — |
| R (1 V) | 6,76 Ω | — | — |
| R (6,43 V) | 14,88 Ω | — | — |
| Incremento de R | +120 % | Tungsteno: α = 4,5×10⁻³ /°C | ✅ consistente |

El exponente n = 0,573 ∈ [0,50; 0,60] es coherente con la bibliografía de filamentos de tungsteno en régimen estacionario. n < 1 confirma que la curva I–V se aplana y R crece con V.

### 6c. Diodo de silicio — ecuación de Shockley (ajuste log-lineal, 6 puntos, SIN N°4)

Modelo: I = I_S · (exp(V / (n·V_T)) − 1),  con V_T = kT/q = 25,69 mV a 25 °C.
Ajuste: ln(I) = −15,71 + 20,81·V

| Parámetro | Valor experimental | Rango teórico (silicio p-n, 25 °C) | Concordancia |
|-----------|-------------------|------------------------------------|-------------|
| **n (factor de idealidad)** | **1,871 ± 0,123** | **1,0–2,0** | **✅** |
| **I_S (corriente de saturación)** | **1,51×10⁻⁷ A** | **10⁻¹² a 10⁻⁶ A** | **✅** |
| R² | 0,9831 | — | — |
| **V_umbral** (extrapolación lineal, zona 0,71–0,75 V) | **0,662 V** | **0,60–0,70 V (silicio)** | **✅** |
| Conductancia dinámica (zona codo) | 9,28 A/V | — | — |

Nota sobre n ≈ 1,87: factor de idealidad cercano a 2 indica que la corriente de recombinación en la zona de vaciamiento domina sobre la difusión. Habitual en diodos de silicio para corrientes de 10–800 mA en la zona del codo exponencial. Literatura: n ∈ [1,5; 2,0] para diodos de señal/rectificadores de Si a temperatura ambiente.

### 6d. Diagnóstico cuantitativo del punto N°4 del diodo (0,70 V; 0,230 A)

Con el ajuste de Shockley (sin N°4), la corriente predicha a 0,70 V es **0,328 A**.
Residuo: Δ = 0,230 − 0,328 = **−0,098 A**, equivalente a **98σ** (σ = δI = 0,001 A).
→ **Outlier estadístico confirmado (>>3σ).** Causa física: resolución del medidor de 10 mV comparable al paso en la zona exponencial del codo; un salto de 10 mV puede generar ≈ 0,1 A de variación de corriente. El último dígito de I está sobrescrito en la hoja.
Acción: reportar tal cual en la tabla con nota (*), excluir del ajuste de Shockley y graficar ambas curvas (con y sin N°4).

### 6e. R a 0,8 V (pedido de la guía — sección 5.3)
| Elemento | I a 0,8 V | R a 0,8 V | Origen |
|----------|-----------|-----------|--------|
| Resistencia | ≈ 0,008 A | ≈ 100 Ω | Ley de Ohm (ajuste lineal) |
| Foquito | ≈ 0,129 A | ≈ 6,2 Ω | **Extrapolado** (ajuste potencial; V_min medido = 1,0 V) |
| Diodo | — | < 0,96 Ω | **No medido** (V_max = 0,75 V); Shockley predice I ≈ 0,93 A a 0,75 V |

## 7. Gráficas (5.1)
Una gráfica I (A) vs V (V) por elemento, con barras de error si puedes:
1. **Foquito:** curva cóncava (se aplana). Añade la curva ajustada I = 0,146·V^0,573.
2. **Resistencia:** recta por el origen con pendiente 0,0100 A/V.
3. **Diodo:** curva casi nula hasta ~0,6 V y luego creciente; marca el punto N°4.
4. *(Opcional)* Las tres juntas, y R vs I para cada elemento (constante, creciente, decreciente).

## 8. Análisis
- **5.2 — Ley de Ohm:** se cumple solo en la **resistencia** (R constante ≈ 100 Ω, gráfica recta por el origen). En el foquito R **aumenta** con I (filamento más caliente) y en el diodo R **disminuye** con I.
- **Punto sospechoso del diodo (0,70 V; 0,230 A):** entre 0,69 y 0,70 V la corriente sube solo 0,015 A y entre 0,70 y 0,71 V sube 0,181 A, lo que rompe la tendencia creciente de la pendiente. El último dígito está sobrescrito en la hoja. La resolución de 10 mV influye mucho cerca del codo (un paso de 10 mV puede mover la corriente ~0,1 A), pero este punto se sale incluso de eso.
- **Cómo tratarlo sin alterar datos:**
  1. Lo ideal es volver a medir el diodo (ver sección 10).
  2. Si no se puede, repórtalo como medido, márcalo como atípico, explica por qué lo es y grafica con y sin ese punto.
- **Potencias:** foquito 2,78 W, resistencia 0,42 W y diodo 0,59 W en su último punto. El foquito disipa más y por eso se calienta más.
- **Comparación foquito–resistencia:** a ~6 V el foquito deja pasar ≈ 0,41 A y la resistencia ≈ 0,06 A.

## 9. Observaciones y posibles fuentes de error
- Algunas lecturas están sobrescritas o corregidas en la hoja (foquito N°2, N°3 y N°5; diodo N°4).
- Resolución del medidor: ΔV ≈ 0,01 V y ΔI ≈ 0,001 A. Pesa mucho en la resistencia a bajos voltajes (±11 Ω a 1 V).
- Los voltajes no son exactamente 1, 2, 3, … V (p. ej. 2,02; 3,04; 6,43), porque el reóstato permite ajustar solo de forma aproximada.
- Calentamiento del foquito y del diodo durante la medición (la resistencia cambia con la temperatura, y las lecturas pueden derivar).
- Lecturas que fluctúan con el medidor automático al cambiar el cursor.
- Resistencia de contactos y cables.
- Se usó 7,5 V en lugar de los 6 V de la guía; no se llegó al voltaje de la fuente en el elemento.
- Parte del procedimiento difiere de la guía (diodo no medido a pasos de corriente; nicrón sin medir).

## 10. Si pueden repetir la medición
- **Diodo:** tomar V con la corriente en pasos de 0,1 A hasta 0,9 A (como pide la guía), sin pasar de 0,9 A.
- **Foquito y diodo a 0,8 V:** medir I directamente, para 5.3.
- Repetir el punto del diodo en ~0,70 V.
- Anotar dígitos con claridad y sin sobrescribir.

## 11. Bibliografía (sugerida)
- Guía de laboratorio N°2, "Curvas características voltaje–corriente" (UNI).
- Sears, Zemansky, Young & Freedman. *Física Universitaria*, vol. 2.
- Serway & Jewett. *Física para Ciencias e Ingeniería*, vol. 2.
- Resnick, Halliday & Krane. *Física*, vol. 2.
