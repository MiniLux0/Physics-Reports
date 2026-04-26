# 🔬 Physics Reports — UNI Facultad de Ciencias

Repositorio de informes de laboratorio de Física II (CF1B2).  
Plantilla basada en `article` estándar — sin dependencias externas.


## ⚙️ Instalación y Configuración
Si eres nuevo en el repositorio y necesitas configurar tu entorno (MiKTeX, VS Code, Git), por favor lee la **[Guía de Configuración del Entorno](docs/INSTALACION.md)** antes de empezar a editar.

## 📂 Estructura

```text
physics-reports/
├── template/          ← plantilla maestra (no editar directamente)
│   ├── main.tex
│   ├── refs.bib
│   ├── sections/
│   └── Figures/
│
├── lab02/             ← informe del laboratorio 2
│   ├── main.tex
│   ├── refs.bib
│   ├── sections/
│   ├── Figures/
│   ├── data/
│   └── analysis/
│
├── docs/              ← documentación y tutoriales
│   └── INSTALACION.md 
│
└── README.md
```

## 🚀 Flujo de trabajo para cada nuevo lab

```bash
# 1. Copiar la plantilla
cp -r template/ lab02/

# 2. Editar SOLO el bloque "DATOS DEL INFORME" en lab02/main.tex

# 3. Trabajar en lab02/sections/ — nunca mezclar con otros labs
```

## 🛠️ Compilación

Con **VS Code + LaTeX Workshop**: compila automáticamente al guardar (`Ctrl + S`).  
*Receta recomendada en settings:* `latexmk (latexmkrc)` o `pdflatex → biber → pdflatex × 2`.

Compilación manual en terminal:
```bash
pdflatex main.tex
biber main
pdflatex main.tex
pdflatex main.tex
```

## 📦 Paquetes requeridos

Todos son estándar en TeX Live / MiKTeX:

| Paquete | Uso |
|---|---|
| `babel` (spanish) | Idioma |
| `amsmath`, `mathtools` | Matemáticas |
| `physics` | Derivadas, gradientes, etc. |
| `siunitx` | Unidades SI |
| `booktabs` | Tablas profesionales |
| `biblatex` + `biber` | Bibliografía |
| `fancyhdr` | Encabezados/pie |
| `titlesec` | Estilo de secciones |
