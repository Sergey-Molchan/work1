import sys
from pathlib import Path
from typing import List, Dict, Any

sys.path.append(str(Path(__file__).parent.parent))
from src.processing import filter_by_state, sort_by_date

def test_filter_by_state() -> None:
    """Тест фильтрации по статусу."""
    test_data: List[Dict[str, Any]] = [
        {'id': 1, 'state': 'EXECUTED'},
        {'id': 2, 'state': 'CANCELED'},
        {'id': 3, 'state': 'EXECUTED'},
        {'id': 4},  # Транзакция без статуса
    ]

    # Тест фильтрации по умолчанию (EXECUTED)
    result = filter_by_state(test_data)
    assert len(result) == 2
    assert all(t['state'] == 'EXECUTED' for t in result)

    # Тест фильтрации по CANCELED
    result = filter_by_state(test_data, 'CANCELED')
    assert len(result) == 1
    assert result[0]['id'] == 2

    # Тест с пустым списком
    assert filter_by_state([]) == []

def test_sort_by_date() -> None:
    """Тест сортировки по дате."""
    test_data: List[Dict[str, Any]] = [
        {'id': 1, 'date': '2023-01-01T00:00:00.000'},
        {'id': 2, 'date': '2024-01-01T00:00:00.000'},
        {'id': 3},  # Транзакция без даты
        {'id': 4, 'date': '2023-06-15T00:00:00.000'}
    ]

    # Сортировка по убыванию
    result = sort_by_date(test_data)
    assert result[0]['id'] == 2
    assert result[1]['id'] == 4
    assert result[2]['id'] == 1

    # Тест с пустым списком
    assert sort_by_date([]) == []

if __name__ == "__main__":
    test_filter_by_state()
    test_sort_by_date()
    print("Все тесты прошли успешно!")