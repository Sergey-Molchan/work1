import unittest
from pathlib import Path
from tempfile import TemporaryDirectory
import csv
from src.reader.transactions_csv import read_transactions_csv


class TestReadTransactionsCSV(unittest.TestCase):
    def setUp(self):
        self.temp_dir = TemporaryDirectory()
        self.test_dir = Path(self.temp_dir.name)

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_read_valid_csv(self):
        """Проверка чтения корректного CSV-файла"""
        file_path = self.test_dir / "valid.csv"
        test_data = [
            {"id": "1", "amount": "100.0"},
            {"id": "2", "amount": "200.0"}
        ]

        with open(file_path, "w") as f:
            writer = csv.DictWriter(f, fieldnames=["id", "amount"])
            writer.writeheader()
            writer.writerows(test_data)

        result = read_transactions_csv(file_path)
        self.assertEqual(result, test_data)

    def test_file_not_found(self):
        """Проверка обработки отсутствующего файла"""
        with self.assertRaises(FileNotFoundError):
            read_transactions_csv(Path("/non/existent/path.csv"))

    def test_invalid_csv_format(self):
        """Проверка обработки битого CSV-файла"""
        file_path = self.test_dir / "invalid.csv"
        with open(file_path, "w") as f:
            f.write("id,amount\n")
            f.write("1,100.0\n")
            f.write("broken,data,extra,columns\n")  # Нарушенная структура

        with self.assertRaises(ValueError) as cm:
            read_transactions_csv(file_path)
        self.assertIn("Ошибка при чтении CSV файла", str(cm.exception))

    def test_directory_instead_of_file(self):
        """Проверка обработки директории вместо файла"""
        with self.assertRaises(ValueError) as cm:
            read_transactions_csv(self.test_dir)
        self.assertIn("Ошибка при чтении CSV файла", str(cm.exception))


if __name__ == "__main__":
    unittest.main()
