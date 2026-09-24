import re

files = [r'g:\Seo\carpinteria web\index.html', r'g:\Seo\carpinteria web\carpinteria-aluminio-pvc.html']

replacements = {
    'href="/"': 'href="index.html"',
    'href="/muebles-a-medida"': 'href="muebles-a-medida.html"',
    'href="/puertas-madera"': 'href="puertas-madera.html"',
    'href="/armarios-empotrados"': 'href="armarios-empotrados.html"',
    'href="/cocinas-a-medida"': 'href="cocinas-a-medida.html"',
    'href="/suelos-tarima-parquet"': 'href="suelos-tarima-parquet.html"',
    'href="/carpinteria-aluminio-pvc"': 'href="carpinteria-aluminio-pvc.html"',
    'href="/ebanisteria-restauracion"': 'href="ebanisteria-restauracion.html"',
}

for file_path in files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    for old, new in replacements.items():
        content = content.replace(old, new)
        
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

print('Links updated to include .html for local testing.')
