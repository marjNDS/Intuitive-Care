file_path = '../sql/csv/Relatorio_cadop.csv'
output_path = '../sql/csv/Relatorio_cadop_utf8.csv'

with open(file_path, "r", encoding="latin1", errors="ignore") as src:
    content = src.read()

with open(output_path, "w", encoding="utf-8") as dst:
    dst.write(content)

print(f"Arquivo convertido salvo em: {output_path}")
