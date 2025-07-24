import pytest
from src.services import investment_bank


@pytest.fixture
def sample_transactions():
    return [
        {"Дата операции": "2023-01-15", "Сумма операции": 1712},
        {"Дата операции": "2023-01-20", "Сумма операции": 843}
    ]

def test_investment_bank(sample_transactions):
    result = investment_bank("2023-01", sample_transactions, 50)
    assert result == (1750-1712) + (850-843)  # 38 + 7 = 45