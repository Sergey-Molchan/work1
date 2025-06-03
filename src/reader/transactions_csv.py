import pandas as pd
from pathlib import Path
from pandas import read_csv
from src.reader.transaction_xlsx import read_transactions_excel


def read_transactions_csv(file_path: Path) -> pd.DataFrame:
    """Читает транзакции из CSV файла"""
    if not file_path.exists():
        raise FileNotFoundError(f"Файл не найден {file_path}")
    try:
        return pd.read_csv(file_path)
    except Exception as e:
        raise ValueError(f"Ошибка при чтении CSV файла {e}")

path_csv = Path("/Users/sergejmolcan/bank1/work1/Data/transactions.csv")
df_csv = read_transactions_csv(path_csv)
print(df_csv)
