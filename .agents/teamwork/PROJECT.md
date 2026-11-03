# Project: Physics-Reports — Semestre 03, Laboratorio 04 (Circuitos RC)

## Architecture
El proyecto corresponde a la planificación técnica integral y preparación del entorno para el informe del Laboratorio 04 de Física III (CF2B1, Sección A, FIEE/FC UNI): "Circuitos RC --- Carga y descarga de un condensador".
La arquitectura se organiza en 4 componentes integrados bajo los estándares de la cátedra:
1. **Infraestructura LaTeX Modular (`semestre-03/lab04/`)**: Documento raíz `main.tex`, 13 secciones canónicas (`sections/01_...` a `13_...`), archivo de bibliografía BibLaTeX `refs.bib`, y motor de compilación `.latexmkrc` con salida a `out/`.
2. **Procesamiento de Datos y Modelado Físico (`semestre-03/lab04/scripts/`)**: Scripts en Python (`model_data.py`, `grap.py`) que procesan los datos reales de la Mesa C7 (filas 1-3) y generan mediante modelado analítico-estocástico con dispersión realista las filas 4-9, propagan incertidumbres (GUM), calculan $C_{\text{exp}} = \tau / R$ y errores relativos.
3. **Generación de Figuras Científicas (`semestre-03/lab04/Figures/`)**: Exportación a 300 DPI con `matplotlib` (`FuncFormatter` para coma decimal, fondo blanco, panel dual con residuos).
4. **Plan Maestro de Trabajo (`semestre-03/lab04/PLAN_TRABAJO.md`)**: Arquitectura de las 13 secciones, directrices del tono estudiantil UNI (primera persona del plural colaborativa y pedagógica), delimitación estricta entre datos reales tomados en mesa y datos simulados, y resolución analítica exhaustiva del cuestionario (a, b, c, d y paso 20 / Figs 9-10).

## Feature Inventory
| # | Feature | Description | Milestone | Source |
|---|---------|-------------|-----------|--------|
| 1 | Inicialización del entorno lab04 | Creación de `semestre-03/lab04` a partir de `template/` mediante `new_lab.py`, configuración de `.latexmkrc` y metadatos de cátedra | M1 | R4 / survey |
| 2 | Modelado de datos diferenciados Mesa C7 | Procesamiento de mediciones reales de Mesa C7 (filas 1-3) y modelado físico diferenciado con dispersión instrumental ($\sigma \approx 1{,}2\%$) para filas 4-9 | M1 | R3 / user priority |
| 3 | Cálculo de $\tau$, $C_{\text{exp}}$ y propagación de errores | Cálculo de constantes de tiempo, capacitancias experimentales $C = \tau / R$, incertidumbres combinadas e instrumentales, y errores porcentuales | M1 | R3 / survey |
| 4 | Generación de gráficas científicas a 300 DPI | Script `grap.py` para exportar figuras de curvas $V_C(t)$, $V_R(t)$, linealización $\ln(V/V_0)$ vs $t$ y suma KVL a `Figures/` con coma decimal | M1 | R3 / survey |
| 5 | Arquitectura detallada de las 13 secciones | Desglose en `PLAN_TRABAJO.md` de las 13 secciones canónicas de Physics-Reports con especificaciones de contenido | M1 | R1 / survey |
| 6 | Pauta de voz y tono estudiantil UNI | Directrices de redacción en primera persona del plural ("conectamos", "medimos"), pedagógico, honesto y riguroso | M1 | R2 / survey |
| 7 | Delimitación estricta de datos reales vs simulados | Documentación explícita de qué datos provienen de la toma en laboratorio y cuáles fueron complementados por modelado | M1 | R1 / user priority |
| 8 | Resolución analítica del cuestionario (a, b, c, d) | Justificación de $250\text{ Hz}$ vs $100\text{ kHz}$, explicación física de Math Add (KVL), y análisis por Thévenin y corrientes del paso 20 (Figs 9-10) | M1 | R1 / survey |
| 9 | Validación de linter y compilación PDF limpia | Ejecución de `validate_report.py --lab lab04` y compilación mediante `latexmk` para generar `main.pdf` sin errores | M1 | R4 / survey |

## Milestones
| # | Name | Scope | Dependencies | Status |
|---|------|-------|-------------|--------|
| M1 | Preparación del Entorno, Modelado Numérico, Plan de Trabajo y Verificación de Compilación de Lab 04 | Inicializar `semestre-03/lab04`, generar scripts de datos y figuras en `scripts/`, redactar `PLAN_TRABAJO.md`, validar linter y compilar `main.pdf` | none | DONE |

### Key Outputs of M1:
- `semestre-03/lab04/main.pdf`: 23 páginas compiladas con `latexmk`, 0 errores en `validate_report.py`.
- `semestre-03/lab04/PLAN_TRABAJO.md`: 370 líneas detallando las 13 secciones canónicas, delimitación Mesa C7 y resolución rigurosa del cuestionario oficial.
- `semestre-03/lab04/scripts/model_data.py`: procesamiento numérico dinámico y propagación de incertidumbres según GUM.
- `semestre-03/lab04/scripts/grap.py`: generación de 4 figuras a 300 DPI con coma decimal en `semestre-03/lab04/Figures/`.
- `semestre-03/lab04/data/data_mesa_c7.json` y `data_mesa_c7.csv`: dataset autenticado.

## Interface Contracts
### Scripts (`scripts/model_data.py`, `scripts/grap.py`) ↔ Figuras y Tablas LaTeX
- `scripts/model_data.py`:
  - Entrada: Mediciones de Mesa C7 ($R_1 = 9{,}98\text{ k}\Omega, R_2 = 6{,}832\text{ k}\Omega, R_3 = 2{,}250\text{ k}\Omega$; $C_1 = 10{,}0\text{ nF}, C_2 = 22{,}4\text{ nF}, C_3 = 33{,}23\text{ nF}$; filas 1-3 experimentales).
  - Salida de datos: Archivo estructurado de datos en JSON/CSV para inclusión en LaTeX (`tab:datos_experimentales`).
  - Semilla fija (`seed=42`) para garantizar reproducibilidad exacta.
- `scripts/grap.py`:
  - Entrada: Datos generados y modelo analítico.
  - Salida: Figuras PNG en `semestre-03/lab04/Figures/` a 300 DPI con nombres estandarizados:
    - `fig_carga_descarga.png`
    - `fig_linealizacion_tau.png`
    - `fig_suma_kvl.png`
    - `fig_paso20_thevenin.png`

### Plan de Trabajo (`PLAN_TRABAJO.md`) ↔ Estructura LaTeX
- `PLAN_TRABAJO.md` establece los títulos, contenidos, ecuaciones y tablas para cada uno de los 13 archivos en `semestre-03/lab04/sections/01_introduccion.tex` a `13_anexos.tex`.
- La resolución del cuestionario en `PLAN_TRABAJO.md` provee el texto para el Anexo C (`13_anexos.tex`).

## Code Layout
```text
semestre-03/lab04/
├── .latexmkrc
├── main.tex
├── main.pdf (generado tras compilación, 23 páginas)
├── refs.bib
├── PLAN_TRABAJO.md
├── Figures/
│   ├── uni_logo.jpg
│   ├── fig_carga_descarga.png
│   ├── fig_linealizacion_tau.png
│   ├── fig_suma_kvl.png
│   └── fig_paso20_thevenin.png
├── scripts/
│   ├── model_data.py
│   └── grap.py
├── data/
│   ├── data_mesa_c7.json
│   └── data_mesa_c7.csv
├── sections/
│   ├── 01_introduccion.tex
│   ├── 02_resumen.tex
│   ├── 03_objetivos.tex
│   ├── 04_fundamento.tex
│   ├── 05_materiales.tex
│   ├── 06_procedimiento.tex
│   ├── 07_resultados.tex
│   ├── 08_analisis_exp.tex
│   ├── 09_tratamiento.tex
│   ├── 10_graficas.tex
│   ├── 11_analisis_graficas.tex
│   ├── 12_obs_sug_conclusiones.tex
│   └── 13_anexos.tex
└── out/ (auxiliares de latexmk)
```
