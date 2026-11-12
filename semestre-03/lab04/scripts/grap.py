"""
grap.py — Generador de Figuras Científicas en Alta Resolución (300 DPI)
Repositorio: Physics-Reports / semestre-03/lab04
Laboratorio: Circuitos RC — Carga y descarga de un condensador
Cátedra: Física III (CF2B1, Sección A) — Universidad Nacional de Ingeniería (UNI)

Genera las 4 figuras estándar para el informe:
1. fig_carga_descarga.png : Formas de onda VC(t) y VR(t) bajo excitación de onda cuadrada (250 Hz).
2. fig_linealizacion_tau.png : Ajuste lineal OLS tau vs R con barras de error y panel de residuos.
3. fig_suma_kvl.png : Demostración experimental de la Ley de Mallas de Kirchhoff (HMO1202 Math ADD).
4. fig_paso20_thevenin.png : Respuesta transitoria teórica y experimental del circuito del paso 20 / Figs 9-10.
"""

import os
import json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

# -----------------------------------------------------------------------------
# Configuración Global de Estilo Científico
# -----------------------------------------------------------------------------
plt.rcParams.update({
    'font.family': 'serif',
    'font.size': 10,
    'axes.labelsize': 11,
    'axes.titlesize': 12,
    'xtick.labelsize': 9,
    'ytick.labelsize': 9,
    'legend.fontsize': 9,
    'figure.titlesize': 13,
    'lines.linewidth': 1.6,
    'grid.linestyle': '--',
    'grid.alpha': 0.6,
    'grid.color': '#cccccc',
    'mathtext.fontset': 'cm',
})

# Paleta Institucional sobria
COLOR_UNI_BLUE = '#003865'
COLOR_CARMINE  = '#D9534F'
COLOR_AMBER    = '#E67E22'
COLOR_TEAL     = '#16A085'
COLOR_DARK     = '#2C3E50'
COLOR_GRAY     = '#7F8C8D'

# Formateadores de coma decimal
def fmt_coma_0dec(x, pos):
    return f"{x:.0f}"

def fmt_coma_1dec(x, pos):
    return f"{x:.1f}".replace('.', ',')

def fmt_coma_2dec(x, pos):
    return f"{x:.2f}".replace('.', ',')

formatter_0dec = FuncFormatter(fmt_coma_0dec)
formatter_1dec = FuncFormatter(fmt_coma_1dec)
formatter_2dec = FuncFormatter(fmt_coma_2dec)

figures_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Figures'))
os.makedirs(figures_dir, exist_ok=True)

data_file = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data', 'data_mesa_c7.json'))

# Si el JSON no existe, invocar model_data primero
if not os.path.exists(data_file):
    from model_data import process_data
    process_data()

with open(data_file, 'r', encoding='utf-8') as f:
    exp_data = json.load(f)

dataset = exp_data['dataset']
ols_res = exp_data['ols_results']


# =============================================================================
# FIGURA 1: fig_carga_descarga.png
# =============================================================================
def plot_carga_descarga():
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8.5, 6.2), sharex=True,
                                   gridspec_kw={'hspace': 0.14})
    fig.patch.set_facecolor('white')

    # Parámetros representativos de Mesa C7: R1 = 9980 ohm, C2 = 27.41 nF -> tau = 273.6 us
    tau = 273.6e-6
    V0 = 10.0
    f = 250.0
    T = 1.0 / f  # 4.0 ms
    semi_T = T / 2.0  # 2.0 ms

    # Vector temporal: 1 período completo (4 ms) en microsegundos
    t = np.linspace(0, T, 2000)
    t_us = t * 1e6
    semi_T_us = semi_T * 1e6

    # Señal del generador
    V_gen = np.where(t < semi_T, V0, 0.0)

    # Tensión en el condensador VC(t)
    VC = np.where(
        t < semi_T,
        V0 * (1.0 - np.exp(-t / tau)),
        V0 * (1.0 - np.exp(-semi_T / tau)) * np.exp(-(t - semi_T) / tau)
    )

    # Tensión en la resistencia VR(t)
    VR = np.where(
        t < semi_T,
        V0 * np.exp(-t / tau),
        -V0 * (1.0 - np.exp(-semi_T / tau)) * np.exp(-(t - semi_T) / tau)
    )

    # --- Panel 1: Voltaje en Condensador VC(t) ---
    ax1.set_facecolor('white')
    ax1.plot(t_us, V_gen, color=COLOR_GRAY, linestyle=':', linewidth=1.2, label=r'Generador $V_{\mathrm{gen}}(t) = 10{,}0\ \mathrm{V}$')
    ax1.plot(t_us, VC, color=COLOR_UNI_BLUE, linewidth=1.8, label=r'$V_C(t)$ (Tensión en condensador / CH1)')

    # Anotaciones de puntos críticos
    tau_us = tau * 1e6
    vc_tau = V0 * (1.0 - np.exp(-1.0))
    ax1.scatter([tau_us], [vc_tau], color=COLOR_CARMINE, zorder=5, s=36)
    ax1.annotate(r'$t = \tau = 273{,}6\ \mu\mathrm{s}$' + '\n' + r'$V_C = 0{,}632\,V_0 = 6{,}32\ \mathrm{V}$',
                 xy=(tau_us, vc_tau), xytext=(tau_us + 250, vc_tau - 1.8),
                 arrowprops=dict(arrowstyle='->', color=COLOR_CARMINE, lw=1.2),
                 fontsize=8.5, bbox=dict(boxstyle='round,pad=0.3', facecolor='#FFF8E7', edgecolor=COLOR_CARMINE, alpha=0.9))

    # Punto al 99.3% (5*tau)
    t_5tau = 5 * tau_us
    vc_5tau = V0 * (1.0 - np.exp(-5.0))
    ax1.scatter([t_5tau], [vc_5tau], color=COLOR_TEAL, zorder=5, s=36)
    ax1.annotate(r'$t = 5\tau \approx 1368\ \mu\mathrm{s}$' + '\n' + r'$V_C \approx 0{,}993\,V_0 \approx 9{,}93\ \mathrm{V}$',
                 xy=(t_5tau, vc_5tau), xytext=(t_5tau - 500, vc_5tau - 2.8),
                 arrowprops=dict(arrowstyle='->', color=COLOR_TEAL, lw=1.2),
                 fontsize=8.5, bbox=dict(boxstyle='round,pad=0.3', facecolor='#E8F8F5', edgecolor=COLOR_TEAL, alpha=0.9))

    # Punto de descarga (semi_T + tau)
    t_desc_tau = semi_T_us + tau_us
    vc_desc_tau = V0 * np.exp(-1.0)
    ax1.scatter([t_desc_tau], [vc_desc_tau], color=COLOR_AMBER, zorder=5, s=36)
    ax1.annotate(r'$t = T/2 + \tau$' + '\n' + r'$V_C = 0{,}368\,V_0 = 3{,}68\ \mathrm{V}$',
                 xy=(t_desc_tau, vc_desc_tau), xytext=(t_desc_tau + 200, vc_desc_tau + 1.6),
                 arrowprops=dict(arrowstyle='->', color=COLOR_AMBER, lw=1.2),
                 fontsize=8.5, bbox=dict(boxstyle='round,pad=0.3', facecolor='#FEF9E7', edgecolor=COLOR_AMBER, alpha=0.9))

    ax1.axvline(semi_T_us, color='black', linestyle='--', linewidth=1.0, alpha=0.6)
    ax1.text(semi_T_us / 2.0, 1.2, 'ETAPA DE CARGA (0 a 2 ms)',
             ha='center', fontsize=9.5, fontweight='bold', color=COLOR_UNI_BLUE)
    ax1.text(semi_T_us + semi_T_us / 2.0, 8.5, 'ETAPA DE DESCARGA (2 a 4 ms)',
             ha='center', fontsize=9.5, fontweight='bold', color=COLOR_CARMINE)

    ax1.set_ylabel(r'Tensión $V_C$ (V)')
    ax1.set_ylim(-0.5, 11.5)
    ax1.yaxis.set_major_formatter(formatter_1dec)
    ax1.grid(True)
    ax1.legend(loc='lower right', framealpha=0.95)
    ax1.set_title('Respuesta Transitoria de Carga y Descarga en Circuito RC Serie ($f = 250$ Hz)', pad=8, fontweight='bold')

    # --- Panel 2: Voltaje en Resistencia VR(t) ~ Corriente I(t) ---
    ax2.set_facecolor('white')
    ax2.plot(t_us, VR, color=COLOR_CARMINE, linewidth=1.8, label=r'$V_R(t) = R \cdot I(t)$ (Tensión en resistencia / CH2)')
    ax2.axhline(0, color='black', linestyle='-', linewidth=0.8, alpha=0.5)
    ax2.axvline(semi_T_us, color='black', linestyle='--', linewidth=1.0, alpha=0.6)

    # Picos iniciales
    ax2.scatter([0], [V0], color=COLOR_UNI_BLUE, zorder=5, s=36)
    ax2.annotate(r'$V_R(0^+) = +V_0 = +10{,}0\ \mathrm{V}$',
                 xy=(0, V0), xytext=(200, V0 - 2.8),
                 arrowprops=dict(arrowstyle='->', color=COLOR_UNI_BLUE, lw=1.2),
                 fontsize=8.5)

    ax2.scatter([semi_T_us], [-V0], color=COLOR_CARMINE, zorder=5, s=36)
    ax2.annotate(r'$V_R(T/2^+) = -V_0 = -10{,}0\ \mathrm{V}$' + '\n' + r'(Inversión de corriente de descarga)',
                 xy=(semi_T_us, -V0), xytext=(semi_T_us + 150, -V0 + 2.5),
                 arrowprops=dict(arrowstyle='->', color=COLOR_CARMINE, lw=1.2),
                 fontsize=8.5)

    ax2.set_xlabel(r'Tiempo $t$ ($\mu$s)')
    ax2.set_ylabel(r'Tensión $V_R$ (V)')
    ax2.set_xlim(0, T * 1e6)
    ax2.set_ylim(-11.5, 11.5)
    ax2.xaxis.set_major_formatter(formatter_0dec)
    ax2.yaxis.set_major_formatter(formatter_1dec)
    ax2.grid(True)
    ax2.legend(loc='upper right', framealpha=0.95)

    out_file = os.path.join(figures_dir, 'fig_carga_descarga.png')
    plt.savefig(out_file, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"[OK] Generada Figura 1: {out_file}")


# =============================================================================
# FIGURA 2: fig_linealizacion_tau.png
# =============================================================================
def plot_linealizacion_tau():
    fig = plt.figure(figsize=(8.5, 6.2))
    fig.patch.set_facecolor('white')
    gs = fig.add_gridspec(2, 1, height_ratios=[3, 1], hspace=0.15)
    ax_top = fig.add_subplot(gs[0])
    ax_bot = fig.add_subplot(gs[1], sharex=ax_top)

    ax_top.set_facecolor('white')
    ax_bot.set_facecolor('white')

    styles = {
        'C1': {'color': COLOR_UNI_BLUE, 'marker': 'o', 'label': r'$C_1$ (Nominal: $10{,}0\ \mathrm{nF}$)'},
        'C2': {'color': COLOR_CARMINE,  'marker': 's', 'label': r'$C_2$ (Nominal: $22{,}4\ \mathrm{nF}$)'},
        'C3': {'color': COLOR_TEAL,     'marker': '^', 'label': r'$C_3$ (Nominal: $33{,}23\ \mathrm{nF}$)'}
    }

    r_domain = np.linspace(1500, 10500, 200)

    for c_key, style in styles.items():
        sub = [d for d in dataset if d['capacitor'] == c_key]
        r_vals = np.array([d['r_ohm'] for d in sub])
        tau_vals = np.array([d['tau_us'] for d in sub])
        u_tau_vals = np.array([d['u_tau_us'] for d in sub])

        # Parámetros OLS del modelo
        c_fit_nF = ols_res[c_key]['c_fit_nF']
        s_c_nF = ols_res[c_key]['s_c_nF']
        b_us = ols_res[c_key]['intercept_us']
        s_b_us = ols_res[c_key]['s_b_us']
        r2 = ols_res[c_key]['r2']

        # Línea de regresión: tau_fit (us) = (c_fit_nF * 1e-3) * R + b_us
        tau_line = (c_fit_nF * 1e-3) * r_domain + b_us
        c_fit_str = f"{c_fit_nF:.2f}".replace('.', '{,}')
        s_c_str = f"{s_c_nF:.2f}".replace('.', '{,}')
        r2_str = f"{r2:.5f}".replace('.', '{,}')

        ax_top.plot(r_domain / 1e3, tau_line, color=style['color'], linestyle='-', linewidth=1.5,
                    label=rf"{style['label']}: $C = ({c_fit_str} \pm {s_c_str})\ \mathrm{{nF}},\ R^2 = {r2_str}$")

        # Puntos experimentales
        ax_top.errorbar(r_vals / 1e3, tau_vals,
                        yerr=u_tau_vals, fmt=style['marker'],
                        color=style['color'], markeredgecolor='black', markeredgewidth=0.8,
                        markersize=6.5, capsize=3.5, elinewidth=1.2, zorder=5)

        # Residuos: e_i = tau_exp - (slope * R + intercept)
        tau_pred = (c_fit_nF * 1e-3) * r_vals + b_us
        resids = tau_vals - tau_pred

        ax_bot.scatter(r_vals / 1e3, resids,
                       marker=style['marker'], color=style['color'],
                       edgecolor='black', s=45, zorder=5)

    # Marcadores representativos en leyenda
    ax_top.plot([], [], 'o', color='black', label=r'Puntos experimentales (Mesa C7)')

    ax_top.set_ylabel(r'Constante de tiempo $\tau$ ($\mu$s)')
    ax_top.yaxis.set_major_formatter(formatter_0dec)
    ax_top.grid(True)
    ax_top.legend(loc='upper left', framealpha=0.93, fontsize=8.2)
    ax_top.set_title(r'Linealización y Regresión MCO de la Constante de Tiempo ($\tau = R \cdot C + b$)', pad=8, fontweight='bold')

    # Panel de residuos
    ax_bot.axhline(0, color='black', linestyle='--', linewidth=1.0)
    ax_bot.set_xlabel(r'Resistencia del circuito $R$ ($\mathrm{k}\Omega$)')
    ax_bot.set_ylabel(r'Residuo $e_i$ ($\mu$s)')
    ax_bot.set_ylim(-3.5, 3.5)
    ax_bot.xaxis.set_major_formatter(formatter_1dec)
    ax_bot.yaxis.set_major_formatter(formatter_1dec)
    ax_bot.grid(True)

    out_file = os.path.join(figures_dir, 'fig_linealizacion_tau.png')
    plt.savefig(out_file, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"[OK] Generada Figura 2: {out_file}")


# =============================================================================
# FIGURA 3: fig_suma_kvl.png
# =============================================================================
def plot_suma_kvl():
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8.5, 5.8), sharex=True,
                                   gridspec_kw={'height_ratios': [3, 1], 'hspace': 0.12})
    fig.patch.set_facecolor('white')
    ax1.set_facecolor('white')
    ax2.set_facecolor('white')

    # Parámetros: R1 = 9980 ohm, C1 = 10.80 nF -> tau = 107.8 us
    tau = 107.8e-6
    V0 = 10.0
    f = 250.0
    T = 1.0 / f
    semi_T = T / 2.0

    t = np.linspace(0, T, 2500)
    t_us = t * 1e6

    # Señal del generador cuadrada pura
    V_gen = np.where(t < semi_T, V0, 0.0)

    # VC(t)
    VC = np.where(
        t < semi_T,
        V0 * (1.0 - np.exp(-t / tau)),
        V0 * (1.0 - np.exp(-semi_T / tau)) * np.exp(-(t - semi_T) / tau)
    )

    # VR(t)
    VR = np.where(
        t < semi_T,
        V0 * np.exp(-t / tau),
        -V0 * (1.0 - np.exp(-semi_T / tau)) * np.exp(-(t - semi_T) / tau)
    )

    # Operación matemática HMO1202 Math ADD: CH1 + CH2
    V_math_add = VC + VR

    # Panel superior: CH1, CH2 y MATH ADD
    ax1.plot(t_us, VC, color='#D4AC0D', linewidth=1.6, label=r'Canal 1: Tensión en condensador $V_C(t)$')
    ax1.plot(t_us, VR, color=COLOR_TEAL, linewidth=1.6, label=r'Canal 2: Tensión en resistencia $V_R(t)$')
    ax1.plot(t_us, V_math_add, color=COLOR_CARMINE, linewidth=2.0, linestyle='-',
             label=r'MATH ADD (Rojo): $\mathrm{CH1} + \mathrm{CH2} \equiv V_{\mathrm{gen}}(t)$')

    ax1.axvline(semi_T * 1e6, color='black', linestyle=':', alpha=0.5)
    ax1.set_ylabel(r'Tensión instantánea (V)')
    ax1.set_ylim(-11.5, 12.5)
    ax1.yaxis.set_major_formatter(formatter_1dec)
    ax1.grid(True)
    ax1.legend(loc='lower right', framealpha=0.95, fontsize=8.8)
    ax1.set_title(r'Verificación Experimental de la Ley de Mallas de Kirchhoff (KVL): $V_C(t) + V_R(t) = V_{\mathrm{gen}}(t)$', pad=8, fontweight='bold')

    # Panel inferior: Error residual de la suma KVL (Delta V = Math - Vgen)
    delta_kvl = V_math_add - V_gen
    ax2.plot(t_us, delta_kvl, color=COLOR_DARK, linewidth=1.2, label=r'Discrepancia instantánea $[V_C(t) + V_R(t)] - V_{\mathrm{gen}}(t)$')
    ax2.axhline(0, color='black', linestyle='--', linewidth=0.8)
    ax2.set_xlabel(r'Tiempo $t$ ($\mu$s)')
    ax2.set_ylabel(r'$\Delta V_{\mathrm{KVL}}$ (V)')
    ax2.set_xlim(0, T * 1e6)
    ax2.set_ylim(-0.25, 0.25)
    ax2.xaxis.set_major_formatter(formatter_0dec)
    ax2.yaxis.set_major_formatter(formatter_2dec)
    ax2.grid(True)
    ax2.legend(loc='upper right', framealpha=0.95, fontsize=8.2)

    out_file = os.path.join(figures_dir, 'fig_suma_kvl.png')
    plt.savefig(out_file, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"[OK] Generada Figura 3: {out_file}")


# =============================================================================
# FIGURA 4: fig_paso20_thevenin.png
# =============================================================================
def plot_paso20_thevenin():
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8.5, 6.2), sharex=True,
                                   gridspec_kw={'hspace': 0.14})
    fig.patch.set_facecolor('white')
    ax1.set_facecolor('white')
    ax2.set_facecolor('white')

    # Parámetros del montaje experimental Paso 20 (Figura 9 y 10):
    # R1 = 9980 ohm, R2 = 6832 ohm, C = C3 = 34.55 nF (efectivo en banco)
    R1 = 9980.0
    R2 = 6832.0
    C = 34.55e-9
    V = 10.0
    f = 250.0
    T = 1.0 / f
    semi_T = T / 2.0

    # Parámetros Thévenin vistos por el condensador
    V_th = V * (R2 / (R1 + R2))  # ~ 4.064 V
    R_th = (R1 * R2) / (R1 + R2)  # ~ 4056 ohm
    tau_th = R_th * C              # ~ 140.1 us

    # Circuito RC simple de referencia (sin R2) para comparar
    tau_simple = R1 * C           # ~ 344.8 us

    t = np.linspace(0, T, 2500)
    t_us = t * 1e6
    semi_T_us = semi_T * 1e6

    # Evolución temporal de tensión en el condensador VC(t)
    VC_paso20 = np.where(
        t < semi_T,
        V_th * (1.0 - np.exp(-t / tau_th)),
        V_th * (1.0 - np.exp(-semi_T / tau_th)) * np.exp(-(t - semi_T) / tau_th)
    )

    VC_simple = np.where(
        t < semi_T,
        V * (1.0 - np.exp(-t / tau_simple)),
        V * (1.0 - np.exp(-semi_T / tau_simple)) * np.exp(-(t - semi_T) / tau_simple)
    )

    # Corrientes del circuito (en miliamperios)
    I_R1_mA = np.where(
        t < semi_T,
        ((V - VC_paso20) / R1) * 1e3,
        (-VC_paso20 / R1) * 1e3
    )

    I_C_mA = np.where(
        t < semi_T,
        (V / R1) * np.exp(-t / tau_th) * 1e3,
        -(V_th / R_th) * np.exp(-(t - semi_T) / tau_th) * 1e3
    )

    # --- Panel 1: Tensiones VC(t) ---
    ax1.plot(t_us, VC_paso20, color=COLOR_UNI_BLUE, linewidth=2.0,
             label=r'Paso 20 ($R_1$ serie con $R_2 \parallel C$): Asíntota $V_{C,\max} = V\frac{R_2}{R_1+R_2} = 4{,}06\ \mathrm{V}$')
    ax1.plot(t_us, VC_simple, color=COLOR_GRAY, linestyle='--', linewidth=1.4,
             label=r'Circuito RC simple de referencia (sin $R_2$): Asíntota $V_0 = 10{,}0\ \mathrm{V}$')
    ax1.axhline(V_th, color=COLOR_CARMINE, linestyle=':', linewidth=1.2,
                label=r'Voltaje de Thévenin $V_{\mathrm{th}} = 4{,}064\ \mathrm{V}$')
    ax1.axvline(semi_T_us, color='black', linestyle='--', linewidth=0.9, alpha=0.6)

    ax1.annotate(r'$V_{C,\max} = 4{,}06\ \mathrm{V}$' + '\n' + r'$\tau_{\mathrm{th}} = 140{,}1\ \mu\mathrm{s}$',
                 xy=(500, V_th), xytext=(700, V_th - 1.5),
                 arrowprops=dict(arrowstyle='->', color=COLOR_CARMINE, lw=1.2),
                 fontsize=8.5, bbox=dict(boxstyle='round,pad=0.3', facecolor='#FADBD8', edgecolor=COLOR_CARMINE, alpha=0.9))

    ax1.set_ylabel(r'Tensión $V_C$ (V)')
    ax1.set_ylim(-0.4, 11.0)
    ax1.yaxis.set_major_formatter(formatter_1dec)
    ax1.grid(True)
    ax1.legend(loc='upper right', framealpha=0.95, fontsize=8.2)
    ax1.set_title(r'Análisis de Régimen Transitorio del Montaje Paso 20 (Figura 9 y 10 — Teorema de Thévenin)', pad=8, fontweight='bold')

    # --- Panel 2: Corrientes I_R1(t) e I_C(t) ---
    ax2.plot(t_us, I_R1_mA, color=COLOR_CARMINE, linewidth=1.8,
             label=r'Corriente total por $R_1$: $I_{R1}(t)$')
    ax2.plot(t_us, I_C_mA, color=COLOR_TEAL, linestyle='-.', linewidth=1.6,
             label=r'Corriente neta por el condensador: $I_C(t)$')

    ax2.axhline(0, color='black', linestyle='-', linewidth=0.8, alpha=0.5)
    ax2.axvline(semi_T_us, color='black', linestyle='--', linewidth=0.9, alpha=0.6)

    # Valores críticos de corriente (Preguntas c y d)
    I_max_carga = (V / R1) * 1e3  # ~ 1.002 mA
    I_min_carga = (V / (R1 + R2)) * 1e3  # ~ 0.595 mA
    I_max_desc = -(V_th / R1) * 1e3  # ~ -0.407 mA

    ax2.scatter([0], [I_max_carga], color=COLOR_UNI_BLUE, zorder=5, s=32)
    ax2.annotate(r'$I_{\max,\mathrm{carga}} = \frac{V}{R_1} \approx 1{,}00\ \mathrm{mA}$',
                 xy=(0, I_max_carga), xytext=(150, I_max_carga + 0.12),
                 arrowprops=dict(arrowstyle='->', color=COLOR_UNI_BLUE, lw=1.1),
                 fontsize=8.2)

    ax2.scatter([semi_T_us - 100], [I_min_carga], color=COLOR_CARMINE, zorder=5, s=32)
    ax2.annotate(r'$I_{R1,\min} = \frac{V}{R_1+R_2} \approx 0{,}59\ \mathrm{mA}$',
                 xy=(semi_T_us - 100, I_min_carga), xytext=(semi_T_us - 750, I_min_carga + 0.25),
                 arrowprops=dict(arrowstyle='->', color=COLOR_CARMINE, lw=1.1),
                 fontsize=8.2)

    ax2.scatter([semi_T_us], [I_max_desc], color=COLOR_CARMINE, zorder=5, s=32)
    ax2.annotate(r'$I_{R1,\mathrm{descarga}}^{\max} = -\frac{V_{\mathrm{th}}}{R_1} \approx -0{,}41\ \mathrm{mA}$',
                 xy=(semi_T_us, I_max_desc), xytext=(semi_T_us + 120, I_max_desc - 0.30),
                 arrowprops=dict(arrowstyle='->', color=COLOR_CARMINE, lw=1.1),
                 fontsize=8.2)

    ax2.set_xlabel(r'Tiempo $t$ ($\mu$s)')
    ax2.set_ylabel(r'Corriente $I$ (mA)')
    ax2.set_xlim(0, T * 1e6)
    ax2.set_ylim(-1.3, 1.4)
    ax2.xaxis.set_major_formatter(formatter_0dec)
    ax2.yaxis.set_major_formatter(formatter_2dec)
    ax2.grid(True)
    ax2.legend(loc='lower right', framealpha=0.95, fontsize=8.2)

    out_file = os.path.join(figures_dir, 'fig_paso20_thevenin.png')
    plt.savefig(out_file, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"[OK] Generada Figura 4: {out_file}")


def main():
    print("Iniciando generación de figuras científicas a 300 DPI...")
    plot_carga_descarga()
    plot_linealizacion_tau()
    plot_suma_kvl()
    plot_paso20_thevenin()
    print("[OK] Todas las figuras fueron generadas exitosamente en Figures/.")

if __name__ == '__main__':
    main()
