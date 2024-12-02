from functools import wraps
from typing import Any, Callable, Dict


def log(filename: str | None = None) -> Callable:
    """
    Декоратор, который логирует вызов функции и ее результат в файл или в консоль.
    filename: Путь к файлу для записи логов. Если не задан, то логи выводятся в консоль.
    Returns: Декорированная функция.
    """

    def wrapper(func: Callable) -> Callable:
        @wraps(func)
        def inner(*args: Any, **kwargs: Dict[str, Any]) -> Any:
            log_message = ""
            try:
                result = func(*args, **kwargs)
                log_message = f"{func.__name__} ok"
                return result
            except Exception as e:
                log_message = f"{func.__name__} error: {e.__class__.__name__}. Inputs: {args}, {kwargs}"
                raise
            finally:
                if filename:
                    with open(filename, "a") as file:
                        file.write(log_message + "\n")
                else:
                    print(log_message)

        return inner

    return wrapper


@log(filename="mylog.txt")
def my_function(x: int, y: int) -> int:
    return x + y


my_function(1, 2)
