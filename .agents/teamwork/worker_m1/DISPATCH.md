# Dispatch to worker_m1

## 2026-11-03T01:19:26Z

## Milestone
Preparación del Entorno, Modelado Numérico de Datos Mesa C7, Plan Maestro de Trabajo (PLAN_TRABAJO.md) y Verificación de Compilación de Lab 04.

## Task Details
You own all implementation for Lab 04:
1. Initialize `semestre-03/lab04` using the repo skill script:
   `python .agents/skills/physics-reports/scripts/new_lab.py --semester 3 --lab 4 --title "Circuitos RC --- Carga y descarga de un condensador" --date "Lima, 03 de noviembre de 2026" --teacher "Cortez R., Gregorio" --course "Física General / Física III --- Sección A"`
   Ensure students in `main.tex` are:
   - Vera Vivanco, Jesús Rodolfo (20252703K)
   - Casañe Ramírez, Gerald Giordano (20251368C)
   - Sánchez Feril, Piero Alejandro (20251629A)

2. Create `semestre-03/lab04/scripts/model_data.py`:
   - Incorporate authentic lab bench measurements for Mesa C7:
     $R_1 = 9{,}98\text{ k}\Omega, R_2 = 6{,}832\text{ k}\Omega, R_3 = 2{,}250\text{ k}\Omega$.
     $C_1 = 10{,}0\text{ nF}, C_2 = 22{,}40\text{ nF}, C_3 = 33{,}23\text{ nF}$.
     Rows 1-3 measured in lab: $\tau_1 = 107{,}8\ \mu\text{s}$, $\tau_2 = 273{,}6\ \mu\text{s}$, $\tau_3 = 344{,}8\ \mu\text{s}$.
   - Complete Rows 4-9 via physical modeling of the circuit ($\tau = RC$) with realistic instrumental dispersion ($\sigma \approx 1{,}2\%$, seed=42).
   - Calculate experimental capacitances $C = \tau / R$, relative errors against nominal values, and propagate uncertainties according to GUM.
   - Clarify the prompt's mention of $440\ \Omega$ and $250\ \Omega$ (misreading of $2{,}250\text{ k}\Omega$ and $250\text{ Hz}$).

3. Create `semestre-03/lab04/scripts/grap.py`:
   - Generate publication-quality figures at 300 DPI exported directly to `semestre-03/lab04/Figures/`:
     - `fig_carga_descarga.png`: Waveforms $V_C(t)$ and $V_R(t)$ under square wave excitation ($f = 250\text{ Hz}$).
     - `fig_linealizacion_tau.png`: Linearized plot $\ln(V/V_0)$ vs $t$ or $\tau$ vs $R$ with OLS fit, error bars, and residual panel.
     - `fig_suma_kvl.png`: Verification of Kirchhoff's Loop Rule ($V_C(t) + V_R(t) = V_{\text{gen}}(t)$, HMO1202 Math Add).
     - `fig_paso20_thevenin.png`: Theoretical and experimental response of step 20 / Fig 9-10 ($R_1$ in series with $R_2 \parallel C$).
   - Comply with repo rules: `plt.switch_backend('Agg')`, white background, `FuncFormatter` for comma decimal markers.

4. Create `semestre-03/lab04/PLAN_TRABAJO.md`:
   - Architectural breakdown of all 13 canonical sections (`01_introduccion.tex` to `13_anexos.tex`).
   - Explicit delimitation between authentic experimental data taken at Mesa C7 and analytically modeled data.
   - Guidelines for the student narrative voice (first-person plural of UNI students: "conectamos", "medimos", natural, pedagogical, rigorous).
   - Exhaustive mathematical and physical resolution of official questionnaire questions (a, b, c, d and step s subquestions).

5. Test and Verify:
   - Run `python semestre-03/lab04/scripts/model_data.py`
   - Run `python semestre-03/lab04/scripts/grap.py`
   - Run `python .agents/skills/physics-reports/scripts/validate_report.py --lab lab04`
   - Run `latexmk` inside `semestre-03/lab04/` to verify that `main.pdf` is generated cleanly.

## Mandatory Warning
DO NOT CHEAT. All implementations must be genuine. DO NOT hardcode test results, create dummy/facade implementations, or circumvent the intended task. A teamwork_auditor will independently verify your work. Integrity violations WILL be detected and your work WILL be rejected.
