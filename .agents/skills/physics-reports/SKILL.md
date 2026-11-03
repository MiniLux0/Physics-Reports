---
name: physics-reports
description: >-
  Expert runbook and toolkit for generating, structuring, calculating, validating,
  and compiling high-quality laboratory physics reports (Física II CF1B2 - Sección A,
  Facultad de Ciencias UNI) using LaTeX (pdflatex + biber + latexmk) and Python.
---

# Physics Reports Generation Skill (UNI Ciencias — Física II)

Guía operacional completa para la creación, redacción, análisis de datos, validación cruzada y compilación de informes de laboratorio de Física II (CF1B2) de la Universidad Nacional de Ingeniería.

---

## 1. Flujo de Trabajo Operativo Integral

```text
[1. Inicialización]  ---> [2. Procesamiento de Datos] ---> [3. Generación de Gráficas (300 DPI)]
         |                                                                   |
         v                                                                   v
[4. Redacción LaTeX (01-13)] ---> [5. Auditoría 13 Agentes] ---> [6. Validación Linter] ---> [7. Compilación latexmk]
```

---

## 2. Paso a Paso

### Paso 1: Inicialización del Nuevo Laboratorio
Ejecutar el script automatizado para crear la estructura de carpetas a partir de `template/`:

```powershell
# Para el tercer semestre (semestre-03)
python .agents/skills/physics-reports/scripts/new_lab.py --semester 3 --lab 1 --title "<Título>" --date "Lima, DD de mes de 2026" --teacher "<Docente>"
```

Esto configurará:
* `semestre-03/labNN/main.tex` con los metadatos y macros de unidades SI requeridas.
* `semestre-03/labNN/.latexmkrc` listo para compilación limpia con carpeta auxiliar `out/`.
* Directorios `Figures/`, `scripts/` y `sections/` (01 a 13).

### Paso 2: Análisis Físico y Tratamiento Matemático
1. Consultar [Guía de Propagación de Incertidumbres](./references/error_propagation.md).
2. Calcular magnitudes directas e indirectas, derivadas parciales y sumas en cuadratura.
3. Evaluar la regresión por mínimos cuadrados (OLS) con errores estándar ($s_m, s_b$, $R^2$) e intervalos de confianza al 95\% ($k=2$).
4. Evaluar el error relativo porcentual respecto a la literatura de referencia (\cite{serway}, \cite{halliday}), garantizando $E_r \le 10\%$ (idealmente $< 1\%$).

### Paso 3: Generación de Gráficas Científicas
1. Escribir o actualizar el script en `labNN/scripts/grap.py` siguiendo la [Guía de Gráficas en Python](./references/python_plotting.md).
2. Ejecutar el script:
   ```powershell
   python semestre-XX/labNN/scripts/grap.py
   ```
3. Verificar que las imágenes resultantes se guarden en `labNN/Figures/` en formato `.png` a 300 DPI (`bbox_inches='tight'`) y con formato de coma decimal en los ejes (`FuncFormatter`).

### Paso 4: Redacción de las Secciones LaTeX (01 a 13)
Seguir estrictamente la estructura detallada en [Guía de Secciones (01 a 13)](./references/sections_guide.md) y las normas de [Estilo y Convenciones LaTeX](./references/latex_guidelines.md):

* **01 Introducción:** Contexto micro $\to$ macro, magnitudes SI y literatura base (\cite{serway}, \cite{halliday}).
* **02 Resumen:** Síntesis cuantitativa con resultados $\pm$ incertidumbres, parámetros OLS y errores relativos.
* **03 Objetivos:** Objetivo general y específicos enumerados.
* **04 Fundamento Teórico:** Modelos físico-matemáticos, deducciones analíticas y ecuaciones numeradas con `\texorpdfstring` en encabezados.
* **05 Materiales y Equipos:** Bloques por instrumento con imágenes estandarizadas (`width=0.50\linewidth, height=5.5cm`) y tabla metrológica de tolerancias.
* **06 Procedimiento Experimental:** Enumeración cronológica con continuidad numérica (`\setcounter{enumi}{...}`) y registro digital en USB.
* **07 Resultados Experimentales:** Tablas `booktabs` envueltas en `\resizebox{\linewidth}{!}{% ... %}`, parámetros constantes y datos crudos.
* **08 Análisis Experimental:** Análisis puramente cualitativo de tendencias, dispersión y variables dominantes; hipótesis físicas tentativas.
* **09 Tratamiento de Datos:** Sustitución numérica paso a paso, propagación analítica en cuadratura y resultados finales.
* **10 Gráficas:** Figuras `[H]` con `width=0.85\linewidth`, captions exhaustivos con citas al script/librerías y párrafo de cierre de transición hacia la Sección 11.
* **11 Análisis de Gráficas:** Evaluación cuantitativa de pendientes, verificación de intercepto ($|b|/s_b < 1$), análisis de residuos y factores de forma.
* **12 Obs / Sug / Conclusiones:** Tres subsecciones independientes: Observaciones (fuentes de error), Sugerencias (mejoras viables) y Conclusiones (cuantitativas, respondiendo a objetivos).
* **13 Anexos:** Anexo A (demostraciones matemáticas), Anexo B (propagación con derivadas parciales y `\boxed{...}`) y Anexo C (cuestionario resuelto + hoja de datos escaneada).

### Paso 5: Auditoría Cruzada Multidisciplinar (13 Subagentes)
Para garantizar coherencia total, ausencia de contradicciones y riguroso cumplimiento de estándares en informes complejos:
- Desplegar 13 subagentes especializados en paralelo, asignando a cada uno una sección específica (`01_introduccion.tex` a `13_anexos.tex`).
- Cada subagente valida la consistencia cruzada de valores numéricos, incertidumbres, citas y sintaxis LaTeX.

### Paso 6: Validación Automática (Linter)
Ejecutar el validador de calidad para detectar inconsistencias antes de compilar:

```powershell
# Validar un laboratorio específico
python .agents/skills/physics-reports/scripts/validate_report.py --lab lab01

# Validar todos los laboratorios del repositorio
python .agents/skills/physics-reports/scripts/validate_report.py --all
```

El validador comprueba 14 directrices críticas:
1. Ausencia de comas decimales crudas en modo matemático (`$2,46$`).
2. Ausencia de caracteres unicode sueltos de temperatura (`°C` / `°`).
3. Cumplimiento de `booktabs` (prohibición de `\hline`) y presencia de `\resizebox` en tablas de 4+ columnas.
4. Sintaxis de `siunitx` (sin subíndices de texto post-unidad en modo texto y `\qtyrange` con argumentos válidos).
5. Integridad y unicidad de etiquetas (`\label{}`) y llamadas cruzadas (`\ref{}`, `\eqref{}`).
6. Existencia de todas las citas (`\cite{}`) en `refs.bib`.
7. Dimensiones estándar de figuras de materiales (`width=0.50\linewidth, height=5.5cm`).
8. Uso de `\texorpdfstring` en encabezados con matemáticas.
9. Prohibición estricta de sintaxis Markdown (`**negrita**`, `# Títulos`) en archivos `.tex`.
10. Detección y reemplazo de delimitadores primitivos `$$ ... $$` por `\[ ... \]`.
11. Detección de etiquetas huérfanas (figuras o tablas declaradas pero no referenciadas en el texto).
12. Presencia del párrafo de transición en la Sección 10 enlazando hacia la Sección 11.
13. Verificación de terminología física rigurosa (ej. *deflectar* vs *deflactar*, *reflexión* vs *rotación* en Lissajous).

### Paso 7: Compilación Oficial con `latexmk`
Compilar el informe desde dentro del directorio del laboratorio:

```powershell
latexmk
```

* **Regla de Oro:** NUNCA ejecutar `pdflatex` directamente — siempre usar `latexmk`.
* `latexmk` gestiona automáticamente múltiples pasadas con `pdflatex` y `biber`, colocando los auxiliares en `out/` y copiando el PDF final a la raíz del laboratorio.
* **Recuperación limpia:** Si una compilación previa fue abortada y corrompió el `.aux`, ejecutar `latexmk -C; latexmk`.
* **Limpieza:** Para limpiar archivos auxiliares manteniendo el PDF final: `latexmk -c`.

---

## 3. Recursos y Referencias Rápidas

* [Guía Detallada de Secciones (01–13)](./references/sections_guide.md)
* [Guía de Convenciones y Paquetes LaTeX](./references/latex_guidelines.md)
* [Estándares de Gráficas Python](./references/python_plotting.md)
* [Metodología de Propagación de Errores](./references/error_propagation.md)
* [Script de Inicialización de Laboratorios](./scripts/new_lab.py)
* [Validador de Informes](./scripts/validate_report.py)
