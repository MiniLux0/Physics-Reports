#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script: grap.py
Laboratorio N.° 01: El osciloscopio como instrumento de medida
Facultad de Ciencias — Universidad Nacional de Ingeniería (UNI)

Generación de gráficas científicas de alta calidad (300 DPI, coma decimal):
1. Gráfica 1: Calibración y Comparación de Voltajes DC (V_osc vs V_mult con ajuste y residuos)
2. Gráfica 2: Formas de Onda AC en el Dominio del Tiempo (Transformador 60 Hz y Generador OWON 250 Hz)
3. Gráfica 3: Modo Graficador XY y Figuras de Lissajous (1:1, 1:2, 1:3, 1:4 y DC XY)
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from pathlib import Path

# Configuración de tipografía y estilo
plt.rcParams.update({
    'font.size': 11,
    'font.family': 'serif',
    'mathtext.fontset': 'cm',
    'axes.labelsize': 12,
    'axes.titlesize': 13,
    'xtick.labelsize': 10,
    'ytick.labelsize': 10,
    'legend.fontsize': 10,
    'figure.titlesize': 14,
    'figure.facecolor': 'white',
    'axes.facecolor': 'white',
    'axes.edgecolor': '#333333',
    'axes.linewidth': 0.8,
    'grid.color': '#DDDDDD',
    'grid.linestyle': '--',
    'grid.linewidth': 0.6,
})

# Formateador de coma decimal para los ejes
def comma_fmt(x, pos):
    return f"{x:.2f}".replace('.', ',').rstrip('0').rstrip(',') if abs(x - int(x)) > 1e-4 else f"{int(x)}"

def comma_fmt_1dec(x, pos):
    return f"{x:.1f}".replace('.', ',')

fig_dir = Path(__file__).resolve().parent.parent / "Figures"
fig_dir.mkdir(exist_ok=True)

# ==============================================================================
# 1. GRÁFICA 1: CALIBRACIÓN DE VOLTAJES DC (V_osc vs V_mult)
# ==============================================================================
print("[*] Generando Gráfica 1: Calibración de Voltajes DC...")

# Datos experimentales en escala óptima
v_mult = np.array([1.442, 2.453, 5.220, 8.030, 11.150]) # Multímetro patrón (V)
dv_mult = np.array([0.001, 0.001, 0.001, 0.001, 0.001])

v_osc = np.array([1.44, 2.45, 5.20, 8.00, 11.20])       # Osciloscopio lectura óptima (V)
dv_osc = np.array([0.02, 0.05, 0.20, 0.20, 0.20])      # Incertidumbre delta_V_osc (V)

# Ajuste lineal por mínimos cuadrados: V_osc = m * V_mult + b
p, cov = np.polyfit(v_mult, v_osc, 1, cov=True)
m, b = p
dm, db = np.sqrt(np.diag(cov))

# Coeficiente de determinación R^2
residuos = v_osc - (m * v_mult + b)
ss_res = np.sum(residuos**2)
ss_tot = np.sum((v_osc - np.mean(v_osc))**2)
r2 = 1 - (ss_res / ss_tot)

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(7.5, 6.0), gridspec_kw={'height_ratios': [3, 1]}, sharex=True)

# Curva de ajuste y línea ideal
x_fit = np.linspace(0.5, 12.0, 200)
ax1.plot(x_fit, x_fit, 'k--', lw=1.2, alpha=0.7, label='Referencia ideal: $V_{\\mathrm{osc}} = V_{\\mathrm{mult}}$')
ax1.plot(x_fit, m * x_fit + b, color='#003865', lw=1.8,
         label=f'Ajuste lineal: $V_{{\\mathrm{{osc}}}} = ({m:.4f}\\pm{dm:.4f})\\,V_{{\\mathrm{{mult}}}} + ({b:.3f}\\pm{db:.3f})$\n$R^2 = {r2:.5f}$')

# Puntos experimentales con barras de error
ax1.errorbar(v_mult, v_osc, xerr=dv_mult, yerr=dv_osc, fmt='o', color='#C00000',
             ecolor='#C00000', elinewidth=1.2, capsize=4, capthick=1.2, markersize=6,
             label='Datos experimentales ($V_{\\mathrm{osc}} \\pm \\delta V$)')

ax1.set_ylabel(r'Voltaje en Osciloscopio $V_{\mathrm{osc}}$ ($\mathrm{V}$)')
ax1.set_title('Calibración y Correlación de Voltajes Continuos DC', pad=12, fontweight='bold')
ax1.legend(loc='upper left', framealpha=0.95, edgecolor='#B0B0B0')
ax1.grid(True)
ax1.yaxis.set_major_formatter(ticker.FuncFormatter(comma_fmt))

# Gráfico de residuos
ax2.axhline(0, color='k', linestyle='--', lw=1.0)
ax2.errorbar(v_mult, residuos, yerr=dv_osc, fmt='s', color='#003865',
             ecolor='#003865', elinewidth=1.0, capsize=3, markersize=5)
ax2.set_xlabel(r'Voltaje Patrón Multímetro $V_{\mathrm{mult}}$ ($\mathrm{V}$)')
ax2.set_ylabel(r'Residuo ($\mathrm{V}$)')
ax2.set_ylim(-0.25, 0.25)
ax2.grid(True)
ax2.xaxis.set_major_formatter(ticker.FuncFormatter(comma_fmt))
ax2.yaxis.set_major_formatter(ticker.FuncFormatter(comma_fmt))

plt.tight_layout()
fig.savefig(fig_dir / "grafica_calibracion_dc.png", dpi=300, bbox_inches='tight', facecolor='white')
plt.close(fig)

# ==============================================================================
# 2. GRÁFICA 2: FORMAS DE ONDA AC EN EL TIEMPO
# ==============================================================================
print("[*] Generando Gráfica 2: Formas de Onda AC en el Tiempo...")

fig, axes = plt.subplots(3, 1, figsize=(8.0, 8.5), sharex=False)

# Panel 1: Senoidal del Transformador (60 Hz, V_p = 9.66 V, V_pp = 19.32 V)
t1 = np.linspace(0, 35, 1000) # ms
f1 = 60.0 # Hz -> T = 16.67 ms
v1 = 9.66 * np.sin(2 * np.pi * (f1 / 1000.0) * t1)

axes[0].plot(t1, v1, color='#003865', lw=2.0, label=r'Senoidal Red: $f = 60{,}0\,\mathrm{Hz},\; V_p = 9{,}66\,\mathrm{V},\; V_{pp} = 19{,}32\,\mathrm{V}$')
axes[0].axhline(0, color='#888888', lw=0.8, ls=':')
axes[0].axvline(16.67, color='#C00000', lw=1.2, ls='--', label=r'Período $T = 16{,}67\,\mathrm{ms}$ ($3{,}33\,\mathrm{div}$ a $5\,\mathrm{ms/div}$)')
axes[0].set_ylabel(r'Voltaje ($\mathrm{V}$)')
axes[0].set_title(r'(a) Onda Senoidal del Transformador ($220\,\mathrm{V} \to 6\,\mathrm{V}$, $60\,\mathrm{Hz}$)', fontweight='bold')
axes[0].legend(loc='upper right', framealpha=0.9)
axes[0].grid(True)
axes[0].set_xlim(0, 35)
axes[0].set_ylim(-12, 12)
axes[0].yaxis.set_major_formatter(ticker.FuncFormatter(comma_fmt))
axes[0].xaxis.set_major_formatter(ticker.FuncFormatter(comma_fmt))

# Panel 2: Triangular Generador OWON (250 Hz, V_p = 4.80 V, T = 4.0 ms)
t2 = np.linspace(0, 10, 1000) # ms
f2 = 250.0 # Hz -> T = 4.0 ms
from scipy import signal
v2 = 4.80 * signal.sawtooth(2 * np.pi * (f2 / 1000.0) * t2, width=0.5)

axes[1].plot(t2, v2, color='#2E7D32', lw=2.0, label=r'Triangular: $f = 250\,\mathrm{Hz},\; V_p = 4{,}80\,\mathrm{V},\; V_{pp} = 9{,}60\,\mathrm{V}$')
axes[1].axhline(0, color='#888888', lw=0.8, ls=':')
axes[1].axvline(4.0, color='#C00000', lw=1.2, ls='--', label=r'Período $T = 4{,}00\,\mathrm{ms}$ ($4{,}0\,\mathrm{div}$ a $1{,}0\,\mathrm{ms/div}$)')
axes[1].set_ylabel(r'Voltaje ($\mathrm{V}$)')
axes[1].set_title(r'(b) Onda Triangular del Generador OWON AG 051F ($250\,\mathrm{Hz}$)', fontweight='bold')
axes[1].legend(loc='upper right', framealpha=0.9)
axes[1].grid(True)
axes[1].set_xlim(0, 10)
axes[1].set_ylim(-6, 6)
axes[1].yaxis.set_major_formatter(ticker.FuncFormatter(comma_fmt))
axes[1].xaxis.set_major_formatter(ticker.FuncFormatter(comma_fmt))

# Panel 3: Cuadrada Generador OWON (250 Hz, V_p = 4.80 V, T = 4.0 ms)
t3 = np.linspace(0, 10, 1000)
v3 = 4.80 * signal.square(2 * np.pi * (f2 / 1000.0) * t3)

axes[2].plot(t3, v3, color='#8E24AA', lw=2.0, label=r'Cuadrada: $f = 250\,\mathrm{Hz},\; V_p = 4{,}80\,\mathrm{V},\; V_{pp} = 9{,}60\,\mathrm{V}$')
axes[2].axhline(0, color='#888888', lw=0.8, ls=':')
axes[2].axvline(4.0, color='#C00000', lw=1.2, ls='--', label=r'Período $T = 4{,}00\,\mathrm{ms}$ ($8{,}0\,\mathrm{div}$ a $0{,}5\,\mathrm{ms/div}$)')
axes[2].set_xlabel(r'Tiempo $t$ ($\mathrm{ms}$)')
axes[2].set_ylabel(r'Voltaje ($\mathrm{V}$)')
axes[2].set_title(r'(c) Onda Cuadrada del Generador OWON AG 051F ($250\,\mathrm{Hz}$)', fontweight='bold')
axes[2].legend(loc='upper right', framealpha=0.9)
axes[2].grid(True)
axes[2].set_xlim(0, 10)
axes[2].set_ylim(-6, 6)
axes[2].yaxis.set_major_formatter(ticker.FuncFormatter(comma_fmt))
axes[2].xaxis.set_major_formatter(ticker.FuncFormatter(comma_fmt))

plt.tight_layout()
fig.savefig(fig_dir / "grafica_ondas_ac.png", dpi=300, bbox_inches='tight', facecolor='white')
plt.close(fig)

# ==============================================================================
# 3. GRÁFICA 3: FIGURAS DE LISSAJOUS Y MODO XY
# ==============================================================================
print("[*] Generando Gráfica 3: Modo Graficador XY y Figuras de Lissajous...")

fig, axes = plt.subplots(2, 3, figsize=(10.5, 6.8))

t = np.linspace(0, 2 * np.pi, 1000)

# (1,1) Lissajous 1:1 normal
x_1 = np.sin(t)
y_1 = np.sin(t + np.pi / 4)
axes[0, 0].plot(x_1, y_1, color='#003865', lw=2.2)
axes[0, 0].set_title(r'Relación 1:1 ($60\,\mathrm{Hz} : 60\,\mathrm{Hz}$)', fontsize=11, fontweight='bold')
axes[0, 0].set_xlabel(r'$V_x$ (CH1)')
axes[0, 0].set_ylabel(r'$V_y$ (CH2)')
axes[0, 0].grid(True)
axes[0, 0].set_aspect('equal')

# (1,2) Lissajous 1:1 invertido (CH2 Invert)
y_1_inv = -np.sin(t + np.pi / 4)
axes[0, 1].plot(x_1, y_1_inv, color='#C00000', lw=2.2)
axes[0, 1].set_title(r'Relación 1:1 (CH2 Invertido)', fontsize=11, fontweight='bold')
axes[0, 1].set_xlabel(r'$V_x$ (CH1)')
axes[0, 1].set_ylabel(r'$V_y$ (CH2)')
axes[0, 1].grid(True)
axes[0, 1].set_aspect('equal')

# (1,3) Lissajous 1:2 (60 Hz : 120 Hz)
y_2 = np.sin(2 * t + np.pi / 3)
axes[0, 2].plot(x_1, y_2, color='#2E7D32', lw=2.2)
axes[0, 2].set_title(r'Relación 1:2 ($60\,\mathrm{Hz} : 120\,\mathrm{Hz}$)', fontsize=11, fontweight='bold')
axes[0, 2].set_xlabel(r'$V_x$ (CH1)')
axes[0, 2].set_ylabel(r'$V_y$ (CH2)')
axes[0, 2].grid(True)
axes[0, 2].set_aspect('equal')

# (2,1) Lissajous 1:3 (60 Hz : 180 Hz)
y_3 = np.sin(3 * t + np.pi / 4)
axes[1, 0].plot(x_1, y_3, color='#8E24AA', lw=2.2)
axes[1, 0].set_title(r'Relación 1:3 ($60\,\mathrm{Hz} : 180\,\mathrm{Hz}$)', fontsize=11, fontweight='bold')
axes[1, 0].set_xlabel(r'$V_x$ (CH1)')
axes[1, 0].set_ylabel(r'$V_y$ (CH2)')
axes[1, 0].grid(True)
axes[1, 0].set_aspect('equal')

# (2,2) Lissajous 1:4 (60 Hz : 240 Hz)
y_4 = np.sin(4 * t + np.pi / 6)
axes[1, 1].plot(x_1, y_4, color='#D84315', lw=2.2)
axes[1, 1].set_title(r'Relación 1:4 ($60\,\mathrm{Hz} : 240\,\mathrm{Hz}$)', fontsize=11, fontweight='bold')
axes[1, 1].set_xlabel(r'$V_x$ (CH1)')
axes[1, 1].set_ylabel(r'$V_y$ (CH2)')
axes[1, 1].grid(True)
axes[1, 1].set_aspect('equal')

# (2,3) Modo XY con voltajes DC (Punto fijo)
axes[1, 2].plot([1.5], [3.0], 'o', color='#003865', markersize=9, label=r'DC Normal ($1{,}5\,\mathrm{V}, +3{,}0\,\mathrm{V}$)')
axes[1, 2].plot([1.5], [-3.0], 's', color='#C00000', markersize=9, label=r'CH2 Invert ($1{,}5\,\mathrm{V}, -3{,}0\,\mathrm{V}$)')
axes[1, 2].axhline(0, color='#888888', lw=0.8, ls=':')
axes[1, 2].axvline(0, color='#888888', lw=0.8, ls=':')
axes[1, 2].set_title(r'Modo XY DC: Punto Estático', fontsize=11, fontweight='bold')
axes[1, 2].set_xlabel(r'$V_x$ (CH1: Pila $1{,}5\,\mathrm{V}$)')
axes[1, 2].set_ylabel(r'$V_y$ (CH2: Fuente $3{,}0\,\mathrm{V}$)')
axes[1, 2].set_xlim(-0.5, 3.5)
axes[1, 2].set_ylim(-4.5, 4.5)
axes[1, 2].legend(loc='lower left', fontsize=8, framealpha=0.9)
axes[1, 2].grid(True)

plt.tight_layout()
fig.savefig(fig_dir / "grafica_lissajous_xy.png", dpi=300, bbox_inches='tight', facecolor='white')
plt.close(fig)

print("[OK] Todas las gráficas científicas fueron generadas exitosamente en Figures/.")
