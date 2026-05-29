import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

# 1. Definición de los datos
mediciones = np.array([1, 2, 3, 4, 5])
gamma_i = np.array([37.09, 41.60, 38.33, 40.20, 41.45])
delta_gamma = 0.88
promedio = 39.73
gamma_ref = 72.8

# 2. Configuración de la figura y tamaño (7, 4.5)
fig, ax = plt.subplots(figsize=(7, 4.5))

# Fondo blanco
fig.patch.set_facecolor('white')
ax.set_facecolor('white')

# 3. Graficar los puntos experimentales con barras de error
ax.errorbar(mediciones, gamma_i, yerr=delta_gamma, fmt='o', color='blue', 
            ecolor='blue', capsize=4, markersize=6, 
            label='Datos experimentales', zorder=3)

# 4. Líneas horizontales (Promedio y Valor Bibliográfico)
# Formateamos los números con coma para el texto de la leyenda
ax.axhline(promedio, color='red', linestyle='--', linewidth=1.5,
           label=f'Promedio ({str(promedio).replace(".", ",")} mN/m)', zorder=2)

ax.axhline(gamma_ref, color='black', linestyle=':', linewidth=1.5,
           label=f'Valor bibliográfico ({str(gamma_ref).replace(".", ",")} mN/m)', zorder=2)

# 5. Configuración de ejes y título
ax.set_xlabel('Medición')
ax.set_ylabel('γ (mN/m)')
ax.set_title('Coeficiente de tensión superficial — Primer método', pad=10)

# 6. Forzar que el eje X solo muestre números enteros
ax.set_xticks(mediciones)

# 7. Formateador para usar la coma como separador decimal en el eje Y
def format_coma(x, pos):
    return f"{x:.1f}".replace('.', ',')

ax.yaxis.set_major_formatter(FuncFormatter(format_coma))

# 8. Estilo: Cuadrícula suave y leyenda
# Solo cuadrícula en Y (opcional) o en ambos ejes, muy tenue
ax.grid(True, linestyle='-', alpha=0.3, color='gray', zorder=1)

# Colocar leyenda dentro del gráfico, buscando la mejor ubicación
ax.legend(loc='best', framealpha=0.9)

# 9. Ajustar márgenes para que no se corte nada
plt.tight_layout()

# 10. Guardar la figura en PDF con alta resolución
plt.savefig('grafica_gamma_m1.pdf', dpi=300, bbox_inches='tight')

# Mostrar el gráfico (opcional al ejecutar en local)
plt.show()