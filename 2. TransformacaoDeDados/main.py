from pdf_reader import extract_tables_from_pdf
from csv_writer import save_dataframe_to_csv
from zipper import zip_files

seu_nome = "Marjory"

df = extract_tables_from_pdf("read/Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf")
csv_path = save_dataframe_to_csv(df = df, output_path = "output/anexo1.csv", encoding = "utf-8-sig")
print(f"CSV salvo em: {csv_path}")
zip_files([csv_path], f"output/Teste_{seu_nome}.zip")
print(f"Zip salvo em: {csv_path}")
