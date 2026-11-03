import os
from pypdf import PdfReader

pdf_path = r'C:\Users\jrvv9\OneDrive\Desktop\Physics-Reports\semestre-03\lab04\main.pdf'
out_pdf_path = r'C:\Users\jrvv9\OneDrive\Desktop\Physics-Reports\semestre-03\lab04\out\main.pdf'

print('--- INDEPENDENT VERIFICATION OF MAIN.PDF ---')
for p in [pdf_path, out_pdf_path]:
    print(f'Checking {p}:')
    assert os.path.exists(p), f'File does not exist: {p}'
    size = os.path.getsize(p)
    print(f'  Size: {size} bytes ({size / 1024 / 1024:.2f} MB)')
    
    with open(p, 'rb') as f:
        header = f.read(10)
        f.seek(-1024, os.SEEK_END)
        tail = f.read(1024)
        assert b'%PDF-' in header, f'Invalid PDF header: {header}'
        assert b'%%EOF' in tail, f'Missing %%EOF in tail: {tail[-100:]}'
    
    reader = PdfReader(p)
    num_pages = len(reader.pages)
    meta = reader.metadata
    print(f'  Pages: {num_pages}')
    print(f'  Producer: {meta.producer if meta else None}')
    print(f'  Creator: {meta.creator if meta else None}')
    print(f'  CreationDate: {meta.creation_date if meta else None}')
    
    assert num_pages == 23, f'Expected 23 pages, got {num_pages}'
    assert size > 1300000 and size < 1400000, f'Expected ~1.33 MB, got {size}'
    assert 'pdfTeX' in meta.producer or 'MiKTeX' in meta.producer, f'Suspicious producer: {meta.producer}'

print('PDF INTEGRITY AND COMPILATION LEGITIMACY VERIFIED!')
