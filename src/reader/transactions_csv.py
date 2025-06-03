import pandas as pd
from pathlib import Path
from pandas import read_csv



def read_transaction_csv(file_path: Path) -> pd.DataFrame:
    """Читает транзакции из CSV файла"""
    try:
        if not file_path.exists():
            raise FileNotFoundError(f"Файл не найден {file_path}")
        return pd.read_csv(file_path)
    except Exception as e:
        raise ValueError(f"Ошибка при чтении CSV файла {e}")

path_csv = Path("/Users/sergejmolcan/bank1/work1/Data/transactions.csv")
df_csv = read_transaction_csv(path_csv)
print(df_csv)
