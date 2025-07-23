import unittest
from pathlib import Path
from tempfile import TemporaryDirectory
import pandas as pd
from src.reader.transactions_xlsx import read_transactions_excel


class TestReadTransactionsExcel(unittest.TestCase):
    def setUp(self):
        self.temp_dir = TemporaryDirectory()
        self.test_dir = Path(self.temp_dir.name)

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_read_valid_excel(self):
        """Проверка чтения корректного Excel-файла"""
        file_path = self.test_dir / "valid.xlsx"
        test_data = [
            {"id": 1, "amount": 100.0},
            {"id": 2, "amount": 200.0}
        ]
        pd.DataFrame(test_data).to_excel(file_path, index=False)

        result = read_transactions_excel(file_path)
        self.assertEqual(result, test_data)

    def test_file_not_found(self):
        """Проверка обработки отсутствующего файла"""
        with self.assertRaises(FileNotFoundError):
            read_transactions_excel(Path("/non/existent/path.xlsx"))

    def test_invalid_excel_format(self):
        """Проверка обработки битого Excel-файла"""
        file_path = self.test_dir / "invalid.xlsx"
        with open(file_path, "w") as f:
            f.write("NOT AN EXCEL FILE")

        with self.assertRaises(ValueError):
            read_transactions_excel(file_path)

    def test_directory_instead_of_file(self):
        """Проверка обработки директории вместо файла"""
        with self.assertRaises(ValueError) as cm:
            read_transactions_excel(self.test_dir)
        self.assertIn("Ошибка при чтении Excel", str(cm.exception))


if __name__ == "__main__":
    unittest.main()
