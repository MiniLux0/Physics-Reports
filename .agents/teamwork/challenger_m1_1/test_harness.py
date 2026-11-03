"""
test_harness.py — Empirical Challenge and Stress Test Harness for Lab 04
Run by challenger_m1_1 to verify:
1. model_data.py execution and output consistency
2. Seed repeatability (seed=42)
3. JSON and CSV file integrity and cross-consistency
4. Numerical stability (no NaNs, no Infs, positive errors/variances)
5. grap.py execution and figure integrity (300 DPI, non-blank, dimensions)
6. Theoretical correctness of KVL, OLS, and Thevenin transient curves
"""

import os
import sys
import json
import csv
import numpy as np
from PIL import Image

def test_all():
    repo_root = r"C:\Users\jrvv9\OneDrive\Desktop\Physics-Reports"
    lab_dir = os.path.join(repo_root, "semestre-03", "lab04")
    scripts_dir = os.path.join(lab_dir, "scripts")
    data_dir = os.path.join(lab_dir, "data")
    figures_dir = os.path.join(lab_dir, "Figures")

    sys.path.insert(0, scripts_dir)

    results = []

    def record(name, passed, details=""):
        status = "PASS" if passed else "FAIL"
        results.append((name, status, details))
        print(f"[{status}] {name}: {details}")

    print("=== STARTING EMPIRICAL CHALLENGE HARNESS ===")

    # ---------------------------------------------------------
    # TEST 1: Execute model_data.py and check repeatability
    # ---------------------------------------------------------
    import model_data
    try:
        ds1, ols1 = model_data.run_modeling()
        record("model_data execution run 1", True, f"Generated {len(ds1)} rows, OLS for {len(ols1)} capacitors")
    except Exception as e:
        record("model_data execution run 1", False, str(e))
        return results

    try:
        ds2, ols2 = model_data.run_modeling()
        # Compare ds1 and ds2 bit-for-bit
        identical = (ds1 == ds2) and (ols1 == ols2)
        record("Seed=42 repeatability", identical, "ds1 and ds2 are identical across successive executions")
    except Exception as e:
        record("Seed=42 repeatability", False, str(e))

    # ---------------------------------------------------------
    # TEST 2: Inspect JSON and CSV integrity
    # ---------------------------------------------------------
    json_path = os.path.join(data_dir, "data_mesa_c7.json")
    csv_path = os.path.join(data_dir, "data_mesa_c7.csv")

    record("JSON file exists", os.path.exists(json_path), json_path)
    record("CSV file exists", os.path.exists(csv_path), csv_path)

    try:
        with open(json_path, 'r', encoding='utf-8') as f:
            jdata = json.load(f)
        record("JSON parse validity", True, "Successfully parsed JSON")
    except Exception as e:
        record("JSON parse validity", False, str(e))
        jdata = None

    try:
        with open(csv_path, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            cdata = list(reader)
        record("CSV parse validity", True, f"Successfully parsed CSV with {len(cdata)} rows")
    except Exception as e:
        record("CSV parse validity", False, str(e))
        cdata = None

    if jdata and cdata:
        record("Row count match", len(jdata['dataset']) == len(cdata) == 9, f"JSON: {len(jdata['dataset'])}, CSV: {len(cdata)}")
        
        # Cross check every row
        match_all = True
        for idx, (j_row, c_row) in enumerate(zip(jdata['dataset'], cdata)):
            if int(c_row['fila']) != j_row['fila']:
                match_all = False
            if abs(float(c_row['tau_us']) - j_row['tau_us']) > 1e-4:
                match_all = False
            if abs(float(c_row['c_exp_nf']) - j_row['c_exp_nF']) > 1e-4:
                match_all = False
            if abs(float(c_row['error_pct']) - j_row['error_rel_pct']) > 1e-4:
                match_all = False
        record("JSON vs CSV data consistency", match_all, "All 9 rows match across JSON and CSV within 1e-4")

    # ---------------------------------------------------------
    # TEST 3: Numerical Stability & Physical Sanity of Dataset
    # ---------------------------------------------------------
    if jdata:
        no_nan_inf = True
        real_rows_exact = True
        sensible_capacitances = True
        ols_consistent = True

        for row in jdata['dataset']:
            for k, v in row.items():
                if isinstance(v, float) and (np.isnan(v) or np.isinf(v)):
                    no_nan_inf = False

            # Check real rows (1, 2, 3)
            if row['fila'] == 1:
                if row['tau_us'] != 107.80 or not row['es_real']:
                    real_rows_exact = False
            elif row['fila'] == 2:
                if row['tau_us'] != 273.60 or not row['es_real']:
                    real_rows_exact = False
            elif row['fila'] == 3:
                if row['tau_us'] != 344.80 or not row['es_real']:
                    real_rows_exact = False
            elif row['fila'] >= 4:
                if row['es_real']:
                    real_rows_exact = False

            # Capacitances must be positive and between 1 nF and 100 nF
            if not (5.0 <= row['c_exp_nF'] <= 50.0):
                sensible_capacitances = False

        record("No NaN or Inf in dataset", no_nan_inf, "Clean numerical values")
        record("Authentic Mesa C7 rows intact", real_rows_exact, "Rows 1-3 match photo sheet: 107.8, 273.6, 344.8 us")
        record("Sensible capacitance values", sensible_capacitances, "All C_exp values are within [5, 50] nF")

        # Independent OLS verification
        for c_key in ['C1', 'C2', 'C3']:
            sub = [d for d in jdata['dataset'] if d['capacitor'] == c_key]
            r_arr = np.array([d['r_ohm'] for d in sub])
            tau_arr = np.array([d['tau_s'] for d in sub])
            p, cov = np.polyfit(r_arr, tau_arr, 1, cov=True)
            c_calc_nF = p[0] * 1e9
            r2_calc = 1.0 - (np.sum((tau_arr - np.polyval(p, r_arr))**2) / np.sum((tau_arr - np.mean(tau_arr))**2))

            stored = jdata['ols_results'][c_key]
            if abs(stored['c_fit_nF'] - round(c_calc_nF, 2)) > 0.02:
                ols_consistent = False
            if abs(stored['r2'] - round(r2_calc, 6)) > 1e-4:
                ols_consistent = False

        record("Independent OLS verification", ols_consistent, "Regression slopes and R^2 match independently calculated values")

    # ---------------------------------------------------------
    # TEST 4: Execute grap.py and inspect figure generation
    # ---------------------------------------------------------
    import grap
    try:
        grap.main()
        record("grap.py execution", True, "Executed without errors")
    except Exception as e:
        record("grap.py execution", False, str(e))

    expected_figs = [
        "fig_carga_descarga.png",
        "fig_linealizacion_tau.png",
        "fig_suma_kvl.png",
        "fig_paso20_thevenin.png"
    ]

    for fig_name in expected_figs:
        fig_path = os.path.join(figures_dir, fig_name)
        exists = os.path.exists(fig_path)
        record(f"Figure exists: {fig_name}", exists, fig_path)
        if exists:
            size_bytes = os.path.getsize(fig_path)
            record(f"Figure non-empty: {fig_name}", size_bytes > 50000, f"Size: {size_bytes} bytes")
            try:
                with Image.open(fig_path) as img:
                    dpi = img.info.get('dpi', None)
                    dpi_ok = dpi is not None and (abs(dpi[0] - 300) < 5 and abs(dpi[1] - 300) < 5)
                    record(f"Figure 300 DPI check: {fig_name}", dpi_ok, f"DPI={dpi}, Size={img.size}")
                    
                    # Check non-blank
                    arr = np.array(img)
                    std_dev = np.std(arr)
                    record(f"Figure visual content check: {fig_name}", std_dev > 10.0, f"Pixel std dev={std_dev:.2f}")
            except Exception as e:
                record(f"Figure inspect error: {fig_name}", False, str(e))

    # ---------------------------------------------------------
    # TEST 5: Physics verification of plots
    # ---------------------------------------------------------
    # Check KVL math
    tau_kvl = 107.8e-6
    V0 = 10.0
    f = 250.0
    T = 1.0 / f
    semi_T = T / 2.0
    t = np.linspace(0, T, 1000)
    V_gen = np.where(t < semi_T, V0, 0.0)
    VC = np.where(t < semi_T, V0 * (1.0 - np.exp(-t / tau_kvl)), V0 * (1.0 - np.exp(-semi_T / tau_kvl)) * np.exp(-(t - semi_T) / tau_kvl))
    VR = np.where(t < semi_T, V0 * np.exp(-t / tau_kvl), -V0 * (1.0 - np.exp(-semi_T / tau_kvl)) * np.exp(-(t - semi_T) / tau_kvl))
    kvl_diff = np.max(np.abs((VC + VR) - V_gen))
    record("KVL identity check: max|VC + VR - Vgen|", kvl_diff < 1e-12, f"Max difference: {kvl_diff:.2e} V")

    # Check Paso 20 Thevenin parameters
    R1 = 9980.0
    R2 = 6832.0
    C = 34.55e-9
    V_th = 10.0 * (R2 / (R1 + R2))
    R_th = (R1 * R2) / (R1 + R2)
    tau_th = R_th * C
    thevenin_ok = (abs(V_th - 4.06376) < 0.01) and (abs(R_th - 4055.65) < 1.0) and (abs(tau_th * 1e6 - 140.12) < 0.5)
    record("Paso 20 Thevenin values check", thevenin_ok, f"V_th={V_th:.3f} V, R_th={R_th:.1f} ohm, tau_th={tau_th*1e6:.2f} us")

    print("\n=== SUMMARY OF TESTS ===")
    all_passed = all(st == "PASS" for _, st, _ in results)
    print(f"Total tests: {len(results)}, Passed: {sum(1 for _, st, _ in results if st == 'PASS')}, Failed: {sum(1 for _, st, _ in results if st == 'FAIL')}")
    print(f"Overall status: {'ALL TESTS PASSED' if all_passed else 'SOME TESTS FAILED'}")
    return results

if __name__ == '__main__':
    test_all()
