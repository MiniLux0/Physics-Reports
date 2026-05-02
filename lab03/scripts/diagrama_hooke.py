import matplotlib.pyplot as plt
import numpy as np

# Configuración de estilo académico
plt.rcParams.update({
    "font.family": "serif",
    "font.size": 10,
    "axes.linewidth": 1,
    "xtick.major.width": 1,
    "ytick.major.width": 1
})

# Dimensiones de la figura (10x7 cm a pulgadas)
fig, ax = plt.subplots(figsize=(10/2.54, 7/2.54), dpi=300)

# Región elástica (lineal)
e_elastic = np.linspace(0, 0.002, 50)
s_elastic = 200000 * e_elastic

# Región plástica (curva)
e_plastic = np.linspace(0.002, 0.025, 100)
s_plastic = 400 + 35000 * (e_plastic - 0.002) - 1.2e6 * (e_plastic - 0.002)**2

# Combinar datos
epsilon = np.concatenate((e_elastic, e_plastic))
sigma = np.concatenate((s_elastic, s_plastic))

# Puntos clave
limite_idx = 49
epsilon_lim = epsilon[limite_idx]
sigma_lim = sigma[limite_idx]

epsilon_rupt = epsilon[-1]
sigma_rupt = sigma[-1]

# Curva principal
ax.plot(epsilon, sigma, color='black', linewidth=1.5)

# Límite elástico
ax.plot(epsilon_lim, sigma_lim, 'ko')
ax.annotate('Límite elástico',
            xy=(epsilon_lim, sigma_lim),
            xytext=(epsilon_lim + 0.001, sigma_lim - 50))

# Línea punteada
ax.plot([0, epsilon_lim], [sigma_lim, sigma_lim], 'k--')
ax.annotate(r'$\sigma_{límite}$',
            xy=(0, sigma_lim),
            xytext=(-0.0025, sigma_lim - 15))

# Punto de ruptura
ax.plot(epsilon_rupt, sigma_rupt, 'kx')
ax.annotate('Punto de ruptura',
            xy=(epsilon_rupt, sigma_rupt),
            xytext=(epsilon_rupt - 0.007, sigma_rupt + 30))

# Ejes
ax.set_xlabel(r'$\epsilon$')
ax.set_ylabel(r'$\sigma$ (Pa)')

# Estilo limpio
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.set_xticks([])
ax.set_yticks([])
ax.set_xlim(left=0)
ax.set_ylim(bottom=0)

plt.tight_layout()
plt.savefig('diagrama_esfuerzo_deformacion.png', dpi=300)
plt.show()
