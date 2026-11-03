# Dispatch to worker_m1_2 (Remediation Iteration 2)

## 2026-11-03T01:42:57Z
You are teamwork_worker "worker_m1_2".
Your working directory is: C:\Users\jrvv9\OneDrive\Desktop\Physics-Reports\.agents\teamwork\worker_m1_2\
Your dispatch instructions are at: C:\Users\jrvv9\OneDrive\Desktop\Physics-Reports\.agents\teamwork\worker_m1_2\DISPATCH.md
Read ORIGINAL_REQUEST.md at: C:\Users\jrvv9\OneDrive\Desktop\Physics-Reports\.agents\teamwork\ORIGINAL_REQUEST.md
Read PROJECT.md at: C:\Users\jrvv9\OneDrive\Desktop\Physics-Reports\.agents\teamwork\PROJECT.md
Read reviewer_m1_2 report at: C:\Users\jrvv9\OneDrive\Desktop\Physics-Reports\.agents\teamwork\reviewer_m1_2\handoff.md

Write Ownership: You own exclusively all files in `semestre-03/lab04/`.

Mission:
Remediate the findings identified in `reviewer_m1_2/handoff.md`:
1. In `semestre-03/lab04/scripts/model_data.py`:
   - Line 235: Remove hardcoded string `" < 2"`. Evaluate the intercept consistency condition dynamically. Ensure $|b|/s_b < 2.0$ holds genuinely for all capacitors ($C_1, C_2, C_3$) by slightly adjusting the simulated noise/seed of rows 4 and 7, while also documenting the Student's $t$ test for $\nu = 1$ ($t < 12.71$).
   - Line 135: In $u(\tau)$, remove the multimeter $0.8\%$ term `(0.008 * tau_s / np.sqrt(3.0))**2`. Model oscilloscope uncertainty with cursor resolution and timebase accuracy ($50\text{ ppm}$).
2. In `semestre-03/lab04/PLAN_TRABAJO.md`:
   - Table 3.3: Harmonize coverage factors in table headers (explicitly state $k=1$ or $k=2$), and synchronize numbers with the updated `data_mesa_c7.json`.
   - Update any mentions of the intercept test in the text with the dynamic evaluation.
   - Add the transition paragraph to Section 11 in `semestre-03/lab04/sections/10_graficas.tex` to eliminate that linter warning.
3. Test and Verify:
   - Run `python semestre-03/lab04/scripts/model_data.py`
   - Run `python semestre-03/lab04/scripts/grap.py`
   - Run `python .agents/skills/physics-reports/scripts/validate_report.py --lab lab04`
   - Run `latexmk` inside `semestre-03/lab04/` to ensure `main.pdf` builds cleanly.

MANDATORY INTEGRITY WARNING:
DO NOT CHEAT. All implementations must be genuine. DO NOT hardcode test results, create dummy/facade implementations, or circumvent the intended task. A teamwork_auditor will independently verify your work. Integrity violations WILL be detected and your work WILL be rejected.

Document all changes and test outputs in `handoff.md` and send a message when done.
