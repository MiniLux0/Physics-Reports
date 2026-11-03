# CAMBIOS_a1.md — Agente 1 (Capítulos 1 y 2)

### 1. Sección 1.2 (Introducción)
- **Ubicación:** Línea ~54 de `sections/01_introduccion.tex`.
- **Texto antes:**
  `El presente documento constituye una guía rigurosa, exhaustiva y pedagógica de la primera gran unidad de la cátedra de Mecánica Cuántica avanzada. Nuestro propósito es desmitificar cada paso algebraico presentado en la pizarra, evitando los habituales \enquote{saltos de fe} matemáticos...`
- **Texto después:**
  `El presente documento constituye una guía rigurosa, exhaustiva y pedagógica de la primera unidad de un curso de Mecánica Cuántica I. Nuestro propósito es desmitificar cada paso algebraico, evitando los habituales \enquote{saltos de fe} matemáticos...`
- **Motivo:** Eliminar marcas de procedencia académica («cátedra», «pizarra») conforme a Parte A, Punto 3.

### 2. Sección 1.3 (Objetivos de Aprendizaje)
- **Ubicación:** Línea ~58 de `sections/01_introduccion.tex`.
- **Texto antes:** `Al culminar el estudio de este cuaderno de cátedra, el estudiante será capaz de:`
- **Texto después:** `Al culminar el estudio de este cuaderno, el estudiante será capaz de:`
- **Motivo:** Neutralizar referencia a «cátedra» (Parte A, Punto 4).

### 3. Sección 1.4 (Tabla 1)
- **Ubicación:** Tabla 1, fila de Sección 2, en `sections/01_introduccion.tex`.
- **Texto antes:** `...Teorema 2.3 (Diagonalización simultánea y ejemplo $3\times 3$ PD3 P3)...`
- **Texto después:** `...Teorema 2.3 (Diagonalización simultánea y ejemplo $3\times 3$)...`
- **Motivo:** Eliminar etiqueta de práctica de aula «PD3 P3» (Parte A, Punto 9).

### 4. Sección 1.4 (Referencia a Tabla 1)
- **Ubicación:** Línea ~69 de `sections/01_introduccion.tex`.
- **Texto antes:** `...tal como se esquematiza en el Cuadro~\ref{tab:hoja_ruta}.`
- **Texto después:** `...tal como se esquematiza en la Tabla~\ref{tab:hoja_ruta}.`
- **Motivo:** Consistencia de referencia cruzada con `es-tabla` de Babel (Parte D, D1).

### 5. Sección 2.5.3 (Operador Desviación)
- **Ubicación:** Línea ~244 de `sections/02_espacio_hilbert_dirac.tex`.
- **Texto antes:** `...(frecuentemente omitido en la notación rápida de clase, pero implícito en todo cálculo).`
- **Texto después:** `...(frecuentemente omitido en la notación abreviada, pero implícito en todo cálculo).`
- **Motivo:** Eliminar referencia informal a «clase» (Parte A, Punto 7).

### 6. Sección 2.7 (Teorema 2.2)
- **Ubicación:** Título y caja de Teorema 2.2 en `sections/02_espacio_hilbert_dirac.tex`.
- **Texto antes:** `\subsection{Teorema Espectral y Completitud (Teorema 2.2 de Cátedra)}` y `\begin{teoremabox}[Teorema 2.2 de Cátedra: ...]`
- **Texto después:** `\subsection{Teorema Espectral y Completitud (Teorema 2.2)}` y `\begin{teoremabox}[Teorema 2.2: ...]`
- **Motivo:** Eliminar «de Cátedra» en títulos y cajas (Parte A, Punto 5).

### 7. Sección 2.7 (Demostración de Teorema 2.2 — Inducción y Gram-Schmidt)
- **Ubicación:** Tras la Ec. (80) [ortogonalidad], al final de la demostración de Teorema 2.2.
- **Texto antes:** (No existía paso 3 explícito de inducción).
- **Texto después:**
  ```latex
  \textit{3. Completitud y diagonalización (inducción sobre la dimensión):}\\
  Por el teorema fundamental del álgebra, el polinomio característico de $\hat{A}$ posee al menos una raíz en $\mathbb{C}$, garantizando la existencia de un primer autovector normalizado $\ket{\phi_1}$ con autovalor real $a_1$. Sea $W = \mathrm{span}\{\ket{\phi_1}\}$ y $W^\perp$ su complemento ortogonal en $\mathcal{H}$. Para todo $\ket{\psi} \in W^\perp$, se cumple $\braket{\phi_1}{\hat{A}\psi} = \matrixel{\phi_1}{\hat{A}}{\psi} = \braket{\hat{A}\phi_1}{\psi} = a_1\braket{\phi_1}{\psi} = 0$, lo que demuestra que el subespacio $W^\perp$ de dimensión $N-1$ es invariante bajo $\hat{A}$. Por hipótesis inductiva sobre la dimensión, la restricción de $\hat{A}$ a $W^\perp$ es hermítica y admite una base ortonormal de autovectores. Si un autovalor $a_n$ posee multiplicidad geométrica $g_n > 1$ (subespacio propio degenerado $E_{a_n}$), el procedimiento de ortonormalización de Gram--Schmidt permite elegir siempre una base ortonormal interna para $E_{a_n}$. La unión de dichas bases conforma una base ortonormal completa de todo el espacio $\mathcal{H}$, demostrando la relación de clausura $\sum_{n=1}^N \ket{\phi_n}\bra{\phi_n} = \hat{I}$ y la diagonalizabilidad de $\hat{A}$.
  ```
- **Motivo:** Completar el rigor matemático probando completitud por inducción sobre la dimensión e invariancia del complemento ortogonal, y especificando Gram-Schmidt en degeneración (Parte C, C1).

### 8. Sección 2.8 (Teorema 2.3)
- **Ubicación:** Título y caja de Teorema 2.3 en `sections/02_espacio_hilbert_dirac.tex`.
- **Texto antes:** `\subsection{Conmutación de Observables y Diagonalización Simultánea (Teorema 2.3 de Cátedra)}` y `\begin{teoremabox}[Teorema 2.3 de Cátedra: ...]`
- **Texto después:** `\subsection{Conmutación de Observables y Diagonalización Simultánea (Teorema 2.3)}` y `\begin{teoremabox}[Teorema 2.3: ...]`
- **Motivo:** Eliminar «de Cátedra» en títulos y cajas (Parte A, Punto 5).

### 9. Sección 2.8 (Demostración de Teorema 2.3 — Implicación Inversa y Redacción)
- **Ubicación:** Línea ~418 de `sections/02_espacio_hilbert_dirac.tex`.
- **Texto antes:**
  `Para comprender a fondo este teorema y prepararnos para resolver cualquier problema de examen, debemos distinguir con absoluto rigor didáctico los dos escenarios posibles...`
- **Texto después:**
  ```latex
  \textbf{Demostración de la Condición Necesaria ($\Leftarrow$):}\\
  Si suponemos que existe una base ortonormal completa común $\{\ket{n}\}$ tal que $\hat{A}\ket{n} = a_n\ket{n}$ y $\hat{B}\ket{n} = b_n\ket{n}$ para todo $n$, entonces:
  \begin{equation}
      [\hat{A}, \hat{B}]\ket{n} = (\hat{A}\hat{B} - \hat{B}\hat{A})\ket{n} = (a_n b_n - b_n a_n)\ket{n} = 0.
      \label{a1-eq:comm_necessary}
  \end{equation}
  Como los autovalores escalares conmutan ($a_n b_n = b_n a_n$) y $\{\ket{n}\}$ es una base completa que genera todo $\mathcal{H}$, el operador $[\hat{A}, \hat{B}]$ anula cualquier combinación lineal $\ket{\psi} = \sum_n c_n\ket{n}$, concluyéndose idénticamente que $[\hat{A}, \hat{B}] = 0$.

  \textbf{Demostración de la Condición Suficiente ($\Rightarrow$):}\\
  Para probar que $[\hat{A}, \hat{B}] = 0$ implica la existencia de una base común y prepararnos para resolver problemas con operadores compatibles, debemos distinguir con absoluto rigor didáctico los dos escenarios posibles: el caso sin degeneración y el caso con degeneración.
  ```
- **Motivo:** Probar la implicación recíproca ($\Leftarrow$) en Teorema 2.3 (Parte C, C2) y sustituir la referencia a «problema de examen» por «problemas con operadores compatibles» (Parte A, Punto 6).

### 10. Sección 2.8.3 (Ejemplo Matricial Guiado)
- **Ubicación:** Subsección 2.8.3 y caja en `sections/02_espacio_hilbert_dirac.tex`.
- **Texto antes:**
  `\subsubsection{Ejemplo Matricial Guiado: Diagonalización Simultánea con Degeneración (Problema 3 de Práctica Dirigida 3)}`
  `Para consolidar la técnica operativa de examen que pide la cátedra, desarrollemos paso a paso el problema canónico de la Práctica Dirigida N° 3.`
  `\textbf{Enunciado (PD3 Problema 3):}`
- **Texto después:**
  `\subsubsection{Ejemplo Matricial Guiado: Diagonalización Simultánea con Degeneración}`
  `Para consolidar la técnica de diagonalización simultánea, desarrollemos paso a paso un problema canónico.`
  `\textbf{Enunciado:}`
- **Motivo:** Eliminar referencias a «Problema 3 de Práctica Dirigida 3», «examen que pide la cátedra» y «PD3» (Parte A, Punto 8).

### Para el Agente 5:
- Ninguna colisión o dependencia cruzada pendiente en Capítulos 1 y 2.
