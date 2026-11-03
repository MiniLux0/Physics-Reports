#!/usr/bin/env python3
"""
Script: new_lab.py
Descripción: Inicializa una nueva carpeta de laboratorio (labNN) a partir de la plantilla `template/`.
Soporta asignación por semestre (semestre-01, semestre-02, etc.).

Uso:
    python new_lab.py --semester 2 --lab 1 --title "Osciloscopio como Instrumento de Medida" --date "Lima, 11 de septiembre de 2026" --teacher "Docente, N."
"""

import argparse
import os
import shutil
import re
import sys
from pathlib import Path

def setup_new_lab(semester_num: int, lab_num: int, title: str = "", date: str = "", teacher: str = "", course: str = "", base_dir: Path = None):
    if base_dir is None:
        base_dir = Path(__file__).resolve().parents[4]  # Repository root

    template_dir = base_dir / "template"
    if not template_dir.exists():
        print(f"[ERROR] No se encontró el directorio de plantilla en {template_dir}", file=sys.stderr)
        sys.exit(1)

    semester_folder_name = f"semestre-{semester_num:02d}"
    semester_dir = base_dir / semester_folder_name
    semester_dir.mkdir(exist_ok=True)

    lab_folder_name = f"lab{lab_num:02d}"
    target_dir = semester_dir / lab_folder_name

    if target_dir.exists():
        print(f"[ERROR] La carpeta {target_dir} ya existe. Abortando para evitar sobreescritura.", file=sys.stderr)
        sys.exit(1)

    print(f"[*] Creando {semester_folder_name}/{lab_folder_name} a partir de template/...")
    shutil.copytree(template_dir, target_dir)

    # Renombrar _latexmkrc a .latexmkrc si existe
    old_latexmkrc = target_dir / "_latexmkrc"
    new_latexmkrc = target_dir / ".latexmkrc"
    if old_latexmkrc.exists():
        if new_latexmkrc.exists():
            old_latexmkrc.unlink()
        else:
            old_latexmkrc.rename(new_latexmkrc)
        print("  -> Renombrado _latexmkrc a .latexmkrc")

    # Asegurar carpetas Figures y scripts
    figures_dir = target_dir / "Figures"
    scripts_dir = target_dir / "scripts"
    figures_dir.mkdir(exist_ok=True)
    scripts_dir.mkdir(exist_ok=True)

    # Copiar el logo de la UNI a Figures si no fue copiado de template/
    if not (figures_dir / "uni_logo.jpg").exists():
        uni_logo_src = template_dir / "Figures" / "uni_logo.jpg"
        if not uni_logo_src.exists():
            uni_logo_src = base_dir / "semestre-02" / "lab05" / "Figures" / "uni_logo.jpg"
        if not uni_logo_src.exists():
            uni_logo_src = base_dir / "semestre-02" / "lab04" / "Figures" / "uni_logo.jpg"
        if uni_logo_src.exists():
            shutil.copy(uni_logo_src, figures_dir / "uni_logo.jpg")
            print("  -> Copiado uni_logo.jpg a Figures/")

    # Modificar main.tex con los metadatos proporcionados
    main_tex = target_dir / "main.tex"
    if main_tex.exists():
        content = main_tex.read_text(encoding="utf-8")
        
        # Reemplazar número de lab
        content = re.sub(
            r'\\newcommand\{\\labnumero\}\{.*?\}',
            f'\\\\newcommand{{\\\\labnumero}}{{{lab_num}}}',
            content
        )
        
        if course:
            content = re.sub(
                r'\\newcommand\{\\labcurso\}\{.*?\}',
                f'\\\\newcommand{{\\\\labcurso}}{{{course}}}',
                content
            )
        if title:
            content = re.sub(
                r'\\newcommand\{\\labtitulo\}\{.*?\}',
                f'\\\\newcommand{{\\\\labtitulo}}{{{title}}}',
                content
            )
        if date:
            content = re.sub(
                r'\\newcommand\{\\labfecha\}\{.*?\}',
                f'\\\\newcommand{{\\\\labfecha}}{{{date}}}',
                content
            )
        if teacher:
            content = re.sub(
                r'\\newcommand\{\\labdocente\}\{.*?\}',
                f'\\\\newcommand{{\\\\labdocente}}{{{teacher}}}',
                content
            )

        main_tex.write_text(content, encoding="utf-8")
        print("  -> Metadatos de main.tex actualizados.")

    print(f"[OK] Laboratorio {semester_folder_name}/{lab_folder_name} inicializado con éxito.")
    print(f"     Directorio: {target_dir}")
    print(f"     Para compilar: cd {semester_folder_name}/{lab_folder_name}; latexmk")

def main():
    parser = argparse.ArgumentParser(description="Inicializar una nueva carpeta de laboratorio para Physics-Reports.")
    parser.add_argument("--semester", type=int, default=3, help="Número de semestre (ej. 2, 3) [Por defecto: 3]")
    parser.add_argument("--lab", type=int, required=True, help="Número de laboratorio (ej. 1, 2, 5)")
    parser.add_argument("--title", type=str, default="", help="Título del informe")
    parser.add_argument("--date", type=str, default="", help="Fecha del informe (ej. 'Lima, 11 de septiembre de 2026')")
    parser.add_argument("--teacher", type=str, default="", help="Docente a cargo (ej. 'Cortez, G.')")
    parser.add_argument("--course", type=str, default="", help="Nombre del curso (ej. 'Física III (CF1C1) --- Sección A')")

    args = parser.parse_args()
    setup_new_lab(args.semester, args.lab, args.title, args.date, args.teacher, args.course)

if __name__ == "__main__":
    main()
