import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))
from src.processing import filter_by_state


def test_filter_by_state():
    test_data = [
        {'id': 1, 'state': 'EXECUTED'},
        {'id': 2, 'state': 'CANCELED'},
        {'id': 3, 'state': 'EXECUTED'}
    ]

    # Тест фильтрации по умолчанию
    result = filter_by_state(test_data)
    assert len(result) == 2
    assert all(t['state'] == 'EXECUTED' for t in result)

    # Тест фильтрации по CANCELED
    result = filter_by_state(test_data, 'CANCELED')
    assert len(result) == 1
    assert result[0]['id'] == 2


if __name__ == "__main__":
    test_filter_by_state()
    print("Все тесты прошли успешно!")