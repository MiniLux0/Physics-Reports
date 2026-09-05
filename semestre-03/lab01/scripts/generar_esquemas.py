import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Configuración tipográfica
plt.rcParams['font.family'] = 'DejaVu Sans'
plt.rcParams['font.size'] = 10
plt.rcParams['axes.unicode_minus'] = False

# -------------------------------------------------------------
# 1. ESQUEMA DEL TUBO DE RAYOS CATÓDICOS (TRC)
# -------------------------------------------------------------
def generar_esquema_trc():
    fig, ax = plt.subplots(figsize=(10, 4.8), dpi=300, facecolor='white')
    ax.set_facecolor('white')
    
    # Tubo de vidrio (envolvente)
    cuello = patches.Rectangle((0.5, 1.2), 4.5, 1.6, fill=False, edgecolor='#4A5568', linewidth=2, linestyle='-')
    ax.add_patch(cuello)
    
    # Campana cónica
    cono = patches.Polygon([[5.0, 2.8], [8.5, 3.8], [8.5, 0.2], [5.0, 1.2]], 
                           closed=True, fill=True, facecolor='#F7FAFC', edgecolor='#4A5568', linewidth=2)
    ax.add_patch(cono)
    
    # Pantalla fosforescente
    pantalla = patches.Rectangle((8.5, 0.2), 0.3, 3.6, fill=True, facecolor='#E2E8F0', edgecolor='#2B6CB0', linewidth=2)
    ax.add_patch(pantalla)
    
    # Capa de fósforo verde
    fosforo = patches.Rectangle((8.7, 0.3), 0.08, 3.4, fill=True, facecolor='#48BB78', edgecolor='none')
    ax.add_patch(fosforo)
    
    # Cátodo caliente (filamento)
    ax.plot([0.8, 1.0, 1.0, 0.8], [1.7, 1.8, 2.2, 2.3], color='#E53E3E', linewidth=2.5)
    ax.text(0.9, 1.4, 'Filamento /\nCátodo (K)', ha='center', va='top', fontsize=8.5, color='#9B2C2C', fontweight='bold')
    
    # Rejilla de control (Wehnelt)
    ax.plot([1.4, 1.4], [1.5, 2.5], color='#4A5568', linewidth=3)
    ax.text(1.4, 2.65, 'Rejilla (G)', ha='center', va='bottom', fontsize=8.5, color='#2D3748')
    
    # Ánodos aceleradores
    anodo1 = patches.Rectangle((1.8, 1.5), 0.3, 1.0, fill=True, facecolor='#CBD5E0', edgecolor='#2D3748', linewidth=1.5)
    anodo2 = patches.Rectangle((2.4, 1.5), 0.3, 1.0, fill=True, facecolor='#CBD5E0', edgecolor='#2D3748', linewidth=1.5)
    ax.add_patch(anodo1)
    ax.add_patch(anodo2)
    ax.text(2.25, 1.3, 'Ánodos\nAceleradores (A)', ha='center', va='top', fontsize=8.5, color='#2D3748')
    
    # Cañón de electrones (llave)
    ax.annotate('', xy=(0.7, 3.0), xytext=(2.8, 3.0), arrowprops=dict(arrowstyle='<->', color='#3182CE', lw=1.2))
    ax.text(1.75, 3.1, 'Cañón Electrónico', ha='center', fontsize=9, color='#2B6CB0', fontweight='bold')

    # Placas deflectoras verticales (controlan eje Y)
    placa_y_sup = patches.Rectangle((3.2, 2.2), 0.8, 0.2, fill=True, facecolor='#EBF8FF', edgecolor='#3182CE', linewidth=1.5)
    placa_y_inf = patches.Rectangle((3.2, 1.6), 0.8, 0.2, fill=True, facecolor='#EBF8FF', edgecolor='#3182CE', linewidth=1.5)
    ax.add_patch(placa_y_sup)
    ax.add_patch(placa_y_inf)
    ax.text(3.6, 2.5, 'Placas $Y$ (Vertical)', ha='center', fontsize=8.5, color='#2B6CB0', fontweight='bold')
    ax.text(3.6, 1.4, '$+V_y / -V_y$', ha='center', fontsize=8, color='#3182CE')

    # Placas deflectoras horizontales (controlan eje X)
    placa_x_sup = patches.Rectangle((4.3, 2.3), 0.6, 0.15, fill=True, facecolor='#FEFCBF', edgecolor='#D69E2E', linewidth=1.5)
    placa_x_inf = patches.Rectangle((4.3, 1.55), 0.6, 0.15, fill=True, facecolor='#FEFCBF', edgecolor='#D69E2E', linewidth=1.5)
    ax.add_patch(placa_x_sup)
    ax.add_patch(placa_x_inf)
    ax.text(4.6, 2.6, 'Placas $X$ (Horizontal)', ha='center', fontsize=8.5, color='#B7791F', fontweight='bold')
    ax.text(4.6, 1.35, '$+V_x / -V_x$', ha='center', fontsize=8, color='#D69E2E')

    # Haz de electrones
    ax.plot([1.0, 3.6], [2.0, 2.0], color='#3182CE', linewidth=2, linestyle='-')
    ax.plot([3.6, 4.6, 8.7], [2.0, 2.2, 3.1], color='#DD6B20', linewidth=2.2, linestyle='-')
    
    # Punto de impacto en pantalla (Spot)
    ax.scatter([8.7], [3.1], color='#38A169', s=120, zorder=5, edgecolors='#22543D', linewidth=2)
    ax.text(8.9, 3.1, ' Punto de Impacto\n Spot $(x, y)$', va='center', fontsize=9, color='#22543D', fontweight='bold')
    
    # Retícula de pantalla
    ax.text(8.65, 4.0, 'Pantalla Fosforescente\ncon Retícula Graduada', ha='center', fontsize=9, color='#2D3748', fontweight='bold')

    ax.set_xlim(0.2, 10.5)
    ax.set_ylim(0.0, 4.4)
    ax.axis('off')
    plt.tight_layout()
    plt.savefig('semestre-03/lab01/Figures/fig_trc_esquema.png', dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()
    print("-> Generado fig_trc_esquema.png")

# -------------------------------------------------------------
# 2. ANATOMÍA DE ONDA SOBRE RETÍCULA DEL OSCILOSCOPIO
# -------------------------------------------------------------
def generar_parametros_onda():
    fig, ax = plt.subplots(figsize=(9, 5.5), dpi=300, facecolor='white')
    ax.set_facecolor('#0F172A') # Fondo oscuro de osciloscopio profesional
    
    # Retícula 10 divisiones horizontales x 8 verticales
    for x in range(0, 11):
        ax.axvline(x, color='#1E293B' if x % 5 != 0 else '#334155', linewidth=1.2 if x % 5 == 0 else 0.8, linestyle='--' if x % 5 != 0 else '-')
        if x < 10:
            for sx in range(1, 5):
                ax.plot([x + sx*0.2, x + sx*0.2], [3.9, 4.1], color='#475569', linewidth=0.8)

    for y in range(0, 9):
        ax.axhline(y, color='#1E293B' if y != 4 else '#334155', linewidth=1.5 if y == 4 else 0.8, linestyle='--' if y != 4 else '-')
        if y < 8:
            for sy in range(1, 5):
                ax.plot([4.9, 5.1], [y + sy*0.2, y + sy*0.2], color='#475569', linewidth=0.8)

    # Señal senoidal (Centro en y=4, Amplitud = 2.4 div, Período = 5.0 div)
    t = np.linspace(0.5, 9.5, 1000)
    V_p_div = 2.4
    T_div = 5.0
    signal = 4.0 + V_p_div * np.sin(2 * np.pi * (t - 1.0) / T_div)
    
    # Trazo de señal amarillo brillante (CH1)
    ax.plot(t, signal, color='#FACC15', linewidth=2.8, label='Canal 1 (CH1: Tensión AC)', zorder=4)
    
    # Línea de referencia GND (y=4)
    ax.plot([0.5, 9.5], [4.0, 4.0], color='#38BDF8', linestyle=':', linewidth=1.5, label='Línea de Referencia Cero (GND)')
    
    # Cotas de Voltaje Pico a Pico (Vpp)
    ax.annotate('', xy=(6.25, 4.0 - V_p_div), xytext=(6.25, 4.0 + V_p_div),
                arrowprops=dict(arrowstyle='<->', color='#F43F5E', lw=2))
    ax.text(6.4, 4.0, '$V_{pp} = 2 V_p = N_{y,pp} \\cdot S_v$', color='#FDA4AF', fontsize=9.5, fontweight='bold', va='center')
    
    # Cota de Voltaje Pico (Vp)
    ax.annotate('', xy=(2.25, 4.0), xytext=(2.25, 4.0 + V_p_div),
                arrowprops=dict(arrowstyle='<->', color='#34D399', lw=2))
    ax.text(2.35, 5.2, '$V_p = N_{y,p} \\cdot S_v$', color='#6EE7B7', fontsize=9.5, fontweight='bold', va='center')

    # Cota de Período (T)
    ax.annotate('', xy=(2.25, 6.7), xytext=(7.25, 6.7),
                arrowprops=dict(arrowstyle='<->', color='#A78BFA', lw=2))
    ax.text(4.75, 7.0, 'Período $T = N_x \\cdot S_t = 1/f$', color='#C4B5FD', fontsize=9.5, fontweight='bold', ha='center')

    # Marcador de Trigger
    ax.scatter([1.0], [4.0], color='#F43F5E', s=80, marker='>', zorder=5)
    ax.text(0.2, 4.3, 'Disparo\nTrigger', color='#F43F5E', fontsize=8, fontweight='bold')

    # Cuadros informativos de escala OSD (On-Screen Display)
    ax.text(0.5, 0.4, 'CH1: 2,00 V/div (DC 1MΩ)', color='#FACC15', fontsize=9, fontweight='bold',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='#1E293B', edgecolor='#FACC15', alpha=0.9))
    ax.text(5.5, 0.4, 'TB: 2,00 ms/div | f = 60,0 Hz', color='#38BDF8', fontsize=9, fontweight='bold',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='#1E293B', edgecolor='#38BDF8', alpha=0.9))

    ax.set_xlim(0, 10)
    ax.set_ylim(0, 8)
    ax.axis('off')
    plt.tight_layout()
    plt.savefig('semestre-03/lab01/Figures/fig_parametros_onda.png', dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()
    print("-> Generado fig_parametros_onda.png")

# -------------------------------------------------------------
# 3. ESQUEMAS DE CIRCUITOS DE CONEXIÓN DE LABORATORIO
# -------------------------------------------------------------
def generar_circuitos_montaje():
    fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(12, 3.8), dpi=300, facecolor='white')
    
    for ax in [ax1, ax2, ax3]:
        ax.set_facecolor('white')
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 8)
        ax.axis('off')
        
    # (a) Circuito Calibración DC
    ax1.set_title('(a) Calibración de Tensión Continua (DC)', fontsize=9.5, fontweight='bold', pad=10, color='#1E293B')
    fuente = patches.FancyBboxPatch((0.8, 2.5), 2.4, 3.0, boxstyle="round,pad=0.2", facecolor='#EFF6FF', edgecolor='#2563EB', lw=1.5)
    ax1.add_patch(fuente)
    ax1.text(2.0, 4.0, 'Fuente DC /\nPila AA\n($V_{\\text{nom}}$)', ha='center', va='center', fontsize=8.5, color='#1E40AF', fontweight='bold')
    
    multi = patches.FancyBboxPatch((4.2, 5.0), 2.2, 2.2, boxstyle="round,pad=0.2", facecolor='#ECFDF5', edgecolor='#059669', lw=1.5)
    ax1.add_patch(multi)
    ax1.text(5.3, 6.1, 'Multímetro\nDigital\n($V_{\\text{mult}}$)', ha='center', va='center', fontsize=8, color='#065F46', fontweight='bold')

    osc = patches.FancyBboxPatch((6.8, 1.8), 2.6, 3.6, boxstyle="round,pad=0.2", facecolor='#FEF2F2', edgecolor='#DC2626', lw=1.5)
    ax1.add_patch(osc)
    ax1.text(8.1, 3.6, 'Osciloscopio\nCanal 1 (CH1)\n($V_{\\text{osc}}$)', ha='center', va='center', fontsize=8.5, color='#991B1B', fontweight='bold')

    # Conexiones eléctricas
    ax1.plot([3.2, 5.3, 5.3], [4.8, 4.8, 5.0], color='#DC2626', lw=2)
    ax1.plot([3.2, 6.8], [4.8, 4.8], color='#DC2626', lw=2)
    ax1.plot([3.2, 5.3, 5.3], [3.2, 3.2, 5.0], color='#1E293B', lw=2)
    ax1.plot([3.2, 6.8], [3.2, 3.2], color='#1E293B', lw=2)
    ax1.text(3.4, 5.1, '(+)', color='#DC2626', fontsize=8, fontweight='bold')
    ax1.text(3.4, 2.7, '(-)', color='#1E293B', fontsize=8, fontweight='bold')

    # (b) Circuito Medición AC
    ax2.set_title('(b) Medición de Formas de Onda AC', fontsize=9.5, fontweight='bold', pad=10, color='#1E293B')
    gen = patches.FancyBboxPatch((0.8, 2.5), 2.8, 3.0, boxstyle="round,pad=0.2", facecolor='#FFFBEB', edgecolor='#D97706', lw=1.5)
    ax2.add_patch(gen)
    ax2.text(2.2, 4.0, 'Generador OWON /\nTransformador\n($60\\text{ Hz} / 250\\text{ Hz}$)', ha='center', va='center', fontsize=8.5, color='#92400E', fontweight='bold')

    osc2 = patches.FancyBboxPatch((6.4, 2.2), 2.8, 3.6, boxstyle="round,pad=0.2", facecolor='#FEF2F2', edgecolor='#DC2626', lw=1.5)
    ax2.add_patch(osc2)
    ax2.text(7.8, 4.0, 'Osciloscopio\nCH1 (AC/1MΩ)\nRetícula $V_p, T$', ha='center', va='center', fontsize=8.5, color='#991B1B', fontweight='bold')

    ax2.plot([3.6, 6.4], [4.6, 4.6], color='#2563EB', lw=2.5, linestyle='-')
    ax2.plot([3.6, 6.4], [3.4, 3.4], color='#1E293B', lw=2.5, linestyle='-')
    ax2.text(5.0, 5.0, 'Cable BNC\nCoaxial', ha='center', fontsize=8, color='#1E40AF', fontweight='bold')

    # (c) Circuito Modo X-Y (Lissajous)
    ax3.set_title('(c) Figuras de Lissajous (Modo X-Y)', fontsize=9.5, fontweight='bold', pad=10, color='#1E293B')
    gen_x = patches.FancyBboxPatch((0.5, 4.5), 2.6, 2.2, boxstyle="round,pad=0.2", facecolor='#EFF6FF', edgecolor='#2563EB', lw=1.5)
    ax3.add_patch(gen_x)
    ax3.text(1.8, 5.6, 'Señal Patrón $f_x$\n(Red $60\\text{ Hz}$)', ha='center', va='center', fontsize=8, color='#1E40AF', fontweight='bold')

    gen_y = patches.FancyBboxPatch((0.5, 1.2), 2.6, 2.2, boxstyle="round,pad=0.2", facecolor='#FFFBEB', edgecolor='#D97706', lw=1.5)
    ax3.add_patch(gen_y)
    ax3.text(1.8, 2.3, 'Señal Variable $f_y$\n(Generador DDS)', ha='center', va='center', fontsize=8, color='#92400E', fontweight='bold')

    osc3 = patches.FancyBboxPatch((6.2, 1.8), 3.2, 4.4, boxstyle="round,pad=0.2", facecolor='#F5F3FF', edgecolor='#7C3AED', lw=1.5)
    ax3.add_patch(osc3)
    ax3.text(7.8, 4.0, 'Osciloscopio\nModo $X$-$Y$\nCH1 $\\to X$\nCH2 $\\to Y$', ha='center', va='center', fontsize=8.5, color='#5B21B6', fontweight='bold')

    ax3.plot([3.1, 6.2], [5.6, 5.6], color='#2563EB', lw=2)
    ax3.plot([3.1, 6.2], [2.3, 2.3], color='#D97706', lw=2)
    ax3.text(4.6, 5.9, 'CH1 ($X$)', ha='center', color='#2563EB', fontsize=8, fontweight='bold')
    ax3.text(4.6, 2.6, 'CH2 ($Y$)', ha='center', color='#D97706', fontsize=8, fontweight='bold')

    plt.tight_layout()
    plt.savefig('semestre-03/lab01/Figures/fig_circuitos_montaje.png', dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()
    print("-> Generado fig_circuitos_montaje.png")

if __name__ == '__main__':
    generar_esquema_trc()
    generar_parametros_onda()
    generar_circuitos_montaje()
