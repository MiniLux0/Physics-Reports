#!/usr/bin/env python3
"""
Script: regenerate_figures.py
Generación perfeccionada de diagramas circuitales y esquemas del Laboratorio 03 a 300 DPI.
Garantiza:
- ax.set_aspect('equal') para círculos perfectamente redondos.
- CERO solapamiento de textos contra trazos, cajas o entre etiquetas.
- Tipografía científica uniforme en español con coma decimal.
"""

import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Backend no interactivo
plt.switch_backend('Agg')

figures_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Figures'))
os.makedirs(figures_dir, exist_ok=True)


# ==============================================================================
# FIGURA 1: CIRCUITO POTENCIOMÉTRICO GENERAL
# ==============================================================================
def plot_circuito_potenciometro():
    fig, ax = plt.subplots(figsize=(13.2, 6.4))
    fig.patch.set_facecolor('white')
    ax.set_facecolor('white')
    ax.set_aspect('equal')
    ax.set_xlim(0, 15.2)
    ax.set_ylim(0, 7.2)
    ax.axis('off')

    # Titulo
    ax.text(7.6, 6.7, 'Esquema del Montaje Experimental: Circuito Potenciométrico y Medición de Curvas V–I',
            fontsize=12.5, fontweight='bold', color='#003865', ha='center', va='center')

    # 1. FUENTE DC (x = 2.0)
    ax.plot([2.0, 2.0], [5.3, 3.9], 'k-', lw=2.2)
    ax.plot([2.0, 2.0], [2.7, 1.2], 'k-', lw=2.2)
    ax.plot([1.5, 2.5], [3.9, 3.9], color='#003865', lw=3.8) # +
    ax.plot([1.7, 2.3], [3.3, 3.3], color='#003865', lw=2.2) # -
    ax.plot([1.5, 2.5], [2.7, 2.7], color='#003865', lw=3.8) # +
    ax.plot([1.7, 2.3], [2.1, 2.1], color='#003865', lw=2.2) # -
    ax.plot([2.0, 2.0], [3.3, 2.7], 'k-', lw=2.2)

    # Signos de polaridad
    ax.text(2.0, 4.35, '+', fontsize=16, fontweight='bold', ha='center', va='center', color='#003865')
    ax.text(2.0, 1.6, '–', fontsize=20, fontweight='bold', ha='center', va='center', color='#003865')

    # Caja de texto Fuente DC
    src_box = patches.FancyBboxPatch((0.1, 2.05), 1.45, 1.6, boxstyle='round,pad=0.08,rounding_size=0.12',
                                     facecolor='#E3F2FD', edgecolor='#0277BD', lw=1.5)
    ax.add_patch(src_box)
    ax.text(0.82, 2.85, 'FUENTE DC\nRegulada\n7,5 V',
            fontsize=9.5, fontweight='bold', color='#01579B', ha='center', va='center')

    # Cables hacia reostato
    ax.plot([2.0, 4.0], [5.3, 5.3], 'k-', lw=2.2)
    ax.plot([2.0, 4.0], [1.2, 1.2], 'k-', lw=2.2)

    # 2. REÓSTATO (x = 4.0)
    ax.plot([4.0, 4.0], [5.3, 4.7], 'k-', lw=2.2)
    ax.plot([4.0, 4.0], [1.7, 1.2], 'k-', lw=2.2)

    ax.plot(4.0, 4.7, 'o', color='#003865', markersize=7.5)
    ax.text(3.6, 4.9, 'A (+)', fontsize=10, fontweight='bold', color='#003865', ha='right', va='center')
    ax.plot(4.0, 1.7, 'o', color='#003865', markersize=7.5)
    ax.text(3.6, 1.5, 'B (–)', fontsize=10, fontweight='bold', color='#003865', ha='right', va='center')

    y_z = np.linspace(1.7, 4.7, 11)
    x_z = [4.0, 4.35, 3.65, 4.35, 3.65, 4.35, 3.65, 4.35, 3.65, 4.35, 4.0]
    ax.plot(x_z, y_z, 'k-', lw=2.2)

    ax.text(2.75, 3.2, 'Reóstato\n(Divisor\nPotenciométrico)\n$R_T = R_1 + R_2$',
            fontsize=8.5, ha='center', va='center', color='#37474F')

    # Cursor C: flecha desde 5.8 a 4.0, punto en 5.8
    ax.annotate('', xy=(4.0, 3.2), xytext=(5.8, 3.2),
                arrowprops=dict(facecolor='#D84315', edgecolor='#D84315', shrink=0.04, width=2.4, headwidth=8.5))
    ax.plot(5.8, 3.2, 'o', color='#D84315', markersize=7)
    # Etiqueta de cursor con holgura absoluta: centrada en 5.7, con zigzag peak en 4.35 y amperimetro en 7.8
    ax.text(5.7, 3.85, 'Cursor móvil (C)', fontsize=9.5, fontweight='bold', color='#D84315', ha='center', va='center')

    ax.plot([5.8, 7.3], [3.2, 3.2], 'k-', lw=2.2)

    # 3. AMPERÍMETRO (x = 7.8, y = 3.2, r = 0.5)
    cir_A = patches.Circle((7.8, 3.2), 0.5, facecolor='#E3F2FD', edgecolor='#003865', lw=2.2)
    ax.add_patch(cir_A)
    ax.text(7.8, 3.2, 'A', fontsize=13, fontweight='bold', ha='center', va='center', color='#003865')
    ax.text(7.8, 4.15, 'Amperímetro\n(en serie)', fontsize=8.5, fontweight='bold', ha='center', va='center', color='#003865')

    ax.plot([8.3, 10.0], [3.2, 3.2], 'k-', lw=2.2)
    ax.plot([10.0, 10.0], [3.2, 2.7], 'k-', lw=2.2)

    # 4. ELEMENTO BAJO ENSAYO (x = 10.0)
    ax.plot(10.0, 2.7, 'ro', markersize=6)
    ax.text(9.3, 2.7, 'a (+)', fontsize=9.5, fontweight='bold', color='#C62828', ha='right', va='center')

    elem_box = patches.FancyBboxPatch((9.1, 1.6), 1.8, 0.9, boxstyle='round,pad=0.05,rounding_size=0.12',
                                      facecolor='#E8F5E9', edgecolor='#2E7D32', lw=2.2)
    ax.add_patch(elem_box)
    ax.text(10.0, 2.05, 'Elemento\nde Ensayo\n(E1, E2, E3)', fontsize=8.5, fontweight='bold',
            ha='center', va='center', color='#1B5E20')

    ax.plot(10.0, 1.4, 'ro', markersize=6)
    ax.text(9.3, 1.4, 'b (–)', fontsize=9.5, fontweight='bold', color='#C62828', ha='right', va='center')

    ax.plot([10.0, 10.0], [1.4, 1.2], 'k-', lw=2.2)
    ax.plot([10.0, 4.0], [1.2, 1.2], 'k-', lw=2.2)
    ax.text(7.0, 0.75, 'Línea de retorno común hacia borne B (0 V)',
            fontsize=8.5, ha='center', va='center', color='#555555', fontstyle='italic')

    # 5. VOLTÍMETRO (x = 12.2)
    ax.plot([10.0, 12.2], [2.7, 2.7], color='#D9534F', lw=1.8, linestyle='--')
    ax.plot([12.2, 12.2], [2.7, 2.55], color='#D9534F', lw=1.8, linestyle='--')

    cir_V = patches.Circle((12.2, 2.05), 0.5, facecolor='#FFEBEE', edgecolor='#D9534F', lw=2.2)
    ax.add_patch(cir_V)
    ax.text(12.2, 2.05, 'V', fontsize=13, fontweight='bold', ha='center', va='center', color='#D9534F')

    ax.plot([12.2, 12.2], [1.55, 1.4], color='#D9534F', lw=1.8, linestyle='--')
    ax.plot([12.2, 10.0], [1.4, 1.4], color='#D9534F', lw=1.8, linestyle='--')

    ax.text(13.0, 2.05, 'Voltímetro\n(en paralelo)\nMide $V_{ab}$',
            fontsize=9, fontweight='bold', ha='left', va='center', color='#D9534F')

    out_path = os.path.join(figures_dir, 'fig_circuito_potenciometro.png')
    plt.savefig(out_path, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"[OK] Generada: {out_path}")


# ==============================================================================
# FIGURA 2: REÓSTATO Y DIAGRAMA DE BLOQUES (PREGUNTA 4)
# ==============================================================================
def plot_reostato_diagrama_bloques():
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12.5, 8.8), gridspec_kw={'height_ratios': [1.15, 1.0]})
    fig.patch.set_facecolor('white')

    # --- PANEL (a): Estructura Física y Terminales ---
    ax1.set_facecolor('white')
    ax1.set_xlim(-0.5, 12.5)
    ax1.set_ylim(-1.5, 5.8)
    ax1.axis('off')
    ax1.set_title(r'(a) Estructura Constructiva y Bornes de Conexión del Reóstato de Laboratorio',
                  fontsize=12, fontweight='bold', color='#003865', pad=12)

    # Cilindro Cerámico
    cyl = patches.FancyBboxPatch((2.0, 1.1), 8.0, 1.6, boxstyle='round,pad=0.08,rounding_size=0.15',
                                 facecolor='#F5F0EB', edgecolor='#8D6E63', lw=2.2)
    ax1.add_patch(cyl)

    # Espiras de alambre resistivo (bobinado)
    for x in np.linspace(2.2, 9.8, 28):
        ax1.plot([x, x], [1.1, 2.7], color='#333333', lw=2)

    # Barra Colectora Superior
    rod = patches.Rectangle((2.0, 3.6), 8.0, 0.35, facecolor='#CFD8DC', edgecolor='#455A64', lw=2)
    ax1.add_patch(rod)

    # Etiquetas sobre la barra divididas a izquierda y derecha para NO colisionar con el cable central
    ax1.text(3.7, 4.25, 'Barra Colectora Metálica',
             fontsize=9.5, fontweight='bold', ha='center', va='center', color='#37474F')
    ax1.text(8.3, 4.25, 'Guía de Baja Resistencia',
             fontsize=9.5, fontweight='bold', ha='center', va='center', color='#37474F')

    # Slider / Cursor C
    slider = patches.FancyBboxPatch((5.4, 2.4), 1.2, 1.4, boxstyle='round,pad=0.04,rounding_size=0.1',
                                    facecolor='#003865', edgecolor='#001F3F', lw=1.8)
    ax1.add_patch(slider)
    ax1.text(6.0, 3.1, 'Cursor\nMóvil', color='white', fontsize=8.5, fontweight='bold', ha='center', va='center')

    # Contacto móvil (escobilla)
    ax1.annotate('', xy=(6.0, 2.1), xytext=(6.0, 2.4),
                 arrowprops=dict(facecolor='#FFD600', edgecolor='#FFD600', width=2.5, headwidth=7))

    # Conductor superior hacia Terminal C (sube despejado por el centro x=6.0)
    ax1.plot([6.0, 6.0], [3.8, 4.8], color='#003865', lw=2.5)
    ax1.plot(6.0, 4.8, 'o', color='#003865', markersize=8)
    ax1.text(6.0, 5.25, 'Terminal C (Cursor Móvil / Salida Regulable)',
             fontsize=10, fontweight='bold', ha='center', va='center', color='#003865')

    # Terminal A (Fijo, Izquierda)
    ax1.plot([2.2, 1.0], [1.9, 1.9], color='#003865', lw=2.5)
    ax1.plot([1.0, 1.0], [1.9, 0.7], color='#003865', lw=2.5)
    ax1.plot(1.0, 0.7, 'o', color='#003865', markersize=8)
    ax1.text(1.0, 0.15, 'Terminal A (Fijo)\nEntrada (+)',
             fontsize=9.5, fontweight='bold', ha='center', va='center', color='#003865')

    # Terminal B (Fijo, Derecha)
    ax1.plot([9.8, 11.0], [1.9, 1.9], color='#003865', lw=2.5)
    ax1.plot([11.0, 11.0], [1.9, 0.7], color='#003865', lw=2.5)
    ax1.plot(11.0, 0.7, 'o', color='#003865', markersize=8)
    ax1.text(11.0, 0.15, 'Terminal B (Fijo)\nReferencia (–)',
             fontsize=9.5, fontweight='bold', ha='center', va='center', color='#003865')

    # Flechas de longitud / resistencia dividida
    ax1.annotate('', xy=(2.2, 0.5), xytext=(6.0, 0.5),
                 arrowprops=dict(arrowstyle='<->', color='#C62828', lw=2))
    ax1.text(4.1, 0.75, r'$R_1 = R_{AC}(x) = R_T \cdot (x/L)$',
             fontsize=9, fontweight='bold', color='#C62828', ha='center', va='center')

    ax1.annotate('', xy=(6.0, 0.5), xytext=(9.8, 0.5),
                 arrowprops=dict(arrowstyle='<->', color='#2E7D32', lw=2))
    ax1.text(7.9, 0.75, r'$R_2 = R_{CB}(x) = R_T \cdot (1 - x/L)$',
             fontsize=9, fontweight='bold', color='#2E7D32', ha='center', va='center')

    # Nota descriptiva inferior
    ax1.text(6.0, -1.0, 'Soporte: Cilindro cerámico aislante refractario devanado con hilo de Nicrón de alta resistividad',
             fontsize=8.5, fontstyle='italic', ha='center', va='center', color='#5D4037')

    # --- PANEL (b): Diagrama de Bloques Funcional ---
    ax2.set_facecolor('white')
    ax2.set_xlim(-0.5, 12.5)
    ax2.set_ylim(-0.4, 3.8)
    ax2.axis('off')
    ax2.set_title(r'(b) Diagrama de Bloques Funcional: Operación como Divisor Potenciométrico de Tensión',
                  fontsize=12, fontweight='bold', color='#003865', pad=12)

    # Bloque 1: FUENTE DC
    b1 = patches.FancyBboxPatch((0.4, 0.8), 2.2, 2.2, boxstyle='round,pad=0.08,rounding_size=0.15',
                                facecolor='#E3F2FD', edgecolor='#0277BD', lw=2.2)
    ax2.add_patch(b1)
    ax2.text(1.5, 1.9, 'FUENTE DC\nESTABILIZADA\n\n$V_{\\mathrm{in}} = 7{,}5\\text{ V}$',
             fontsize=9, fontweight='bold', ha='center', va='center', color='#01579B')

    # Flechas Bloque 1 -> Bloque 2
    ax2.annotate('', xy=(3.8, 2.3), xytext=(2.6, 2.3),
                 arrowprops=dict(arrowstyle='->', color='#0277BD', lw=2.2))
    ax2.text(3.2, 2.65, 'Borne A (+)', fontsize=8.5, fontweight='bold', color='#0277BD', ha='center', va='center')

    ax2.annotate('', xy=(3.8, 1.5), xytext=(2.6, 1.5),
                 arrowprops=dict(arrowstyle='->', color='#0277BD', lw=2.2))
    ax2.text(3.2, 1.15, 'Borne B (–)', fontsize=8.5, fontweight='bold', color='#0277BD', ha='center', va='center')

    # Bloque 2: REÓSTATO (DIVISOR POTENCIOMÉTRICO)
    b2 = patches.FancyBboxPatch((3.8, 0.5), 4.3, 2.7, boxstyle='round,pad=0.08,rounding_size=0.15',
                                facecolor='#FFF8E1', edgecolor='#FF8F00', lw=2.2)
    ax2.add_patch(b2)
    ax2.text(5.95, 2.8, 'REÓSTATO (DIVISOR POTENCIOMÉTRICO)',
             fontsize=9.5, fontweight='bold', ha='center', va='center', color='#E65100')
    ax2.text(5.95, 2.45, 'Resistencia total: $R_T = R_1 + R_2$',
             fontsize=8.5, fontweight='bold', ha='center', va='center', color='#BF360C')
    ax2.text(5.95, 1.5, '• Segmento superior: $R_1(x) = R_T \\cdot (x/L)$\n' +
                         '• Segmento inferior: $R_2(x) = R_T \\cdot (1 - x/L)$\n' +
                         '• Toma intermedia: Cursor deslizante C',
             fontsize=8, ha='center', va='center', color='#4E342E')

    # Flechas Bloque 2 -> Bloque 3 (desplazadas para amplitud)
    ax2.annotate('', xy=(9.4, 2.3), xytext=(8.1, 2.3),
                 arrowprops=dict(arrowstyle='->', color='#D84315', lw=2.2))
    ax2.text(8.75, 2.7, 'Cursor C\n($V_{\\mathrm{out}}$)',
             fontsize=8.5, fontweight='bold', color='#D84315', ha='center', va='center')

    ax2.plot([8.1, 9.4], [1.5, 1.5], color='#37474F', lw=2.2)
    ax2.text(8.75, 1.15, 'Común (B)',
             fontsize=8.5, fontweight='bold', color='#37474F', ha='center', va='center')

    # Bloque 3: ELEMENTO BAJO PRUEBA (más espacioso a la derecha)
    b3 = patches.FancyBboxPatch((9.4, 0.6), 2.7, 2.5, boxstyle='round,pad=0.08,rounding_size=0.15',
                                facecolor='#E8F5E9', edgecolor='#2E7D32', lw=2.2)
    ax2.add_patch(b3)
    ax2.text(10.75, 2.65, 'ELEMENTO DE ENSAYO\n(CARGA EXPERIMENTAL)',
             fontsize=8.5, fontweight='bold', ha='center', va='center', color='#1B5E20')
    ax2.text(10.75, 1.55, 'Tensión suministrada:\n' +
                          '$V_{\\mathrm{out}} \\in [0{,}00\\,;\\,6{,}50]\\text{ V}$\n\n' +
                          '$V_{\\mathrm{out}}(x) = V_{\\mathrm{in}} \\cdot \\frac{R_2(x)}{R_T}$',
             fontsize=8.5, fontweight='bold', ha='center', va='center', color='#2E7D32')

    plt.tight_layout()
    out_path = os.path.join(figures_dir, 'fig_reostato_diagrama_bloques.png')
    plt.savefig(out_path, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"[OK] Generada: {out_path}")


# ==============================================================================
# FIGURA 3: CIRCUITO ESPECÍFICO DEL DIODO (PREGUNTA 5)
# ==============================================================================
def plot_circuito_diodo_especifico():
    fig = plt.figure(figsize=(14.2, 7.0))
    fig.patch.set_facecolor('white')
    ax = fig.add_subplot(1, 1, 1)
    ax.set_facecolor('white')
    ax.set_aspect('equal')
    ax.set_xlim(0, 16.2)
    ax.set_ylim(0, 7.2)
    ax.axis('off')

    ax.text(8.0, 6.8, 'Montaje Experimental: Circuito Potenciométrico para la Caracterización del Diodo de Silicio',
            fontsize=12.5, fontweight='bold', color='#003865', ha='center', va='center')

    # 1. FUENTE DC (x = 2.0)
    ax.plot([2.0, 2.0], [5.3, 3.9], 'k-', lw=2.2)
    ax.plot([2.0, 2.0], [2.7, 1.0], 'k-', lw=2.2)
    ax.plot([1.5, 2.5], [3.9, 3.9], color='#003865', lw=3.8) # +
    ax.plot([1.7, 2.3], [3.3, 3.3], color='#003865', lw=2.2) # -
    ax.plot([1.5, 2.5], [2.7, 2.7], color='#003865', lw=3.8) # +
    ax.plot([1.7, 2.3], [2.1, 2.1], color='#003865', lw=2.2) # -
    ax.plot([2.0, 2.0], [3.3, 2.7], 'k-', lw=2.2)

    ax.text(2.0, 4.35, '+', fontsize=16, fontweight='bold', ha='center', va='center', color='#003865')
    ax.text(2.0, 1.55, '–', fontsize=20, fontweight='bold', ha='center', va='center', color='#003865')

    src_box = patches.FancyBboxPatch((0.1, 2.05), 1.45, 1.6, boxstyle='round,pad=0.08,rounding_size=0.12',
                                     facecolor='#E3F2FD', edgecolor='#0277BD', lw=1.5)
    ax.add_patch(src_box)
    ax.text(0.82, 2.85, 'FUENTE DC\nRegulada\n7,5 V',
            fontsize=9.5, fontweight='bold', color='#01579B', ha='center', va='center')

    # Cables hacia reostato
    ax.plot([2.0, 4.0], [5.3, 5.3], 'k-', lw=2.2)
    ax.plot([2.0, 4.0], [1.0, 1.0], 'k-', lw=2.2)

    # 2. REÓSTATO (x = 4.0)
    ax.plot([4.0, 4.0], [5.3, 4.7], 'k-', lw=2.2)
    ax.plot([4.0, 4.0], [1.7, 1.0], 'k-', lw=2.2)

    ax.plot(4.0, 4.7, 'o', color='#003865', markersize=7.5)
    ax.text(3.6, 4.9, 'A (+)', fontsize=10, fontweight='bold', color='#003865', ha='right', va='center')
    ax.plot(4.0, 1.7, 'o', color='#003865', markersize=7.5)
    ax.text(3.6, 1.5, 'B (–)', fontsize=10, fontweight='bold', color='#003865', ha='right', va='center')

    y_z = np.linspace(1.7, 4.7, 11)
    x_z = [4.0, 4.35, 3.65, 4.35, 3.65, 4.35, 3.65, 4.35, 3.65, 4.35, 4.0]
    ax.plot(x_z, y_z, 'k-', lw=2.2)

    ax.text(2.75, 3.2, 'Reóstato\n(Divisor\nPotenciométrico)\n$R_T = R_1 + R_2$',
            fontsize=8.5, ha='center', va='center', color='#37474F')

    # Cursor C
    ax.annotate('', xy=(4.0, 3.2), xytext=(5.6, 3.2),
                arrowprops=dict(facecolor='#D84315', edgecolor='#D84315', shrink=0.04, width=2.4, headwidth=8.5))
    ax.plot(5.6, 3.2, 'o', color='#D84315', markersize=7)
    ax.text(5.4, 3.85, 'Cursor (C)', fontsize=9.5, fontweight='bold', color='#D84315', ha='center', va='center')

    # Conductor hacia amperímetro con flecha ID
    ax.plot([5.6, 7.0], [3.2, 3.2], 'k-', lw=2.2)
    ax.annotate('', xy=(6.55, 3.2), xytext=(6.2, 3.2),
                arrowprops=dict(arrowstyle='->', color='#B71C1C', lw=2.2))
    ax.text(6.38, 3.55, r'$I_D$', fontsize=10, fontweight='bold', color='#B71C1C', ha='center', va='center')

    # 3. AMPERÍMETRO (x = 7.5, y = 3.2, r = 0.5)
    cir_A = patches.Circle((7.5, 3.2), 0.5, facecolor='#E3F2FD', edgecolor='#003865', lw=2.2)
    ax.add_patch(cir_A)
    ax.text(7.5, 3.2, 'A', fontsize=13, fontweight='bold', ha='center', va='center', color='#003865')
    ax.text(7.5, 4.25, 'Amperímetro Digital\n(en serie, 0–1 A)',
            fontsize=8.5, fontweight='bold', ha='center', va='center', color='#003865')

    # Conductor hacia terminal 'a' del diodo
    ax.plot([8.0, 8.8], [3.2, 3.2], 'k-', lw=2.2)

    # 4. DIODO SEMICONDUCTOR DE SILICIO
    # Terminal a (+)
    ax.plot(8.8, 3.2, 'ro', markersize=6)
    ax.text(8.45, 3.55, 'a (+)', fontsize=10, fontweight='bold', color='#C62828', ha='center', va='center')

    # Conexión al diodo
    ax.plot([8.8, 9.4], [3.2, 3.2], 'k-', lw=2.2)

    # Triángulo del diodo (Ánodo)
    diodo_x = [9.4, 9.4, 10.2]
    diodo_y = [2.65, 3.75, 3.2]
    diodo_poly = patches.Polygon(np.column_stack([diodo_x, diodo_y]), closed=True,
                                 facecolor='#BBDEFB', edgecolor='#003865', lw=2.2)
    ax.add_patch(diodo_poly)

    # Barra del cátodo
    ax.plot([10.2, 10.2], [2.6, 3.8], color='#003865', lw=3.2)
    ax.plot([10.2, 11.4], [3.2, 3.2], 'k-', lw=2.2)

    # Etiquetas de Ánodo y Cátodo con separación amplia
    ax.text(9.1, 2.25, 'Ánodo (p)', fontsize=9, fontweight='bold', ha='center', va='center', color='#003865')
    ax.text(10.5, 2.25, 'Cátodo (n)', fontsize=9, fontweight='bold', ha='center', va='center', color='#003865')
    ax.text(10.0, 1.62, 'Diodo Semiconductor\nde Silicio (1N4007)',
            fontsize=8.5, fontweight='bold', ha='center', va='center', color='#003865')

    # Terminal b (–)
    ax.plot(11.4, 3.2, 'ro', markersize=6)
    ax.text(11.75, 3.55, 'b (–)', fontsize=10, fontweight='bold', color='#C62828', ha='center', va='center')

    # 5. VOLTÍMETRO EN PARALELO (arriba del diodo, amplio lazo)
    ax.plot([8.8, 8.8], [3.2, 5.2], color='#D9534F', lw=1.8, linestyle='--')
    ax.plot([8.8, 9.5], [5.2, 5.2], color='#D9534F', lw=1.8, linestyle='--')

    cir_V = patches.Circle((10.1, 5.2), 0.5, facecolor='#FFEBEE', edgecolor='#D9534F', lw=2.2)
    ax.add_patch(cir_V)
    ax.text(10.1, 5.2, 'V', fontsize=13, fontweight='bold', ha='center', va='center', color='#D9534F')

    ax.plot([10.6, 11.4], [5.2, 5.2], color='#D9534F', lw=1.8, linestyle='--')
    ax.plot([11.4, 11.4], [5.2, 3.2], color='#D9534F', lw=1.8, linestyle='--')

    ax.text(10.1, 6.15, 'Voltímetro Digital (en paralelo)\nMide caída directa neta $V_D$',
            fontsize=8.5, fontweight='bold', ha='center', va='center', color='#D9534F')

    # Retorno hacia B
    ax.plot([11.4, 11.4], [3.2, 1.0], 'k-', lw=2.2)
    ax.plot([11.4, 4.0], [1.0, 1.0], 'k-', lw=2.2)
    ax.text(7.2, 0.55, 'Línea de retorno común hacia borne B (0 V)',
            fontsize=8.5, ha='center', va='center', color='#555555', fontstyle='italic')

    # 6. PANEL LATERAL DE REGÍMENES DE OPERACIÓN (x = 12.3 a 15.9)
    card = patches.FancyBboxPatch((12.2, 0.65), 3.7, 5.7, boxstyle='round,pad=0.08,rounding_size=0.15',
                                  facecolor='#FAFAFA', edgecolor='#90A4AE', lw=2.0)
    ax.add_patch(card)

    ax.text(14.05, 5.95, 'REGÍMENES DE OPERACIÓN\nDEL DIODO DE SILICIO',
            fontsize=9.5, fontweight='bold', ha='center', va='center', color='#1A237E')

    # 1. Corte
    ax.text(14.05, 4.85, '1. Región de Corte / Bloqueo\n' +
                         '• $0 \\leq V_D < 0{,}60\\text{ V}$\n' +
                         '• $I_D \\approx 0{,}000\\text{ A}$ (juntura inactiva)',
            fontsize=8.2, ha='center', va='center', color='#424242')

    # 2. Codo
    ax.text(14.05, 3.65, '2. Zona de Umbral o Codo\n' +
                         '• $0{,}60 \\leq V_D \\leq 0{,}66\\text{ V}$\n' +
                         '• Umbral experimental:\n' +
                         '  $V_u \\approx 0{,}66 \\pm 0{,}02\\text{ V}$',
            fontsize=8.2, ha='center', va='center', color='#E65100')

    # 3. Conducción exponencial
    ax.text(14.05, 2.3, '3. Conducción Exponencial\n' +
                         '• $0{,}66 < V_D \\leq 0{,}75\\text{ V}$\n' +
                         '• Corriente asciende a $0{,}783\\text{ A}$\n' +
                         '• Resistencia estática colapsa',
            fontsize=8.2, ha='center', va='center', color='#B71C1C')

    # Alerta
    alert_box = patches.FancyBboxPatch((12.55, 0.9), 3.0, 0.6, boxstyle='round,pad=0.04,rounding_size=0.08',
                                       facecolor='#FFEBEE', edgecolor='#D32F2F', lw=1.5)
    ax.add_patch(alert_box)
    ax.text(14.05, 1.2, '¡Precaución con $I_{\\mathrm{max}}$! ($I \\leq 0{,}85\\text{ A}$)',
            fontsize=8, fontweight='bold', ha='center', va='center', color='#C62828')

    out_path = os.path.join(figures_dir, 'fig_circuito_diodo_especifico.png')
    plt.savefig(out_path, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"[OK] Generada: {out_path}")


if __name__ == '__main__':
    print("[*] Regenerando las 3 figuras perfeccionadas a 300 DPI...")
    plot_circuito_potenciometro()
    plot_reostato_diagrama_bloques()
    plot_circuito_diodo_especifico()
    print("[DONE] Finalizado con éxito.")
