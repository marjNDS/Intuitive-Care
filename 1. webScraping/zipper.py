from typing import List
from pathlib import Path
import zipfile
import os

def zip_files(files: List[Path], output_zip_path: str = "arquivos.zip") -> Path:
    """
    Compacta os arquivos fornecidos em um único arquivo .zip.

    :param files: Lista de caminhos para os arquivos que serão compactados.
    :param output_zip_path: Nome ou caminho completo do arquivo .zip de saída.
    :return: Caminho para o arquivo .zip gerado.
    """
    output_path = Path(output_zip_path)

    # Garante que o diretório onde o zip será salvo exista
    os.makedirs(output_path.parent, exist_ok=True)

    # Cria o arquivo .zip e adiciona os arquivos dentro dele
    with zipfile.ZipFile(output_path, mode="w", compression=zipfile.ZIP_DEFLATED) as zipf:
        for file in files:
            if file.exists():
                # arcname define o nome do arquivo dentro do zip (sem o caminho completo)
                zipf.write(file, arcname=file.name)

    return output_path
