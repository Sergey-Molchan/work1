import pytest
from src.processing import filter_by_state

@pytest.fixture
def sample_transactions():
    return [
        {'id': 1, 'state': 'EXECUTED'},
        {'id': 2, 'state': 'CANCELED'},
        {'id': 3, 'state': 'EXECUTED'},
        {'id': 4, 'state': 'PENDING'}
    ]

def test_default_filter(sample_transactions):
    result = filter_by_state(sample_transactions)
    assert len(result) == 2
    assert all(t['state'] == 'EXECUTED' for t in result)

def test_custom_filter(sample_transactions):
    result = filter_by_state(sample_transactions, 'CANCELED')
    assert len(result) == 1
    assert result[0]['id'] == 2

def test_empty_result():
    assert filter_by_state([], 'EXECUTED') == []