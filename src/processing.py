def filter_by_state(transactions: list[dict], state: str = 'EXECUTED') -> list[dict]:
    """
    Фильтрует список словарей по значению ключа 'state'.

    :param transactions: Список словарей с транзакциями
    :param state: Значение состояния для фильтрации (по умолчанию 'EXECUTED')
    :return: Отфильтрованный список словарей
    """
    return [transaction for transaction in transactions if transaction.get('state') == state]