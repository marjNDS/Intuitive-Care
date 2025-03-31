import pandas as pd
from pathlib import Path

# Caminho para os CSVs
csv_dir = Path("../sql/csv")
arquivos_csv = sorted(csv_dir.glob("*.csv"))
encoding = 'utf-8'

# Lista para armazenar DataFrames
dfs = []

for arquivo in arquivos_csv:
    print(f"Lendo: {arquivo.name}")

    df = pd.read_csv(arquivo, sep=';', encoding=encoding)

    # Substitui vírgula por ponto apenas nas colunas numéricas
    for coluna in ['VL_SALDO_INICIAL', 'VL_SALDO_FINAL']:
        if coluna in df.columns:
            df[coluna] = (
                df[coluna]
                .astype(str)
                .str.replace(',', '.', regex=False)
                .astype(float)
            )

    dfs.append(df)

df_unificado = pd.concat(dfs, ignore_index=True)

saida = csv_dir / "demonstracoes_contabeis_unificado.csv"
df_unificado.to_csv(saida, sep=';', index=False, encoding=encoding)

print(f"\n✅ Arquivo final salvo em: {saida}")
