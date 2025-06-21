from src.logger_config import setup_logger
from typing import Union

masks_logger = setup_logger("masks")


def mask_card(number: Union[str, int]) -> str:
    """Маскирует номер карты, оставляя первые 6 и последние 4 цифры"""
    try:
        num_str = str(number) if not isinstance(number, str) else number
        cleaned = "".join(c for c in num_str if c.isdigit())

        if len(cleaned) != 16:
            raise ValueError("Номер карты должен содержать 16 цифр")

        masked = f"{cleaned[:4]} {cleaned[4:6]}** **** {cleaned[-4:]}"
        masks_logger.info(f"Успешно замаскирована карта: {masked}")
        return masked

    except ValueError as e:
        masks_logger.error(f"Ошибка маскировки карты: {e} | Входные данные: {number}")
        raise


def mask_account(number: Union[str, int]) -> str:
    """Маскирует номер счета, оставляя последние 4 цифры"""
    try:
        num_str = str(number) if not isinstance(number, str) else number

        if len(num_str) < 4:
            raise ValueError("Номер счета должен содержать минимум 4 цифры")

        if not num_str.isdigit():
            raise ValueError("Номер счета должен содержать только цифры")

        masked = f"**{num_str[-4:]}"
        masks_logger.info(f"Успешно замаскирован счет: {masked}")
        return masked

    except ValueError as e:
        masks_logger.error(f"Ошибка маскировки счета: {e} | Входные данные: {number}")
        raise
