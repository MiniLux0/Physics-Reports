# Guía de colaboración — Physics Reports

Este documento explica cómo contribuir al repositorio sin pisar el trabajo de otros.
Está pensado para quien nunca ha usado Git antes.

---

## Regla fundamental

**Nadie trabaja directamente en `main`.**

`main` contiene solo versiones revisadas y que compilan. Tu trabajo va en tu propia rama hasta que esté listo.

---

## Primera vez: clonar el repositorio

Si aún no tienes el proyecto en tu computadora:

```bash
git clone https://github.com/MiniLux0/Physics-Reports.git
cd Physics-Reports
```

Luego instala MiKTeX y configura VS Code siguiendo [`docs/MiKTeX.md`](MiKTeX.md) y [`docs/Git.md`](Git.md).

---

## Flujo de trabajo para cada laboratorio

### 1. Asegúrate de tener `main` actualizado

Antes de empezar a trabajar, sincroniza tu copia local:

```bash
git checkout main
git pull origin main
```

### 2. Crea tu rama

```bash
git checkout -b nombre-lab02
```

Usa tu nombre o iniciales, por ejemplo: `garcia-lab02`, `torres-lab02`.

> Esta rama es tuyo. Puedes hacer los cambios que quieras sin afectar a nadie.

### 3. Trabaja en tu carpeta

Edita únicamente dentro de `lab02/`. La estructura esperada es:

```
lab02/
├── main.tex
├── refs.bib
├── sections/
│   ├── 01_introduccion.tex
│   ├── 02_resumen.tex
│   └── ...
├── Figures/
├── data/
└── analysis/
```

No modifiques `template/` ni archivos en la raíz del proyecto.

### 4. Guarda tu avance con commits

Cada vez que termines algo concreto (una sección, una gráfica, los datos):

```bash
git add .
git commit -m "descripción breve de lo que hiciste"
```

Ejemplos de buenos mensajes:
- `"agrega sección de resultados lab02"`
- `"corrige figura del circuito"`
- `"completa análisis de incertidumbres"`

No hagas un solo commit con todo al final. Commits frecuentes = más fácil revertir errores.

### 5. Sube tu rama a GitHub

```bash
git push -u origin nombre-lab02
```

Las siguientes veces en la misma rama basta con:

```bash
git push
```

### 6. Abre un Pull Request

1. Ve al repositorio en GitHub.
2. Aparecerá un banner amarillo con tu rama y el botón **"Compare & pull request"** — haz clic.
3. Escribe un título claro: `"Lab02 completo — García"`.
4. En la descripción menciona qué secciones están listas y si falta algo.
5. Haz clic en **"Create pull request"**.

Quien administra el repo revisará que compile, verificará los resultados, y aprobará o pedirá correcciones.

---

## Si `main` se actualiza mientras trabajas

Esto va a pasar seguido. Para incorporar los cambios sin perder tu trabajo:

```bash
git checkout main
git pull origin main
git checkout nombre-lab02
git merge main
```

Si hay conflictos, Git te avisará qué archivos tienen choques. Resuélvelos, luego:

```bash
git add .
git commit -m "merge con main actualizado"
```

---

## Resumen rápido

```bash
# Una sola vez
git clone https://github.com/MiniLux0/Physics-Reports.git

# Al inicio de cada sesión
git checkout main && git pull origin main
git checkout -b nombre-lab02        # solo la primera vez
git checkout nombre-lab02           # las demás veces

# Mientras trabajas
git add .
git commit -m "qué hiciste"

# Para subir
git push

# Si main se actualizó
git merge main
```

---

## Errores frecuentes

| Error | Causa | Solución |
|---|---|---|
| `error: failed to push` | No has hecho pull antes | `git pull --rebase origin main` |
| `CONFLICT` al hacer merge | Dos personas editaron el mismo archivo | Abre el archivo, elige qué versión conservar, luego `git add` + `git commit` |
| Edité `main` sin querer | Olvidaste crear tu rama | `git stash`, cambia de rama, `git stash pop` |
| El PDF no compila en mi rama | Error en el `.tex` | Compila localmente antes de hacer push |

---

*Cualquier duda, abre un Issue en el repositorio o avisa por el grupo.*