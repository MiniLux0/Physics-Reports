"""
Script para ensamblar automáticamente el informe final manuscrito completo:
Bloque 1 (Jesús Vera: Portada a Materiales) +
Bloque 2 (Gerald Casañe: Procedimiento, Resultados, Tratamiento, Anexo A) +
Bloque 3 (Piero Sánchez: Análisis, Gráficas, Obs/Sug/Conclusiones, Anexos B, C, D) +
Test Metrológico Grupal 5T1 (1 página al final)
"""

import sys
import os
import fitz

def merge_report(jesus_pdf_path=None, output_path="informe_manuscrito_final_completo.pdf"):
    f_gerald = r"C:\Users\jrvv9\Downloads\CamScanner 14-09-2026 23.19.pdf"
    f_piero = r"C:\Users\jrvv9\Downloads\CamScanner 09-14-2026 23.25.pdf"
    f_test = r"C:\Users\jrvv9\OneDrive\Desktop\Physics-Reports\semestre-03\lab01\test_5t1_osciloscopio.pdf"
    
    doc_out = fitz.open()
    
    # 1. Bloque 1: Jesús Vera
    if jesus_pdf_path and os.path.exists(jesus_pdf_path):
        doc_j = fitz.open(jesus_pdf_path)
        print(f"[+] Insertando Bloque 1 (Jesús Vera): {len(doc_j)} páginas")
        doc_out.insert_pdf(doc_j)
    else:
        print("[-] Bloque 1 (Jesús Vera) no especificado o pendiente.")
        
    # 2. Bloque 2: Gerald Casañe
    if os.path.exists(f_gerald):
        doc_g = fitz.open(f_gerald)
        print(f"[+] Insertando Bloque 2 (Gerald Casañe): {len(doc_g)} páginas")
        doc_out.insert_pdf(doc_g)
    else:
        print(f"[!] Archivo de Gerald no encontrado en {f_gerald}")
        
    # 3. Bloque 3: Piero Sánchez
    if os.path.exists(f_piero):
        doc_p = fitz.open(f_piero)
        print(f"[+] Insertando Bloque 3 (Piero Sánchez): {len(doc_p)} páginas")
        doc_out.insert_pdf(doc_p)
    else:
        print(f"[!] Archivo de Piero no encontrado en {f_piero}")
        
    # 4. Test 5T1 oficial (1 página al final)
    if os.path.exists(f_test):
        doc_t = fitz.open(f_test)
        print(f"[+] Insertando Test 5T1 Oficial: {len(doc_t)} página(s)")
        doc_out.insert_pdf(doc_t)
    else:
        print(f"[!] Archivo de Test 5T1 no encontrado en {f_test}")
        
    doc_out.save(output_path)
    print(f"\n[OK] Documento ensamblado exitosamente en: {output_path} ({len(doc_out)} páginas totales)")

if __name__ == "__main__":
    jesus_file = sys.argv[1] if len(sys.argv) > 1 else None
    merge_report(jesus_file)
