import json
import numpy as np

with open(r'C:\Users\jrvv9\OneDrive\Desktop\Physics-Reports\semestre-03\lab04\data\data_mesa_c7.json', encoding='utf-8') as f:
    data = json.load(f)

dataset = data['dataset']
ols_results = data['ols_results']

print('--- INDEPENDENT RE-VERIFICATION OF OLS ---')
for c_key in ['C1', 'C2', 'C3']:
    rows = [d for d in dataset if d['capacitor'] == c_key]
    R = np.array([d['r_ohm'] for d in rows])
    tau = np.array([d['tau_s'] for d in rows])
    
    # Independent Polyfit
    p, cov = np.polyfit(R, tau, 1, cov=True)
    slope = p[0]
    intercept = p[1]
    s_m = np.sqrt(cov[0, 0])
    s_b = np.sqrt(cov[1, 1])
    
    t_stat = abs(intercept) / s_b
    passed_2sigma = bool(t_stat < 2.0)
    passed_student = bool(t_stat < 12.706)
    
    tau_pred = slope * R + intercept
    ss_res = np.sum((tau - tau_pred)**2)
    ss_tot = np.sum((tau - np.mean(tau))**2)
    r2 = 1.0 - (ss_res / ss_tot)
    
    rec = ols_results[c_key]
    
    print(f"{c_key}:")
    print(f"  Calculated slope: {slope*1e9:.4f} nF vs Recorded: {rec['c_fit_nF']} +- {rec['s_c_nF']}")
    print(f"  Calculated intercept: {intercept*1e6:.4f} us vs Recorded: {rec['intercept_us']} +- {rec['s_b_us']}")
    print(f"  Calculated t_stat: {t_stat:.4f} vs Recorded: {rec['t_stat']}")
    print(f"  Calculated passed_2sigma: {passed_2sigma} vs Recorded: {rec['passed_2sigma']}")
    print(f"  Calculated passed_student: {passed_student} vs Recorded: {rec['passed_student']}")
    print(f"  Calculated R2: {r2:.6f} vs Recorded: {rec['r2']}")
    
    assert round(slope*1e9, 2) == rec['c_fit_nF']
    assert round(s_m*1e9, 2) == rec['s_c_nF']
    assert round(intercept*1e6, 2) == rec['intercept_us']
    assert round(s_b*1e6, 2) == rec['s_b_us']
    assert round(t_stat, 2) == rec['t_stat']
    assert passed_2sigma == rec['passed_2sigma']
    assert passed_student == rec['passed_student']
    assert round(r2, 6) == rec['r2']
print('ALL OLS RE-CALCULATIONS MATCH EXACTLY!')
