# Configuración de Git, GitHub y VS Code

Esta guía cubre todo lo necesario para contribuir al repositorio desde Windows.

---

## 1. Instalar Git

Descarga el instalador desde [git-scm.com/download/win](https://git-scm.com/download/win).

Durante la instalación hay un paso crítico — en la pantalla **"Adjusting your PATH environment"**, selecciona:

```
Git from the command line and also from 3rd-party software
```

El resto de opciones déjalas por defecto. Sin esto, Git no funcionará dentro de VS Code.

**Verificar que quedó bien instalado** — abre una terminal y escribe:

```bash
git --version
```

Deberías ver algo como `git version 2.xx.x`.

---

## 2. Crear cuenta en GitHub

Si aún no tienes cuenta, ve a [github.com](https://github.com) y haz clic en **Sign up**. Usa un correo al que tengas acceso fácil.

---

## 3. Instalar VS Code

Descarga desde [code.visualstudio.com](https://code.visualstudio.com/) e instala con opciones por defecto.

---

## 4. Configurar Git con tu identidad

Antes de hacer cualquier commit, dile a Git quién eres. Abre la terminal de VS Code (`Ctrl + `` ` ``) y ejecuta:

```bash
git config --global user.name "Tu Nombre"
git config --global user.email "tu@correo.com"
```

Usa el mismo correo de tu cuenta de GitHub. Esto aparecerá en cada commit que hagas.

---

## 5. Conectar VS Code con GitHub

1. Abre VS Code
2. Haz clic en el ícono de **Accounts** (esquina inferior izquierda)
3. Selecciona **Sign in to GitHub**
4. Se abrirá el navegador — inicia sesión y autoriza VS Code

VS Code quedará autenticado con tu cuenta y podrás clonar, hacer push y pull sin ingresar contraseña cada vez.

---

## 6. Clonar el repositorio

1. Presiona `Ctrl + Shift + P`
2. Escribe `Git: Clone` y selecciónalo
3. Pega la URL del repositorio:

```
https://github.com/MiniLux0/Physics-Reports.git
```

4. Elige una carpeta local donde quieras guardarlo
5. Cuando termine, VS Code preguntará `Open Repository?` — haz clic en **Open**

---

## Siguiente paso

Con el repositorio clonado, lee **[Workflow.md](Workflow.md)** para saber cómo trabajar con ramas y pull requests.