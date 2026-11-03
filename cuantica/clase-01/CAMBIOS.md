# Registro Unificado de Modificaciones (CAMBIOS.md)
**Documento:** *Mecánica Cuántica I (CF3A1) – Fundamentos Operacionales, Álgebra de Conmutadores, Incertidumbre Generalizada y Momento Angular Tensorial*  
**Fecha:** 31 de octubre de 2026  
**Auditoría y Edición Técnica:** Orquestación en 5 Agentes Especializados

---

## 1. AGENTE 1 — Capítulos 1 y 2 (Introducción, Espacios de Hilbert, Dirac, Teoremas 2.2 y 2.3)

### 1.1 Sección 1.2: Eliminación de marcas de aula y procedencia (Parte A, Punto 3)
- **Ubicación:** `sections/01_introduccion.tex`, línea ~54.
- **Texto antes:** `El presente documento constituye una guía rigurosa, exhaustiva y pedagógica de la primera gran unidad de la cátedra de Mecánica Cuántica avanzada. Nuestro propósito es desmitificar cada paso algebraico presentado en la pizarra, evitando los habituales \enquote{saltos de fe} matemáticos...`
- **Texto después:** `El presente documento constituye una guía rigurosa, exhaustiva y pedagógica de la primera unidad de un curso de Mecánica Cuántica I. Nuestro propósito es desmitificar cada paso algebraico, evitando los habituales \enquote{saltos de fe} matemáticos...`
- **Motivo:** Neutralizar el tono a libro de texto autónomo, eliminando referencias a «la cátedra» y «la pizarra».

### 1.2 Sección 1.3: Objetivos de aprendizaje (Parte A, Punto 4)
- **Ubicación:** `sections/01_introduccion.tex`, línea ~58.
- **Texto antes:** `Al culminar el estudio de este cuaderno de cátedra, el estudiante será capaz de:`
- **Texto después:** `Al culminar el estudio de este cuaderno, el estudiante será capaz de:`
- **Motivo:** Eliminación de la palabra «cátedra».

### 1.3 Sección 1.4: Síntesis temática en Tabla 1 (Parte A, Punto 9; Parte D, D1)
- **Ubicación:** `sections/01_introduccion.tex`, líneas ~69, 81 y 89.
- **Texto antes:**
  - `...tal como se esquematiza en el Cuadro~\ref{tab:hoja_ruta}.`
  - `...Teorema 2.3 (Diagonalización simultánea y ejemplo $3\times 3$ PD3 P3)...`
  - `...y 5 ejercicios propuestos de nivel examen.`
- **Texto después:**
  - `...tal como se esquematiza en la Tabla~\ref{tab:hoja_ruta}.`
  - `...Teorema 2.3 (Diagonalización simultánea y ejemplo $3\times 3$)...`
  - `...y 5 ejercicios propuestos de nivel avanzado.`
- **Motivo:** Unificación de «Cuadro» a «Tabla» conforme a `es-tabla` de Babel y eliminación de códigos de aula («PD3 P3», «nivel examen»).

### 1.4 Sección 2.5.3: Operador Desviación (Parte A, Punto 7)
- **Ubicación:** `sections/02_espacio_hilbert_dirac.tex`, línea ~244.
- **Texto antes:** `...(frecuentemente omitido en la notación rápida de clase, pero implícito en todo cálculo).`
- **Texto después:** `...(frecuentemente omitido en la notación abreviada, pero implícito en todo cálculo).`
- **Motivo:** Sustitución de «notación rápida de clase» por «notación abreviada».

### 1.5 Sección 2.7: Título y entorno del Teorema 2.2 (Parte A, Punto 5)
- **Ubicación:** `sections/02_espacio_hilbert_dirac.tex`, líneas ~339 y 344.
- **Texto antes:** `\subsection{Teorema Espectral y Completitud (Teorema 2.2 de Cátedra)}` y `\begin{teoremabox}[Teorema 2.2 de Cátedra: ...]`
- **Texto después:** `\subsection{Teorema Espectral y Completitud (Teorema 2.2)}` y `\begin{teoremabox}[Teorema 2.2: ...]`
- **Motivo:** Eliminación de «de Cátedra» en encabezado y recuadro.

### 1.6 Sección 2.7: Demostración de completitud por inducción y Gram–Schmidt (Parte C, C1)
- **Ubicación:** `sections/02_espacio_hilbert_dirac.tex`, tras la demostración de ortogonalidad (línea ~404).
- **Texto antes:** No se incluía la prueba de clausura/diagonalización inductiva.
- **Texto después:** Se añadió el paso 3 riguroso:
  ```latex
  \textit{3. Completitud y diagonalización (inducción sobre la dimensión):}\\
  Por el teorema fundamental del álgebra, el polinomio característico de $\hat{A}$ posee al menos una raíz en $\mathbb{C}$, garantizando la existencia de un primer autovector normalizado $\ket{\phi_1}$ con autovalor real $a_1$. Sea $W = \mathrm{span}\{\ket{\phi_1}\}$ y $W^\perp$ su complemento ortogonal en $\mathcal{H}$. Para todo $\ket{\psi} \in W^\perp$, se cumple $\braket{\phi_1}{\hat{A}\psi} = \matrixel{\phi_1}{\hat{A}}{\psi} = \braket{\hat{A}\phi_1}{\psi} = a_1\braket{\phi_1}{\psi} = 0$, lo que demuestra que el subespacio $W^\perp$ de dimensión $N-1$ es invariante bajo $\hat{A}$. Por hipótesis inductiva sobre la dimensión, la restricción de $\hat{A}$ a $W^\perp$ es hermítica y admite una base ortonormal de autovectores. Si un autovalor $a_n$ posee multiplicidad geométrica $g_n > 1$ (subespacio propio degenerado $E_{a_n}$), el procedimiento de ortonormalización de Gram--Schmidt permite elegir siempre una base ortonormal interna para $E_{a_n}$. La unión de dichas bases conforma una base ortonormal completa de todo el espacio $\mathcal{H}$, demostrando la relación de clausura $\sum_{n=1}^N \ket{\phi_n}\bra{\phi_n} = \hat{I}$ y la diagonalizabilidad de $\hat{A}$.
  ```
- **Motivo:** Proporcionar la prueba completa de completitud espectral vía subespacios invariantes ortogonales e inducción dimensional finita, con ortonormalización de Gram–Schmidt en subespacios degenerados.

### 1.7 Sección 2.8: Teorema 2.3, Implicación Inversa y Redacción (Parte A, Puntos 5 y 6; Parte C, C2)
- **Ubicación:** `sections/02_espacio_hilbert_dirac.tex`, líneas ~406, 411 y 418.
- **Texto antes:**
  `\subsection{Conmutación de Observables y Diagonalización Simultánea (Teorema 2.3 de Cátedra)}`
  `\begin{teoremabox}[Teorema 2.3 de Cátedra: Operadores Compatibles y Base Común]`
  `Para comprender a fondo este teorema y prepararnos para resolver cualquier problema de examen...`
- **Texto después:**
  `\subsection{Conmutación de Observables y Diagonalización Simultánea (Teorema 2.3)}`
  `\begin{teoremabox}[Teorema 2.3: Operadores Compatibles y Base Común]`
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
- **Motivo:** Eliminar «de Cátedra» y «problema de examen», y añadir la deducción matemática formal en dos líneas del recíproco ($\Leftarrow$).

### 1.8 Sección 2.8.3: Ejemplo Matricial Guiado (Parte A, Punto 8)
- **Ubicación:** `sections/02_espacio_hilbert_dirac.tex`, líneas ~477–482.
- **Texto antes:**
  `\subsubsection{Ejemplo Matricial Guiado: Diagonalización Simultánea con Degeneración (Problema 3 de Práctica Dirigida 3)}`
  `Para consolidar la técnica operativa de examen que pide la cátedra, desarrollemos paso a paso el problema canónico de la Práctica Dirigida N° 3.`
  `\textbf{Enunciado (PD3 Problema 3):}`
- **Texto después:**
  `\subsubsection{Ejemplo Matricial Guiado: Diagonalización Simultánea con Degeneración}`
  `Para consolidar la técnica de diagonalización simultánea, desarrollemos paso a paso un problema canónico.`
  `\textbf{Enunciado:}`
- **Motivo:** Eliminación integral de marcas de aula («Práctica Dirigida 3», «pide la cátedra», «PD3»).

---

## 2. AGENTE 2 — Capítulos 3 y 4 (Incertidumbre, Funciones de Operadores, Hadamard, BCH)

### 2.1 Sección 3.1: Desigualdad de Cauchy–Schwarz (Parte C, C3)
- **Ubicación:** `sections/03_incertidumbre_robertson_schrodinger.tex`, línea ~55.
- **Texto antes:** `Queda formalmente demostrada la desigualdad de Cauchy--Schwarz sin recurrir a derivadas de funciones reales ni asumir que el producto interno sea real \cite{sakurai}.`
- **Texto después:** `Queda formalmente demostrada la desigualdad de Cauchy--Schwarz sin recurrir a derivadas de funciones reales ni asumir que el producto interno sea real \cite{sakurai}. Nótese que la igualdad en la Ec.~\eqref{eq:cauchy_schwarz} se alcanza si y solo si $\braket{\phi}{\phi} = 0 \iff \ket{\phi} = 0$, lo cual equivale a la dependencia lineal $\ket{u} = -\lambda\ket{v}$ entre ambos estados (con el escalar óptimo $\lambda = -\braket{v}{u}/\braket{v}{v}$).`
- **Motivo:** Formular rigurosamente la condición necesaria y suficiente de saturación de Cauchy–Schwarz.

### 2.2 Sección 3.5: Reducción a Heisenberg (Parte A, Punto 10)
- **Ubicación:** `sections/03_incertidumbre_robertson_schrodinger.tex`, línea ~180.
- **Texto antes:** `\begin{alertabox}[¿Por qué el profesor eliminó el término del anticonmutador en la pizarra?]`
- **Texto después:** `\begin{alertabox}[¿Por qué puede descartarse el término del anticonmutador?]`
- **Motivo:** Redacción estrictamente impersonal sin alusiones a «profesor» ni «pizarra».

### 2.3 Sección 3.6: Ejemplo Resuelto 2 — Covarianza Cuántica Explícita (Parte C, C4)
- **Ubicación:** `sections/03_incertidumbre_robertson_schrodinger.tex`, líneas ~259–267.
- **Texto antes:** Argumentación cualitativa sobre el carácter simultáneamente real e imaginario de la integral para justificar $\ev{\{\hat{x}, \hat{p}_x\}} = 0$.
- **Texto después:** Cálculo analítico exacto paso a paso:
  ```latex
  \begin{align}
      \ev{\hat{x}\hat{p}_x} &= \int_{-\infty}^\infty \psi^*(x)\hat{x}\left(\iu\hbar\frac{x}{\sigma^2}\psi(x)\right)\dif x = \frac{\iu\hbar}{\sigma^2}\int_{-\infty}^\infty x^2 |\psi(x)|^2\,\dif x \nonumber\\
      &= \frac{\iu\hbar}{\sigma^2}\ev{\hat{x}^2} = \frac{\iu\hbar}{\sigma^2}\left(\frac{\sigma^2}{2}\right) = \frac{\iu\hbar}{2}.
      \label{a2-eq:xp_exp}
  \end{align}
  Puesto que $\hat{x}$ y $\hat{p}_x$ son operadores hermíticos, $(\hat{x}\hat{p}_x)\adj = \hat{p}_x\hat{x}$, de modo que el valor esperado del producto inverso es su complejo conjugado:
  \begin{equation}
      \ev{\hat{p}_x\hat{x}} = \ev{\hat{x}\hat{p}_x}^* = \left(\frac{\iu\hbar}{2}\right)^* = -\frac{\iu\hbar}{2}.
      \label{a2-eq:px_exp}
  \end{equation}
  Por consiguiente, el valor esperado del anticonmutador se anula de forma exacta:
  \begin{equation}
      \ev{\{\hat{x}, \hat{p}_x\}} = \ev{\hat{x}\hat{p}_x + \hat{p}_x\hat{x}} = \ev{\hat{x}\hat{p}_x} + \ev{\hat{p}_x\hat{x}} = \frac{\iu\hbar}{2} - \frac{\iu\hbar}{2} = 0 \implies \mathrm{Cov}(\hat{x}, \hat{p}_x) = 0.
  \end{equation}
  ```
- **Motivo:** Demostración algebraica rigurosa y verificada a mano que descarta la justificación heurística previa y evita cualquier desbordamiento tipográfico.

### 2.4 Sección 4.2.1: Conmutación con Funciones de Operadores (Parte B, B3)
- **Ubicación:** `sections/04_funciones_operadores_hadamard_bch.tex`, líneas ~93–96.
- **Texto antes:**
  ```latex
  \begin{equation}
      [\hat{A}, \hat{B}] \neq 0 \implies [\hat{B}, F(\hat{A})] \neq 0.
  \end{equation}
  ```
- **Texto después:**
  ```latex
  \begin{equation}
      [\hat{B}, F(\hat{A})] \neq 0 \quad (\text{en general}).
  \end{equation}
  (Cabe advertir que la implicación estricta $[\hat{A}, \hat{B}] \neq 0 \implies [\hat{B}, F(\hat{A})] \neq 0$ no es universal: por ejemplo, tomando las matrices de Pauli con $\hat{A} = \sigma_x$, $\hat{B} = \sigma_z$ y la función $F(z) = z^2$, se tiene $[\sigma_x, \sigma_z] = -2\iu\sigma_y \neq 0$, pero $F(\sigma_x) = \sigma_x^2 = \hat{I}$ conmuta idénticamente con $\sigma_z$).
  ```
- **Motivo:** Enmendar la falsedad lógica de la implicación condicional e ilustrar el contraejemplo canónico de álgebra de espín.

### 2.5 Sección 4.5: Condición de validez de BCH y Geometría de $\mathrm{SO}(3)$ (Parte A, Punto 11; Parte D, D4)
- **Ubicación:** `sections/04_funciones_operadores_hadamard_bch.tex`, líneas ~278 y 320.
- **Texto antes:**
  - `Como enfatizó el profesor en clase, \textbf{esto es falso}: la Ec.~\eqref{eq:bch_simplificada_recap}...`
  - `...resultante de la no conmutatividad geométrica de la esfera tridimensional.`
- **Texto después:**
  - `\textbf{Esto es falso}: la Ec.~\eqref{eq:bch_simplificada_recap}...`
  - `...resultante de la no conmutatividad geométrica de las rotaciones en $\mathbb{R}^3$.`
- **Motivo:** Eliminar mención al docente en clase y utilizar la terminología geométrica estándar de la teoría de grupos de Lie.

---

## 3. AGENTE 3 — Capítulo 5 (Momento Angular, Álgebra de Lie, CCOC, Acoplamiento)

### 3.1 Sección 5.6.1: Modelo Vectorial y Estados Fundamentales (Parte D, D4)
- **Ubicación:** `sections/05_momento_angular_tensorial_ccoc.tex`, línea ~317.
- **Texto antes:** `Solo para el estado monoestable con $\ell = 0$ (donde $\hat{\vec{L}}\ket{0, 0} = \vec{0}$)...`
- **Texto después:** `Solo para el estado $\ell = 0$ (donde $\hat{\vec{L}}\ket{0, 0} = \vec{0}$)...`
- **Motivo:** Retirar el adjetivo «monoestable» (inaplicable a autoestados cuánticos del momento angular).

### 3.2 Sección 5.6.3: CCOC con Espín y Corrección Ortográfica (Parte D, D3)
- **Ubicación:** `sections/05_momento_angular_tensorial_ccoc.tex`, líneas ~341, 354 y 365.
- **Detalle:** Se confirmó la correcta acentuación (`esféricamente`), la tupla completa $\text{CCOC}_{\text{completo}} = \{\hat{H}, \hat{L}^2, \hat{L}_z, \hat{S}^2, \hat{S}_z\}$ y la nota aclaratoria respecto a la naturaleza escalar proporcional a la identidad de $\hat{S}^2 = \frac{3}{4}\hbar^2\hat{I}$ para electrones.

### 3.3 Sección 5.8: Corrección en Matriz $\hat{L}_y\hat{L}_x$ para $\ell=1$ (Parte B, B1)
- **Ubicación:** `sections/05_momento_angular_tensorial_ccoc.tex`, Ec. (277) [línea ~486].
- **Texto antes:**
  ```latex
  \hat{L}_y\hat{L}_x = \frac{\hbar^2}{2}\begin{pmatrix} -\iu & 0 & -\iu \\ 0 & 0 & 0 \\ -\iu & 0 & \iu \end{pmatrix}.
  ```
- **Texto después:**
  ```latex
  \hat{L}_y\hat{L}_x = \frac{\hbar^2}{2}\begin{pmatrix} -\iu & 0 & -\iu \\ 0 & 0 & 0 \\ \iu & 0 & \iu \end{pmatrix}.
  ```
- **Motivo:** Corregir el signo de la entrada (3,1), cuyo valor algebraico exacto es $(\iu)(1) = +\iu$. Con esta corrección, la resta directa $\hat{L}_x\hat{L}_y - \hat{L}_y\hat{L}_x$ reproduce con exactitud milimétrica la matriz diagonal $\iu\hbar\hat{L}_z$.

### 3.4 Sección 5.9: Atribución de la Factorización de la Función de Onda (Parte C, C5)
- **Ubicación:** `sections/05_momento_angular_tensorial_ccoc.tex`, línea ~531.
- **Texto antes:** `Por el Teorema 2.3 de diagonalización simultánea, la función de onda espacial se factoriza exactamente por separación de variables:`
- **Texto después:** `El Teorema 2.3 garantiza la existencia de una base ortonormal común de autoestados simultáneos para el CCOC $\{\hat{H}, \hat{L}^2, \hat{L}_z\}$. Debido a la estructura diferencial del laplaciano en coordenadas esféricas (donde la parte angular coincide con $-\hat{L}^2/(\hbar^2 r^2)$), el método de separación de variables conduce de forma natural a la factorización espacial de las funciones de onda:`
- **Motivo:** Distinguir claramente la garantía abstracta de existencia de base espectral simultánea (Teorema 2.3) del método diferencial de separación de variables inducido por la geometría esférica del laplaciano.

### 3.5 Sección 5.10.2: Conmutador de $\hat{J}^2$ con Componentes Polares (Parte C, C7)
- **Ubicación:** `sections/05_momento_angular_tensorial_ccoc.tex`, Ec. (296) [línea ~648].
- **Texto antes:**
  ```latex
  &= \boxed{2\iu\hbar\left(\hat{J}_{1x}\hat{J}_{2y} - \hat{J}_{1y}\hat{J}_{2x}\right) \neq 0}.
  ```
- **Texto después:**
  ```latex
  &= \boxed{2\iu\hbar\left(\hat{J}_{1x}\hat{J}_{2y} - \hat{J}_{1y}\hat{J}_{2x}\right) \neq 0 \quad (\text{en general})}.
  ```
- **Motivo:** Rigor operacional indicando que el conmutador es no nulo como operador genérico, evitando ambigüedades en subespacios donde la acción particular pudiera anularse.

### 3.6 Sección 5.10.6: Acción Bipartita en el Bloque $M=0$ (Parte B, B2)
- **Ubicación:** `sections/05_momento_angular_tensorial_ccoc.tex`, Ec. (316) [líneas ~714–717].
- **Texto antes:**
  `&= 2\hbar^2\ket{1, -1} + (\hbar\sqrt{2}\ket{0, -1})(\hbar\sqrt{2}\ket{0, 0}) = 2\hbar^2\ket{1, -1} + 2\hbar^2\ket{0, 0}.`
- **Texto después:**
  ```latex
  \begin{align}
      \hat{J}^2\ket{1, -1} &= \left(2\hbar^2 + 2\hbar^2 + 2\hbar^2(1)(-1)\right)\ket{1, -1} + \hat{L}_{1-}\hat{L}_{2+}\ket{1, -1} \nonumber\\
      &= 2\hbar^2\ket{1, -1} + (\hat{L}_{1-}\ket{1}_1) \otimes (\hat{L}_{2+}\ket{-1}_2) \nonumber\\
      &= 2\hbar^2\ket{1, -1} + (\hbar\sqrt{2}\ket{0}_1) \otimes (\hbar\sqrt{2}\ket{0}_2) = 2\hbar^2\ket{1, -1} + 2\hbar^2\ket{0, 0}.
  \end{align}
  ```
- **Motivo:** Notación rigurosa de operadores actuando en sus respectivos factores del producto tensorial $\mathcal{H}_1 \otimes \mathcal{H}_2$. Se revalidó a mano el bloque $3\times 3$ completo y la obtención de los autovalores $\lambda \in \{0, 2\hbar^2, 6\hbar^2\}$.

---

## 4. AGENTE 4 — Capítulo 6, Bibliografía y Anexos

### 4.1 Sección 6.1: Supresión de Etiquetas de Aula en Problemas 4 y 5 (Parte A, Punto 12)
- **Ubicación:** `sections/06_ejercicios_resueltos_y_propuestos.tex`, cajas de Problemas 4 y 5.
- **Texto antes:**
  - `\begin{ejemplobox}[Problema Resuelto 4: Efecto Zeeman Orbital y Precesión de Larmor Cuántica (PD3 P2)]`
  - `\begin{ejemplobox}[Problema Resuelto 5: Oscilador 2D Isótropo y Modos Circulares Cuánticos (PD3 P4)]`
- **Texto después:**
  - `\begin{ejemplobox}[Problema Resuelto 4: Efecto Zeeman Orbital y Precesión de Larmor Cuántica]`
  - `\begin{ejemplobox}[Problema Resuelto 5: Oscilador 2D Isótropo y Modos Circulares Cuánticos]`
- **Motivo:** Eliminación de los códigos de prácticas «(PD3 P2)» y «(PD3 P4)».

### 4.2 Sección 6.2: Neutralización de Dificultad y Etiquetas en Ejercicios Propuestos (Parte A, Puntos 12 y 13)
- **Ubicación:** `sections/06_ejercicios_resueltos_y_propuestos.tex`, líneas ~330, 389, 390, 414, 415.
- **Texto antes:**
  - `\subsection{Ejercicios Propuestos para Autoestudio (Nivel Examen / Zettili)}`
  - `\begin{ejerciciobox}[Ejercicio Propuesto 4: Estructura Fina y Desdoblamiento Espín-Órbita (PD3 P8)]`
  - `\textbf{Nivel: Examen / Intermedio-Avanzado}\\`
  - `\begin{ejerciciobox}[Ejercicio Propuesto 5: Entrelazamiento Cuántico y Traza Parcial (PD3 P5)]`
  - `\textbf{Nivel: Examen / Avanzado}\\`
- **Texto después:**
  - `\subsection{Ejercicios Propuestos para Autoestudio (Nivel Avanzado / Zettili)}`
  - `\begin{ejerciciobox}[Ejercicio Propuesto 4: Estructura Fina y Desdoblamiento Espín-Órbita]`
  - `\textbf{Nivel: Avanzado}\\`
  - `\begin{ejerciciobox}[Ejercicio Propuesto 5: Entrelazamiento Cuántico y Traza Parcial]`
  - `\textbf{Nivel: Avanzado}\\`
- **Motivo:** Supresión de códigos «PD3 P8», «PD3 P5» y de toda alusión a «Nivel Examen».

### 4.3 Sección 6.2.4 y Anexo C.4: Definición Física de la Constante $\xi$ (Parte C, C6)
- **Ubicación:** `sections/06_ejercicios_resueltos_y_propuestos.tex` (línea ~393) y `sections/07_anexo_demostraciones.tex` (línea ~225).
- **Texto antes:** `\hat{H}_{SO} = \xi(\hat{\vec{L}}\cdot\hat{\vec{S}}), \quad \xi > 0.` (sin contextualizar la constante $\xi$).
- **Texto después:** Se añadió la aclaración explícita:
  `donde la constante $\xi \equiv \ev{\xi(r)}_{2p}$ es el valor esperado radial de la función de acoplamiento espín-órbita $\xi(r)$ evaluada en el subespacio del nivel $2p$ (consistente con la Sección~\ref{subsec:acoplamiento_espin_orbita}).`
  Y correlativamente en la solución C.4:
  `Evaluando el valor propio de $\hat{H}_{SO} = \frac{\xi}{2}(\hat{J}^2 - \hat{L}^2 - \hat{S}^2)$ (donde $\xi \equiv \ev{\xi(r)}_{2p}$ es el valor esperado radial de la función de acoplamiento espín-órbita de la Sección~\ref{subsec:acoplamiento_espin_orbita}) sobre el estado acoplado...`
- **Motivo:** Unificar la notación de perturbación efectiva con la función radial $\xi(r)$ deducida en el Capítulo 5.

### 4.4 Anexo B: Formulario Maestro y CCOC con Espín (Parte D, D1 y D3)
- **Ubicación:** `sections/07_anexo_demostraciones.tex`, líneas ~76 y 126.
- **Texto antes:**
  - `...el Cuadro~\ref{tab:formulario_maestro}...`
  - `\textbf{CCOC} & $\{\hat{H}, \hat{L}^2, \hat{L}_z\}$ (orbital; con espín, $\{\hat{H}, \hat{L}^2, \hat{L}_z, \hat{S}_z\}$)...`
- **Texto después:**
  - `...la Tabla~\ref{tab:formulario_maestro}...`
  - `\textbf{CCOC} & $\{\hat{H}, \hat{L}^2, \hat{L}_z\}$ (orbital; con espín, $\{\hat{H}, \hat{L}^2, \hat{L}_z, \hat{S}^2, \hat{S}_z\}$) & Base ortonormal común $\ket{n, \ell, m_\ell}$ (orbital) o $\ket{n, \ell, m_\ell, s, m_s}$ en átomos hidrogenoides ($\hat{S}^2$ es constante trivial para $s=1/2$). \\`
- **Motivo:** Coherencia de referencias con `Tabla` e inclusión de $\hat{S}^2$ en el CCOC con espín aclarando su trivialidad para $s=1/2$.

### 4.5 Bibliografía Canónica (`refs.bib`) (Parte D, D5)
- **Ubicación:** Entrada `@book{cohen}` en `refs.bib`.
- **Texto antes:** `publisher = {Wiley-Interscience}, address = {Paris, France}`
- **Texto después:** `publisher = {Wiley; Hermann}, address = {Nueva York; Par{\'i}s}`
- **Verificación adicional de identificadores:**
  - **Zettili [1]:** ISBN `978-0-470-02672-4` verificado y confirmado (edición estándar Wiley 2009).
  - **Sakurai & Napolitano [2]:** DOI `10.1017/9781108587280` verificado y confirmado (Cambridge University Press 2020).
- **Motivo:** Normalización de coedición histórica (Wiley/Hermann) para la obra de Cohen-Tannoudji.

---

## 5. AGENTE 5 — Integrador y Verificador

### 5.1 Portada y Encabezados Globales (Parte A, Puntos 1 y 2)
- **Ubicación:** `main.tex`, líneas ~4, 168 y 266.
- **Texto antes:**
  - Línea 4: `%%  Cuaderno de Cátedra: Mecánica Cuántica I`
  - Línea 168: `\fancyhead[R]{\small\textit{Clase 01 --- Fundamentos y Momento Angular}}`
  - Línea 266: `\textit{Basado en las lecciones de cátedra y referencias canónicas (\cite{zettili, sakurai, cohen, dirac, ballentine}).}`
- **Texto después:**
  - Línea 4: `%%  Cuaderno: Mecánica Cuántica I`
  - Línea 168: `\fancyhead[R]{\small\textit{Fundamentos y Momento Angular}}`
  - Línea 266: `\textit{Basado en referencias canónicas (\cite{zettili, sakurai, cohen, dirac, ballentine}).}`
- **Motivo:** Supresión total de denominaciones de clase y lecciones de cátedra en el archivo maestro.

### 5.2 Figura 1: Hoja de Ruta Conceptual (Parte D, D2)
- **Ubicación:** `Figures/fig_mapa_dependencias.tex`, nodos (b) y (n).
- **Texto antes:**
  - Nodo (b): `\textbf{4. Hadamard y BCH}`
  - Nodo (n): `\textbf{4.5 Simetr\'ias y Noether}`
- **Texto después:**
  - Nodo (b): `\textbf{4.4--4.5 BCH}`
  - Nodo (n): `\textbf{4.7 Simetr\'ias y Noether}`
- **Motivo:** Sincronización exacta con las secciones reales del Capítulo 4.

### 5.3 Búsqueda Global de Residuos (Grep)
- Se ejecutó un escaneo insensible a mayúsculas con expresiones regulares sobre todos los archivos `.tex` y `.bib` para los términos: `profesor`, `pizarra`, `cátedra`, `catedra`, `clase`, `en clase`, `práctica dirigida`, `practica dirigida`, `pd3`, `pide la`, `foto`, `apunte`, `nivel examen`, `teorema 2.2 de`, `teorema 2.3 de`.
- **Resultado:** **0 coincidencias** en todo el repositorio.

### 5.4 Control de Compilación y Calidad Tipográfica
- Se realizaron dos compilaciones completas con `latexmk` invocando `pdflatex` y `biber`.
- **Referencias indefinidas:** 0 (ningún `??` en el documento).
- **Overfull boxes:** Se eliminaron los overfull severos reportados en la auditoría (Ec. 65 con +62.7 pt y cadena en Ec. 124 con +3.06 pt). No se introdujo ningún overfull box nuevo.
- El PDF final generado [`main.pdf`](file:///C:/Users/jrvv9/OneDrive/Desktop/Physics-Reports/cuantica/clase-01/main.pdf) (84 páginas) se encuentra íntegro y sincronizado en la raíz del proyecto.

---

## 6. Pendientes / Ambiguos
- **Ninguno:** Todos los puntos solicitados de las Partes A, B, C y D fueron resueltos de manera concluyente y verificados analíticamente a mano.
