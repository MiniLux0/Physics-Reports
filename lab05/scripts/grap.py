import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
import os

# 1. Definición de los datos (en unidades de 10^-5 °C^-1)
materiales = ['Cobre', 'Aluminio', 'Vidrio borosilicato']
alfa_exp = np.array([1.6009, 2.4569, 0.24255])  
delta_alfa = np.array([0.0690, 0.1054, 0.01448])  
alfa_ref = np.array([1.70, 2.30, 0.240])  

# 2. Configuración de la figura
fig, ax = plt.subplots(figsize=(7, 4.5))
fig.patch.set_facecolor('white')
ax.set_facecolor('white')

# Posiciones en X
x = np.arange(len(materiales))

# 3. Graficar los puntos experimentales con barras de error
ax.errorbar(x, alfa_exp, yerr=delta_alfa, fmt='o', color='blue',
            ecolor='blue', capsize=6, markersize=8, elinewidth=2,
            label='Valores experimentales ($\\alpha \\pm \\delta\\alpha$)', zorder=3)

# 4. Graficar los valores de referencia (teóricos) como puntos rojos
ax.scatter(x, alfa_ref, color='red', marker='x', s=100, linewidths=2.5,
           label='Valores de referencia ($\\alpha_{\\text{ref}}$)', zorder=4)

# 5. Configuración de ejes y título
ax.set_xticks(x)
ax.set_xticklabels(materiales, fontsize=11)
ax.set_ylabel('$\\alpha$ ($\\times 10^{-5}$ °C$^{-1}$)', fontsize=11)
ax.set_title('Coeficiente de dilatación lineal por material', fontsize=12, pad=12)

# Formateador para usar la coma como separador decimal en el eje Y
def format_coma(val, pos):
    return f"{val:.2f}".replace('.', ',')
ax.yaxis.set_major_formatter(FuncFormatter(format_coma))

# 6. Estilo: Cuadrícula suave y leyenda
ax.grid(True, linestyle='--', alpha=0.5, color='gray', zorder=1)
ax.legend(loc='best', framealpha=0.9, fontsize=10)

# Ajustar límites del eje Y para centrar la visualización (incluyendo el cero para mostrar escala real)
ax.set_ylim(0, 2.8)

# 7. Guardar la figura en PNG con alta resolución en Figures/
os.makedirs('../Figures', exist_ok=True)
plt.savefig('../Figures/grafica_alfa.png', dpi=300, bbox_inches='tight')
print("Gráfica generada con éxito en Figures/grafica_alfa.png")
