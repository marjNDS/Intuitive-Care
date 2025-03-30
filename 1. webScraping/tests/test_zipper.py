import unittest
from pathlib import Path
import zipfile
import os
import tempfile

from zipper import zip_files

class TestZipper(unittest.TestCase):
    def setUp(self):
        # Cria um diretório temporário para os arquivos de teste
        self.temp_dir = tempfile.TemporaryDirectory()
        self.temp_path = Path(self.temp_dir.name)

        # Cria dois arquivos temporários de teste
        self.file1 = self.temp_path / "arquivo1.txt"
        self.file2 = self.temp_path / "arquivo2.txt"
        self.file1.write_text("conteúdo do arquivo 1")
        self.file2.write_text("conteúdo do arquivo 2")

        # Caminho onde o zip será criado
        self.output_zip = self.temp_path / "teste.zip"

    def tearDown(self):
        # Remove o diretório temporário e tudo dentro dele
        self.temp_dir.cleanup()

    def test_zip_files_creates_zip(self):
        # Executa a função
        result_zip_path = zip_files([self.file1, self.file2], output_zip_path=str(self.output_zip))

        # Verifica se o arquivo .zip foi criado
        self.assertTrue(result_zip_path.exists())

        # Abre o .zip e verifica se os arquivos estão lá dentro
        with zipfile.ZipFile(result_zip_path, "r") as zipf:
            zip_content = zipf.namelist()
            self.assertIn("arquivo1.txt", zip_content)
            self.assertIn("arquivo2.txt", zip_content)

    def test_zip_files_ignores_missing_file(self):
        # Adiciona um arquivo inexistente à lista
        fake_file = self.temp_path / "inexistente.txt"
        result_zip_path = zip_files([self.file1, fake_file], output_zip_path=str(self.output_zip))

        # Abre o .zip e verifica que só o arquivo existente foi incluído
        with zipfile.ZipFile(result_zip_path, "r") as zipf:
            zip_content = zipf.namelist()
            self.assertIn("arquivo1.txt", zip_content)
            self.assertNotIn("inexistente.txt", zip_content)

if __name__ == "__main__":
    unittest.main()
