import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Configuración global de estilo para que luzca académico
plt.style.use('default')
plt.rcParams.update({'font.size': 10, 'axes.grid': True, 'grid.alpha': 0.5, 'grid.linestyle': '--'})

# ==========================================
# DATOS ACTUALIZADOS (Esfuerzo Real)
# ==========================================

# 1. Datos Resorte Metálico
F_resorte = np.array([4.898, 7.392, 9.849, 12.343, 14.747, 17.241])
eps_resorte = np.array([0.7952, 0.9337, 1.1084, 1.3193, 1.5120, 1.6867])
sig_resorte = np.array([30.84, 47.08, 63.62, 80.41, 96.64, 113.65]) # kPa

# 2. Datos Liga (Carga)
DeltaL_liga_c = np.array([0.0250, 0.0440, 0.0730, 0.1080, 0.1290, 0.1410])
F_liga_c = np.array([4.898, 7.392, 9.849, 12.343, 14.747, 17.241])
eps_liga_c = np.array([0.07310, 0.12865, 0.21345, 0.31579, 0.37719, 0.41228])
sig_liga_c = np.array([61.42, 98.39, 143.05, 179.27, 218.67, 261.23]) # kPa

# 3. Datos Liga (Descarga)
# Nota: La descarga llega hasta F = 4.898 (no hay dato de masa 0)
DeltaL_liga_d = np.array([0.1320, 0.1180, 0.1130, 0.0800, 0.0520])
F_liga_d = np.array([14.747, 12.343, 9.849, 7.392, 4.898])
eps_liga_d = np.array([0.38596, 0.34503, 0.33041, 0.23392, 0.15205])
sig_liga_d = np.array([233.78, 171.86, 135.40, 101.95, 64.54]) # kPa

# ==========================================
# GRÁFICA 2: σ vs ε Resorte (Esfuerzo Real)
# ==========================================
plt.figure(figsize=(8, 6))
slope, intercept, r_value, p_value, std_err = linregress(eps_resorte, sig_resorte)
line_x = np.linspace(min(eps_resorte)-0.05, max(eps_resorte)+0.05, 100)
line_y = slope * line_x + intercept

plt.plot(eps_resorte, sig_resorte, 'bo', label='Datos experimentales')
plt.plot(line_x, line_y, 'r--', label='Ajuste lineal')

texto_ajuste = f"$\\sigma(\\varepsilon) = ({slope:.2f} \pm {std_err:.2f})\\cdot\\varepsilon + ({intercept:.2f})$\n"
texto_ajuste += f"$Y = {slope:.2f} \pm {std_err:.2f}$ kPa\n"
texto_ajuste += f"$R^2 = {r_value**2:.4f}$"
plt.text(0.8, 100, texto_ajuste, bbox=dict(facecolor='white', alpha=0.8, edgecolor='gray'))

plt.title('Esfuerzo Real vs Deformación (Módulo de Young) - Resorte')
plt.xlabel('$\\varepsilon$ (adimensional)')
plt.ylabel('$\\sigma$ (kPa)')
plt.legend()
plt.savefig('grafica_2_resorte_esfuerzo_real.png', dpi=300, bbox_inches='tight')
plt.close()

# ==========================================
# GRÁFICA NUEVA: F vs Δℓ Liga (Carga y Descarga)
# ==========================================
plt.figure(figsize=(8, 6))
plt.plot(DeltaL_liga_c, F_liga_c, 'b-o', label='Carga')
plt.plot(DeltaL_liga_d, F_liga_d, 'r-s', label='Descarga')

plt.title('Fuerza vs Deformación Longitudinal - Liga Elástica')
plt.xlabel('$\\Delta\\ell$ (m)')
plt.ylabel('F (N)')
plt.legend()
plt.savefig('grafica_nueva_liga_fuerza.png', dpi=300, bbox_inches='tight')
plt.close()

# ==========================================
# GRÁFICA 3: σ vs ε Liga (Carga)
# ==========================================
plt.figure(figsize=(8, 6))
# Ajuste Polinomial (Grado 2)
coefs_c = np.polyfit(eps_liga_c, sig_liga_c, 2)
poly_c = np.poly1d(coefs_c)
x_poly_c = np.linspace(min(eps_liga_c)-0.02, max(eps_liga_c)+0.02, 100)

plt.plot(eps_liga_c, sig_liga_c, 'bo', label='Datos experimentales')
plt.plot(x_poly_c, poly_c(x_poly_c), 'r-', label='Ajuste polinomial')

texto_c = f"$\\sigma(\\varepsilon) = {coefs_c[0]:.2f}\\varepsilon^2 + {coefs_c[1]:.2f}\\varepsilon + {coefs_c[2]:.2f}$"
plt.text(0.08, 220, texto_c, bbox=dict(facecolor='white', alpha=0.8, edgecolor='gray'))

plt.title('Esfuerzo Real vs Deformación - Carga (Liga Elástica)')
plt.xlabel('$\\varepsilon$ (adimensional)')
plt.ylabel('$\\sigma$ (kPa)')
plt.legend()
plt.savefig('grafica_3_liga_carga.png', dpi=300, bbox_inches='tight')
plt.close()

# ==========================================
# GRÁFICA 4: σ vs ε Liga (Descarga)
# ==========================================
plt.figure(figsize=(8, 6))
# Ajuste Polinomial (Grado 2)
coefs_d = np.polyfit(eps_liga_d, sig_liga_d, 2)
poly_d = np.poly1d(coefs_d)
x_poly_d = np.linspace(min(eps_liga_d)-0.02, max(eps_liga_d)+0.02, 100)

plt.plot(eps_liga_d, sig_liga_d, 'bo', label='Datos experimentales')
plt.plot(x_poly_d, poly_d(x_poly_d), 'r-', label='Ajuste polinomial')

texto_d = f"$\\sigma(\\varepsilon) = {coefs_d[0]:.2f}\\varepsilon^2 + {coefs_d[1]:.2f}\\varepsilon + {coefs_d[2]:.2f}$"
plt.text(0.16, 200, texto_d, bbox=dict(facecolor='white', alpha=0.8, edgecolor='gray'))

plt.title('Esfuerzo Real vs Deformación - Descarga (Liga Elástica)')
plt.xlabel('$\\varepsilon$ (adimensional)')
plt.ylabel('$\\sigma$ (kPa)')
plt.legend()
plt.savefig('grafica_4_liga_descarga.png', dpi=300, bbox_inches='tight')
plt.close()

# ==========================================
# GRÁFICA 5: Lazo de Histéresis
# ==========================================
plt.figure(figsize=(8, 6))
plt.plot(eps_liga_c, sig_liga_c, 'b-o', label='Carga ($\\varepsilon_c$)')
plt.plot(eps_liga_d, sig_liga_d, 'r-s', label='Descarga ($\\varepsilon_d$)')


eps_loop = np.concatenate((eps_liga_c, eps_liga_d[::-1]))
sig_loop = np.concatenate((sig_liga_c, sig_liga_d[::-1]))
plt.fill(eps_loop, sig_loop, color='purple', alpha=0.2, label='Área de Histéresis')

plt.title('Lazo de Histéresis (Esfuerzo Real vs Deformación)')
plt.xlabel('Deformación ($\\varepsilon$)')
plt.ylabel('Esfuerzo ($\\sigma$) [kPa]')
plt.legend()
plt.text(0.15, 200, "Área disipada $\\approx 13.8$ kJ/m$^3$", bbox=dict(facecolor='white', alpha=0.8, edgecolor='gray'))
plt.savefig('grafica_5_histeresis.png', dpi=300, bbox_inches='tight')
plt.close()

print("¡Gráficas generadas exitosamente!")