# CAMBIOS_a4.md — Agente 4 (Capítulo 6, Bibliografía y Anexos)

### 1. Sección 6.1.4 (Problema Resuelto 4 — Efecto Zeeman)
- **Ubicación:** Caja de Problema Resuelto 4 en `sections/06_ejercicios_resueltos_y_propuestos.tex`.
- **Texto antes:** `\begin{ejemplobox}[Problema Resuelto 4: Efecto Zeeman Orbital y Precesión de Larmor Cuántica (PD3 P2)]`
- **Texto después:** `\begin{ejemplobox}[Problema Resuelto 4: Efecto Zeeman Orbital y Precesión de Larmor Cuántica]`
- **Motivo:** Eliminar etiqueta de aula «(PD3 P2)» (Parte A, Punto 12).

### 2. Sección 6.1.5 (Problema Resuelto 5 — Oscilador 2D)
- **Ubicación:** Caja de Problema Resuelto 5 en `sections/06_ejercicios_resueltos_y_propuestos.tex`.
- **Texto antes:** `\begin{ejemplobox}[Problema Resuelto 5: Oscilador 2D Isótropo y Modos Circulares Cuánticos (PD3 P4)]`
- **Texto después:** `\begin{ejemplobox}[Problema Resuelto 5: Oscilador 2D Isótropo y Modos Circulares Cuánticos]`
- **Motivo:** Eliminar etiqueta de aula «(PD3 P4)» (Parte A, Punto 12).

### 3. Sección 6.2 (Subtítulo de Ejercicios Propuestos)
- **Ubicación:** Subsección 6.2 en `sections/06_ejercicios_resueltos_y_propuestos.tex`.
- **Texto antes:** `\subsection{Ejercicios Propuestos para Autoestudio (Nivel Examen / Zettili)}`
- **Texto después:** `\subsection{Ejercicios Propuestos para Autoestudio (Nivel Avanzado / Zettili)}`
- **Motivo:** Eliminar alusión a «Nivel Examen» (Parte A, Punto 13).

### 4. Sección 6.2.4 (Ejercicio Propuesto 4 — Acoplamiento Espín-Órbita)
- **Ubicación:** Subsección 6.2.4 en `sections/06_ejercicios_resueltos_y_propuestos.tex`.
- **Texto antes:**
  `\begin{ejerciciobox}[Ejercicio Propuesto 4: Estructura Fina y Desdoblamiento Espín-Órbita (PD3 P8)]`
  `\textbf{Nivel: Examen / Intermedio-Avanzado}\\`
  `\hat{H}_{SO} = \xi(\hat{\vec{L}}\cdot\hat{\vec{S}}), \quad \xi > 0.`
- **Texto después:**
  `\begin{ejerciciobox}[Ejercicio Propuesto 4: Estructura Fina y Desdoblamiento Espín-Órbita]`
  `\textbf{Nivel: Avanzado}\\`
  `\hat{H}_{SO} = \xi(\hat{\vec{L}}\cdot\hat{\vec{S}}), \quad \xi > 0,`
  `donde la constante $\xi \equiv \ev{\xi(r)}_{2p}$ es el valor esperado radial de la función de acoplamiento espín-órbita $\xi(r)$ evaluada en el subespacio del nivel $2p$ (consistente con la Sección~\ref{subsec:separacion_central_espacial}).`
- **Motivo:** Eliminar etiquetas «(PD3 P8)» y «Nivel: Examen» (Parte A, Puntos 12 y 13), y clarificar el significado físico de $\xi$ como valor medio radial $\ev{\xi(r)}_{2p}$ consistente con la Sección 5.10.1 (Parte C, C6).

### 5. Sección 6.2.5 (Ejercicio Propuesto 5 — Estados de Bell)
- **Ubicación:** Subsección 6.2.5 en `sections/06_ejercicios_resueltos_y_propuestos.tex`.
- **Texto antes:**
  `\begin{ejerciciobox}[Ejercicio Propuesto 5: Entrelazamiento Cuántico y Traza Parcial (PD3 P5)]`
  `\textbf{Nivel: Examen / Avanzado}\\`
- **Texto después:**
  `\begin{ejerciciobox}[Ejercicio Propuesto 5: Entrelazamiento Cuántico y Traza Parcial]`
  `\textbf{Nivel: Avanzado}\\`
- **Motivo:** Eliminar «(PD3 P5)» y neutralizar nivel a «Avanzado» (Parte A, Puntos 12 y 13).

### 6. Anexo B (Formulario Maestro — Referencia y CCOC con Espín)
- **Ubicación:** Línea ~76 y Tabla 2 en `sections/07_anexo_demostraciones.tex`.
- **Texto antes:**
  `...el Cuadro~\ref{tab:formulario_maestro}...`
  `\textbf{CCOC} & $\{\hat{H}, \hat{L}^2, \hat{L}_z\}$ (orbital; con espín, $\{\hat{H}, \hat{L}^2, \hat{L}_z, \hat{S}_z\}$)...`
- **Texto después:**
  `...la Tabla~\ref{tab:formulario_maestro}...`
  `\textbf{CCOC} & $\{\hat{H}, \hat{L}^2, \hat{L}_z\}$ (orbital; con espín, $\{\hat{H}, \hat{L}^2, \hat{L}_z, \hat{S}^2, \hat{S}_z\}$) & Base ortonormal común $\ket{n, \ell, m_\ell}$ (orbital) o $\ket{n, \ell, m_\ell, s, m_s}$ en átomos hidrogenoides ($\hat{S}^2$ es constante trivial para $s=1/2$). \\`
- **Motivo:** Unificar «Tabla» vía `\ref` (Parte D, D1) y estandarizar la tupla del CCOC con espín aclarando la trivialidad escalar de $\hat{S}^2$ para $s=1/2$ (Parte D, D3).

### 7. Anexo C (Solución C.4 — Definición de $\xi$)
- **Ubicación:** Solución C.4 en `sections/07_anexo_demostraciones.tex`.
- **Texto antes:** `\item Evaluando el valor propio de $\hat{H}_{SO} = \frac{\xi}{2}(\hat{J}^2 - \hat{L}^2 - \hat{S}^2)$ sobre el estado acoplado...`
- **Texto después:** `\item Evaluando el valor propio de $\hat{H}_{SO} = \frac{\xi}{2}(\hat{J}^2 - \hat{L}^2 - \hat{S}^2)$ (donde $\xi \equiv \ev{\xi(r)}_{2p}$ es el valor esperado radial de la función de acoplamiento espín-órbita de la Sección~\ref{subsec:separacion_central_espacial}) sobre el estado acoplado...`
- **Motivo:** Clarificar rigurosamente la definición de $\xi$ en el solucionario (Parte C, C6).

### 8. Bibliografía (`refs.bib`)
- **Ubicación:** Entrada `@book{cohen}` en `refs.bib`.
- **Texto antes:**
  `publisher = {Wiley-Interscience}, address = {Paris, France}`
- **Texto después:**
  `publisher = {Wiley; Hermann}, address = {Nueva York; Par{\'i}s}`
- **Verificaciones adicionales:**
  - ISBN de Zettili [1]: `978-0-470-02672-4` verificado y confirmado (Wiley 2nd Ed.).
  - DOI de Sakurai [2]: `10.1017/9781108587280` verificado y confirmado (Cambridge University Press 3rd Ed.).
- **Motivo:** Actualizar ciudad y coedición de Cohen-Tannoudji Vol. 1 conforme a Parte D, D5.

### Para el Agente 5:
- Ningún pendiente o conflicto en Capítulo 6, Anexos o Bibliografía.
