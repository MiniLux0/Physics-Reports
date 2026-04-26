# Instalación de LaTeX con MiKTeX

Esta guía cubre la instalación de MiKTeX y la extensión de LaTeX para VS Code.
Al terminar podrás abrir archivos `.tex`, compilarlos a PDF, e instalar paquetes automáticamente cuando falten.

---

## 1. Instalar MiKTeX

MiKTeX es el motor que convierte código LaTeX en PDF.

Descarga el instalador desde [miktex.org/download](https://miktex.org/download) y ejecuta con opciones por defecto.

---

## 2. Actualizar MiKTeX (obligatorio)

Después de instalar, abre **MiKTeX Console** y ve a la pestaña **Updates**:

1. Clic en **Check for updates**
2. Clic en **Update now**

Sin esto pueden aparecer errores de paquetes faltantes o compilación fallida.

---

## 3. Activar instalación automática de paquetes

Para que MiKTeX descargue paquetes sin preguntar cada vez:

1. Abre **MiKTeX Console**
2. Ve a **Settings → General**
3. En "Package installation", selecciona **Always install missing packages on-the-fly**

---

## 4. Instalar la extensión LaTeX Workshop en VS Code

LaTeX Workshop permite compilar y previsualizar PDF directamente desde VS Code.

1. Abre VS Code
2. Ve a Extensiones (`Ctrl + Shift + X`)
3. Busca `LaTeX Workshop` (autor: James Yu)
4. Haz clic en **Install**

---

## 5. Compilar el proyecto

Abre `main.tex` del laboratorio y guarda con `Ctrl + S`. LaTeX Workshop compilará automáticamente usando el `.latexmkrc` incluido en el proyecto.

El PDF aparecerá en el panel derecho de VS Code. Si no abre solo, presiona el ícono de vista previa en la esquina superior derecha del editor.

**Si la compilación falla la primera vez**, espera a que MiKTeX termine de descargar los paquetes necesarios (puede tardar unos minutos en la primera ejecución) y vuelve a guardar.

---

## Siguiente paso

Con LaTeX funcionando, lee **[Git.md](Git.md)** para configurar Git y clonar el repositorio.