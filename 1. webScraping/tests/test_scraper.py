import unittest
from unittest.mock import patch
from bs4 import BeautifulSoup

from scraper import get_file_links_by_keyword_and_extension

class TestGetFileLinks(unittest.TestCase):
    @patch("requests.get")
    def test_get_file_links_by_keyword_and_extension(self, mock_get):
        # HTML simulado como se fosse da página real
        html_content = """
        <html>
            <body>
                <a href="/arquivos/anexo1.pdf">Anexo I</a>
                <a href="/arquivos/anexo2.pdf">Anexo II</a>
                <a href="/outro/relatorio.docx">Relatório Final</a>
                <a href="/nao_incluir.zip">Outro Arquivo</a>
            </body>
        </html>
        """
        # Configura o mock para retornar um objeto com .text igual ao HTML acima
        mock_get.return_value.status_code = 200
        mock_get.return_value.text = html_content

        # Define os filtros
        filters = {
            "Anexo I": ".pdf",
            "Anexo II": ".pdf",
            "Relatório Final": ".docx"
        }

        # Executa a função
        result = get_file_links_by_keyword_and_extension(
            url="https://falso.gov.br/pagina",
            filters=filters
        )

        # Define a saída esperada
        expected_links = [
            "https://falso.gov.br/arquivos/anexo1.pdf",
            "https://falso.gov.br/arquivos/anexo2.pdf",
            "https://falso.gov.br/outro/relatorio.docx"
        ]

        self.assertEqual(sorted(result), sorted(expected_links))

if __name__ == "__main__":
    unittest.main()
