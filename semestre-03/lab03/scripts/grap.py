#!/usr/bin/env python3
"""
Script: grap.py
Laboratorio 03: Curvas características Voltaje-Corriente (CF2B1 - Sección A)
Universidad Nacional de Ingeniería - Facultad de Ciencias

Genera gráficas científicas a 300 DPI con:
- Barras de error en variables dependientes e independientes.
- Regresiones OLS (resistencia) y ajustes no lineales (foquito y diodo).
- Paneles inferiores de residuos.
- Formateo de coma decimal con FuncFormatter.
- Diagrama esquemático del circuito experimental con reóstato potenciómetro.
"""

import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import matplotlib.patches as patches
from matplotlib.ticker import FuncFormatter
from scipy.optimize import curve_fit

# Asegurar backend no interactivo
plt.switch_backend('Agg')

# Directorio de salida de figuras
figures_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Figures'))
os.makedirs(figures_dir, exist_ok=True)

# Formateadores con coma decimal
def format_coma_1dec(val, pos):
    return f"{val:.1f}".replace('.', ',')

def format_coma_2dec(val, pos):
    return f"{val:.2f}".replace('.', ',')

def format_coma_3dec(val, pos):
    return f"{val:.3f}".replace('.', ',')

def format_coma_res(val, pos):
    return f"{val:+.3f}".replace('.', ',')

# ==============================================================================
# DATOS EXPERIMENTALES
# ==============================================================================

# Incertidumbres instrumentales
delta_V = 0.01   # V
delta_I = 0.001  # A

# 1. Resistencia de carbón (Nominal 100 Ω)
v_res = np.array([0.00, 1.00, 2.00, 3.05, 4.03, 5.00, 6.02, 6.49])
i_res = np.array([0.000, 0.010, 0.020, 0.031, 0.040, 0.050, 0.060, 0.065])

# 2. Lámpara incandescente (Foquito de tungsteno)
v_foq = np.array([0.00, 1.00, 2.02, 3.04, 4.01, 5.01, 6.01, 6.43])
i_foq = np.array([0.000, 0.148, 0.218, 0.272, 0.318, 0.366, 0.412, 0.432])

# 3. Diodo semiconductor de silicio
v_dio = np.array([0.00, 0.61, 0.69, 0.70, 0.71, 0.72, 0.73, 0.75])
i_dio = np.array([0.000, 0.050, 0.215, 0.230, 0.411, 0.537, 0.690, 0.783])

# ==============================================================================
# FIGURA 1: RESISTENCIA DE CARBÓN (LEY DE OHM) + RESIDUOS
# ==============================================================================
def plot_resistencia():
    # OLS para V vs I: V = R * I + b
    # Filtramos el punto (0,0) para evaluar el ajuste riguroso de los puntos activos
    # pero incluimos todos para la curva global
    x = v_res[1:]  # V (V)
    y = i_res[1:]  # I (A)
    
    # Ajuste I = G * V + b_I
    p_I, cov_I = np.polyfit(x, y, 1, cov=True)
    m_I, b_I = p_I[0], p_I[1]
    s_m_I = np.sqrt(cov_I[0, 0])
    s_b_I = np.sqrt(cov_I[1, 1])
    
    # Inverso: V = R * I + b_V
    p_V, cov_V = np.polyfit(y, x, 1, cov=True)
    R_fit, b_V = p_V[0], p_V[1]
    s_R = np.sqrt(cov_V[0, 0])
    s_b_V = np.sqrt(cov_V[1, 1])
    
    y_pred = m_I * x + b_I
    residuos = y - y_pred
    r2 = 1 - (np.sum(residuos**2) / np.sum((y - np.mean(y))**2))
    
    fig = plt.figure(figsize=(8, 6.2))
    fig.patch.set_facecolor('white')
    gs = gridspec.GridSpec(2, 1, height_ratios=[3.2, 1.0], hspace=0.12)
    
    ax_main = fig.add_subplot(gs[0])
    ax_res = fig.add_subplot(gs[1], sharex=ax_main)
    ax_main.set_facecolor('white')
    ax_res.set_facecolor('white')
    
    # Formateadores
    ax_main.xaxis.set_major_formatter(FuncFormatter(format_coma_1dec))
    ax_main.yaxis.set_major_formatter(FuncFormatter(format_coma_3dec))
    ax_res.xaxis.set_major_formatter(FuncFormatter(format_coma_1dec))
    ax_res.yaxis.set_major_formatter(FuncFormatter(format_coma_res))
    
    # Datos y ajuste
    v_line = np.linspace(0, 7.0, 200)
    ax_main.errorbar(v_res, i_res, xerr=delta_V, yerr=delta_I, fmt='o', color='#003865',
                     ecolor='#003865', elinewidth=1.2, capsize=3, capthick=1.2, markersize=5.5,
                     label=r'Pares medidos ($V \pm \delta V, I \pm \delta I$)', zorder=4)
    
    ax_main.plot(v_line, m_I * v_line + b_I, color='#D9534F', linewidth=1.8,
                 label=f'Ajuste MCO: $I = ({m_I*1e3:.2f} \\pm {s_m_I*1e3:.2f})\\times 10^{{-3}}\\,V + ({b_I*1e3:.2f} \\pm {s_b_I*1e3:.2f})\\times 10^{{-3}}$ A\n'
                       f'Resistencia experimental: $R = ({R_fit:.2f} \\pm {s_R:.2f})\\,\\Omega$ ($R^2 = {r2:.5f}$)', zorder=3)
    
    # Línea ideal teórica de 100 Ohms exactos pasando por el origen
    ax_main.plot(v_line, v_line / 100.0, color='gray', linestyle='--', linewidth=1.2,
                 label=r'Modelo óhmico ideal ($R_{\mathrm{nom}} = 100{,}0\,\Omega$)', zorder=2)
    
    ax_main.set_ylabel(r'Intensidad de corriente $I$ (A)', fontsize=11)
    ax_main.set_title(r'Característica Voltaje--Corriente: Resistencia de Carbón ($100\,\Omega$)', fontsize=12, fontweight='bold', pad=10)
    ax_main.grid(True, linestyle=':', alpha=0.6, color='gray')
    ax_main.legend(loc='upper left', framealpha=0.95, fontsize=9.2)
    plt.setp(ax_main.get_xticklabels(), visible=False)
    
    # Residuos
    ax_res.axhline(0, color='gray', linestyle='--', linewidth=1.2)
    ax_res.errorbar(x, residuos, yerr=delta_I, fmt='s', color='#003865',
                    ecolor='#003865', elinewidth=1.2, capsize=3, markersize=4.5, zorder=3)
    ax_res.set_xlabel(r'Diferencia de potencial $V$ (V)', fontsize=11)
    ax_res.set_ylabel(r'Residuo (A)', fontsize=9.5)
    ax_res.grid(True, linestyle=':', alpha=0.6, color='gray')
    ax_res.set_ylim(-0.0025, 0.0025)
    
    out_path = os.path.join(figures_dir, 'fig_resistencia_ohmica.png')
    plt.savefig(out_path, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"[OK] Generada: {out_path}")

# ==============================================================================
# FIGURA 2: FOQUITO INCANDESCENTE (MODELO NO LINEAL DE POTENCIAS) + RESIDUOS
# ==============================================================================
def plot_foquito():
    # Modelo I = k * V^n (para V > 0)
    x = v_foq[1:]
    y = i_foq[1:]
    
    # Ajuste en espacio logarítmico: ln(I) = ln(k) + n * ln(V)
    log_x = np.log(x)
    log_y = np.log(y)
    p_log, cov_log = np.polyfit(log_x, log_y, 1, cov=True)
    n_exp = p_log[0]
    ln_k = p_log[1]
    k_exp = np.exp(ln_k)
    s_n = np.sqrt(cov_log[0, 0])
    s_ln_k = np.sqrt(cov_log[1, 1])
    s_k = k_exp * s_ln_k
    
    # Evaluación no lineal
    v_line = np.linspace(0.01, 7.0, 200)
    y_line = k_exp * (v_line ** n_exp)
    
    y_pred = k_exp * (x ** n_exp)
    residuos = y - y_pred
    r2 = 1 - (np.sum(residuos**2) / np.sum((y - np.mean(y))**2))
    
    fig = plt.figure(figsize=(8, 6.2))
    fig.patch.set_facecolor('white')
    gs = gridspec.GridSpec(2, 1, height_ratios=[3.2, 1.0], hspace=0.12)
    
    ax_main = fig.add_subplot(gs[0])
    ax_res = fig.add_subplot(gs[1], sharex=ax_main)
    ax_main.set_facecolor('white')
    ax_res.set_facecolor('white')
    
    ax_main.xaxis.set_major_formatter(FuncFormatter(format_coma_1dec))
    ax_main.yaxis.set_major_formatter(FuncFormatter(format_coma_2dec))
    ax_res.xaxis.set_major_formatter(FuncFormatter(format_coma_1dec))
    ax_res.yaxis.set_major_formatter(FuncFormatter(format_coma_res))
    
    ax_main.errorbar(v_foq, i_foq, xerr=delta_V, yerr=delta_I, fmt='o', color='#D9534F',
                     ecolor='#D9534F', elinewidth=1.2, capsize=3, capthick=1.2, markersize=5.5,
                     label=r'Pares medidos ($V \pm \delta V, I \pm \delta I$)', zorder=4)
    
    ax_main.plot(v_line, y_line, color='#003865', linewidth=1.8,
                 label=f'Ajuste ley de potencias: $I = ({k_exp:.3f} \\pm {s_k:.3f})\\,V^{{{n_exp:.3f} \\pm {s_n:.3f}}}$ A\n'
                       f'Exponente $n < 1$ evidencia comportamiento termorresistivo ($R^2 = {r2:.4f}$)', zorder=3)
    
    # Línea tangente inicial en frío (R_frio = 1 V / 0.148 A = 6.76 Ohms)
    ax_main.plot(v_line, v_line / 6.76, color='gray', linestyle=':', linewidth=1.2,
                 label=r'Comportamiento tangencial en frío ($R_0 \approx 6{,}76\,\Omega$)', zorder=2)
    
    ax_main.set_ylabel(r'Intensidad de corriente $I$ (A)', fontsize=11)
    ax_main.set_title(r'Característica Voltaje--Corriente: Lámpara Incandescente (Tungsteno)', fontsize=12, fontweight='bold', pad=10)
    ax_main.grid(True, linestyle=':', alpha=0.6, color='gray')
    ax_main.legend(loc='lower right', framealpha=0.95, fontsize=9.2)
    ax_main.set_ylim(-0.02, 0.50)
    plt.setp(ax_main.get_xticklabels(), visible=False)
    
    # Residuos
    ax_res.axhline(0, color='gray', linestyle='--', linewidth=1.2)
    ax_res.errorbar(x, residuos, yerr=delta_I, fmt='s', color='#D9534F',
                    ecolor='#D9534F', elinewidth=1.2, capsize=3, markersize=4.5, zorder=3)
    ax_res.set_xlabel(r'Diferencia de potencial $V$ (V)', fontsize=11)
    ax_res.set_ylabel(r'Residuo (A)', fontsize=9.5)
    ax_res.grid(True, linestyle=':', alpha=0.6, color='gray')
    ax_res.set_ylim(-0.015, 0.015)
    
    out_path = os.path.join(figures_dir, 'fig_foquito_tungsteno.png')
    plt.savefig(out_path, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"[OK] Generada: {out_path}")

# ==============================================================================
# FIGURA 3: DIODO SEMICONDUCTOR DE SILICIO
# ==============================================================================
def plot_diodo():
    fig = plt.figure(figsize=(8, 5.8))
    fig.patch.set_facecolor('white')
    ax = fig.add_subplot(111)
    ax.set_facecolor('white')
    
    ax.xaxis.set_major_formatter(FuncFormatter(format_coma_2dec))
    ax.yaxis.set_major_formatter(FuncFormatter(format_coma_2dec))
    
    # Separamos el punto atípico (índice 3: V=0.70, I=0.230)
    v_norm = np.array([v_dio[i] for i in range(len(v_dio)) if i != 3])
    i_norm = np.array([i_dio[i] for i in range(len(i_dio)) if i != 3])
    
    # Ajuste de curva exponencial Shockley aproximada en conducción directa: I = I0 * (exp(V / V0) - 1)
    # Ajustamos sobre los puntos normales con V >= 0.61 V
    v_cond = v_norm[1:]
    i_cond = i_norm[1:]
    
    def shockley(v, i_s, v_t):
        return i_s * (np.exp(v / v_t) - 1.0)
    
    try:
        popt, _ = curve_fit(shockley, v_cond, i_cond, p0=[1e-9, 0.040], maxfev=10000)
        v_model = np.linspace(0.50, 0.76, 200)
        i_model = shockley(v_model, *popt)
        fit_ok = True
    except Exception:
        fit_ok = False
    
    # Trazamos los puntos experimentales válidos
    ax.errorbar(v_norm, i_norm, xerr=delta_V, yerr=delta_I, fmt='o', color='#2E7D32',
                ecolor='#2E7D32', elinewidth=1.4, capsize=3.5, capthick=1.4, markersize=6,
                label=r'Puntos válidos ($V \pm \delta V, I \pm \delta I$)', zorder=5)
    
    # Punto anómalo / sobrescrito en hoja
    ax.errorbar([v_dio[3]], [i_dio[3]], xerr=delta_V, yerr=delta_I, fmt='D', color='#E65100',
                ecolor='#E65100', elinewidth=1.4, capsize=4, capthick=1.4, markersize=7,
                label=r'Punto $N^\circ 4$ anómalo/sobrescrito ($0{,}70\,\text{V}; 0{,}230\,\text{A}$)', zorder=6)
    
    if fit_ok:
        ax.plot(v_model, i_model, color='#1B5E20', linewidth=1.8, linestyle='-',
                label=r'Ajuste Shockley de conducción directa: $I \propto \exp(V/\eta V_T)$', zorder=3)
    
    # Proyección de tensión umbral (tangente en la zona de máxima pendiente de conducción)
    # Tomamos los últimos 3 puntos para trazar la recta tangente dinámica
    p_tang = np.polyfit(v_norm[-3:], i_norm[-3:], 1)
    v_tang_axis = np.linspace(0.65, 0.76, 100)
    i_tang_axis = p_tang[0] * v_tang_axis + p_tang[1]
    v_umbral = -p_tang[1] / p_tang[0]
    
    ax.plot(v_tang_axis, i_tang_axis, color='#7CB342', linestyle='--', linewidth=1.4,
            label=f'Tangente de conducción lineal (Tensión umbral $V_u \\approx {v_umbral:.2f}\\,\\text{{V}}$)', zorder=2)
    
    # Línea vertical en tensión umbral
    ax.axvline(v_umbral, color='gray', linestyle=':', linewidth=1.2, alpha=0.8)
    ax.text(v_umbral - 0.035, 0.45, f'$V_u \\approx {v_umbral:.2f}\\,\\mathrm{{V}}$', fontsize=10,
            fontweight='bold', color='#1B5E20', rotation=90)
    
    ax.set_xlabel(r'Diferencia de potencial $V$ (V)', fontsize=11)
    ax.set_ylabel(r'Intensidad de corriente $I$ (A)', fontsize=11)
    ax.set_title(r'Característica Voltaje--Corriente: Diodo Semiconductor de Silicio', fontsize=12, fontweight='bold', pad=10)
    ax.grid(True, linestyle=':', alpha=0.6, color='gray')
    ax.legend(loc='upper left', framealpha=0.95, fontsize=9.2)
    ax.set_xlim(-0.02, 0.80)
    ax.set_ylim(-0.03, 0.88)
    
    out_path = os.path.join(figures_dir, 'fig_diodo_silicio.png')
    plt.savefig(out_path, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"[OK] Generada: {out_path}")

# ==============================================================================
# FIGURA 4: COMPARACIÓN GLOBAL DE LOS TRES ELEMENTOS
# ==============================================================================
def plot_comparativa():
    fig = plt.figure(figsize=(8.5, 5.8))
    fig.patch.set_facecolor('white')
    ax = fig.add_subplot(111)
    ax.set_facecolor('white')
    
    ax.xaxis.set_major_formatter(FuncFormatter(format_coma_1dec))
    ax.yaxis.set_major_formatter(FuncFormatter(format_coma_2dec))
    
    # Curvas trazadas
    # 1. Resistencia
    ax.errorbar(v_res, i_res, xerr=delta_V, yerr=delta_I, fmt='o-', color='#003865',
                linewidth=1.4, markersize=5, capsize=2.5,
                label=r'Resistencia carbón ($100\,\Omega$): Lineal óhmico ($R = \mathrm{cte}$)', zorder=3)
    
    # 2. Foquito
    ax.errorbar(v_foq, i_foq, xerr=delta_V, yerr=delta_I, fmt='s-', color='#D9534F',
                linewidth=1.4, markersize=5, capsize=2.5,
                label=r'Foquito tungsteno: Sublineal termorresistivo ($R$ crece con $I$)', zorder=4)
    
    # 3. Diodo
    ax.errorbar(v_dio, i_dio, xerr=delta_V, yerr=delta_I, fmt='^-', color='#2E7D32',
                linewidth=1.4, markersize=5.5, capsize=2.5,
                label=r'Diodo silicio: Superlineal exponencial ($R$ decrece con $I$)', zorder=5)
    
    ax.set_xlabel(r'Diferencia de potencial aplicada $V$ (V)', fontsize=11)
    ax.set_ylabel(r'Intensidad de corriente $I$ (A)', fontsize=11)
    ax.set_title(r'Contraste Comparativo de Características $I$--$V$ para Tres Elementos', fontsize=12, fontweight='bold', pad=10)
    ax.grid(True, linestyle=':', alpha=0.6, color='gray')
    ax.legend(loc='upper left', framealpha=0.95, fontsize=9.5)
    ax.set_xlim(-0.1, 7.0)
    ax.set_ylim(-0.03, 0.88)
    
    out_path = os.path.join(figures_dir, 'fig_comparativa_elementos.png')
    plt.savefig(out_path, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"[OK] Generada: {out_path}")

# ==============================================================================
# FIGURA 5: RESISTENCIA APARENTE R = V/I vs CORRIENTE I
# ==============================================================================
def plot_resistencia_vs_corriente():
    fig = plt.figure(figsize=(8.5, 5.8))
    fig.patch.set_facecolor('white')
    ax = fig.add_subplot(111)
    ax.set_facecolor('white')
    
    ax.xaxis.set_major_formatter(FuncFormatter(format_coma_2dec))
    ax.yaxis.set_major_formatter(FuncFormatter(format_coma_1dec))
    
    # Cálculo de R = V / I para puntos activos (excluyendo V=0)
    # Resistencia
    r_calc_res = v_res[1:] / i_res[1:]
    # Foquito
    r_calc_foq = v_foq[1:] / i_foq[1:]
    # Diodo (excluyendo punto atípico 3)
    idx_dio_val = [i for i in range(1, len(v_dio)) if i != 3]
    r_calc_dio = v_dio[idx_dio_val] / i_dio[idx_dio_val]
    i_dio_val = i_dio[idx_dio_val]
    
    ax.plot(i_res[1:], r_calc_res, 'o-', color='#003865', linewidth=1.5, markersize=6,
            label=r'Resistencia de carbón: $R \approx 100\,\Omega$ ($\Delta R/R \approx 0{,}8\%$, invariable)')
    
    ax.plot(i_foq[1:], r_calc_foq, 's-', color='#D9534F', linewidth=1.5, markersize=6,
            label=r'Lámpara incandescente: $R$ crece de $6{,}8\,\Omega$ a $14{,}9\,\Omega$ ($+119\%$)')
    
    ax.plot(i_dio_val, r_calc_dio, '^-', color='#2E7D32', linewidth=1.5, markersize=6.5,
            label=r'Diodo semiconductor: $R$ decrece de $12{,}2\,\Omega$ a $0{,}96\,\Omega$ ($-92\%$)')
    
    ax.set_xlabel(r'Intensidad de corriente $I$ (A)', fontsize=11)
    ax.set_ylabel(r'Resistencia estática aparente $R = V/I$ ($\Omega$)', fontsize=11)
    ax.set_title(r'Evolución de la Resistencia Estática $R(I)$ según el Régimen Conductor', fontsize=12, fontweight='bold', pad=10)
    ax.grid(True, linestyle=':', alpha=0.6, color='gray')
    ax.legend(loc='center right', framealpha=0.95, fontsize=9.2)
    ax.set_xlim(-0.02, 0.85)
    ax.set_ylim(0, 110)
    
    out_path = os.path.join(figures_dir, 'fig_resistencia_vs_corriente.png')
    plt.savefig(out_path, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"[OK] Generada: {out_path}")

# ==============================================================================
# FIGURA 6: DIAGRAMA ESQUEMÁTICO DEL CIRCUITO CON POTENCIÓMETRO
# ==============================================================================
def plot_circuito_esquema():
    fig, ax = plt.subplots(figsize=(8, 4.5))
    fig.patch.set_facecolor('white')
    ax.set_facecolor('white')
    
    # Dibujar líneas del circuito
    # Fuente DC a la izquierda
    ax.plot([1.0, 1.0], [1.0, 4.0], 'k-', lw=2)
    ax.plot([0.7, 1.3], [2.7, 2.7], 'k-', lw=3)  # Placa positiva
    ax.plot([0.85, 1.15], [2.3, 2.3], 'k-', lw=2) # Placa negativa
    ax.text(0.4, 2.5, r'$V_{\mathrm{in}} = 7{,}5\,\mathrm{V}$' + '\n(Fuente DC)', fontsize=10, ha='center', va='center')
    ax.text(1.2, 2.85, r'$+$', fontsize=12, fontweight='bold')
    ax.text(1.2, 2.05, r'$-$', fontsize=14, fontweight='bold')
    
    # Conexiones superiores e inferiores hacia el reóstato
    ax.plot([1.0, 3.5], [4.0, 4.0], 'k-', lw=2)
    ax.plot([1.0, 3.5], [1.0, 1.0], 'k-', lw=2)
    
    # Reóstato como divisor de voltaje (cuerpo resistivo vertical)
    ax.plot([3.5, 3.5], [1.0, 1.5], 'k-', lw=2)
    # Zig-zag del reóstato
    y_vals = np.linspace(1.5, 3.5, 9)
    x_vals = [3.5, 3.7, 3.3, 3.7, 3.3, 3.7, 3.3, 3.7, 3.5]
    ax.plot(x_vals, y_vals, 'k-', lw=2)
    ax.plot([3.5, 3.5], [3.5, 4.0], 'k-', lw=2)
    ax.text(2.6, 2.5, 'Reóstato\n(Potenciómetro\ndivisor de $V$)', fontsize=9.5, ha='center', va='center')
    
    # Flecha del cursor móvil
    ax.annotate('', xy=(3.5, 2.7), xytext=(4.3, 2.7),
                arrowprops=dict(facecolor='black', shrink=0.05, width=1.5, headwidth=7))
    ax.plot([4.3, 5.0], [2.7, 2.7], 'k-', lw=2)
    ax.text(4.2, 3.0, 'Cursor móvil', fontsize=9, ha='center')
    
    # Amperímetro en serie
    ax.plot([5.0, 5.5], [2.7, 2.7], 'k-', lw=2)
    circle_A = plt.Circle((5.8, 2.7), 0.3, color='#003865', fill=False, lw=2)
    ax.add_patch(circle_A)
    ax.text(5.8, 2.7, 'A', fontsize=12, fontweight='bold', ha='center', va='center', color='#003865')
    ax.text(5.8, 3.2, 'Amperímetro\n(en serie)', fontsize=8.5, ha='center', color='#003865')
    ax.plot([6.1, 7.0], [2.7, 2.7], 'k-', lw=2)
    
    # Elemento bajo prueba (entre bornes a y b)
    ax.plot([7.0, 7.0], [2.7, 2.3], 'k-', lw=2)
    # Caja del elemento
    rect = plt.Rectangle((6.5, 1.7), 1.0, 0.6, fill=True, facecolor='#E3F2FD', edgecolor='#003865', lw=2)
    ax.add_patch(rect)
    ax.text(7.0, 2.0, 'Elemento\n(E1, E2, E3)', fontsize=9, fontweight='bold', ha='center', va='center')
    ax.plot([7.0, 7.0], [1.7, 1.0], 'k-', lw=2)
    
    # Bornes a y b
    ax.plot(7.0, 2.4, 'ro', markersize=5)
    ax.text(7.25, 2.4, 'a', fontsize=11, fontweight='bold', color='red')
    ax.plot(7.0, 1.3, 'ro', markersize=5)
    ax.text(7.25, 1.3, 'b', fontsize=11, fontweight='bold', color='red')
    
    # Retorno a la línea de tierra común del potenciómetro
    ax.plot([7.0, 3.5], [1.0, 1.0], 'k-', lw=2)
    
    # Voltímetro en paralelo entre a y b
    ax.plot([7.0, 8.2], [2.4, 2.4], 'k--', lw=1.5)
    ax.plot([8.2, 8.2], [2.4, 2.1], 'k--', lw=1.5)
    circle_V = plt.Circle((8.2, 1.85), 0.28, color='#D9534F', fill=False, lw=2)
    ax.add_patch(circle_V)
    ax.text(8.2, 1.85, 'V', fontsize=12, fontweight='bold', ha='center', va='center', color='#D9534F')
    ax.text(8.9, 1.85, 'Voltímetro\n(en paralelo)', fontsize=8.5, ha='left', va='center', color='#D9534F')
    ax.plot([8.2, 8.2], [1.57, 1.3], 'k--', lw=1.5)
    ax.plot([8.2, 7.0], [1.3, 1.3], 'k--', lw=1.5)
    
    ax.set_xlim(0, 10.2)
    ax.set_ylim(0.5, 4.5)
    ax.axis('off')
    ax.set_title(r'Esquema del Montaje Experimental: Circuito Potenciométrico y Medición de Curvas $V$--$I$',
                 fontsize=11.5, fontweight='bold', pad=10)
    
    out_path = os.path.join(figures_dir, 'fig_circuito_potenciometro.png')
    plt.savefig(out_path, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"[OK] Generada: {out_path}")

# ==============================================================================
# FIGURA 7: DIAGRAMA DE BLOQUES Y ESTRUCTURA DEL REÓSTATO (TEST N°3 - PREG. 4)
# ==============================================================================
def plot_reostato_diagrama_bloques():
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 7.5), gridspec_kw={'height_ratios': [1.1, 1.0]})
    fig.patch.set_facecolor('white')

    # --- Panel 1: Estructura Física y Terminales ---
    ax1.set_facecolor('white')
    ax1.set_xlim(-0.5, 11.5)
    ax1.set_ylim(-1.2, 5.0)
    ax1.axis('off')
    ax1.set_title(r'(a) Estructura Física y Configuración de Terminales del Reóstato de Laboratorio',
                  fontsize=11.5, fontweight='bold', color='#003865', pad=10)

    # Cilindro cerámico
    cyl = patches.FancyBboxPatch((1.5, 0.8), 7.0, 1.6, boxstyle='round,pad=0.1,rounding_size=0.2',
                                 facecolor='#EDE8E3', edgecolor='#7D6B58', lw=2)
    ax1.add_patch(cyl)
    ax1.text(5.0, 1.6, 'Cilindro Cerámico Aislante (Soporte Refractario)', color='#7D6B58',
             fontsize=9.5, fontweight='bold', ha='center', va='center')

    # Espiras de alambre resistivo (bobinado)
    for x in np.linspace(1.8, 8.2, 26):
        ax1.plot([x, x], [0.8, 2.4], color='#333333', lw=2)
        ax1.plot([x, x+0.12], [2.4, 2.4], color='#555555', lw=1.5)

    # Barra colectora superior
    rod = patches.Rectangle((1.5, 3.4), 7.0, 0.35, facecolor='#B0BEC5', edgecolor='#37474F', lw=1.8)
    ax1.add_patch(rod)
    ax1.text(5.0, 3.9, 'Barra Colectora Metálica Deslizante (Baja Resistencia)',
             fontsize=9, ha='center', color='#37474F', fontstyle='italic')

    # Cursor deslizante C
    slider = patches.FancyBboxPatch((4.5, 2.2), 1.0, 1.4, boxstyle='round,pad=0.05,rounding_size=0.1',
                                    facecolor='#003865', edgecolor='#001F3F', lw=1.5)
    ax1.add_patch(slider)
    ax1.annotate('', xy=(5.0, 2.2), xytext=(5.0, 3.4),
                 arrowprops=dict(arrowstyle='<->', color='yellow', lw=2.5))
    ax1.text(5.0, 2.7, 'Cursor\nMóvil', color='white', fontsize=8, fontweight='bold', ha='center', va='center')

    # Terminal C
    ax1.plot([5.0, 5.0], [3.75, 4.5], color='#003865', lw=2.5)
    ax1.plot(5.0, 4.5, 'o', color='#003865', markersize=9)
    ax1.text(5.0, 4.8, 'Terminal C (Cursor / Salida Variable)', fontsize=9.5, fontweight='bold',
             ha='center', color='#003865')

    # Terminal A
    ax1.plot([1.5, 0.5], [1.6, 1.6], color='#003865', lw=2.5)
    ax1.plot([0.5, 0.5], [1.6, 0.0], color='#003865', lw=2.5)
    ax1.plot(0.5, 0.0, 'o', color='#003865', markersize=9)
    ax1.text(0.5, -0.4, 'Terminal A (Fijo)\nEntrada (+)', fontsize=9, fontweight='bold',
             ha='center', color='#003865')

    # Terminal B
    ax1.plot([8.5, 9.5], [1.6, 1.6], color='#003865', lw=2.5)
    ax1.plot([9.5, 9.5], [1.6, 0.0], color='#003865', lw=2.5)
    ax1.plot(9.5, 0.0, 'o', color='#003865', markersize=9)
    ax1.text(9.5, -0.4, 'Terminal B (Fijo)\nReferencia ($-$)', fontsize=9, fontweight='bold',
             ha='center', color='#003865')

    # Cotas de resistencia dividida
    ax1.annotate('', xy=(1.5, 0.2), xytext=(5.0, 0.2),
                 arrowprops=dict(arrowstyle='<->', color='#B71C1C', lw=1.8))
    ax1.text(3.25, 0.4, r'$R_1 = R_{AC}(x) = R_T \cdot (x/L)$', fontsize=9, color='#B71C1C',
             ha='center', fontweight='bold')

    ax1.annotate('', xy=(5.0, 0.2), xytext=(8.5, 0.2),
                 arrowprops=dict(arrowstyle='<->', color='#1B5E20', lw=1.8))
    ax1.text(6.75, 0.4, r'$R_2 = R_{CB}(x) = R_T \cdot (1 - x/L)$', fontsize=9, color='#1B5E20',
             ha='center', fontweight='bold')

    # --- Panel 2: Diagrama de Bloques Funcional ---
    ax2.set_facecolor('white')
    ax2.set_xlim(-0.5, 11.5)
    ax2.set_ylim(-0.5, 4.0)
    ax2.axis('off')
    ax2.set_title(r'(b) Diagrama de Bloques Funcional: Operación como Divisor Potenciométrico de Tensión',
                  fontsize=11.5, fontweight='bold', color='#003865', pad=10)

    # Bloque 1: Fuente
    b1 = patches.FancyBboxPatch((0.2, 1.2), 2.2, 1.6, boxstyle='round,pad=0.1,rounding_size=0.15',
                                facecolor='#E3F2FD', edgecolor='#0277BD', lw=2)
    ax2.add_patch(b1)
    ax2.text(1.3, 2.0, 'FUENTE DC\nESTABILIZADA\n' + r'$V_{\mathrm{in}} = 7{,}5\,\mathrm{V}$',
             fontsize=8.5, fontweight='bold', ha='center', va='center', color='#01579B')

    ax2.annotate('', xy=(3.4, 2.4), xytext=(2.4, 2.4),
                 arrowprops=dict(arrowstyle='->', color='#01579B', lw=2))
    ax2.text(2.9, 2.65, r'Borne A (+)', fontsize=8, ha='center', color='#01579B', fontweight='bold')

    ax2.annotate('', xy=(3.4, 1.4), xytext=(2.4, 1.4),
                 arrowprops=dict(arrowstyle='->', color='#01579B', lw=2))
    ax2.text(2.9, 1.15, r'Borne B ($-$)', fontsize=8, ha='center', color='#01579B', fontweight='bold')

    # Bloque 2: Red Potenciométrica
    b2 = patches.FancyBboxPatch((3.4, 0.8), 3.8, 2.4, boxstyle='round,pad=0.1,rounding_size=0.15',
                                facecolor='#FFF8E1', edgecolor='#FF8F00', lw=2)
    ax2.add_patch(b2)
    ax2.text(5.3, 2.6, 'REÓSTATO (DIVISOR RESISTIVO)\n' + r'Resistencia total: $R_T = R_1 + R_2$',
             fontsize=8.5, fontweight='bold', ha='center', va='center', color='#E65100')
    ax2.text(5.3, 1.6, r'Segmento superior: $R_1(x)$' + '\n' +
                       r'Segmento inferior: $R_2(x)$' + '\n' +
                       r'Cursor deslizante: $C$',
             fontsize=8, ha='center', va='center', color='#BF360C')

    # Flecha Divisor -> Carga
    ax2.annotate('', xy=(8.2, 2.3), xytext=(7.2, 2.3),
                 arrowprops=dict(arrowstyle='->', color='#D84315', lw=2.2))
    ax2.text(7.7, 2.7, r'Cursor C' + '\n' + r'$V_{\mathrm{out}}(x)$', fontsize=8,
             ha='center', color='#D84315', fontweight='bold')

    ax2.plot([7.2, 8.2], [1.3, 1.3], color='#37474F', lw=2)
    ax2.text(7.7, 1.05, r'Común (Borne B)', fontsize=8, ha='center', color='#37474F')

    # Bloque 3: Carga
    b3 = patches.FancyBboxPatch((8.2, 0.9), 2.8, 2.1, boxstyle='round,pad=0.1,rounding_size=0.15',
                                facecolor='#E8F5E9', edgecolor='#2E7D32', lw=2)
    ax2.add_patch(b3)
    ax2.text(9.6, 1.95, 'ELEMENTO DE PRUEBA\n(CARGA EXPERIMENTAL)\n' +
                        r'$V_{\mathrm{out}} \in [0{,}00\,;\,6{,}50]\,\mathrm{V}$' + '\n\n' +
                        r'$V_{\mathrm{out}}(x) = V_{\mathrm{in}} \cdot \frac{R_2(x)}{R_T}$',
             fontsize=8, fontweight='bold', ha='center', va='center', color='#1B5E20')

    plt.tight_layout()
    out_path = os.path.join(figures_dir, 'fig_reostato_diagrama_bloques.png')
    plt.savefig(out_path, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"[OK] Generada: {out_path}")

# ==============================================================================
# FIGURA 8: CIRCUITO ESPECÍFICO DEL DIODO (TEST N°3 - PREG. 5)
# ==============================================================================
def plot_circuito_diodo_especifico():
    fig = plt.figure(figsize=(10, 5.5))
    fig.patch.set_facecolor('white')
    ax = fig.add_subplot(1, 1, 1)
    ax.set_facecolor('white')
    ax.set_xlim(-0.2, 11.2)
    ax.set_ylim(-0.2, 6.2)
    ax.axis('off')
    ax.set_title(r'Montaje Experimental del Circuito Potenciométrico para la Caracterización del Diodo de Silicio',
                 fontsize=11.5, fontweight='bold', color='#003865', pad=12)

    # Fuente DC
    ax.plot([0.8, 0.8], [1.2, 5.0], color='#111111', lw=2)
    ax.plot([0.5, 1.1], [3.3, 3.3], color='#003865', lw=3.5)
    ax.plot([0.65, 0.95], [2.9, 2.9], color='#003865', lw=2.2)
    ax.text(0.8, 3.6, r'$+$', fontsize=12, fontweight='bold', ha='center', color='#003865')
    ax.text(0.8, 2.55, r'$-$', fontsize=14, fontweight='bold', ha='center', color='#003865')
    ax.text(0.15, 3.1, 'Fuente DC\n' + r'$V_{\mathrm{in}} = 7{,}5\,\mathrm{V}$' + '\n(Estabilizada)',
            fontsize=9, ha='center', va='center', fontweight='bold', color='#003865')

    ax.plot([0.8, 3.2], [5.0, 5.0], color='#111111', lw=2)
    ax.plot([0.8, 3.2], [1.2, 1.2], color='#111111', lw=2)

    # Reóstato
    ax.plot([3.2, 3.2], [5.0, 4.6], color='#111111', lw=2)
    ax.plot([3.2, 3.2], [1.6, 1.2], color='#111111', lw=2)
    ax.plot(3.2, 4.6, 'o', color='#003865', markersize=7)
    ax.text(2.85, 4.6, 'A', fontsize=11, fontweight='bold', color='#003865')
    ax.plot(3.2, 1.6, 'o', color='#003865', markersize=7)
    ax.text(2.85, 1.6, 'B', fontsize=11, fontweight='bold', color='#003865')

    y_z = np.linspace(1.6, 4.6, 11)
    x_z = [3.2, 3.45, 2.95, 3.45, 2.95, 3.45, 2.95, 3.45, 2.95, 3.45, 3.2]
    ax.plot(x_z, y_z, color='#111111', lw=2.2)
    ax.text(2.1, 3.1, 'Reóstato\ncomo divisor\nde tensión\n' + r'($R_T$)',
            fontsize=8.5, ha='center', va='center', color='#555555')

    # Cursor C
    ax.annotate('', xy=(3.2, 3.4), xytext=(4.1, 3.4),
                arrowprops=dict(facecolor='#D84315', edgecolor='#D84315', shrink=0.02, width=2, headwidth=8))
    ax.plot(4.1, 3.4, 'o', color='#D84315', markersize=7)
    ax.text(4.1, 3.75, 'C (Cursor)', fontsize=10, fontweight='bold', color='#D84315', ha='center')

    # Línea al amperímetro
    ax.plot([4.1, 5.2], [3.4, 3.4], color='#111111', lw=2)
    ax.annotate('', xy=(4.8, 3.4), xytext=(4.4, 3.4),
                arrowprops=dict(arrowstyle='->', color='#B71C1C', lw=2))
    ax.text(4.6, 3.65, r'$I_D$', fontsize=10, fontweight='bold', color='#B71C1C', ha='center')

    cir_A = patches.Circle((5.6, 3.4), 0.35, facecolor='white', edgecolor='#003865', lw=2.2)
    ax.add_patch(cir_A)
    ax.text(5.6, 3.4, 'A', fontsize=12, fontweight='bold', ha='center', va='center', color='#003865')
    ax.text(5.6, 4.05, 'Amperímetro Digital\n(en serie, escala 0--1 A)', fontsize=8, ha='center', color='#003865')

    ax.plot([5.95, 7.0], [3.4, 3.4], color='#111111', lw=2)

    # Diodo
    ax.plot(7.0, 3.4, 'ro', markersize=5)
    ax.text(6.85, 3.7, 'a (+)', fontsize=9.5, fontweight='bold', color='#B71C1C')

    diodo_x = [7.2, 7.2, 7.8]
    diodo_y = [2.9, 3.9, 3.4]
    diodo_poly = patches.Polygon(np.column_stack([diodo_x, diodo_y]), closed=True,
                                 facecolor='#BBDEFB', edgecolor='#003865', lw=2)
    ax.add_patch(diodo_poly)
    ax.plot([7.8, 7.8], [2.85, 3.95], color='#003865', lw=3)
    ax.plot([7.0, 7.2], [3.4, 3.4], color='#111111', lw=2)
    ax.plot([7.8, 8.4], [3.4, 3.4], color='#111111', lw=2)

    ax.text(7.1, 2.6, 'Ánodo (p)', fontsize=8.5, ha='center', color='#003865', fontweight='bold')
    ax.text(7.9, 2.6, 'Cátodo (n)', fontsize=8.5, ha='center', color='#003865', fontweight='bold')
    ax.text(7.5, 4.25, 'Diodo Semiconductor\n(Juntura p-n de Si)', fontsize=9,
            fontweight='bold', ha='center', color='#003865')

    ax.plot(8.4, 3.4, 'ro', markersize=5)
    ax.text(8.55, 3.7, 'b ($-$)', fontsize=9.5, fontweight='bold', color='#B71C1C')

    # Cierre de lazo
    ax.plot([8.4, 8.4], [3.4, 1.2], color='#111111', lw=2)
    ax.plot([8.4, 3.2], [1.2, 1.2], color='#111111', lw=2)
    ax.text(5.8, 0.85, 'Conductor común de retorno hacia borne B (0 V)',
            fontsize=8.5, color='#555555', ha='center')

    # Voltímetro
    ax.plot([7.0, 7.0], [3.4, 5.2], color='#D9534F', lw=1.8, linestyle='--')
    ax.plot([7.0, 7.3], [5.2, 5.2], color='#D9534F', lw=1.8, linestyle='--')

    cir_V = patches.Circle((7.7, 5.2), 0.35, facecolor='white', edgecolor='#D9534F', lw=2.2)
    ax.add_patch(cir_V)
    ax.text(7.7, 5.2, 'V', fontsize=12, fontweight='bold', ha='center', va='center', color='#D9534F')
    ax.text(7.7, 5.8, 'Voltímetro Digital (en paralelo, escala 0--10 V)\nMide caída directa neta ' + r'$V_D$',
            fontsize=8, ha='center', color='#D9534F', fontweight='bold')

    ax.plot([8.1, 8.4], [5.2, 5.2], color='#D9534F', lw=1.8, linestyle='--')
    ax.plot([8.4, 8.4], [5.2, 3.4], color='#D9534F', lw=1.8, linestyle='--')

    # Info box
    info_box = patches.FancyBboxPatch((9.2, 0.6), 1.9, 5.0, boxstyle='round,pad=0.1,rounding_size=0.15',
                                      facecolor='#F5F5F5', edgecolor='#9E9E9E', lw=1.5)
    ax.add_patch(info_box)
    ax.text(10.15, 5.25, 'REGÍMENES\nDE OPERACIÓN', fontsize=8.5, fontweight='bold', ha='center', color='#212121')

    ax.text(10.15, 4.3, r'$\mathbf{1.\;Corte/Bloqueo}$' + '\n' +
                         r'$0 \leq V_D < 0{,}60\,\mathrm{V}$' + '\n' +
                         r'$I_D \approx 0{,}000\,\mathrm{A}$',
            fontsize=7.5, ha='center', color='#424242')

    ax.text(10.15, 3.0, r'$\mathbf{2.\;Zona\;del\;Codo}$' + '\n' +
                         r'$0{,}60 \leq V_D \leq 0{,}66\,\mathrm{V}$' + '\n' +
                         r'Umbral $V_u \approx 0{,}66\,\mathrm{V}$',
            fontsize=7.5, ha='center', color='#E65100')

    ax.text(10.15, 1.6, r'$\mathbf{3.\;Conducción\;Exp.}$' + '\n' +
                         r'$0{,}66 < V_D \leq 0{,}75\,\mathrm{V}$' + '\n' +
                         r'$I_D \to 0{,}783\,\mathrm{A}$' + '\n' +
                         r'¡Cuidado con $I_{\mathrm{max}}$!',
            fontsize=7.5, ha='center', color='#B71C1C')

    out_path = os.path.join(figures_dir, 'fig_circuito_diodo_especifico.png')
    plt.savefig(out_path, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"[OK] Generada: {out_path}")

# ==============================================================================
# EJECUCIÓN PRINCIPAL
# ==============================================================================
if __name__ == '__main__':
    print("[*] Iniciando generación de gráficas científicas a 300 DPI...")
    plot_resistencia()
    plot_foquito()
    plot_diodo()
    plot_comparativa()
    plot_resistencia_vs_corriente()
    plot_circuito_esquema()
    plot_reostato_diagrama_bloques()
    plot_circuito_diodo_especifico()
    print("[DONE] Todas las figuras fueron generadas exitosamente en lab03/Figures/")

