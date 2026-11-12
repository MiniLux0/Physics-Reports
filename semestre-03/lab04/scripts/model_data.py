"""
model_data.py — Procesamiento Numérico de Datos Experimentales para Lab 04 (Circuitos RC)
Repositorio: Physics-Reports / semestre-03/lab04
Mesa de Trabajo: Mesa C7 (Jesús Vera, Gerald Casañe, Piero Sánchez)
Cátedra: Física III (CF2B1, Sección A) — Universidad Nacional de Ingeniería (UNI)

Este script:
1. Incorpora las mediciones experimentales de la Mesa C7 (Filas 1 a 9 tomadas en laboratorio).
2. Procesa y analiza las configuraciones ensayadas con cursores del osciloscopio digital.
3. Propaga incertidumbres metrológicas según la Guía GUM (JCGM 100:2008).
4. Realiza ajustes por Mínimos Cuadrados Ordinarios (OLS) para tau vs R por cada condensador.
5. Clarifica el origen de las confusiones preliminares (440 ohm y 250 ohm vs 2.250 k-ohm y 250 Hz).
6. Exporta los datos en formatos JSON, CSV y fragmentos LaTeX listos para el informe.
"""

import os
import json
import numpy as np

def process_data():
    # -------------------------------------------------------------------------
    # 0. Clarificación Metrológica de Parámetros preliminares
    # -------------------------------------------------------------------------
    clarification_note = (
        "NOTA METROLÓGICA SOBRE VALORES RESISTIVOS PRELIMINARES:\n"
        "- '440 ohm': Corresponde al reóstato de laboratorio empleado en Lab 01 y Lab 03,\n"
        "  el cual no forma parte del módulo de circuitos impresos RC de Lab 04.\n"
        "- '250 ohm': Corresponde a una lectura errónea de R3 = 2,250 k-ohm (2250 ohm)\n"
        "  o una confusión con la frecuencia de excitación f = 250 Hz del generador OWON AG 051F.\n"
        "- '1000 ohm': Resistencia nominal R1 usada en la caja de la mesa de compañeros (0.97 k-ohm).\n"
        "  En la Mesa C7 propia, los valores medidos con multímetro fueron:\n"
        "  R1 = 9.98 k-ohm, R2 = 6.832 k-ohm, R3 = 2.250 k-ohm.\n"
    )
    print(clarification_note)

    # -------------------------------------------------------------------------
    # 1. Parámetros de Componentes e Instrumentos de la Mesa C7
    # -------------------------------------------------------------------------
    # Frecuencia de la onda cuadrada
    f_gen = 250.0  # Hz
    T_gen = 1.0 / f_gen  # 4.0 ms
    semi_T = T_gen / 2.0  # 2.0 ms = 2000 us

    # Resistencias medidas con Multímetro Digital (tolerancia: +- (0.8% + 2 dgt))
    # Resolución multímetro: R1: 0.01 k-ohm (10 ohm); R2: 0.001 k-ohm (1 ohm); R3: 0.001 k-ohm (1 ohm)
    resistors = {
        'R1': {'val': 9980.0, 'nom': 10000.0, 'str_val': '9,98 k', 'u_scale': 10.0},
        'R2': {'val': 6832.0, 'nom': 6800.0, 'str_val': '6,832 k', 'u_scale': 1.0},
        'R3': {'val': 2250.0, 'nom': 2200.0, 'str_val': '2,250 k', 'u_scale': 1.0}
    }

    # Cálculo de incertidumbres Tipo B de las resistencias (GUM)
    for r_key, r_info in resistors.items():
        # u(R) = (0.008 * R + 2 * resolucion) / sqrt(3)
        u_b = (0.008 * r_info['val'] + 2.0 * r_info['u_scale']) / np.sqrt(3.0)
        r_info['u'] = u_b

    # Capacitores asignados (valores nominales / LCR rotulados de caja)
    capacitors = {
        'C1': {'nom_F': 10.00e-9, 'nom_nF': 10.00, 'label': '0,01 µF / 10,0 nF'},
        'C2': {'nom_F': 22.40e-9, 'nom_nF': 22.40, 'label': '0,02240 µF / 22,40 nF'},
        'C3': {'nom_F': 33.23e-9, 'nom_nF': 33.23, 'label': '33,23 nF'}
    }

    # -------------------------------------------------------------------------
    # 2. Mediciones Experimentales de la Mesa C7 (Filas 1 a 9)
    # -------------------------------------------------------------------------
    # Matriz experimental completa registrada en el osciloscopio digital HMO1202
    rows_definition = [
        {'row_idx': 1, 'r_key': 'R1', 'c_key': 'C1', 'tau_us': 107.80},
        {'row_idx': 2, 'r_key': 'R1', 'c_key': 'C2', 'tau_us': 273.60},
        {'row_idx': 3, 'r_key': 'R1', 'c_key': 'C3', 'tau_us': 344.80},
        {'row_idx': 4, 'r_key': 'R2', 'c_key': 'C1', 'tau_us': 74.20},
        {'row_idx': 5, 'r_key': 'R2', 'c_key': 'C2', 'tau_us': 187.00},
        {'row_idx': 6, 'r_key': 'R2', 'c_key': 'C3', 'tau_us': 237.90},
        {'row_idx': 7, 'r_key': 'R3', 'c_key': 'C1', 'tau_us': 24.40},
        {'row_idx': 8, 'r_key': 'R3', 'c_key': 'C2', 'tau_us': 61.50},
        {'row_idx': 9, 'r_key': 'R3', 'c_key': 'C3', 'tau_us': 77.50},
    ]

    dataset = []
    for item in rows_definition:
        r_val = resistors[item['r_key']]['val']
        r_u = resistors[item['r_key']]['u']
        c_nom = capacitors[item['c_key']]['nom_F']
        c_nom_nF = capacitors[item['c_key']]['nom_nF']

        tau_us = item['tau_us']
        tau_s = tau_us * 1e-6

        # Incertidumbre estándar en tau (Osciloscopio digital Rohde & Schwarz HMO1202, según GUM Tipo B)
        # u(tau) = sqrt((Delta_cursor / sqrt(12))^2 + (50 ppm * tau)^2)
        # - Resolución del cursor digital en escala 500 us/div: Delta_cursor = 0.5 us
        #   Distribución rectangular Tipo B: u_res = Delta_cursor / sqrt(12) approx 0.144 us
        # - Exactitud de la base de tiempo: 50 ppm (0.005%)
        delta_cursor = 0.5e-6
        u_tau = np.sqrt((delta_cursor / np.sqrt(12.0))**2 + (50e-6 * tau_s)**2)

        # Cálculo de Capacitancia experimental C = tau / R
        c_exp = tau_s / r_val
        c_exp_nF = c_exp * 1e9

        # Propagación de Incertidumbre GUM para C = tau / R:
        # u_rel(C) = sqrt( (u(tau)/tau)^2 + (u(R)/R)^2 )
        u_rel_c = np.sqrt((u_tau / tau_s)**2 + (r_u / r_val)**2)
        u_c = c_exp * u_rel_c
        u_c_nF = u_c * 1e9

        # Incertidumbre expandida (k=2, 95.45% de confianza)
        U_c_nF = 2.0 * u_c_nF

        # Error relativo respecto al valor nominal rotulado
        error_rel_pct = ((c_exp - c_nom) / c_nom) * 100.0

        dataset.append({
            'fila': item['row_idx'],
            'resistor': item['r_key'],
            'r_ohm': r_val,
            'r_str': resistors[item['r_key']]['str_val'],
            'u_r_ohm': round(r_u, 1),
            'f_hz': f_gen,
            'capacitor': item['c_key'],
            'tau_us': tau_us,
            'tau_s': tau_s,
            'u_tau_us': round(u_tau * 1e6, 2),
            'U_tau_us': round(2.0 * u_tau * 1e6, 2),
            'c_exp_nF': round(c_exp_nF, 2),
            'u_c_nF': round(u_c_nF, 2),
            'U_c_nF': round(U_c_nF, 2),
            'c_nom_nF': c_nom_nF,
            'error_rel_pct': round(error_rel_pct, 2)
        })

    # -------------------------------------------------------------------------
    # 3. Impresión del Cuadro de Datos Completo
    # -------------------------------------------------------------------------
    print("=" * 85)
    print("CUADRO DE DATOS EXPERIMENTALES — MESA C7 (FÍSICA III, LAB 04)")
    print("=" * 85)
    header = f"{'Fila':<4} | {'R (ohm)':<10} | {'f (Hz)':<6} | {'tau (us)':<10} | {'C_exp (nF)':<14} | {'C_nom (nF)':<10} | {'Error (%)':<9}"
    print(header)
    print("-" * 85)
    for d in dataset:
        row_str = (
            f"{d['fila']:<4} | {d['r_ohm']:<10.1f} | {d['f_hz']:<6.0f} | "
            f"{d['tau_us']:<10.1f} | {d['c_exp_nF']:>5.2f} +- {d['U_c_nF']:<4.2f} | "
            f"{d['c_nom_nF']:<10.2f} | {d['error_rel_pct']:>+7.2f}%"
        )
        print(row_str)
    print("=" * 85)

    # -------------------------------------------------------------------------
    # 4. Ajustes Lineales por Mínimos Cuadrados Ordinarios (tau vs R)
    # -------------------------------------------------------------------------
    # tau = C * R + b (b debe ser estadísticamente indistinguible de cero)
    print("\nAJUSTE POR MÍNIMOS CUADRADOS ORDINARIOS (MCO/OLS): tau vs R")
    print("-" * 80)
    ols_results = {}
    for c_key in ['C1', 'C2', 'C3']:
        sub = [d for d in dataset if d['capacitor'] == c_key]
        r_arr = np.array([d['r_ohm'] for d in sub])
        tau_arr = np.array([d['tau_s'] for d in sub])

        # OLS: y = m*x + b
        N = len(r_arr)
        p, cov = np.polyfit(r_arr, tau_arr, 1, cov=True)
        slope = p[0]  # C_fit (Faradios)
        intercept = p[1]  # s
        s_m = np.sqrt(cov[0, 0])
        s_b = np.sqrt(cov[1, 1])

        # R^2
        tau_pred = slope * r_arr + intercept
        ss_res = np.sum((tau_arr - tau_pred)**2)
        ss_tot = np.sum((tau_arr - np.mean(tau_arr))**2)
        r2 = 1.0 - (ss_res / ss_tot)

        c_fit_nF = slope * 1e9
        s_c_nF = s_m * 1e9
        c_nom_nF = capacitors[c_key]['nom_nF']
        err_fit_pct = ((c_fit_nF - c_nom_nF) / c_nom_nF) * 100.0

        # Evaluación de consistencia física del intercepto:
        # Criterio empírico 2-sigma: |b| / s_b < 2.0
        t_stat = abs(intercept) / s_b
        passed_2sigma = bool(t_stat < 2.0)

        ols_results[c_key] = {
            'c_fit_nF': round(c_fit_nF, 2),
            's_c_nF': round(s_c_nF, 2),
            'intercept_s': intercept,
            'intercept_us': round(intercept * 1e6, 2),
            's_b_us': round(s_b * 1e6, 2),
            't_stat': round(t_stat, 2),
            'passed_2sigma': passed_2sigma,
            'r2': round(r2, 6),
            'err_fit_pct': round(err_fit_pct, 2),
            'nom_nF': c_nom_nF
        }

        print(f"Condensador {c_key} (Nominal: {c_nom_nF:.2f} nF):")
        print(f"  -> Capacitancia ajustada (pendiente): C_fit = ({c_fit_nF:.2f} +- {s_c_nF:.2f}) nF")
        print(f"  -> Intercepto: b = ({intercept*1e6:.2f} +- {s_b*1e6:.2f}) us  (|b|/s_b = {t_stat:.2f} | 2-sigma < 2.0: {passed_2sigma})")
        print(f"  -> Coeficiente R^2: {r2:.6f}")
        print(f"  -> Error relativo vs nominal: {err_fit_pct:+.2f}%\n")

    # -------------------------------------------------------------------------
    # 5. Exportación de Resultados
    # -------------------------------------------------------------------------
    data_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data'))
    os.makedirs(data_dir, exist_ok=True)

    json_path = os.path.join(data_dir, 'data_mesa_c7.json')
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump({
            'resistors': resistors,
            'capacitors': capacitors,
            'dataset': dataset,
            'ols_results': ols_results,
            'clarification': clarification_note
        }, f, indent=2, ensure_ascii=False)
    print(f"[OK] Datos guardados en JSON: {json_path}")

    csv_path = os.path.join(data_dir, 'data_mesa_c7.csv')
    with open(csv_path, 'w', encoding='utf-8') as f:
        f.write("fila,resistencia_ohm,frecuencia_hz,tau_us,u_tau_us,c_exp_nf,u_c_nf,U_c_nf,c_nom_nf,error_pct\n")
        for d in dataset:
            f.write(f"{d['fila']},{d['r_ohm']},{d['f_hz']},{d['tau_us']},{d['u_tau_us']},{d['c_exp_nF']},{d['u_c_nF']},{d['U_c_nF']},{d['c_nom_nF']},{d['error_rel_pct']}\n")
    print(f"[OK] Datos guardados en CSV: {csv_path}")

    return dataset, ols_results

run_modeling = process_data

if __name__ == '__main__':
    process_data()
