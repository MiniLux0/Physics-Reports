import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from matplotlib.ticker import FuncFormatter
import os

# ============================================================
# 1. Definición de los datos experimentales
# ============================================================
x_exp = np.array([1.0, 2.0, 3.0, 4.0, 5.0])
y_exp = np.array([10.2, 20.5, 29.8, 40.1, 50.4])
x_err = np.array([0.05, 0.05, 0.05, 0.05, 0.05])
y_err = np.array([0.3, 0.4, 0.3, 0.5, 0.4])

# ============================================================
# 2. Ajuste por Mínimos Cuadrados (OLS)
# ============================================================
N = len(x_exp)
m, b = np.polyfit(x_exp, y_exp, 1)
y_fit = m * x_exp + b
residuos = y_exp - y_fit
s_y = np.sqrt(np.sum(residuos**2) / (N - 2))
s_m = s_y / np.sqrt(np.sum((x_exp - np.mean(x_exp))**2))
s_b = s_y * np.sqrt(1/N + (np.mean(x_exp)**2) / np.sum((x_exp - np.mean(x_exp))**2))
r2 = 1 - (np.sum(residuos**2) / np.sum((y_exp - np.mean(y_exp))**2))

# ============================================================
# 3. Configuración de la figura con panel de residuos
# ============================================================
fig = plt.figure(figsize=(8, 6.0))
fig.patch.set_facecolor('white')
gs = gridspec.GridSpec(2, 1, height_ratios=[3.2, 1.0], hspace=0.12)

ax_main = fig.add_subplot(gs[0])
ax_res = fig.add_subplot(gs[1], sharex=ax_main)
ax_main.set_facecolor('white')
ax_res.set_facecolor('white')

# Formateador de coma decimal
def format_coma(val, pos):
    return f"{val:.1f}".replace('.', ',')

def format_coma_res(val, pos):
    return f"{val:+.2f}".replace('.', ',')

ax_main.yaxis.set_major_formatter(FuncFormatter(format_coma))
ax_main.xaxis.set_major_formatter(FuncFormatter(format_coma))
ax_res.yaxis.set_major_formatter(FuncFormatter(format_coma_res))
ax_res.xaxis.set_major_formatter(FuncFormatter(format_coma))

# Panel principal: Datos + Ajuste OLS
x_line = np.linspace(0.5, 5.5, 200)
ax_main.errorbar(x_exp, y_exp, xerr=x_err, yerr=y_err, fmt='o', color='#003865',
                 ecolor='#003865', elinewidth=1.5, capsize=4, capthick=1.5, markersize=6,
                 label=r'Datos experimentales ($y \pm \delta y$)', zorder=4)

ax_main.plot(x_line, m * x_line + b, color='#D9534F', linewidth=2.0, linestyle='-',
             label=f'Ajuste MCO: $y = ({m:.2f}\\pm{s_m:.2f})\,x + ({b:.2f}\\pm{s_b:.2f})$\n($R^2 = {r2:.4f}$)', zorder=3)

ax_main.set_ylabel(r'Variable Dependiente $Y$ (unidad)', fontsize=11)
ax_main.set_title(r'Gráfica Experimental con Ajuste Lineal y Residuos', fontsize=12, fontweight='bold', pad=10)
ax_main.grid(True, linestyle=':', alpha=0.6, color='gray')
ax_main.legend(loc='upper left', framealpha=0.95, fontsize=9.5)
plt.setp(ax_main.get_xticklabels(), visible=False)

# Panel inferior: Residuos
ax_res.axhline(0, color='gray', linestyle='--', linewidth=1.2)
ax_res.errorbar(x_exp, residuos, yerr=y_err, fmt='s', color='#003865',
                ecolor='#003865', elinewidth=1.2, capsize=3, markersize=5, zorder=3)
ax_res.set_xlabel(r'Variable Independiente $X$ (unidad)', fontsize=11)
ax_res.set_ylabel(r'Residuo', fontsize=10)
ax_res.grid(True, linestyle=':', alpha=0.6, color='gray')

# ============================================================
# 4. Exportación en alta resolución (DPI 300) a Figures/
# ============================================================
figures_dir = os.path.join(os.path.dirname(__file__), '..', 'Figures')
os.makedirs(figures_dir, exist_ok=True)
output_path = os.path.join(figures_dir, 'grafica1.png')
plt.savefig(output_path, dpi=300, bbox_inches='tight')
print(f"[OK] Gráfica generada con éxito en {output_path}")

