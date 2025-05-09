from typing import Callable, Optional, Any
import functools
import sys


def log(filename: Optional[str] = None) -> Callable:
    """Декоратор для логирования вызовов функций и ошибок в формате:
    - При успехе: '{func_name} ok'
    - При ошибке: '{func_name} error: {error}. Inputs: {args}, {kwargs}'
    """

    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            func_name = func.__name__
            args_repr = ", ".join(map(repr, args))
            kwargs_repr = ", ".join(f"{k}={repr(v)}" for k, v in kwargs.items())
            signature = f"({args_repr}{', ' if kwargs_repr else ''}{kwargs_repr})"

            try:
                result = func(*args, **kwargs)
                status_message = f"{func_name} ok\n"

                if filename:
                    with open(filename, "a", encoding="utf-8") as f:
                        f.write(status_message)
                else:
                    print(status_message, end="")

                return result
            except Exception as e:
                error_message = (
                    f"{func_name} error: {repr(e)}. Inputs: {signature}\n"  # Исправлено здесь
                )

                if filename:
                    with open(filename, "a", encoding="utf-8") as f:
                        f.write(error_message)
                else:
                    print(error_message, end="", file=sys.stderr)

                raise e

        return wrapper

    return decorator
