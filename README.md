# 🏦 Банковский процессор транзакций

Простая библиотека для обработки банковских операций: маскирует карты/счета, фильтрует и сортирует транзакции.

---

## 📦 Установка

```bash
pip install bank-transactions-processor

🚀 Быстрый старт
Импорт функций

from bank_processor import (
    mask_card,
    mask_account,
    filter_by_state,
    sort_by_date,
    filter_by_currency
)
💡 Основные возможности
🔒 Маскировка данных

# Карта: 1234567890123456 → 1234 56** **** 3456
mask_card("1234567890123456")

# Счет: 73654108430135874305 → **4305 
mask_account("73654108430135874305")

📊 Фильтрация транзакций

transactions = [
    {'id': 1, 'state': 'EXECUTED', 'date': '2023-01-01'},
    {'id': 2, 'state': 'CANCELED', 'date': '2024-01-01'}
]

# Только выполненные операции
filter_by_state(transactions, 'EXECUTED')

# Транзакции в USD
filter_by_currency(transactions, 'USD')

📅 Сортировка

# По дате (новые сверху)
sort_by_date(transactions)

⚙️ Тестирование
Запуск всех тестов с отчетом о покрытии:

bash
pytest tests/ --cov=src --cov-report=html

📚 Документация
Маскировка данных
Функция	Формат ввода	Пример вывода
mask_card(number)	16-19 цифр	7000 79** **** 6361
mask_account(number)	Любая длина (≥4 цифр)	**4305
Обработка транзакций
Параметр	Значения	По умолчанию
state	EXECUTED/CANCELED	EXECUTED
reverse	True/False	True (новые)

❗ Частые ошибки
python
# Неверный формат карты
try:
    mask_card("1234")  # Вызовет ValueError
except ValueError as e:
    print(f"Ошибка: {e}")

🤖 Генераторы

# Генерация номеров карт
for num in card_number_generator(1, 5):
    print(num)  # 0000 0000 0000 0001, 0000 0000 0000 0002...

📄 Логирование
Декоратор @log записывает историю вызовов:


@log("operations.log")
def transfer(amount):
    # Логи будут сохранены в файл
    return process_payment(amount)