import pandas as pd
from unittest.mock import patch, mock_open
import pytest
from pathlib import Path
from src.reader.transactions_csv import read_transactions_csv



@patch("pandas.read_csv")
@patch("pathlib.Path.exists", return_value=True)
def test_read_transaction_csv(mock_exists, mock_read_csv):
    # Тестовые данные
    test_data = pd.DataFrame({"ID": [1, 2], "Amount": [100, 200]})
    mock_read_csv.return_value = test_data

    result = read_transactions_csv(Path("fake_path.csv"))

    mock_exists.assert_called_once()
    mock_read_csv.assert_called_once_with(Path("fake_path.csv"))
    assert result.equals(test_data)

@patch("pathlib.Path.exists", return_value=False)
def test_read_transactions_csv_file_not_found(mock_exists):
    with pytest.raises(FileNotFoundError):
        read_transactions_csv(Path("nonexistent.csv"))
