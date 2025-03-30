import unittest
from unittest.mock import patch, MagicMock, mock_open
from pathlib import Path
from downloader import download_file, download_files

class TestDownloader(unittest.TestCase):

    @patch("builtins.open", new_callable=mock_open)
    @patch("requests.get")
    def test_download_file_success(self, mock_get, mock_file):
        # Simula uma resposta bem-sucedida
        mock_response = MagicMock()
        mock_response.iter_content = lambda chunk_size: [b"conteudo de teste"]
        mock_response.status_code = 200
        mock_response.raise_for_status = lambda: None
        mock_get.return_value = mock_response

        url = "https://www.site.com/teste.pdf"
        dest_folder = "downloads"

        result = download_file(url, dest_folder)
        expected_path = Path(dest_folder) / "teste.pdf"

        self.assertEqual(result, expected_path)
        mock_get.assert_called_once_with(url, stream=True)
        mock_file.assert_called_once_with(expected_path, "wb")

    @patch("requests.get")
    def test_download_file_failure(self, mock_get):
        # Simula erro na requisição
        mock_get.side_effect = Exception("Falha na conexão")

        url = "https://www.site.com/falha.pdf"
        result = download_file(url, "downloads")

        self.assertIsNone(result)

    @patch("downloader.download_file")
    def test_download_files_parallel(self, mock_download_file):
        # Simula o download de múltiplos arquivos
        mock_download_file.side_effect = lambda url, folder: Path(folder) / url.split("/")[-1]

        urls = [
            "https://exemplo.com/arquivo1.pdf",
            "https://exemplo.com/arquivo2.pdf",
            "https://exemplo.com/arquivo3.pdf"
        ]

        result = download_files(urls, dest_folder="downloads", max_workers=3)

        expected = [
            Path("downloads") / "arquivo1.pdf",
            Path("downloads") / "arquivo2.pdf",
            Path("downloads") / "arquivo3.pdf"
        ]

        self.assertEqual(sorted(result), sorted(expected))

if __name__ == "__main__":
    unittest.main()
