from typing import List, Dict  # Добавляем этот импорт
import pytest
from src.generators import filter_by_currency, transaction_descriptions, card_number_generator


# Остальной код остаётся без изменений


@pytest.fixture
def test_transactions() -> List[Dict]:
    return [
        {"id": 1, "operationAmount": {"currency": {"code": "USD"}}, "description": "Payment"},
        {"id": 2, "operationAmount": {"currency": {"code": "EUR"}}, "description": "Transfer"},
        {"id": 3, "operationAmount": {"currency": {"code": "USD"}}, "description": "Withdrawal"},
    ]


@pytest.mark.parametrize("currency, expected_ids", [("USD", [1, 3]), ("EUR", [2])])
def test_filter_by_currency(test_transactions, currency, expected_ids):
    result = list(filter_by_currency(test_transactions, currency))
    assert [t["id"] for t in result] == expected_ids


def test_transaction_descriptions(test_transactions):
    descriptions = list(transaction_descriptions(test_transactions))
    assert descriptions == ["Payment", "Transfer", "Withdrawal"]


@pytest.mark.parametrize("start, stop, expected", [
    (1, 3, ["0000000000000001", "0000000000000002", "0000000000000003"]),
    (10, 12, ["0000000000000010", "0000000000000011", "0000000000000012"]),
])
def test_card_number_generator(start, stop, expected):
    assert list(card_number_generator(start, stop)) == expected
