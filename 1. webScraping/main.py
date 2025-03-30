from downloader import download_files
from zipper import zip_files
from scraper import get_file_links_by_keyword_and_extension
from pathlib import Path

if __name__ == "__main__":
    site_url = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"
    filters = {
        "Anexo I": ".pdf",
        "Anexo II": ".pdf",
    }

    pdf_urls = get_file_links_by_keyword_and_extension(site_url, filters)
    files_paths = download_files(pdf_urls)
    print(files_paths)
    zip_files(files=files_paths, output_zip_path="downloads/compactado.zip")
