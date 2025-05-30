# 🏦 Банковский процессор транзакций (обновленная версия)

Библиотека для обработки банковских операций с поддержкой:
- Маскировки карт/счетов 🛡️
- Фильтрации и сортировки транзакций 📊
- Конвертации валют через API 💱
- Логирования операций 📝

---

## 🚀 Быстрый старт

### Установка
```bash
pip install -r requirements.txt  # Установите зависимости
Настройка окружения
Создайте файл .env в корне проекта:

ini
EXCHANGE_API_KEY=ваш_ключ_здесь  # Ключ от apilayer.com
Поместите файл operations.json в папку data/.

💡 Основные возможности
🔄 Загрузка транзакций
python
from utils.utils import load_transactions

transactions = load_transactions("data/operations.json")  # Автоматическая проверка формата
💱 Конвертация валют
python
from external_api.api import convert_to_rub

transaction = {
    "operationAmount": {
        "amount": "100",
        "currency": {"code": "USD"}
    }
}
print(convert_to_rub(transaction))  # 7500.0 (при курсе 75 RUB/USD)
🛠️ Расширенные функции
🗂️ Фильтрация и сортировка
python
from src.processing import filter_by_state, sort_by_date

# Только выполненные операции
executed_ops = filter_by_state(transactions, "EXECUTED")  

# Сортировка по дате (новые сверху)
sorted_ops = sort_by_date(executed_ops)
📅 Форматирование даты
python
from src.widget import get_date

print(get_date("2024-03-11T02:26:18.671407"))  # 11.03.2024
🧪 Тестирование
Запуск тестов
bash
pytest tests/ -v  # Все тесты
pytest tests/test_external_api.py  # Только модуль API
Покрытие кода
bash
pytest tests/ --cov=src --cov-report=html
🗂️ Структура проекта
bank1/
├── data/                   # Файлы с транзакциями
├── external_api/           # Интеграция с валютным API
├── utils/                  # Утилиты загрузки данных
├── src/                    # Основная логика
├── tests/                  # Юнит-тесты
├── .env.example            # Шаблон конфигурации
└── requirements.txt        # Зависимости
⚠️ Частые проблемы
Ошибка конвертации валют
python
# Проверьте:
# 1. Наличие API-ключа в .env
# 2. Корректный формат транзакции:
{
    "operationAmount": {
        "amount": "100",
        "currency": {"code": "USD"}  # Обязательные поля!
    }
}
Логирование операций
python
@log_to_file  # Запись в файл
def risky_operation():
    ...

@log_to_console  # Вывод в терминал
def safe_operation():
    ...