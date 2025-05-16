import os
import requests
from dotenv import load_dotenv
from typing import Dict

load_dotenv()


def convert_to_rub(transaction: Dict) -> float:
    try:
        amount = transaction['operationAmount']['amount']
        currency = transaction['operationAmount']['currency']['code']
    except KeyError:
        raise ValueError("Некорректная транзакция")

    if currency == 'RUB':
        return float(amount)

    api_key = os.getenv('EXCHANGE_API_KEY')
    url = f"https://api.apilayer.com/exchangerates_data/latest?base={currency}"
    headers = {'apikey': api_key}

    response = requests.get(url, headers=headers, timeout=10)
    # Проверяем статус ответа
    if response.status_code != 200:
        raise ValueError(f"Ошибка API: код {response.status_code}")

    rates = response.json().get('rates', {})
    if 'RUB' not in rates:
        raise ValueError("Курс RUB не найден")

    return float(amount) * rates['RUB']
