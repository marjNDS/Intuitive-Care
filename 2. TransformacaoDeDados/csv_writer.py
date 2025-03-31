import pandas as pd
from typing import Union
from pathlib import Path

def save_dataframe_to_csv(df: pd.DataFrame, output_path: Union[str, Path], encoding: str = "utf-8", index: bool = False) -> Path:
    """
    Salva um DataFrame como um arquivo CSV

    :param df: DataFrame a ser salvo
    :param output_path: Caminho do arquivo CSV de saída (com .csv no final)
    :param encoding: Codificação do arquivo (padrão: utf-8)
    :param index: Se deve salvar o índice como coluna no CSV (padrão: False)
    :return: Caminho do arquivo CSV salvo
    """
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)  # Garante que a pasta exista

    df.to_csv(output_path, index=index, encoding=encoding)

    return output_path
