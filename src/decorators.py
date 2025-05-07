from datetime import datetime
import functools
from typing import Callable, Optional, Any


def log(filename: Optional[str] = None) -> Callable:
    """Декоратор для логирования вызовов функций и ошибок."""

    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            # Формирование информации о вызове
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            func_name = func.__name__
            args_repr = [repr(arg) for arg in args]
            kwargs_repr = [f"{k}={repr(v)}" for k, v in kwargs.items()]
            signature = ", ".join(args_repr + kwargs_repr)
            log_message = f"{timestamp} - Вызов: {func_name}({signature})\n"

            try:
                result = func(*args, **kwargs)
                log_message += f"{timestamp} - Результат: {repr(result)}\n"
            except Exception as e:
                error_message = f"{timestamp} - Ошибка: {repr(e)}\n"
                log_message += error_message
                # Запись лога перед пробросом исключения
                if filename:
                    with open(filename, "a", encoding="utf-8") as f:
                        f.write(log_message)
                else:
                    print(log_message, end="")
                raise e  # Пробрасываем исключение дальше

            # Запись лога при успешном выполнении
            if filename:
                with open(filename, "a", encoding="utf-8") as f:
                    f.write(log_message)
            else:
                print(log_message, end="")

            return result

        return wrapper

    return decorator