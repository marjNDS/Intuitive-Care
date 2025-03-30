from typing import List
from pathlib import Path
import requests
import os
from tqdm import tqdm
from concurrent.futures import ThreadPoolExecutor, as_completed

def download_file(url: str, dest_folder: str) -> Path:
    """
    Faz o download de um único arquivo e salva no diretório especificado.

    :param url: URL do arquivo.
    :param dest_folder: Diretório de destino.
    :return: Caminho completo do arquivo salvo.
    """
    filename = url.split("/")[-1].split("?")[0]
    filepath = Path(dest_folder) / filename

    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()

        with open(filepath, "wb") as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)

        return filepath
    except Exception as e:
        tqdm.write(f"[ERRO] Falha ao baixar {url}: {e}")
        return None

def download_files(urls: List[str], dest_folder: str = "downloads", max_workers: int = 5) -> List[Path]:
    """
    Faz o download paralelo de arquivos com barra de progresso.

    :param urls: Lista de URLs dos arquivos.
    :param dest_folder: Pasta onde os arquivos serão salvos.
    :param max_workers: Número de threads paralelas (default: 5).
    :return: Lista de caminhos dos arquivos baixados com sucesso.
    """
    # Garante que o diretório de destino exista
    os.makedirs(dest_folder, exist_ok=True)
    saved_files = []  # Lista para armazenar os caminhos dos arquivos salvos

    # Cria um pool de threads para execução paralela dos downloads
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        # Mapeia cada URL a uma "future" (chamada assíncrona da função download_file)
        futures = {
            executor.submit(download_file, url, dest_folder): url
            for url in urls
        }

        # Exibe uma barra de progresso e aguarda cada download terminar
        for future in tqdm(
            as_completed(futures), total=len(futures),
            desc="Baixando arquivos", unit="arquivo"
        ):
            result = future.result()  # Obtém o resultado da thread (caminho do arquivo)
            if result:
                saved_files.append(result)  # Se o download deu certo, adiciona à lista final

    return saved_files  # Retorna todos os caminhos dos arquivos que foram baixados com sucesso

