import pandas as pd
from pathlib import Path


def read_transactions_excel(file_path: Path) -> list[dict]:
    """Читает транзакции из Excel файла и возвращает список словарей."""
    if not file_path.exists():
        raise FileNotFoundError(f"Файл не найден {file_path}")

    try:
        df = pd.read_excel(file_path)
        return df.to_dict("records")
    except Exception as e:
        raise ValueError(f"Ошибка при чтении Excel: {e}")
