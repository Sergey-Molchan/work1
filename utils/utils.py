import json
from typing import List, Dict, Any
from src.logger_config import setup_logger


utils_logger = setup_logger("utils")


def load_transactions(file_path: str) -> List[Dict[str, Any]]:
    """
    Загружает транзакции из JSON файла
    Args:
        file_path (str): Путь к JSON файлу с транзакциями
    Returns:
        List[Dict[str, Any]]: Список транзакций
    Raises:
        FileNotFoundError: Если файл не существует
        json.JSONDecodeError: Если файл содержит некорректный JSON
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)

            if not isinstance(data, list):
                utils_logger.warning(f"Файл {file_path} не содержит список транзакций")
                return []

            utils_logger.info(f"Успешно загружено {len(data)} транзакций из {file_path}")
            return data

    except FileNotFoundError :
        utils_logger.error(f"Файл не найден: {file_path}")
        raise
    except json.JSONDecodeError as e:
        utils_logger.error(f"Ошибка декодирования JSON в файле {file_path}: {str(e)}")
        raise
    except Exception as e:
        utils_logger.error(f"Неожиданная ошибка при загрузке {file_path}: {str(e)}")
        raise
