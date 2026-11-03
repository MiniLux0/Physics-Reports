# Generación de Gráficas Científicas en Python

Plantilla y estándares para la creación de figuras científicas de alta calidad con `matplotlib`, `numpy` y `scipy` en `labNN/scripts/grap.py`.

---

## 1. Plantilla Estándar: Regresión Lineal OLS + Panel de Residuos

```python
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from matplotlib.ticker import FuncFormatter
import os

# 1. Datos experimentales
x_exp = np.array([1.442, 2.453, 5.220, 8.030, 11.150])  # Tensión multímetro (V)
y_exp = np.array([1.400, 2.440, 5.200, 8.000, 11.200])  # Tensión osciloscopio (V)
x_err = np.array([0.008, 0.013, 0.027, 0.041, 0.057])   # Incertidumbre multímetro
y_err = np.array([0.050, 0.100, 0.200, 0.200, 0.200])   # Incertidumbre osciloscopio

# 2. Ajuste por Mínimos Cuadrados Ponderados / OLS
N = len(x_exp)
m, b = np.polyfit(x_exp, y_exp, 1)
y_fit = m * x_exp + b
residuos = y_exp - y_fit
s_y = np.sqrt(np.sum(residuos**2) / (N - 2))
s_m = s_y / np.sqrt(np.sum((x_exp - np.mean(x_exp))**2))
s_b = s_y * np.sqrt(1/N + (np.mean(x_exp)**2) / np.sum((x_exp - np.mean(x_exp))**2))
r2 = 1 - (np.sum(residuos**2) / np.sum((y_exp - np.mean(y_exp))**2))

# 3. Configuración de Lienzo con Gridspec (Figura principal + Residuos)
fig = plt.figure(figsize=(8, 6.5))
fig.patch.set_facecolor('white')
gs = gridspec.GridSpec(2, 1, height_ratios=[3.2, 1.0], hspace=0.12)

ax_main = fig.add_subplot(gs[0])
ax_res = fig.add_subplot(gs[1], sharex=ax_main)
ax_main.set_facecolor('white')
ax_res.set_facecolor('white')

# 4. Formateador de coma decimal
def format_coma(val, pos):
    return f"{val:.1f}".replace('.', ',')
def format_coma_res(val, pos):
    return f"{val:+.2f}".replace('.', ',')

ax_main.yaxis.set_major_formatter(FuncFormatter(format_coma))
ax_main.xaxis.set_major_formatter(FuncFormatter(format_coma))
ax_res.yaxis.set_major_formatter(FuncFormatter(format_coma_res))
ax_res.xaxis.set_major_formatter(FuncFormatter(format_coma))

# 5. Panel Principal: Datos + Ajuste + Línea Teórica Ideal (1:1)
x_line = np.linspace(0, 12, 200)
ax_main.errorbar(x_exp, y_exp, xerr=x_err, yerr=y_err, fmt='o', color='#003865',
                 ecolor='#003865', elinewidth=1.5, capsize=4, capthick=1.5, markersize=6,
                 label=r'Datos experimentales ($V_{\mathrm{osc}} \pm \delta V_{\mathrm{osc}}$)', zorder=4)

ax_main.plot(x_line, m * x_line + b, color='#D9534F', linewidth=2.0, linestyle='-',
             label=f'Ajuste MCO: $V_{{\\mathrm{{osc}}}} = ({m:.4f}\\pm{s_m:.4f})\,V_{{\\mathrm{{mult}}}} + ({b:.3f}\\pm{s_b:.3f})$\n($R^2 = {r2:.5f}$)', zorder=3)

ax_main.plot(x_line, x_line, color='gray', linewidth=1.2, linestyle='--',
             label=r'Respuesta ideal ($V_{\mathrm{osc}} = V_{\mathrm{mult}}$)', zorder=2)

ax_main.set_ylabel(r'Tensión en Osciloscopio $V_{\mathrm{osc}}$ (V)', fontsize=11)
ax_main.set_title(r'Curva de Calibración de Tensión Continua (DC)', fontsize=12, fontweight='bold', pad=10)
ax_main.grid(True, linestyle=':', alpha=0.6, color='gray')
ax_main.legend(loc='upper left', framealpha=0.95, fontsize=9.5)
plt.setp(ax_main.get_xticklabels(), visible=False)

# 6. Panel Inferior: Residuos
ax_res.axhline(0, color='gray', linestyle='--', linewidth=1.2)
ax_res.errorbar(x_exp, residuos, yerr=y_err, fmt='s', color='#003865',
                ecolor='#003865', elinewidth=1.2, capsize=3, markersize=5, zorder=3)
ax_res.set_xlabel(r'Tensión en Multímetro $V_{\mathrm{mult}}$ (V)', fontsize=11)
ax_res.set_ylabel(r'Residuo (V)', fontsize=10)
ax_res.grid(True, linestyle=':', alpha=0.6, color='gray')
ax_res.set_ylim(-0.25, 0.25)

# 7. Exportación a Figures/ a 300 DPI
figures_dir = os.path.join(os.path.dirname(__file__), '..', 'Figures')
os.makedirs(figures_dir, exist_ok=True)
output_path = os.path.join(figures_dir, 'fig_calibracion_dc.png')
plt.savefig(output_path, dpi=300, bbox_inches='tight')
print(f"[OK] Gráfica generada en: {output_path}")
```

---

## 2. Plantilla: Formas de Onda y Reconstrucción Vectorial a 300 DPI

```python
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
import os

# Base de tiempo y señales
t = np.linspace(0, 33.33, 1000)  # Dos ciclos completos a 60 Hz (ms)
v_seno = 9.60 * np.sin(2 * np.pi * 0.060 * t)

fig, ax = plt.subplots(figsize=(8, 4.2))
fig.patch.set_facecolor('white')
ax.set_facecolor('white')

def format_coma(val, pos):
    return f"{val:.1f}".replace('.', ',')

ax.xaxis.set_major_formatter(FuncFormatter(format_coma))
ax.yaxis.set_major_formatter(FuncFormatter(format_coma))

ax.plot(t, v_seno, color='#003865', linewidth=2.0, label=r'Onda senoidal experimental ($V_p = 9{,}60\,\mathrm{V}, f = 60{,}0\,\mathrm{Hz}$)')
ax.axhline(6.79, color='#D9534F', linestyle='--', linewidth=1.5, label=r'Tensión eficaz $V_{\mathrm{rms}} = 6{,}79\,\mathrm{V}$')
ax.axhline(-6.79, color='#D9534F', linestyle='--', linewidth=1.5)

ax.set_xlabel(r'Tiempo $t$ (ms)', fontsize=11)
ax.set_ylabel(r'Tensión $v(t)$ (V)', fontsize=11)
ax.set_title(r'Señal Alterna Senoidal --- Transformador 220 V / 6 V', fontsize=12, fontweight='bold', pad=10)
ax.grid(True, linestyle=':', alpha=0.6, color='gray')
ax.legend(loc='upper right', framealpha=0.95, fontsize=9.5)

figures_dir = os.path.join(os.path.dirname(__file__), '..', 'Figures')
os.makedirs(figures_dir, exist_ok=True)
plt.savefig(os.path.join(figures_dir, 'fig_ondas_ac.png'), dpi=300, bbox_inches='tight')
```

---

## 3. Reglas de Estilo para Figuras Científicas

1. **Fondo:** Siempre blanco puro (`facecolor='white'`).
2. **Formato Decimal:** Todas las etiquetas de ejes con números reales deben presentar coma decimal vía `FuncFormatter`.
3. **Barras de Error:** Obligatorias en datos experimentales (`fmt='o'`, `capsize=4`, `elinewidth=1.5`).
4. **Paleta de Colores:**
   - Datos experimentales: Azul institucional UNI `#003865` o azul marino.
   - Ajustes / Curvas teóricas: Rojo `#D9534F` o carmesí.
   - Respaldo / Referencia ideal: Gris neutro `gray` con trazo discontinuo `--`.
5. **Resolución y Guardado:**
   - Resolución: `dpi=300`.
   - Ajuste de márgenes: `bbox_inches='tight'`.
   - Ubicación: Guardar directamente en `labNN/Figures/<nombre_figura>.png`.
