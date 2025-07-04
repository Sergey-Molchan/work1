🏦 Банковский процессор транзакций (версия 2.0)
Библиотека для обработки банковских операций с поддержкой:

📁 Чтение данных из JSON/CSV/Excel
🛡️ Маскировка карт и счетов
📊 Фильтрация и сортировка транзакций
💱 Конвертация валют через API
📝 Детальное логирование операций
✅ Покрытие тестами >80%
🚀 Быстрый старт

Установка

bash
pip install -r requirements.txt
Настройка окружения

Создайте файл .env в корне проекта:
ini
EXCHANGE_API_KEY=ваш_ключ_от_apilayer.com
LOG_LEVEL=INFO  # DEBUG/INFO/WARNING/ERROR
Поместите файлы операций в папку data/:
operations.json
transactions.csv
financial_operations.xlsx
💡 Основные возможности

🔄 Загрузка транзакций

Поддержка трех форматов:

python
from utils.file_reader import load_json, load_csv, load_excel

# Автоматическое определение формата
transactions = load_json("data/operations.json")  
transactions = load_csv("data/transactions.csv")
transactions = load_excel("data/financial_operations.xlsx")
🛡️ Маскировка данных

Автоматическое определение типа данных (карта/счет):

python
from src.masking import mask_data

print(mask_data("1234567890123456"))  # 1234 56** **** 3456
print(mask_data("123456789012345"))   # Ошибка в логах
📝 Логирование операций

Все операции маскировки логируются в logs/masks.log:

2025-05-28 14:44:30 - INFO - Успешно замаскирована карта: 1234 56** **** 3456
2025-05-28 14:44:30 - ERROR - Ошибка маскировки: Номер карты должен содержать 16 цифр
🛠️ Расширенные функции

💱 Конвертация валют

python
from external_api.api import convert_to_rub

transaction = {
    "amount": "100",
    "currency": "USD"
}
print(convert_to_rub(transaction))  # → 7500.0 RUB (курс 75)
🔍 Фильтрация и сортировка

python
from src.processing import filter_by_state, sort_by_date

executed_ops = filter_by_state(transactions, "EXECUTED")
sorted_ops = sort_by_date(executed_ops, ascending=False)
📅 Форматирование даты

python
from src.widget import format_date

print(format_date("2024-03-11T02:26:18.671407"))  # → 11.03.2024
🧪 Тестирование

Запуск тестов

bash
pytest tests/ -v  # Все тесты
pytest tests/test_file_readers.py  # Только модуль чтения файлов
Проверка покрытия

bash
pytest --cov=src --cov=utils --cov-report=html
Откройте htmlcov/index.html для просмотра отчета

📂 Структура проекта

bank-processor/
├── data/                   # Файлы с транзакциями (JSON/CSV/XLSX)
├── external_api/           # Интеграция с валютным API
├── logs/                   # Логи операций (masks.log)
├── utils/                  # Утилиты загрузки данных
│   ├── file_reader.py      # Загрузка JSON/CSV/XLSX
│   └── ...                 
├── src/                    # Основная логика
│   ├── masking.py          # Маскировка данных
│   ├── processing.py       # Фильтрация и сортировка
│   └── ...
├── tests/                  # Юнит-тесты
│   ├── test_file_readers.py# Тесты CSV/Excel
│   ├── test_masking.py     # Тесты маскировки
│   └── ...
├── .gitignore              # Игнорируемые файлы
├── .env.example            # Шаблон конфигурации
└── requirements.txt        # Зависимости
⚠️ Частые проблемы

Ошибка конвертации валют:

Проверьте наличие API-ключа в .env
Убедитесь в корректном формате транзакции:
python
{
    "operationAmount": {
        "amount": "100",
        "currency": {"code": "USD"}  # Обязательное поле!
    }
}
Ошибки чтения файлов:

Для CSV: проверьте разделитель (должен быть запятая)
Для Excel: убедитесь в наличии листа с данными
Общий формат данных:
python
[
    {"date": "2024-01-01", "description": "...", ...},
    ...
]
🔧 Разработка

Работа с Git

bash
git checkout -b homework-3  # Создание ветки
git add .
git commit -m "feat: add CSV/Excel support"
git push origin homework-3
Создайте Pull Request из homework-3 в develop
Убедитесь, что все тесты проходят
Проверьте покрытие кода (>80%)
Требования к коду

Все новые функции должны иметь тесты
Используйте логирование вместо print()
Сохраняйте форматирование данных
Документируйте публичные методы
✅ Решенные задачи в текущей версии

Работа с файлами

✔️ Чтение данных из CSV
✔️ Чтение данных из Excel
✔️ Единый интерфейс для разных форматов
✔️ Автоматическое определение формата файла
Тестирование

✔️ Mock-тесты для чтения файлов
✔️ Покрытие кода >80%
✔️ Отдельные тесты для новых модулей
✔️ Интеграция с pytest
Логирование

✔️ Централизованная система логов
✔️ Запись ошибок маскировки
✔️ Разделение по уровням (DEBUG, INFO, ERROR)
✔️ Ротация логов (ежедневная)
Инфраструктура

✔️ Обновленный .gitignore
✔️ Поддержка .env файлов
✔️ Автоматическая установка зависимостей
✔️ Документирование всех новых функций