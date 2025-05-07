import pytest
import os
from decorators import log


@log("test_log.txt")
def risky_function(a: int, b: int) -> float:
    return a / b


@log()
def safe_function(text: str) -> str:
    return text.upper()


def test_log_to_file() -> None:
    if os.path.exists("test_log.txt"):
        os.remove("test_log.txt")

    risky_function(10, 2)  # Успешный вызов
    with pytest.raises(ZeroDivisionError):
        risky_function(5, 0)  # Ошибочный вызов

    with open("test_log.txt", "r", encoding="utf-8") as f:
        logs = f.read()
        assert "Результат: 5.0" in logs
        assert "ZeroDivisionError" in logs


def test_log_to_console(capsys: pytest.CaptureFixture) -> None:
    safe_function("hello")
    captured = capsys.readouterr()
    assert "Результат: 'HELLO'" in captured.out


def test_error_logging(capsys: pytest.CaptureFixture) -> None:
    with pytest.raises(ZeroDivisionError):
        risky_function(1, 0)
    captured = capsys.readouterr()
    assert "ZeroDivisionError" in captured.out