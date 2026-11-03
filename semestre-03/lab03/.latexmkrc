# .latexmkrc
$pdf_mode   = 1;        # usar pdflatex
$bibtex_use = 2;        # usar biber
$out_dir    = 'out';    # auxiliares en out/
$pdflatex   = 'pdflatex -interaction=nonstopmode -synctex=1 %O %S';

# copiar el PDF a la raiz del lab despues de compilar
$success_cmd = 'powershell -Command "Copy-Item \'%D\' \'%R.pdf\'"';
