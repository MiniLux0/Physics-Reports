# CAMBIOS_a2.md — Agente 2 (Capítulos 3 y 4)

### 1. Sección 3.1 (Cauchy–Schwarz — Caso de Igualdad)
- **Ubicación:** Línea ~55 de `sections/03_incertidumbre_robertson_schrodinger.tex`.
- **Texto antes:** `Queda formalmente demostrada la desigualdad de Cauchy--Schwarz sin recurrir a derivadas de funciones reales ni asumir que el producto interno sea real \cite{sakurai}.`
- **Texto después:** `Queda formalmente demostrada la desigualdad de Cauchy--Schwarz sin recurrir a derivadas de funciones reales ni asumir que el producto interno sea real \cite{sakurai}. Nótese que la igualdad en la Ec.~\eqref{eq:cauchy_schwarz} se alcanza si y solo si $\braket{\phi}{\phi} = 0 \iff \ket{\phi} = 0$, lo cual equivale a la dependencia lineal $\ket{u} = -\lambda\ket{v}$ entre ambos estados (con el escalar óptimo $\lambda = -\braket{v}{u}/\braket{v}{v}$).`
- **Motivo:** Especificar con rigor matemático las condiciones de saturación/igualdad en Cauchy–Schwarz (Parte C, C3).

### 2. Sección 3.5 (Reducción a Heisenberg)
- **Ubicación:** Título del recuadro alertabox en `sections/03_incertidumbre_robertson_schrodinger.tex`.
- **Texto antes:** `\begin{alertabox}[¿Por qué el profesor eliminó el término del anticonmutador en la pizarra?]`
- **Texto después:** `\begin{alertabox}[¿Por qué puede descartarse el término del anticonmutador?]`
- **Motivo:** Eliminar alusiones a «el profesor» y «la pizarra» en el recuadro metodológico (Parte A, Punto 10).

### 3. Sección 3.6 (Ejemplo Resuelto 2 — Covarianza Cuántica Explícita)
- **Ubicación:** Ecs. (124–125), final del Ejemplo Resuelto 2 en `sections/03_incertidumbre_robertson_schrodinger.tex`.
- **Texto antes:** Argumento heurístico de que un valor esperado de un operador hermítico no puede tener parte imaginaria no nula, concluyendo $\ev{\{\hat{x}, \hat{p}_x\}} = 0$.
- **Texto después:** Cálculo explícito riguroso:
  ```latex
  \ev{\hat{x}\hat{p}_x} = \frac{\iu\hbar}{\sigma^2}\ev{\hat{x}^2} = \frac{\iu\hbar}{2}, \qquad \ev{\hat{p}_x\hat{x}} = \ev{\hat{x}\hat{p}_x}^* = -\frac{\iu\hbar}{2},
  ```
  de donde $\ev{\{\hat{x}, \hat{p}_x\}} = \frac{\iu\hbar}{2} - \frac{\iu\hbar}{2} = 0 \implies \mathrm{Cov}(\hat{x}, \hat{p}_x) = 0$.
- **Motivo:** Reemplazar el argumento heurístico por una deducción analítica paso a paso verificada a mano (Parte C, C4).

### 4. Sección 4.2.1 (Funciones de Operadores y Conmutación)
- **Ubicación:** Ec. previa a (139), subsección 4.2.1 de `sections/04_funciones_operadores_hadamard_bch.tex`.
- **Texto antes:**
  ```latex
  Por el contrario, si los operadores \textbf{no conmutan} ($[\hat{A}, \hat{B}] \neq 0$), entonces en general $\hat{B}$ \textbf{no conmuta con la función del operador}:
  \begin{equation}
      [\hat{A}, \hat{B}] \neq 0 \implies [\hat{B}, F(\hat{A})] \neq 0.
  \end{equation}
  ```
- **Texto después:**
  ```latex
  Por el contrario, si los operadores \textbf{no conmutan} ($[\hat{A}, \hat{B}] \neq 0$), entonces en general $\hat{B}$ \textbf{no conmuta con la función del operador}:
  \begin{equation}
      [\hat{B}, F(\hat{A})] \neq 0 \quad (\text{en general}).
  \end{equation}
  (Cabe advertir que la implicación estricta $[\hat{A}, \hat{B}] \neq 0 \implies [\hat{B}, F(\hat{A})] \neq 0$ no es universal: por ejemplo, tomando las matrices de Pauli con $\hat{A} = \sigma_x$, $\hat{B} = \sigma_z$ y la función $F(z) = z^2$, se tiene $[\sigma_x, \sigma_z] = -2\iu\sigma_y \neq 0$, pero $F(\sigma_x) = \sigma_x^2 = \hat{I}$ conmuta idénticamente con $\sigma_z$).
  ```
- **Motivo:** Corregir falsedad matemática formal de la implicación condicional general e incorporar el contraejemplo estándar de Pauli (Parte B, B3).

### 5. Sección 4.5 (BCH Simplificado frente a General)
- **Ubicación:** Línea ~278 de `sections/04_funciones_operadores_hadamard_bch.tex`.
- **Texto antes:** `Como enfatizó el profesor en clase, \textbf{esto es falso}: la Ec.~\eqref{eq:bch_simplificada_recap}...`
- **Texto después:** `\textbf{Esto es falso}: la Ec.~\eqref{eq:bch_simplificada_recap}...`
- **Motivo:** Eliminar referencia a «el profesor en clase» (Parte A, Punto 11).

### 6. Sección 4.5 (Redacción de Geometría de Lie)
- **Ubicación:** Línea ~320 de `sections/04_funciones_operadores_hadamard_bch.tex`.
- **Texto antes:** `...resultante de la no conmutatividad geométrica de la esfera tridimensional.`
- **Texto después:** `...resultante de la no conmutatividad geométrica de las rotaciones en $\mathbb{R}^3$.`
- **Motivo:** Precisión en terminología de teoría de grupos de Lie (Parte D, D4).

### Para el Agente 5:
- Ningún pendiente o conflicto en Capítulos 3 y 4.
