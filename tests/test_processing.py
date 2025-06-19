import pytest
from src.processing import (
    filter_by_state,
    sort_by_date,
    search_by_description,
    count_by_categories
)


@pytest.fixture
def test_transactions() -> list[dict]:
    """Фикстура с тестовыми транзакциями."""
    return [
        {'id': 1, 'state': 'EXECUTED', 'date': '2023-01-01T00:00:00.000', 'description': 'Перевод'},
        {'id': 2, 'state': 'CANCELED', 'date': '2024-01-01T00:00:00.000', 'description': 'Пополнение'},
        {'id': 3, 'state': 'EXECUTED', 'date': '2023-06-15T00:00:00.000', 'description': 'Перевод'},
        {'id': 4},  # Транзакция без статуса, даты и описания
    ]


def test_filter_by_state(test_transactions):
    """Тест фильтрации по статусу."""
    result = filter_by_state(test_transactions)
    assert len(result) == 2
    assert all(t['state'] == 'EXECUTED' for t in result)


def test_sort_by_date(test_transactions):
    """Тест сортировки по дате."""
    result = sort_by_date(test_transactions)
    assert result[0]['id'] == 2  # Самая свежая транзакция
    assert result[-1]['id'] == 4  # Транзакция без даты должна быть в конце


def test_search_by_description(test_transactions):
    """Тест поиска по описанию."""
    result = search_by_description(test_transactions, "перевод")
    assert len(result) == 2
    assert all("Перевод" in t["description"] for t in result if 'description' in t)


def test_count_by_categories(test_transactions):
    """Тест подсчета по категориям."""
    counts = count_by_categories(test_transactions, ["Перевод", "Пополнение"])
    assert counts["Перевод"] == 2
    assert counts["Пополнение"] == 1
    assert "Открытие вклада" not in counts  # Проверка отсутствующей категории