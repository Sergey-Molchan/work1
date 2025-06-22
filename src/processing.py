from datetime import datetime
from typing import List, Dict
import re
from collections import Counter


def filter_by_state(transactions: List[Dict], state: str = 'EXECUTED') -> List[Dict]:
    """Фильтрует транзакции по статусу."""
    return [t for t in transactions if t.get('state') == state]


def sort_by_date(transactions: List[Dict[str, str | int]], reverse: bool = True) -> List[Dict]:
    """Сортирует транзакции по дате."""

    def get_date_key(x: Dict[str, str | int]) -> datetime:
        date_str = x.get('date', '')
        try:
            return datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%S.%f") if date_str else datetime.min
        except ValueError:
            return datetime.min

    return sorted(transactions, key=get_date_key, reverse=reverse)


def search_by_description(transactions: List[Dict], search_string: str) -> List[Dict]:
    """
    Ищет транзакции по описанию с использованием регулярных выражений.
    Регистр не учитывается.
    """
    try:
        pattern = re.compile(search_string, re.IGNORECASE)
        return [t for t in transactions if 'description' in t and pattern.search(t['description'])]
    except re.error:
        return []


def count_by_categories(transactions: List[Dict], categories: List[str]) -> Dict[str, int]:
    """
    Подсчитывает количество операций по заданным категориям.

    Args:
        transactions: Список транзакций
        categories: Список категорий для подсчета

    Returns:
        Словарь с количеством операций по каждой категории
    """
    descriptions = [t.get('description', '').lower() for t in transactions]
    category_counts = Counter(descriptions)

    return {category: category_counts.get(category.lower(), 0) for category in categories}