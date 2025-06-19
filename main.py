import json
import re
import csv
from datetime import datetime
from pathlib import Path
from typing import List, Dict
from collections import Counter
from src.masks import mask_card, mask_account

def search_by_description(transactions: List[Dict], search_string: str) -> List[Dict]:
    """Поиск по описанию с помощью регулярных выражений"""
    try:
        pattern = re.compile(search_string, re.IGNORECASE)
        return [t for t in transactions if 'description' in t and pattern.search(t['description'])]
    except re.error:
        return []


def count_by_categories(transactions: List[Dict], categories: List[str]) -> Dict[str, int]:
    """Подсчет операций по категориям"""
    descriptions = [t.get('description', '').lower() for t in transactions]
    category_counts = Counter(descriptions)
    return {category: category_counts.get(category.lower(), 0) for category in categories}


def filter_by_state(transactions: List[Dict], state: str = 'EXECUTED') -> List[Dict]:
    """Фильтрация по статусу"""
    return [t for t in transactions if t.get('state', '').upper() == state.upper()]


def sort_by_date(transactions: List[Dict], reverse: bool = True) -> List[Dict]:
    """Сортировка по дате"""

    def get_date_key(x: Dict) -> datetime:
        date_str = x.get('date', '')
        try:
            return datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%S.%f") if date_str else datetime.min
        except ValueError:
            return datetime.min

    return sorted(transactions, key=get_date_key, reverse=reverse)


def filter_rub_only(transactions: List[Dict]) -> List[Dict]:
    """Фильтрация рублевых транзакций"""
    return [t for t in transactions
            if t.get('operationAmount', {}).get('currency', {}).get('code') == 'RUB']


def load_json(file_path: Path) -> List[Dict]:
    """Загрузка JSON"""
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)


def load_csv(file_path: Path) -> List[Dict]:
    """Загрузка CSV"""
    with open(file_path, 'r', encoding='utf-8') as f:
        return list(csv.DictReader(f))


def load_excel(file_path: Path) -> List[Dict]:
    """Загрузка Excel (заглушка)"""
    # В реальности: import pandas as pd; pd.read_excel(file_path)
    return []


def mask_account_number(data: str) -> str:
    """
    Маскирует номер карты или счета, автоматически определяя тип
    Использует функции из masks.py
    """
    if not data:
        return "**XXXX"

    parts = data.split()
    if len(parts) < 2:
        return "**XXXX"

    number = parts[-1]

    try:
        if "счет" in data.lower():
            return f"Счет {mask_account(number)}"
        else:
            # Убираем все нецифровые символы для проверки
            cleaned = "".join(c for c in number if c.isdigit())
            if len(cleaned) == 16:
                return f"{' '.join(parts[:-1])} {mask_card(number)}"
            return f"{' '.join(parts[:-1])} {number}"  # Если не карта и не счет
    except ValueError:
        return "**XXXX"

def print_transaction(transaction: Dict, index: int):
    """Вывод транзакции"""
    date = (datetime.strptime(transaction['date'], "%Y-%m-%dT%H:%M:%S.%f").strftime("%d.%m.%Y")
            if 'date' in transaction else "Дата неизвестна")
    description = transaction.get('description', 'Без описания')
    from_ = mask_account_number(transaction.get('from', ''))
    to_ = mask_account_number(transaction.get('to', ''))
    amount = transaction.get('operationAmount', {}).get('amount', '0')
    currency = transaction.get('operationAmount', {}).get('currency', {}).get('name', '')

    print(f"\nОперация #{index}")
    print(f"{date} {description}")
    if from_ != "**XXXX":
        print(f"{from_} -> {to_}")
    else:
        print(f"{to_}")
    print(f"Сумма: {amount} {currency}")


def main():
    """Главное меню программы"""
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.\n")
    print("Выберите тип файла:")
    print("1. JSON")
    print("2. CSV")
    print("3. Excel")

    # Выбор файла
    file_type = input("Ваш выбор (1-3): ")
    file_path = Path("/Users/sergejmolcan/bank1/work1/Data/")

    if file_type == "1":
        file_path /= "operations.json"
        transactions = load_json(file_path)
        print("\nДля обработки выбран JSON-файл.")
    elif file_type == "2":
        file_path /= "transactions.csv"
        transactions = load_csv(file_path)
        print("\nДля обработки выбран CSV-файл.")
    elif file_type == "3":
        file_path /= "transactions_excel.xlsx"
        transactions = load_excel(file_path)
        print("\nДля обработки выбран Excel-файл.")
    else:
        print("Неверный выбор. Завершение программы.")
        return

    # Фильтрация по статусу
    while True:
        print("\nДоступные статусы: EXECUTED, CANCELED, PENDING")
        state = input("Введите статус для фильтрации: ").upper()
        if state in ["EXECUTED", "CANCELED", "PENDING"]:
            transactions = filter_by_state(transactions, state)
            print(f"\nОперации отфильтрованы по статусу '{state}'")
            break
        else:
            print(f"Статус операции '{state}' недоступен.")

    if not transactions:
        print("\nНе найдено ни одной транзакции, подходящей под ваши условия фильтрации")
        return

    # Дополнительные фильтры
    if input("\nОтсортировать операции по дате? (да/нет): ").lower() == 'да':
        order = input("Отсортировать по возрастанию или по убыванию? (возрастанию/убыванию): ")
        transactions = sort_by_date(transactions, reverse=order == 'убыванию')

    if input("\nВыводить только рублевые транзакции? (да/нет): ").lower() == 'да':
        transactions = filter_rub_only(transactions)

    if input("\nОтфильтровать список транзакций по определенному слову в описании? (да/нет): ").lower() == 'да':
        search_word = input("Введите слово для поиска: ")
        transactions = search_by_description(transactions, search_word)

    # Вывод результатов
    if not transactions:
        print("\nНе найдено ни одной транзакции, подходящей под ваши условия фильтрации")
        return

    print("\nРаспечатываю итоговый список транзакций...")
    print(f"\nВсего банковских операций в выборке: {len(transactions)}")

    categories = list({t.get('description', '') for t in transactions})
    stats = count_by_categories(transactions, categories)
    print("\nСтатистика по категориям:")
    for cat, count in stats.items():
        print(f"{cat}: {count}")

    for idx, transaction in enumerate(transactions, 1):
        print_transaction(transaction, idx)


if __name__ == "__main__":
    main()