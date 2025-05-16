import json
from typing import List, Dict, Any


def load_transactions(file_path: str) -> List[Dict[str, Any]]:
    """Загружает транзакции из JSON-файла."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return data if isinstance(data, list) else []
    except (FileNotFoundError, json.JSONDecodeError):
        return []
