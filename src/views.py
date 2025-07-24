from typing import Dict, Any
import pandas as pd
from datetime import datetime
import logging
import requests


logger = logging.getLogger(__name__)


def get_greeting(current_time: datetime) -> str:
    """Определяет приветствие по времени суток"""
    hour = current_time.hour
    if 5 <= hour < 12:
        return "Доброе утро"
    elif 12 <= hour < 17:
        return "Добрый день"
    elif 17 <= hour < 23:
        return "Добрый вечер"
    return "Доброй ночи"


def fetch_currency_rates(currencies: list) -> list:
    """Получает курсы валют через API (пример для USD и EUR)"""
    try:
        rates = []
        for currency in currencies:
            response = requests.get(f"https://api.exchangerate-api.com/v4/latest/{currency}")
            rates.append({"currency": currency, "rate": response.json()["rates"]["RUB"]})
        return rates
    except Exception as e:
        logger.error(f"Currency API error: {e}")
        return []


def main_page(date_str: str) -> Dict[str, Any]:
    """
    Генерирует JSON для главной страницы
    :param date_str: Дата в формате 'YYYY-MM-DD HH:MM:SS'
    :return: Словарь с данными для JSON-ответа
    """
    try:
        date = datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S')
        df = pd.read_excel("data/operations.xlsx")  # Чтение транзакций

        # Топ-5 транзакций
        top_transactions = (
            df.nlargest(5, "Сумма платежа")
            .to_dict("records")
        )

        return {
            "greeting": get_greeting(date),
            "cards": [{
                "last_four": str(txn["Номер карты"])[-4:],
                "total_spent": txn["Сумма платежа"],
                "cashback": txn["Кешбэк"]
            } for txn in df.to_dict("records")],
            "top_transactions": top_transactions,
            "currency_rates": fetch_currency_rates(["USD", "EUR"]),
            "stock_prices": []  # Заглушка для акций
        }
    except Exception as e:
        logger.error(f"Main page error: {e}")
        return {"error": str(e)}