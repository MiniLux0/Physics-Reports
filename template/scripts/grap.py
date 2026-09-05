import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
import os

# 1. Definición de los datos
# x_data = np.array([1, 2, 3])
# y_data = np.array([10.5, 20.3, 30.1])
# y_err  = np.array([0.5, 0.4, 0.6])

# 2. Configuración de la figura
fig, ax = plt.subplots(figsize=(7, 4.5))
fig.patch.set_facecolor('white')
ax.set_facecolor('white')

# 3. Graficado con barras de error
# ax.errorbar(x_data, y_data, yerr=y_err, fmt='o', color='blue',
#             ecolor='blue', capsize=6, markersize=8, elinewidth=2,
#             label=r'Valores experimentales', zorder=3)

# 4. Formato de ejes
# ax.set_xlabel(r'Variable $X$ (unidad)', fontsize=11)
# ax.set_ylabel(r'Variable $Y$ (unidad)', fontsize=11)
ax.set_title('Título de la Gráfica', fontsize=12, pad=12)

# Formateador para usar la coma como separador decimal
def format_coma(val, pos):
    return f"{val:.2f}".replace('.', ',')

ax.yaxis.set_major_formatter(FuncFormatter(format_coma))

# 5. Estilo: Cuadrícula y leyenda
ax.grid(True, linestyle='--', alpha=0.5, color='gray', zorder=1)
# ax.legend(loc='best', framealpha=0.9, fontsize=10)

# 6. Exportación en alta resolución (DPI 300) a Figures/
figures_dir = os.path.join(os.path.dirname(__file__), '..', 'Figures')
os.makedirs(figures_dir, exist_ok=True)
output_path = os.path.join(figures_dir, 'grafica1.png')
plt.savefig(output_path, dpi=300, bbox_inches='tight')
print(f"Gráfica generada con éxito en {output_path}")
