#!/usr/bin/env python3
"""
Script: validate_report.py
Descripción: Validador de calidad y cumplimiento de directrices para informes de laboratorio en LaTeX.
Comprueba sintaxis matemática, macros de siunitx, subíndices en unidades, argumentos de qtyrange,
caracteres unicode, consistencia de labels/refs, citas en bibtex, formato de tablas (booktabs + resizebox)
y estándares del repositorio UNI Ciencias.

Uso:
    python validate_report.py --lab lab01
    python validate_report.py --all
"""

import argparse
import re
import sys
from pathlib import Path

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
if hasattr(sys.stderr, 'reconfigure'):
    sys.stderr.reconfigure(encoding='utf-8', errors='replace')

class ReportValidator:
    def __init__(self, lab_dir: Path):
        self.lab_dir = lab_dir
        self.tex_files = list(lab_dir.glob("sections/*.tex")) + [lab_dir / "main.tex"]
        self.bib_file = lab_dir / "refs.bib"
        self.main_file = lab_dir / "main.tex"
        self.errors = []
        self.warnings = []

    def log_error(self, file_path: Path, line_no: int, msg: str):
        self.errors.append(f"[ERROR] {file_path.name}:{line_no} -> {msg}")

    def log_warning(self, file_path: Path, line_no: int, msg: str):
        self.warnings.append(f"[WARN]  {file_path.name}:{line_no} -> {msg}")

    def validate_math_commas(self):
        """Verifica que no haya comas crudas en modo matemático como $2,46$ (excluyendo macros de siunitx y {,})."""
        for tf in self.tex_files:
            if not tf.exists():
                continue
            lines = tf.read_text(encoding="utf-8").splitlines()
            for idx, line in enumerate(lines, 1):
                cleaned = line.split("%")[0]
                
                # Extraer fragmentos en math mode inline $...$
                inline_math = re.findall(r'\$([^$]+)\$', cleaned)
                for math_chunk in inline_math:
                    # Remover llamadas a macros siunitx válidas que usan coma internamente
                    sanitized = re.sub(r'\\qtyrange\{[^}]*\}\{[^}]*\}\{[^}]*\}', '', math_chunk)
                    sanitized = re.sub(r'\\(qty|SI)\{[^}]*\}\{[^}]*\}', '', sanitized)
                    sanitized = re.sub(r'\\num\{[^}]*\}', '', sanitized)
                    sanitized = re.sub(r'\{,\}', '', sanitized)
                    # Buscar dígitos separados por coma cruda: \d+,\d+
                    if re.search(r'\d+,\d+', sanitized):
                        self.log_warning(tf, idx, f"Coma decimal cruda en modo matemático: '${math_chunk}$'. Use '{{,}}' o macros de siunitx ('\\num{{...}}', '\\qty{{...}}').")

    def validate_unicode_degrees(self):
        """Verifica que no se usen símbolos unicode sueltos de grados (° o ℃)."""
        for tf in self.tex_files:
            if not tf.exists():
                continue
            lines = tf.read_text(encoding="utf-8").splitlines()
            for idx, line in enumerate(lines, 1):
                cleaned = line.split("%")[0]
                if "°" in cleaned or "℃" in cleaned:
                    self.log_error(tf, idx, f"Símbolo unicode suelto ('°' o '℃'). Use '\\unit{{\\degree}}', '\\qty{{...}}{{\\celsius}}' o '^{{\\circ}}\\text{{C}}'.")

    def validate_siunitx_subscripts_and_ranges(self):
        """Verifica que no se usen subíndices de texto en macros \\qty y que \\qtyrange tenga solo 3 argumentos."""
        for tf in self.tex_files:
            if not tf.exists():
                continue
            lines = tf.read_text(encoding="utf-8").splitlines()
            for idx, line in enumerate(lines, 1):
                cleaned = line.split("%")[0]

                # Detectar \qty{...}{...}_{\text{...}} en texto fuera de math mode
                if re.search(r'\\qty\{[^}]*\}\{[^}]*\}_\s*\{', cleaned):
                    # Verificar si no está dentro de $...$ o \[...\]
                    self.log_error(tf, idx, r"Subíndice post-unidad '\qty{...}{...}_{...}' en modo texto causa error de LaTeX. Declare la unidad compuesta con '\DeclareSIUnit' (ej. '\voltpp', '\voltrms').")

                # Detectar \qtyrange con 4 argumentos como \qtyrange{1}{\milli\volt}{10}{\volt}
                range_matches = re.finditer(r'\\qtyrange\{([^}]*)\}\{([^}]*)\}', cleaned)
                for rm in range_matches:
                    start_pos = rm.start()
                    after_str = cleaned[rm.end():]
                    # Si el primer argumento o segundo argumento contiene comandos LaTeX de unidades
                    arg1, arg2 = rm.group(1), rm.group(2)
                    if '\\' in arg1 or '\\' in arg2:
                        self.log_error(tf, idx, f"Argumento inválido en '\\qtyrange{{{arg1}}}{{{arg2}}}'. '\\qtyrange' solo acepta números en los primeros 2 argumentos: '\\qtyrange{{val1}}{{val2}}{{unidad}}'.")

    def validate_booktabs_and_tables(self):
        """Verifica que las tablas usen booktabs, nunca \\hline y usen \\resizebox si tienen 4+ columnas."""
        for tf in self.tex_files:
            if not tf.exists():
                continue
            content = tf.read_text(encoding="utf-8")
            lines = content.splitlines()

            for idx, line in enumerate(lines, 1):
                cleaned = line.split("%")[0]
                if r"\hline" in cleaned:
                    self.log_error(tf, idx, r"Uso prohibido de '\hline'. Utilice '\toprule', '\midrule' o '\bottomrule' de booktabs.")

            # Buscar tablas completas para verificar resizebox en 4+ columnas
            table_blocks = re.findall(r'\\begin\{table\}.*?\\end\{table\}', content, re.DOTALL)
            for tb in table_blocks:
                tabular_spec = re.search(r'\\begin\{tabular\}\s*\{([^}]+)\}', tb)
                if tabular_spec:
                    spec = tabular_spec.group(1)
                    # Contar columnas (l, r, c, p, m, b, X)
                    col_count = len(re.findall(r'[lrcpmbX]', spec))
                    if col_count >= 4 and r'\resizebox' not in tb:
                        self.log_warning(tf, 0, f"Tabla con {col_count} columnas sin '\\resizebox{{\\linewidth}}{{!}}{{% ... %}}'. Podría desbordar el margen horizontal (Overfull \\hbox).")

    def validate_labels_and_refs(self):
        """Comprueba unicidad de labels y resolución de todas las referencias cruzadas."""
        labels = set()
        refs = []

        label_pattern = re.compile(r'\\label\{([^}]+)\}')
        ref_pattern = re.compile(r'\\(eq|sec|tab|fig)?ref\{([^}]+)\}')

        for tf in self.tex_files:
            if not tf.exists():
                continue
            lines = tf.read_text(encoding="utf-8").splitlines()
            for idx, line in enumerate(lines, 1):
                cleaned = line.split("%")[0]
                for l in label_pattern.findall(cleaned):
                    if l in labels:
                        self.log_error(tf, idx, f"Label duplicado: '{l}'")
                    else:
                        labels.add(l)

                for _, r in ref_pattern.findall(cleaned):
                    refs.append((tf, idx, r))

        for tf, idx, r in refs:
            if r not in labels:
                self.log_error(tf, idx, f"Referencia rota '\\ref{{{r}}}' o '\\eqref{{{r}}}'. No existe el label correspondiente.")

    def validate_citations(self):
        """Comprueba que todas las citas \\cite{clave} existan en refs.bib."""
        if not self.bib_file.exists():
            self.log_error(self.bib_file, 0, "No se encontró el archivo refs.bib.")
            return

        bib_content = self.bib_file.read_text(encoding="utf-8")
        bib_keys = set(re.findall(r'@\w+\s*\{\s*([^,]+),', bib_content))

        cite_pattern = re.compile(r'\\cite\{([^}]+)\}')
        for tf in self.tex_files:
            if not tf.exists():
                continue
            lines = tf.read_text(encoding="utf-8").splitlines()
            for idx, line in enumerate(lines, 1):
                cleaned = line.split("%")[0]
                for c_group in cite_pattern.findall(cleaned):
                    for key in c_group.split(","):
                        key = key.strip()
                        if key and key not in bib_keys:
                            self.log_error(tf, idx, f"Cita no encontrada en refs.bib: '\\cite{{{key}}}'")

    def validate_materials_figure_sizes(self):
        """Verifica que las figuras de 05_materiales tengan el tamaño estándar."""
        mat_file = self.lab_dir / "sections" / "05_materiales.tex"
        if not mat_file.exists():
            return
        lines = mat_file.read_text(encoding="utf-8").splitlines()
        inc_pattern = re.compile(r'\\includegraphics\[(.*?)\]')
        for idx, line in enumerate(lines, 1):
            cleaned = line.split("%")[0]
            for m in inc_pattern.findall(cleaned):
                if "width=0.50\\linewidth" not in m or "height=5.5cm" not in m:
                    self.log_warning(mat_file, idx, f"Dimensiones no estándar en material: [{m}]. Estándar: [width=0.50\\linewidth, height=5.5cm]")

    def validate_math_headings(self):
        """Verifica que las expresiones matemáticas en encabezados usen \\texorpdfstring."""
        heading_pattern = re.compile(r'\\(section|subsection|subsubsection)\{([^}]+)\}')
        for tf in self.tex_files:
            if not tf.exists():
                continue
            lines = tf.read_text(encoding="utf-8").splitlines()
            for idx, line in enumerate(lines, 1):
                cleaned = line.split("%")[0]
                for _, title in heading_pattern.findall(cleaned):
                    if "$" in title and r"\texorpdfstring" not in title:
                        self.log_warning(tf, idx, f"Modo matemático en título sin '\\texorpdfstring': '{title}'. Podría generar avisos en marcadores PDF.")

    def validate_markdown_syntax(self):
        """Verifica que no se haya filtrado sintaxis de Markdown (**negrita**, *cursiva*, ## Encabezado) en archivos .tex."""
        for tf in self.tex_files:
            if not tf.exists():
                continue
            lines = tf.read_text(encoding="utf-8").splitlines()
            for idx, line in enumerate(lines, 1):
                cleaned = line.split("%")[0]
                if re.search(r'\*\*[^*]+\*\*', cleaned):
                    self.log_error(tf, idx, "Sintaxis de Markdown detectada ('**texto**'). Use '\\textbf{texto}' en LaTeX.")
                if re.search(r'^\s*#{1,6}\s+', cleaned):
                    self.log_error(tf, idx, "Encabezado de Markdown detectado ('# Título'). Use '\\section{...}', '\\subsection{...}' en LaTeX.")

    def validate_display_math_delimiters(self):
        """Advierte sobre el uso de '$$ ... $$' en lugar de '\\[ ... \\]' o entornos 'equation'."""
        for tf in self.tex_files:
            if not tf.exists():
                continue
            content = tf.read_text(encoding="utf-8")
            if "$$" in content:
                # Contar apariciones de $$
                matches = [i for i, line in enumerate(content.splitlines(), 1) if "$$" in line.split("%")[0]]
                for line_no in matches:
                    self.log_warning(tf, line_no, "Uso de '$$ ... $$' (primitiva de TeX). Se recomienda usar '\\[ ... \\]' o '\\begin{equation*}'.")

    def validate_display_math_commas(self):
        """Verifica que no haya comas crudas en entornos matemáticos en bloque (equation, align, \\[...\\])."""
        for tf in self.tex_files:
            if not tf.exists():
                continue
            content = tf.read_text(encoding="utf-8")
            # Buscar bloques de display math
            display_blocks = re.findall(r'(\\begin\{(equation|align)\*?\}.*?\\end\{\2\*?\}|\\\[.*?\\\])', content, re.DOTALL)
            for block_tuple in display_blocks:
                block = block_tuple[0] if isinstance(block_tuple, tuple) else block_tuple
                # Remover comentarios de cada línea
                cleaned_block = "\n".join([line.split("%")[0] for line in block.splitlines()])
                # Remover macros siunitx y {,}
                sanitized = re.sub(r'\\qtyrange\{[^}]*\}\{[^}]*\}\{[^}]*\}', '', cleaned_block)
                sanitized = re.sub(r'\\(qty|SI)\{[^}]*\}\{[^}]*\}', '', sanitized)
                sanitized = re.sub(r'\\num\{[^}]*\}', '', sanitized)
                sanitized = re.sub(r'\{,\}', '', sanitized)
                if re.search(r'\d+,\d+', sanitized):
                    self.log_warning(tf, 0, "Coma decimal cruda '\\d+,\\d+' en ecuación matemática en bloque. Use '{{,}}' o '\\qty{{...}}{{...}}'.")

    def validate_orphan_labels(self):
        """Advierte si figuras o tablas con \\label{fig:...} o \\label{tab:...} no son referenciadas en el texto (excluyendo fig:mat_ que ilustran bloques de materiales)."""
        labels = {}
        all_text = ""
        for tf in self.tex_files:
            if not tf.exists():
                continue
            content = tf.read_text(encoding="utf-8")
            all_text += "\n" + content
            for match in re.finditer(r'\\label\{(fig:[^}]+|tab:[^}]+)\}', content):
                label_name = match.group(1)
                # Omitir figuras de bloques de materiales individuales
                if label_name.startswith("fig:mat_"):
                    continue
                labels[label_name] = tf

        for label_name, tf in labels.items():
            ref_pattern = rf'\\(eq|sec|tab|fig)?ref\{{{re.escape(label_name)}\}}'
            if not re.search(ref_pattern, all_text):
                self.log_warning(tf, 0, f"Etiqueta huérfana '\\label{{{label_name}}}'. Nunca es citada en el informe con '\\ref{{{label_name}}}'.")

    def validate_section_10_closing(self):
        """Verifica que la sección 10 (Gráficas) contenga el párrafo de transición a la sección 11."""
        grap_file = self.lab_dir / "sections" / "10_graficas.tex"
        if not grap_file.exists():
            return
        content = grap_file.read_text(encoding="utf-8")
        if r"\ref{sec:analisis_graficas}" not in content and "analisis_graficas" not in content:
            self.log_warning(grap_file, 0, "La Sección 10 no contiene el párrafo de cierre y enlace hacia la Sección 11 ('\\ref{sec:analisis_graficas}').")

    def validate_common_physics_typos(self):
        """Verifica que no existan errores léxicos físicos comunes (ej. deflactaba, rotación afín en Lissajous)."""
        typos = {
            r'\bdeflactab\w*': "Uso de 'deflactar' (término económico). Use 'deflectar' o 'desviar'.",
            r'\brotaci[oó]n af[ií]n\b': "En figuras de Lissajous con CH2 INVERT, se trata de una 'reflexión especular respecto al eje horizontal' y no de una 'rotación afín'."
        }
        for tf in self.tex_files:
            if not tf.exists():
                continue
            lines = tf.read_text(encoding="utf-8").splitlines()
            for idx, line in enumerate(lines, 1):
                cleaned = line.split("%")[0]
                for pattern, msg in typos.items():
                    if re.search(pattern, cleaned, re.IGNORECASE):
                        self.log_error(tf, idx, msg)

    def run(self) -> bool:
        print(f"=== Validando {self.lab_dir.name} ===")
        self.validate_unicode_degrees()
        self.validate_math_commas()
        self.validate_display_math_commas()
        self.validate_display_math_delimiters()
        self.validate_markdown_syntax()
        self.validate_common_physics_typos()
        self.validate_siunitx_subscripts_and_ranges()
        self.validate_booktabs_and_tables()
        self.validate_labels_and_refs()
        self.validate_orphan_labels()
        self.validate_citations()
        self.validate_materials_figure_sizes()
        self.validate_math_headings()
        self.validate_section_10_closing()

        for w in self.warnings:
            print(w)
        for e in self.errors:
            print(e)

        if not self.errors and not self.warnings:
            print(f"[OK] {self.lab_dir.name}: Todo cumple al 100% con los estándares y directrices.")
            return True
        elif not self.errors:
            print(f"[OK con advertencias] {self.lab_dir.name}: 0 errores, {len(self.warnings)} advertencia(s).")
            return True
        else:
            print(f"[FALLO] {self.lab_dir.name}: {len(self.errors)} error(es), {len(self.warnings)} advertencia(s).")
            return False

def main():
    parser = argparse.ArgumentParser(description="Validador de directrices de informes LaTeX.")
    parser.add_argument("--lab", type=str, help="Carpeta del laboratorio a validar (ej. lab01 o lab05)")
    parser.add_argument("--semester", type=int, default=None, help="Número de semestre (ej. 2 o 3)")
    parser.add_argument("--all", action="store_true", help="Validar todos los laboratorios existentes")

    args = parser.parse_args()
    base_dir = Path(__file__).resolve().parents[4]

    labs_to_check = []
    if args.all or not args.lab:
        if args.semester:
            sem_pattern = f"semestre-{args.semester:02d}/lab*"
            labs_to_check = sorted([d for d in base_dir.glob(sem_pattern) if d.is_dir()])
        else:
            labs_to_check = sorted([d for d in base_dir.glob("semestre-*/lab*") if d.is_dir()] + [d for d in base_dir.glob("lab*") if d.is_dir()])
    elif args.lab:
        lab_name = args.lab if args.lab.startswith("lab") else f"lab{int(args.lab):02d}"
        if args.semester:
            target = base_dir / f"semestre-{args.semester:02d}" / lab_name
        else:
            target = base_dir / lab_name
            if not target.exists():
                matches = list(base_dir.glob(f"semestre-*/{lab_name}"))
                if matches:
                    target = matches[0]

        if not target.exists():
            print(f"No existe el directorio de laboratorio: {target}")
            sys.exit(1)
        labs_to_check = [target]

    overall_success = True
    for l in labs_to_check:
        v = ReportValidator(l)
        if not v.run():
            overall_success = False
        print()

    if not overall_success:
        sys.exit(1)

if __name__ == "__main__":
    main()
