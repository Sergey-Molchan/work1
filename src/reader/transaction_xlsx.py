import pandas as pd
from pathlib import Path



def read_transactions_excel(file_path: Path) -> pd.DataFrame:
    """"Читает транзакции из Excel файла """
    try:
        if not file_path.exists():
            raise FileNotFoundError(f"Файл не найден {file_path}")
        return pd.read_excel(file_path)
    except Exception as e:
        raise ValueError(f"Ошибка при чтении Excel {e}")


path_excel = Path("/Users/sergejmolcan/bank1/work1/Data/transactions_excel.xlsx")
df_excel = read_transactions_excel(path_excel)
print(df_excel)