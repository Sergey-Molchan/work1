def get_mask_card_number(card_number: str) -> str:
    """Маскирует номер карты в формате 0000 00** **** 0000"""
    return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"

def get_mask_account(account: str) -> str:
    """Маскирует номер счета в формате **0000"""
    return "**" + account[-4:]

def mask_account_card(payment_info: str) -> str:
    """Маскирует карту/счет в строке"""
    parts = payment_info.split()
    if parts[0] == "Счет":
        return f"Счет {get_mask_account(parts[-1])}"
    return f"{' '.join(parts[:-1])} {get_mask_card_number(parts[-1])}"

def get_date(iso_date: str) -> str:
    """Форматирует дату из ISO в ДД.ММ.ГГГГ"""
    return f"{iso_date[8:10]}.{iso_date[5:7]}.{iso_date[:4]}"