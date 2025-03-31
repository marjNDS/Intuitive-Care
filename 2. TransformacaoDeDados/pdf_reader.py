import pdfplumber
import pandas as pd
from typing import Union, List
from pathlib import Path

def _clean_table(table: List[List[str]]) -> pd.DataFrame:
    """
    Limpa quebras de linha e espaços de uma tabela extraída e transforma em DataFrame.

    :param table: o dataframe a ser limpo.
    :return: dataframe sem quebras de linhas e espaços em branco no início ou fim do dado.
    """
    clean_table = [
        [cell.replace('\n', ' ').strip() if cell else '' for cell in row]
        for row in table
    ]
    return pd.DataFrame(clean_table[1:], columns=clean_table[0])

def _replace_abreviations(df: pd.DataFrame) -> pd.DataFrame:
    """
    Substitui as abreviações nas colunas OD e AMB por descrições completas.

    :param df: o dataframe a ser tratado
    :return:
    """
    replacers = {
        "OD": {"OD": "Seg. Odontológica"},
        "AMB": {"AMB": "Seg. Ambulatorial"}
    }

    for col, map in replacers.items():
        if col in df.columns:
            df[col] = df[col].replace(map)
    return df

def extract_tables_from_pdf(pdf_path: Union[str, Path]) -> pd.DataFrame:
    """
    Extrai todas as tabelas do PDF do Anexo I, página por página, e retorna como um único DataFrame.

    :param pdf_path: Caminho para o arquivo PDF.
    :return: DataFrame contendo a junção de todas as tabelas extraídas.
    """
    all_tables = []

    with pdfplumber.open(pdf_path) as pdf:
        for i, page in enumerate(pdf.pages):
            table = page.extract_table()

            if not table:
                continue

            df = _clean_table(table)
            df = _replace_abreviations(df)
            all_tables.append(df)

    if not all_tables:
        raise ValueError("Nenhuma tabela foi encontrada no PDF.")

    return pd.concat(all_tables, ignore_index=True)
