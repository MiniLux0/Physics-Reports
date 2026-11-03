import json
import numpy as np

with open(r'C:\Users\jrvv9\OneDrive\Desktop\Physics-Reports\semestre-03\lab04\data\data_mesa_c7.json', encoding='utf-8') as f:
    data = json.load(f)

dataset = data['dataset']
resistors = data['resistors']

print('--- INDEPENDENT RE-VERIFICATION OF METROLOGY ---')
delta_cursor = 0.5e-6
u_res_expected = delta_cursor / np.sqrt(12.0)

for d in dataset:
    r_key = d['resistor']
    r_val = resistors[r_key]['val']
    r_scale = resistors[r_key]['u_scale']
    
    # Check u(R)
    u_b_r = (0.008 * r_val + 2.0 * r_scale) / np.sqrt(3.0)
    assert abs(u_b_r - resistors[r_key]['u']) < 1e-9
    assert round(u_b_r, 1) == d['u_r_ohm']
    
    # Check u(tau): ONLY cursor resolution + 50 ppm timebase
    tau_s = d['tau_s']
    u_tau_expected = np.sqrt(u_res_expected**2 + (50e-6 * tau_s)**2)
    assert abs(round(u_tau_expected * 1e6, 2) - d['u_tau_us']) < 1e-9
    assert abs(round(2.0 * u_tau_expected * 1e6, 2) - d['U_tau_us']) < 1e-9
    
    # Check C_exp and u_c
    c_exp_expected = tau_s / r_val
    assert abs(round(c_exp_expected * 1e9, 2) - d['c_exp_nF']) < 1e-9
    
    u_rel_c = np.sqrt((u_tau_expected / tau_s)**2 + (u_b_r / r_val)**2)
    u_c_expected = c_exp_expected * u_rel_c
    assert abs(round(u_c_expected * 1e9, 2) - d['u_c_nF']) < 1e-9
    assert abs(round(2.0 * u_c_expected * 1e9, 2) - d['U_c_nF']) < 1e-9

print('ALL METROLOGICAL UNCERTAINTIES VERIFIED AND MATHEMATICALLY GENUINE!')
