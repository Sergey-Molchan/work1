def mask_card(number: str) -> str:
    if len(number) != 16 or not number.isdigit():
        raise ValueError("Некорректный номер карты")
    # Форматирование с пробелами
    return f"{number[:4]} {number[4:6]}** **** {number[-4:]}"


def mask_account(number: str) -> str:
    """Маскирует номер счета, оставляя последние 4 цифры."""
    if len(number) < 4 or not number.isdigit():
        raise ValueError("Некорректный номер счета")
    return f"**{number[-4:]}"
