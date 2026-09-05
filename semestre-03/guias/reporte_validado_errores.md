# Consolidado de Datos Experimentales, Incertidumbres y Referencias Técnicas
## Laboratorio N.° 01: El Osciloscopio como Instrumento de Medida
**Facultad de Ciencias — Universidad Nacional de Ingeniería (UNI)**

---

## 1. Metadatos del Experimento

- **Curso:** Laboratorio de Física General / Física III (CF1B2)
- **Mesa de Trabajo:** N.° 03
- **Integrantes:**
  1. Casaño Ramírez, Gerald Giordano — Código: `20251368C`
  2. Sánchez Feril, Piero Alejandro — Código: `20251629A`
  3. Vera Vivanco, Jesús Rodolfo — Código: `20252703K`
- **Fecha de Toma de Datos:** 03 de septiembre de 2026

---

## 2. Fichas Metrológicas y Hojas de Datos Oficiales

Las especificaciones técnicas, tolerancias e incertidumbres de los instrumentos han sido extraídas directamente de sus hojas de datos y manuales de fabricante almacenados localmente en el repositorio:

| Instrumento | Modelo / Fabricante | Hoja Técnica / Manual Oficial | Parámetros Metrológicos Clave | Incertidumbre Instrumental ($\delta x$) |
| :--- | :--- | :--- | :--- | :--- |
| **Osciloscopio Digital** | Rohde & Schwarz HMO1202 / RTC1002 | [RTC1000 Specs (PDF)](./datasheets/RTC1000_specs_en_3607-4287-22_v1000.pdf)<br>[RTC1000 Brochure (PDF)](./datasheets/RTC1000_bro_en_3607-4287-12_v0700.pdf) | - Ancho de banda: $200\text{ MHz}$<br>- Tasa de muestreo: $2\text{ GSa/s}$<br>- Retícula: $8\text{ div} \times 12\text{ div}$<br>- Impedancia: $1\text{ M}\Omega \pm 2\%$ // $14\text{ pF}$<br>- Ganancia DC: $\pm 3\%$ fondo escala<br>- Base de tiempo: $\pm 50\text{ ppm}$ | - Retícula vertical: $\delta N_{\text{div}} = \pm 0{,}1\text{ div}$<br>- Retícula horizontal: $\delta N_x = \pm 0{,}1\text{ div}$<br>- DVM: $\pm(0{,}5\% + 1\text{ dgt})$<br>- Frecuencímetro: $\pm 0{,}05\%$ |
| **Generador de Señales** | OWON AG 051F (Serie AG-S) | [OWON AG-S Spec Sheet (PDF)](./datasheets/OWON%20AG%20S%20Series%20Spec%20Sheet.pdf)<br>[OWON AG-S Manual (PDF)](./datasheets/OWON%20AG%20S%20Series%20USER%20MANUAL.pdf) | - Tecnología DDS, DAC de $14\text{ bits}$<br>- Rango: $1\text{ }\mu\text{Hz} - 5\text{ MHz}$<br>- Resolución frec: $1\text{ }\mu\text{Hz}$ ($\pm 1\text{ ppm}$)<br>- Amplitud: $20\text{ mV}_{pp} - 20\text{ V}_{pp}$ (High-Z)<br>- Impedancia salida: $50\ \Omega$ | - Amplitud: $\pm(1{,}0\% + 1\text{ mV})$<br>- Frecuencia: $\pm 1\text{ ppm}$ |
| **Multímetro Digital** | True-RMS Industrial | Manual de Usuario / Patrón | - Escala DCV: $0{,}001\text{ V}$ resol.<br>- Escala ACV: $0{,}01\text{ V}$ resol. | - DC: $\pm(0{,}5\% + 2\text{ dgt}) \to \pm 0{,}001\text{ V}$<br>- AC: $\pm(1{,}0\% + 3\text{ dgt}) \to \pm 0{,}010\text{ V}$ |
| **Transformador Reductor** | Monofásico $220\text{ V} / 6\text{ V}$ | Red Eléctrica Nacional ($60\text{ Hz}$) | - Entrada: $220\text{ V}_{\text{rms}} \pm 5\%$<br>- Salida: $6{,}0\text{ V}_{\text{rms}}$ nominal | - Frecuencia de red: $60{,}00 \pm 0{,}05\text{ Hz}$ |
| **Pila Alcalina** | Cilíndrica AA | Electroquímica $\text{Zn/MnO}_2$ | - Tensión de celda en reposo | - Nominal: $1{,}50\text{ V}$ |
| **Fuente Regulada DC** | Multisalida de Banco | Regulador Lineal / Zener | - Salidas fijas conmutables | - $2{,}5\text{ V}$, $4{,}5\text{ V}$, $7{,}5\text{ V}$, $10{,}5\text{ V}$ |

---

## 3. Metodología de Propagación de Errores e Incertidumbres

Siguiendo las directrices metrológicas del *Guide to the Expression of Uncertainty in Measurement* (GUM) y Taylor (1997):

1. **Lectura Vertical de Voltaje en Retícula:**
   $$V_{\text{osc}} = N_{\text{div}} \cdot S_v$$
   $$\delta V_{\text{osc}} = \delta N_{\text{div}} \cdot S_v = (\pm 0{,}1\text{ div}) \cdot S_v$$

2. **Lectura Horizontal de Período y Frecuencia:**
   $$T = N_x \cdot S_t \implies \delta T = \delta N_x \cdot S_t = (\pm 0{,}1\text{ div}) \cdot S_t$$
   $$f = \frac{1}{T} \implies \delta f = \left|\frac{\partial f}{\partial T}\right| \delta T = \frac{\delta T}{T^2} = f^2 \cdot \delta T$$

3. **Conversión RMS a Pico y Pico a Pico (Señal Senoidal Pura):**
   $$V_p = \sqrt{2} \cdot V_{\text{rms}} \implies \delta V_p = \sqrt{2} \cdot \delta V_{\text{rms}}$$
   $$V_{pp} = 2 V_p = 2\sqrt{2} \cdot V_{\text{rms}} \implies \delta V_{pp} = 2\sqrt{2} \cdot \delta V_{\text{rms}}$$
   $$V_{\text{rms,calc}} = \frac{V_p}{\sqrt{2}} \implies \delta V_{\text{rms,calc}} = \frac{\delta V_p}{\sqrt{2}}$$

4. **Error Relativo Porcentual frente al Patrón:**
   $$e_r = \frac{|X_{\text{exp}} - X_{\text{patron}}|}{X_{\text{patron}}} \times 100\%$$

---

## 4. Parte B — Medidas de Voltajes Constantes DC (Con Margen de Error)

### Tabla B: Mediciones en Diferentes Escalas Verticales

| Fuente | $V_{\text{nom}}$ | $V_{\text{mult}}$ (Patrón) | Escala $S_v$ | Lectura $N_{\text{div}}$ | Voltaje $V_{\text{osc}} \pm \delta V_{\text{osc}}$ | Error Relativo ($e_r$) | Estado |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Pila Alcalina** | $1{,}50\text{ V}$ | $1{,}442 \pm 0{,}001\text{ V}$ | $5\text{ V/div}$ | $0{,}3 \pm 0{,}1\text{ div}$ | $1{,}50 \pm 0{,}50\text{ V}$ | **$4{,}02\%$** | Aceptable |
| | | | $2\text{ V/div}$ | $0{,}7 \pm 0{,}1\text{ div}$ | $1{,}40 \pm 0{,}20\text{ V}$ | **$2{,}91\%$** | Bueno |
| | | | $1\text{ V/div}$ | $1{,}4 \pm 0{,}1\text{ div}$ | $1{,}40 \pm 0{,}10\text{ V}$ | **$2{,}91\%$** | Bueno |
| | | | $0{,}5\text{ V/div}$ | $2{,}9 \pm 0{,}1\text{ div}$ | $1{,}45 \pm 0{,}05\text{ V}$ | **$0{,}55\%$** | Muy Bueno |
| | | | $0{,}2\text{ V/div}$ | **$7{,}2 \pm 0{,}1\text{ div}$** | **$1{,}44 \pm 0{,}02\text{ V}$** | **$0{,}14\%$** | **Óptima** |
| **Fuente Pos. 1** | $2{,}50\text{ V}$ | $2{,}453 \pm 0{,}001\text{ V}$ | $5\text{ V/div}$ | $0{,}5 \pm 0{,}1\text{ div}$ | $2{,}50 \pm 0{,}50\text{ V}$ | **$1{,}92\%$** | Bueno |
| | | | $2\text{ V/div}$ | $1{,}2 \pm 0{,}1\text{ div}$ | $2{,}40 \pm 0{,}20\text{ V}$ | **$2{,}16\%$** | Bueno |
| | | | $1\text{ V/div}$ | $2{,}5 \pm 0{,}1\text{ div}$ | $2{,}50 \pm 0{,}10\text{ V}$ | **$1{,}92\%$** | Bueno |
| | | | $0{,}5\text{ V/div}$ | **$4{,}9 \pm 0{,}1\text{ div}$** | **$2{,}45 \pm 0{,}05\text{ V}$** | **$0{,}12\%$** | **Óptima** |
| | | | $0{,}2\text{ V/div}$ | *Fuera Escala* | --- | --- | Saturation ($>8\text{ div}$) |
| **Fuente Pos. 2** | $4{,}50\text{ V}$ | $5{,}220 \pm 0{,}001\text{ V}$<br>*(en vacío)* | $5\text{ V/div}$ | $1{,}0 \pm 0{,}1\text{ div}$ | $5{,}00 \pm 0{,}50\text{ V}$ | **$4{,}21\%$** | Aceptable |
| | | | $2\text{ V/div}$ | **$2{,}6 \pm 0{,}1\text{ div}$** | **$5{,}20 \pm 0{,}20\text{ V}$** | **$0{,}38\%$** | **Óptima** |
| | | | $<2\text{ V/div}$ | *Fuera Escala* | --- | --- | Saturation |
| **Fuente Pos. 3** | $7{,}50\text{ V}$ | $8{,}030 \pm 0{,}001\text{ V}$<br>*(en vacío)* | $5\text{ V/div}$ | $1{,}6 \pm 0{,}1\text{ div}$ | $8{,}00 \pm 0{,}50\text{ V}$ | **$0{,}37\%$** | Muy Bueno |
| | | | $2\text{ V/div}$ | **$4{,}0 \pm 0{,}1\text{ div}$** | **$8{,}00 \pm 0{,}20\text{ V}$** | **$0{,}37\%$** | **Óptima** |
| | | | $<2\text{ V/div}$ | *Fuera Escala* | --- | --- | Saturation |
| **Fuente Pos. 4** | $10{,}50\text{ V}$ | $11{,}150 \pm 0{,}001\text{ V}$<br>*(en vacío)* | $5\text{ V/div}$ | $2{,}2 \pm 0{,}1\text{ div}$ | $11{,}00 \pm 0{,}50\text{ V}$ | **$1{,}35\%$** | Bueno |
| | | | $2\text{ V/div}$ | **$5{,}6 \pm 0{,}1\text{ div}$** | **$11{,}20 \pm 0{,}20\text{ V}$** | **$0{,}45\%$** | **Óptima** |
| | | | $<2\text{ V/div}$ | *Fuera Escala* | --- | --- | Saturation |

---

## 5. Parte C — Medidas de Voltajes Variables AC (Transformador 220 V / 6 V — 60 Hz)

### Valores Teóricos y Patrones con Incertidumbre
- $V_{\text{rms,mult}} = 6{,}830 \pm 0{,}010\text{ V}$
- $V_{p,\text{teo}} = \sqrt{2} \cdot (6{,}830 \pm 0{,}010) = 9{,}659 \pm 0{,}014\text{ V}$
- $V_{pp,\text{teo}} = 2 \cdot (9{,}659 \pm 0{,}014) = 19{,}318 \pm 0{,}028\text{ V}$
- $T_{\text{teo}} = \frac{1}{60{,}00 \pm 0{,}05\text{ Hz}} = 16{,}667 \pm 0{,}014\text{ ms}$

### Tabla C: Mediciones Experimentales del Transformador

| Parámetro Medido | Escala / Base | Lectura Retícula | Magnitud Calculada ($\pm \delta$) | Valor Patrón | Error Relativo ($e_r$) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Voltaje Pico a Pico ($V_{pp}$)** | $5\text{ V/div}$ | $N_{y,pp} = 3{,}9 \pm 0{,}1\text{ div}$ | $V_{pp} = 19{,}50 \pm 0{,}50\text{ V}$ | $19{,}32 \pm 0{,}03\text{ V}$ | **$0{,}93\%$** |
| **Amplitud Semionda ($V_p$)** | $2\text{ V/div}$ | $N_{y,p} = 4{,}8 \pm 0{,}1\text{ div}$ | $V_p = 9{,}60 \pm 0{,}20\text{ V}$ | $9{,}66 \pm 0{,}01\text{ V}$ | **$0{,}62\%$** |
| **Voltaje Eficaz ($V_{\text{rms}}$)** | De $V_p$ | $V_p / \sqrt{2}$ | $V_{\text{rms}} = 6{,}79 \pm 0{,}14\text{ V}$ | $6{,}83 \pm 0{,}01\text{ V}$ | **$0{,}59\%$** |
| **Período ($T$) a $5\text{ ms/div}$** | $5\text{ ms/div}$ | $N_x = 3{,}3 \pm 0{,}1\text{ div}$ | $T = 16{,}50 \pm 0{,}50\text{ ms}$ | $16{,}67 \pm 0{,}01\text{ ms}$ | **$1{,}02\%$** |
| **Frecuencia ($f$) a $5\text{ ms/div}$** | $f = 1/T$ | Derivada: $\delta f = f^2 \delta T$ | $f = 60{,}6 \pm 1{,}8\text{ Hz}$ | $60{,}00 \pm 0{,}05\text{ Hz}$ | **$1{,}00\%$** |
| **Período ($T$) a $2\text{ ms/div}$** | $2\text{ ms/div}$ | $N_x = 8{,}3 \pm 0{,}1\text{ div}$ | $T = 16{,}60 \pm 0{,}20\text{ ms}$ | $16{,}67 \pm 0{,}01\text{ ms}$ | **$0{,}42\%$** |
| **Frecuencia ($f$) a $2\text{ ms/div}$** | $f = 1/T$ | Derivada: $\delta f = f^2 \delta T$ | $f = 60{,}24 \pm 0{,}73\text{ Hz}$ | $60{,}00 \pm 0{,}05\text{ Hz}$ | **$0{,}40\%$** |
| **Frecuencímetro por Hardware** | Quick View | Conteo digital | $f_{\text{dig}} = 60{,}30 \pm 0{,}10\text{ Hz}$ | $60{,}00 \pm 0{,}05\text{ Hz}$ | **$0{,}50\%$** |

---

## 6. Parte D — Medidas de Voltajes Variables AC (Generador OWON AG 051F)

### Parámetros Fijados en el Generador
- **Frecuencia fija:** $f_{\text{gen}} = 250{,}00 \pm 0{,}01\text{ Hz} \implies T = 4{,}000 \pm 0{,}001\text{ ms}$
- **Amplitud fijada:** $V_p = 4{,}80 \pm 0{,}05\text{ V} \implies V_{pp} = 9{,}60 \pm 0{,}10\text{ V}$

### Tabla D: Resultados según Forma de Onda

| Función de Onda | $V_{\text{mult}}$ (RMS Patrón) | Escala $S_v$ | Amplitud $V_p \pm \delta V_p$ | Base $S_t$ | Período $N_x$ | Período $T \pm \delta T$ | Frecuencia $f \pm \delta f$ | $e_r$ ($f$) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Senoidal** | $3{,}420 \pm 0{,}010\text{ V}$ | $2\text{ V/div}$ | $4{,}80 \pm 0{,}20\text{ V}$ | $0{,}5\text{ ms/div}$ | $8{,}0 \pm 0{,}1\text{ div}$ | $4{,}00 \pm 0{,}05\text{ ms}$ | $250{,}0 \pm 3{,}1\text{ Hz}$ | **$0{,}00\%$** |
| **Triangular**| $2{,}790 \pm 0{,}010\text{ V}$ | $2\text{ V/div}$ | $4{,}80 \pm 0{,}20\text{ V}$ | $1{,}0\text{ ms/div}$ | $4{,}0 \pm 0{,}1\text{ div}$ | $4{,}00 \pm 0{,}10\text{ ms}$ | $250{,}0 \pm 6{,}2\text{ Hz}$ | **$0{,}00\%$** |
| **Cuadrada**  | $4{,}800 \pm 0{,}020\text{ V}$ | $2\text{ V/div}$ | $4{,}80 \pm 0{,}20\text{ V}$ | $0{,}5\text{ ms/div}$ | $8{,}0 \pm 0{,}1\text{ div}$ | $4{,}00 \pm 0{,}05\text{ ms}$ | $250{,}0 \pm 3{,}1\text{ Hz}$ | **$0{,}00\%$** |

---

## 7. Respuestas Técnicas a los Resultados Mínimos de la Guía

### 1. Tabla Comparativa de Tres Columnas (DC con Incertidumbres)
| Salida / Fuente | $V_{\text{nom}}$ | $V_{\text{mult}}$ (Patrón) | $V_{\text{osc}}$ (Óptimo) | Error Relativo ($e_r$) |
| :--- | :--- | :--- | :--- | :--- |
| **Pila Alcalina** | $1{,}50\text{ V}$ | $1{,}442 \pm 0{,}001\text{ V}$ | $1{,}440 \pm 0{,}020\text{ V}$ | **$0{,}14\%$** |
| **Fuente Regulada (Salida 1)** | $2{,}50\text{ V}$ | $2{,}453 \pm 0{,}001\text{ V}$ | $2{,}450 \pm 0{,}050\text{ V}$ | **$0{,}12\%$** |
| **Fuente Regulada (Salida 2)** | $4{,}50\text{ V}$ | $5{,}220 \pm 0{,}001\text{ V}$ | $5{,}200 \pm 0{,}200\text{ V}$ | **$0{,}38\%$** |
| **Fuente Regulada (Salida 3)** | $7{,}50\text{ V}$ | $8{,}030 \pm 0{,}001\text{ V}$ | $8{,}000 \pm 0{,}200\text{ V}$ | **$0{,}37\%$** |
| **Fuente Regulada (Salida 4)** | $10{,}50\text{ V}$ | $11{,}150 \pm 0{,}001\text{ V}$ | $11{,}200 \pm 0{,}200\text{ V}$ | **$0{,}45\%$** |

---

### 2. ¿Es realmente constante el voltaje dado por esta fuente?
- **Rizado Residual (Ripple):** Al acoplar el osciloscopio en modo **AC** y elevar la ganancia a $5\text{ mV/div}$, se evidencia que la señal presenta un rizado residual de rectificación con amplitud pico a pico $\Delta V_{\text{ripple}} < 8\text{ mV}$ con periodicidad de $100\text{ Hz}$ / $120\text{ Hz}$ proveniente del puente de diodos.
- **Regulación de Carga:** El potencial terminal disminuye cuando se demanda corriente por la caída en la impedancia interna de la fuente ($V = V_{\text{th}} - I_L R_{\text{int}}$). En circuito abierto se registraron los valores máximos ($5{,}220\text{ V}$ para la posición nominal de $4{,}50\text{ V}$).
- **Conclusión:** Macroscópicamente el voltaje es estable y constante dentro de una tolerancia temporal de $\pm 0{,}2\%$.

---

### 3. Período y Frecuencia del Transformador a Diferentes Bases de Tiempo
Período nominal de la red eléctrica: $T_{\text{nom}} = \frac{1}{60{,}00\text{ Hz}} = 16{,}667\text{ ms}$.
- **A $5\text{ ms/div}$:** $N_x = 3{,}3 \pm 0{,}1\text{ div} \implies T = 16{,}50 \pm 0{,}50\text{ ms} \implies f = 60{,}6 \pm 1{,}8\text{ Hz}$ ($e_r = 1{,}0\%$).
- **A $2\text{ ms/div}$:** $N_x = 8{,}3 \pm 0{,}1\text{ div} \implies T = 16{,}60 \pm 0{,}20\text{ ms} \implies f = 60{,}24 \pm 0{,}73\text{ Hz}$ ($e_r = 0{,}4\%$).
- **A $1\text{ ms/div}$:** El semiperíodo ocupa $N_{x,T/2} = 8{,}3 \pm 0{,}1\text{ div} \implies T = 16{,}60 \pm 0{,}20\text{ ms} \implies f = 60{,}24\text{ Hz}$.
- **Frecuencímetro por Hardware:** $f_{\text{dig}} = 60{,}30 \pm 0{,}10\text{ Hz}$.

---

### 4. Modo Graficador XY y Figuras de Lissajous (Pasos 16 al 19)
Ecuaciones paramétricas en pantalla:
$$\begin{cases} x(t) = A_x \sin(2\pi f_x t) \\ y(t) = A_y \sin(2\pi f_y t + \phi) \end{cases}$$
con $f_x = 60\text{ Hz}$ fijo (CH1) y $f_y$ variable (CH2):

1. **$f_y = 60\text{ Hz}$ (Relación 1:1):** Elipse estacionaria. Cuando $\phi = 0$ o $\pi$, la elipse degenera en un segmento de recta de pendiente positiva o negativa.
2. **Paso 17 (CH2 Invertido):** La inversión del canal Y ($y \to -y$) genera una reflexión especular respecto al eje horizontal, invirtiendo la pendiente de la figura.
3. **$f_y = 120\text{ Hz}$ (Relación 1:2):** Figura en forma de "8" o parábola bicúspide ($2$ tangentes horizontales y $1$ vertical).
4. **$f_y = 180\text{ Hz}$ (Relación 1:3):** Curva cerrada con 3 bucles ($3$ lóbulos verticales y $1$ horizontal).
5. **$f_y = 240\text{ Hz}$ (Relación 1:4):** Curva simétrica con 4 bucles cerrados estables.

---

### 5. Modo XY con Voltajes Continuos DC ($V_x = 1{,}5\text{ V}$, $V_y = 3{,}0\text{ V}$)
- **Señal observada:** Al ser potenciales invariables en el tiempo, no existe deflexión dinámica ni barrido temporal. Se proyecta un **punto luminoso fijo** en el primer cuadrante de la retícula en $(x, y) = (+1{,}5\text{ V}, +3{,}0\text{ V})$.

---

### 6. Modo XY con Voltajes DC y CH2 Invertido
- **Señal observada:** Al negar el potencial vertical ($V_y \to -3{,}0\text{ V}$), el punto luminoso se traslada verticalmente hacia la mitad inferior de la pantalla, posicionándose en el cuarto cuadrante $(x, y) = (+1{,}5\text{ V}, -3{,}0\text{ V})$.

---

## 8. Bibliografía y Referencias de Hojas de Datos

### Enlaces Locales a Datasheets y Manuales del Repositorio
1. **Rohde & Schwarz RTC1000 Series:**
   - [Especificaciones Técnicas Completas (Version 10.00)](./datasheets/RTC1000_specs_en_3607-4287-22_v1000.pdf)
   - [Ficha de Datos del Fabricante (Version 05.01)](./datasheets/RTC1000_dat_en_3607-4287-32_v0501.pdf)
   - [Brochure del Producto (Version 07.00)](./datasheets/RTC1000_bro_en_3607-4287-12_v0700.pdf)
2. **OWON AG-S Series Arbitrary Waveform Generator:**
   - [Hoja de Especificaciones de Rendimiento (Spec Sheet)](./datasheets/OWON%20AG%20S%20Series%20Spec%20Sheet.pdf)
   - [Manual de Usuario Oficial (User Manual)](./datasheets/OWON%20AG%20S%20Series%20USER%20MANUAL.pdf)

### Entradas BibTeX para el Informe Oficial (`refs.bib`)

```bibtex
@manual{rs_rtc1000_specs,
    author       = {{Rohde \& Schwarz GmbH \& Co. KG}},
    title        = {{R\&S\textregistered RTC1000 Oscilloscope --- Specifications}},
    year         = {2024},
    version      = {10.00},
    organization = {Rohde \& Schwarz},
    address      = {Munich, Germany},
    note         = {PD 3607.4287.22}
}

@manual{owon_ags_spec,
    author       = {{Fujian Lilliput Optoelectronics Technology Co., Ltd.}},
    title        = {{AG-S Series 1-CH High Frequency Arbitrary Waveform Generator --- Performance Specifications}},
    year         = {2023},
    organization = {OWON Technology},
    address      = {Zhangzhou, China}
}

@manual{owon_ags_manual,
    author       = {{Fujian Lilliput Optoelectronics Technology Co., Ltd.}},
    title        = {{AG-S Series Arbitrary Waveform Generator User Manual}},
    year         = {2023},
    organization = {OWON Technology},
    address      = {Zhangzhou, China}
}

@book{taylor,
    author    = {Taylor, John R.},
    title     = {An Introduction to Error Analysis: The Study of Uncertainties in Physical Measurements},
    edition   = {2},
    publisher = {University Science Books},
    year      = {1997},
    address   = {Sausalito, California}
}

@book{serway,
    author    = {Serway, Raymond A. and Jewett, John W.},
    title     = {F\'isica para ciencias e ingenier\'ia},
    volume    = {2},
    edition   = {10},
    publisher = {Cengage Learning},
    year      = {2018},
    address   = {Ciudad de M\'exico}
}

@book{halliday,
    author    = {Halliday, David and Resnick, Robert and Walker, Jearl},
    title     = {Fundamentals of Physics},
    edition   = {10},
    publisher = {Wiley},
    year      = {2014},
    address   = {Hoboken, NJ}
}
```
