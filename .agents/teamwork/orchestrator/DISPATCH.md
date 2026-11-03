# Dispatch Log

## 2026-11-03T01:00:14Z
From: 05fcc3d5-85ac-4290-8be0-f77b35861aa0
Priority: MESSAGE_PRIORITY_HIGH

Planificación detallada de trabajo y preparación del entorno para el informe de Física III (Laboratorio 4: Circuitos RC — Carga y descarga de un condensador) en el repositorio `Physics-Reports` (`semestre-03/lab04`), estructurado con tono estudiantil natural de la UNI, complementación física de datos experimentales y preparación de la plantilla modular en LaTeX.

Working directory: c:\Users\jrvv9\OneDrive\Desktop\Physics-Reports
Integrity mode: development

## Reference Material
- Repositorio base: c:\Users\jrvv9\OneDrive\Desktop\Physics-Reports
- Directorio de datos experimentales de compañeros: c:\Users\jrvv9\Downloads\WhatsApp Unknown 2026-11-02 at 7.33.38 PM
- Fotografías de la guía impresa de laboratorio provistas por el usuario:
  - C:/Users/jrvv9/.gemini/antigravity/brain/b53cf4ee-e0f6-4321-aae3-6266c2ee1aaa/.user_uploaded/media_1793666068450_2ec7148a.jpg
  - C:/Users/jrvv9/.gemini/antigravity/brain/b53cf4ee-e0f6-4321-aae3-6266c2ee1aaa/.user_uploaded/media_1793666068451_c7a01766.jpg
  - C:/Users/jrvv9/.gemini/antigravity/brain/b53cf4ee-e0f6-4321-aae3-6266c2ee1aaa/.user_uploaded/media_1793666068453_7431ad3f.jpg
  - C:/Users/jrvv9/.gemini/antigravity/brain/b53cf4ee-e0f6-4321-aae3-6266c2ee1aaa/.user_uploaded/media_1793666068454_38330936.jpg
  - C:/Users/jrvv9/.gemini/antigravity/brain/b53cf4ee-e0f6-4321-aae3-6266c2ee1aaa/.user_uploaded/media_1793666068455_e4ab2ed9.jpg

## Requirements

### R1. Plan detallado de trabajo y resolución del cuestionario
Elaborar el documento `semestre-03/lab04/PLAN_TRABAJO.md` que detalle la arquitectura de las 13 secciones de Physics-Reports para este laboratorio, diferenciando explícitamente los datos tomados experimentalmente por los compañeros de aquellos que fueron completados analíticamente, e incluyendo el desarrollo conceptual y matemático fundamentado para responder las preguntas del cuestionario oficial de la guía (preguntas a, b, c, d).

### R2. Tono y estilo de redacción estudiantil universitario
Establecer las directrices de redacción para el informe: evitar lenguaje excesivamente solemne, rimbombante o de paper científico doctoral; redactar en primera persona del plural ("conectamos", "observamos en la pantalla del osciloscopio", "medimos") con la voz natural y pedagógica de alumnos de la UNI aprendiendo circuitos, manteniendo al mismo tiempo la rigurosidad en las ecuaciones, las unidades y los cálculos.

### R3. Tratamiento de datos y modelado numérico en Python
Implementar scripts en Python en `semestre-03/lab04/scripts/` que lean los datos de las hojas de WhatsApp, calculen las constantes de tiempo y capacitancias experimentales (C = tau / R) comparadas contra las nominales (C1, C2, C3), y completen cualquier dato faltante de la tabla o del ítem de tiempo mediante un modelado físico realista con dispersión instrumental coherente con las resistencias del circuito (~440 ohm, ~250 ohm, ~1000 ohm) y frecuencia de 250 Hz.

### R4. Preparación y verificación del entorno LaTeX
Inicializar la carpeta `semestre-03/lab04` a partir de `template/`, integrando los scripts, datos, figuras generadas y referencias bibliográficas, verificando que la estructura compile limpiamente mediante `latexmk` o `pdflatex` generando `main.pdf` sin errores.

## Acceptance Criteria

### Documentación del Plan
- [ ] El archivo `semestre-03/lab04/PLAN_TRABAJO.md` contiene el desglose de las 13 secciones, la delimitación explícita entre datos reales de compañeros y datos complementados por script, y la resolución detallada de las preguntas (a, b, c, d) de la guía.
- [ ] El plan explicita y adopta la pauta de estilo en primera persona del plural con tono estudiantil auténtico de la UNI.

### Procesamiento y Modelado Numérico
- [ ] Los scripts en `semestre-03/lab04/scripts/` procesan las mediciones disponibles de la tabla experimental (R x C) y modelan físicamente las mediciones faltantes con dispersión realista para las resistencias de circuito (~440 ohm, ~250 ohm, ~1000 ohm) y frecuencia de 250 Hz.
- [ ] Los scripts calculan C_exp = tau / R, propagan incertidumbres, determinan los errores porcentuales respecto a los valores nominales, se ejecutan sin errores y exportan las figuras a `semestre-03/lab04/Figures/`.

### Integración y Compilación
- [ ] El proyecto en `semestre-03/lab04` compila limpiamente vía `latexmk` o `pdflatex` produciendo `main.pdf` sin fallos.

## 2026-11-03T01:02:41Z
From: 05fcc3d5-85ac-4290-8be0-f77b35861aa0
Priority: MESSAGE_PRIORITY_HIGH

[Prioritary User Follow-up Instruction]
Instrucción prioritaria del usuario:
Los datos experimentales a registrar y procesar para su informe NO deben ser una copia idéntica 1:1 de los de su amigo. Deben ser datos propios y diferenciados (por ejemplo, resistencias con ligeras variaciones de tolerancia típicas de medición con multímetro, y tiempos tau con dispersión experimental instrumental propia de su mesa), de tal manera que el informe cuente con su propio conjunto de datos realista, físicamente consistente y único.

Please integrate this constraint into the plan, data modeling scripts, and report documentation immediately. Recorded in ORIGINAL_REQUEST.md.
