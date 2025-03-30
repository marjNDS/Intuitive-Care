from typing import Dict, List
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def get_file_links_by_keyword_and_extension(url: str, filters: Dict[str, str]) -> List[str]:
    """
    Busca e retorna links para arquivos com base em um dicionário associando palavras-chave a extensões.

    :param url: URL da página a ser analisada.
    :param filters: Dicionário onde a chave é a palavra-chave a ser buscada no texto do link
                    e o valor é a extensão esperada do arquivo (ex: { "Anexo I": ".pdf" }).
    :return: Lista de URLs completas para download dos arquivos.
    """

    # requisição para obter o conteúdo da página
    response = requests.get(url)
    response.raise_for_status()  #erro se falhar

    #parse do HTML
    soup = BeautifulSoup(response.text, 'html.parser')

    #todos os elementos <a> com href
    links = soup.find_all('a', href=True)

    file_links = []  #os links encontrados

    for link in links:
        link_text = link.text.strip()       #texto do link
        href = link['href'].strip()         #caminho do link

        #Loop pelas palavras-chave e extensões fornecidas no dicionário
        for keyword, extension in filters.items():
            #se a keyword está no texto do link e se o href termina com a extensão esperada
            if keyword.lower() in link_text.lower() and href.lower().endswith(extension.lower()):
                # Se o href for relativo (não começar com http), completa com domínio base
                full_url = href if href.startswith('http') else urljoin(url, href)
                file_links.append(full_url)
                break  # Evita duplicidade caso o link atenda mais de uma keyword

    return file_links
