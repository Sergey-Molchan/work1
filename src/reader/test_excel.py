from src.reader.transaction_xlsx import read_transactions_excel
import pandas as pd
from unittest.mock import patch, mock_open
import pytest
from pathlib import Path


@patch("pandas.read_excel")
@patch("pathlib.Path.exists", return_value=True)
def test_read_transactions_excel(mock_exists, mock_read_excel):
    test_data = pd.DataFrame({"ID": [1, 2], "Amount": [300, 400]})
    mock_read_excel.return_value = test_data

    result = read_transactions_excel(Path("fake_path.xlsx"))

    mock_exists.assert_called_once()
    mock_read_excel.assert_called_once_with(Path("fake_path.xlsx"))
    assert result.equals(test_data)