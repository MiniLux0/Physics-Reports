# Análisis consolidado — Lab 01: El osciloscopio como instrumento de medida

**Documento:** `main.pdf` (33 páginas, integrantes Vera Vivanco / Casañe Ramírez / Sánchez Feril)
**Base de comparación:** guía oficial `guia_lab01_osciloscopio.pdf` + feedback externo recibido

---

## 1. Veredicto general

El informe está en un **muy buen nivel técnico** (regresión OLS correcta, deducciones RMS correctas, trazabilidad con la hoja de datos manuscrita, cumplimiento completo del cuestionario de resultados mínimos). El feedback externo que compartiste es acertado en sus observaciones: identifica correctamente qué ya se corrigió respecto a una versión anterior y qué sigue pendiente.

Habiendo revisado el `main.pdf` actual contra ambos documentos (mi lectura original + el feedback externo), mi conclusión es:

> **De las correcciones que el feedback externo pedía, la mayoría de las "buenas" ya están incorporadas en esta versión. Pero de los 3 puntos que ese feedback marca como obligatorios, 2 siguen presentes tal cual en el texto actual, y el tercero está parcialmente resuelto.**

**Nota general estimada: 8.7–9.0/10** — sólido, pero con 3-4 afirmaciones puntuales que un docente exigente puede objetar, más la ausencia de evidencia fotográfica real del instrumento.

---

## 2. Verificación línea por línea: ¿qué está resuelto y qué no?

Contrasté cada uno de los puntos "obligatorios" del feedback externo contra el texto real del `main.pdf` que me pasaste. Esto es lo que encontré:

### 🔴 PENDIENTE — Frase "Δf < 0,1 Hz" (Sección 9.3)

Sigue exactamente igual en el texto:

> *"La diferencia con la frecuencia nominal de 250,00 Hz es inferior a la resolución de lectura en retícula (∆f < 0,1 Hz), encontrándose el valor nominal plenamente dentro del intervalo de incertidumbre experimental."*

Esto contradice la propia incertidumbre que el informe reporta dos líneas antes: **f = (250,0 ± 3,1) Hz**. No se puede decir que la diferencia es "menor a 0,1 Hz por resolución de retícula" cuando la incertidumbre real del método es de 3,1 Hz. Es una afirmación más fuerte de lo que los datos permiten.

**Corrección sugerida (aplicar tal cual):**
> "La frecuencia obtenida fue (250,0 ± 3,1) Hz. La diferencia entre el valor central medido y el nominal es nula por redondeo a la cifra significativa reportada; en cualquier caso, el valor nominal de 250 Hz se encuentra plenamente contenido dentro del intervalo de incertidumbre experimental."

---

### 🔴 PENDIENTE — Explicación causal de los 5,220 V sin matizar (Secciones 8.1, 12.1 y C.2)

El texto afirma como hecho establecido, en tres lugares distintos del informe:

> *"Este efecto es propio de fuentes de banco lineales donde, en ausencia de carga resistiva externa (I = 0), el filtro capacitivo de salida se carga al valor pico rectificado sin experimentar la caída óhmica de regulación interna (Vout = Vth − ILRint)."*

El modelo Vout = Vth − ILRint es razonable como hipótesis, pero el informe **no realizó ninguna medición bajo carga** que permita confirmar que esa es la causa real de la desviación (+0,72 V, +0,53 V, +0,65 V) en *esta* fuente regulada en particular. Presentarlo como causa demostrada en tres secciones (Análisis, Observaciones y Cuestionario) es sobreinterpretar el dato.

**Corrección sugerida** (aplicar en las 3 apariciones):
> "Una explicación plausible es el comportamiento característico de fuentes de banco lineales en vacío (filtrado capacitivo sin caída óhmica de carga, Vout ≈ Vth). Sin embargo, esta hipótesis no fue verificada experimentalmente mediante mediciones bajo distintas cargas, por lo que se reporta como explicación tentativa y no como causa confirmada."

---

### 🔴 PENDIENTE — Afirmación sobre ausencia de histéresis/deriva térmica (Sección 11.1, punto 4)

Texto actual:

> *"los residuos se distribuyen aleatoriamente alrededor del valor cero dentro de una banda estrecha inferior a ±0,05 V, sin evidenciar patrones no lineales, histéresis ni deriva térmica sistemática en el rango evaluado (1,4 V a 11,2 V)."*

Con **5 puntos tomados en una sola pasada ascendente** no es posible descartar histéresis (necesitarías subir y bajar la escala) ni deriva térmica (necesitarías repetir en el tiempo). Es una afirmación que va más allá de lo que el diseño experimental permite concluir.

**Corrección sugerida:**
> "...sin evidenciar patrones no lineales sistemáticos en los residuos. No obstante, el número de observaciones (n = 5, tomadas en una sola secuencia) no permite evaluar de forma concluyente la presencia de histéresis o deriva térmica, para lo cual se requerirían mediciones bidireccionales y repetidas en el tiempo."

---

### 🟡 PARCIAL — Tratamiento de incertidumbres (Anexo B + Sección 9.1)

Este es el punto más técnico y el que el feedback externo marca con más énfasis. Al revisarlo:

- El Anexo B.1 sí **presenta correctamente** la fórmula de propagación en cuadratura y clasifica u(Sv) como incertidumbre tipo B rectangular: u(Sv) = (±3%/√3)·Sv. Esto es correcto formalmente.
- **Pero** en la práctica (Sección 9.1, ecuaciones 13–17), todos los cálculos usan únicamente δVosc = 0,1 div × Sv, **sin combinar** la componente de ganancia del fabricante. Es decir: el Anexo B describe un modelo de incertidumbre combinada que el cuerpo del informe no aplica.
- Esto no es necesariamente "incorrecto" —el informe explica que asume calibración previa y por eso usa solo el término de apreciación visual como "incertidumbre operativa"— pero esa decisión metodológica debería estar justificada explícitamente donde se presentan los cálculos (Sección 9.1), no solo mencionada de pasada en el Anexo.

**Corrección sugerida:** añadir una frase en la Sección 9.1, antes de las ecuaciones (13)-(17):
> "Se reporta δVosc = Sv·δNy como incertidumbre operativa dominante, dado que el instrumento fue previamente calibrado y la componente de ganancia del fabricante (±3 % f.e.) resulta subdominante frente al error de apreciación visual en las escalas empleadas (ver Anexo B.1 para el modelo completo en cuadratura)."

También sería más riguroso etiquetar explícitamente ±0,0039 y ±0,026 V (Sección 9.1.1, regresión OLS) como **"errores estándar del ajuste"**, ya que actualmente se presentan sin esa aclaración, y esto se presta a confusión con una incertidumbre expandida (95 %).

---

## 3. Cosas que el feedback externo pedía y que SÍ están ya bien resueltas en esta versión

Verifiqué estas también contra el texto — están correctamente implementadas, no requieren más cambios:

| Punto | Estado en el texto actual |
|---|---|
| Consistencia de la regresión OLS (m, b, R²) | ✅ Un solo valor consistente (m=1,0036, b=−0,021, R²=0,99995) en Resumen, 9.1.1, Fig. 12, 11.1 y Conclusiones |
| Explicación del desplazamiento GND a y=−4 div | ✅ Bien justificado en 6.2 y en la nota metodológica de la Tabla 2 |
| Separación multímetro-patrón vs. valor nominal | ✅ Tabla 5 (C.1) distingue correctamente Vnom, Vmult y Vosc |
| Eliminación de "error = 0,00 %" | ✅ Ya no aparece; se usa "discrepancia inferior a..." en su lugar |
| Factor de forma kf = π/(2√2) | ✅ Presente y correctamente derivado en 11.2 |
| Lissajous como reflexión (x,y)→(x,−y), no "rotación" | ✅ Lenguaje correcto en 8.4, 11.3 y C.4–C.6 |
| Tiempo de subida como spec de catálogo, no medición | ✅ Correctamente atribuido a [4] en 8.3 |
| Curva teórica vs. valor experimental en Fig. 13 | ✅ Bien diferenciados Vp,ref (teórico) y Vp (medido) en el pie de figura |
| Rizado como observación cualitativa, no cuantificada | ✅ Sección 12.1 punto 2 ya usa "se constató cualitativamente" |

---

## 4. Punto que ambos análisis coinciden en marcar como el más visible: capturas reales del osciloscopio

Tanto mi primera revisión como el feedback externo llegan a la misma observación: **las Figuras 12, 13 y 14 son gráficos generados con Python/Matplotlib**, no capturas de pantalla reales del instrumento. La guía pide explícitamente (paso 4 de Resultados Mínimos) capturar la pantalla cuadriculada vía USB (BMP/GIF/PNG), y las Preguntas 5 y 6 del cuestionario piden lo mismo para el modo XY con DC.

Si en el laboratorio sí tomaron esas capturas (probable, dado que la guía las pide con procedimiento detallado paso a paso), **es el pendiente de mayor impacto por resolver**: agregarlas como figuras adicionales o anexo, antes que cualquier ajuste de redacción.

---

## 5. Lista de acción priorizada

1. **🔴 Agregar 2–4 capturas reales del osciloscopio** (DC con GND desplazado, senoidal del transformador, onda del generador, una figura de Lissajous) — mayor impacto, cumplimiento directo de la guía.
2. **🔴 Reescribir la frase "Δf < 0,1 Hz"** en la Sección 9.3 (una sola edición puntual).
3. **🔴 Matizar la explicación de los 5,220 V** como hipótesis no verificada, en las 3 secciones donde aparece (8.1, 12.1, C.2).
4. **🔴 Suavizar "sin evidenciar... histéresis ni deriva térmica"** en 11.1, punto 4.
5. **🟡 Justificar explícitamente en 9.1** por qué se usa solo δVosc = Sv·δNy y no la fórmula combinada del Anexo B; etiquetar ±0,0039/±0,026 V como errores estándar del ajuste.

Con los puntos 1–4 resueltos, el informe queda en un nivel muy defendible frente a cualquier revisión exigente del docente.