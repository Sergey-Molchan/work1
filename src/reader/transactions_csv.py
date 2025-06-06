import csv
from pathlib import Path


def read_transactions_csv(file_path: Path) -> list[dict]:
    """Читает транзакции из CSV файла и возвращает список словарей."""
    if not file_path.exists():
        raise FileNotFoundError(f"Файл не найден {file_path}")

    try:
        with open(file_path, mode="r", encoding="utf-8") as file:
            # Читаем все строки для проверки структуры
            lines = file.readlines()
            reader = csv.DictReader(lines)

            # Проверяем, что все строки имеют одинаковое количество полей
            dialect = csv.Sniffer().sniff(lines[0])
            for line in lines[1:]:
                if len(line.split(dialect.delimiter)) != len(reader.fieldnames):
                    raise ValueError("Несогласованное количество полей в CSV файле")

            # Если проверка прошла, читаем файл заново
            file.seek(0)
            return list(csv.DictReader(file))

    except csv.Error as e:
        raise ValueError(f"Ошибка формата CSV: {e}")
    except Exception as e:
        raise ValueError(f"Ошибка при чтении CSV файла: {e}")
