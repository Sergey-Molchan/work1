from src.processing import filter_by_state, sort_by_date, search_by_description, count_by_categories
from src.widget import mask_account_card, get_date
from src.reader.transactions_csv import read_transactions_csv
from src.reader.transactions_xlsx import read_transactions_excel
from pathlib import Path
from typing import List, Dict
import json
from src.views import main_page
from src.services import investment_bank
from src.reports import spending_by_category
import pandas as pd


def run_all():
    # Пример вызова функций
    print(main_page("2023-01-20 14:30:00"))

    df = pd.read_excel("data/operations.xlsx")
    print(investment_bank("2023-01", df.to_dict("records"), 50))
    print(spending_by_category(df, "Супермаркеты"))


def load_transactions(file_type: str) -> List[Dict]:
    """Загружает транзакции из файла в папке data/"""
    data_dir = Path("data")
    data_dir.mkdir(exist_ok=True)  # Создаем папку если её нет

    try:
        if file_type == "1":
            file_path = data_dir / "operations.json"
            with open(file_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        elif file_type == "2":
            file_path = data_dir / "transactions.csv"
            return read_transactions_csv(file_path)
        elif file_type == "3":
            file_path = data_dir / "transactions.xlsx"
            return read_transactions_excel(file_path)
        else:
            raise ValueError("Неверный тип файла")
    except Exception as e:
        raise ValueError(f"Ошибка загрузки файла: {e}")


def print_transaction(transaction: Dict, index: int) -> None:
    """Выводит информацию о транзакции"""
    date = get_date(transaction.get('date', '')) or "Дата неизвестна"
    description = transaction.get('description', 'Без описания')

    from_ = mask_account_card(transaction['from']) if 'from' in transaction else None
    to_ = mask_account_card(transaction['to']) if 'to' in transaction else None

    amount = transaction.get('operationAmount', {}).get('amount', '0')
    currency = transaction.get('operationAmount', {}).get('currency', {}).get('name', '')

    print(f"\nОперация #{index}")
    print(f"{date} {description}")
    if from_:
        print(f"{from_} -> {to_}")
    else:
        print(f"{to_}")
    print(f"Сумма: {amount} {currency}")


def main() -> None:
    """Основная функция приложения"""
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.\n")

    # Выбор файла
    print("Доступные файлы в папке data/:")
    print("1. operations.json")
    print("2. transactions.csv")
    print("3. transactions.xlsx")

    file_type = input("Выберите файл (1-3): ")

    try:
        transactions = load_transactions(file_type)
        print(f"\nЗагружено {len(transactions)} транзакций")
    except Exception as e:
        print(f"\nОшибка: {e}")
        return

    # Фильтрация по статусу
    state = input("\nВведите статус для фильтрации (EXECUTED/CANCELED/PENDING): ").upper()
    filtered = filter_by_state(transactions, state)
    print(f"\nНайдено {len(filtered)} транзакций со статусом {state}")

    if not filtered:
        return

    # Сортировка
    if input("\nОтсортировать по дате (да/нет)? ").lower() == 'да':
        reverse = input("По убыванию (да/нет)? ").lower() == 'да'
        filtered = sort_by_date(filtered, reverse=reverse)

    # Поиск по описанию
    if input("\nФильтровать по описанию (да/нет)? ").lower() == 'да':
        search = input("Введите текст для поиска: ")
        filtered = search_by_description(filtered, search)
        print(f"\nНайдено {len(filtered)} транзакций по запросу '{search}'")

    # Вывод результатов
    if not filtered:
        print("\nНет транзакций, соответствующих критериям")
        return

    print("\nРезультаты:")
    for idx, trans in enumerate(filtered, 1):
        print_transaction(trans, idx)

    # Статистика
    categories = list({t.get('description', '') for t in filtered if t.get('description')})
    if categories:
        stats = count_by_categories(filtered, categories)
        print("\nСтатистика по категориям:")
        for cat, count in stats.items():
            print(f"{cat}: {count}")


if __name__ == "__main__":
    main()