from functools import wraps
from typing import Callable, Any, Dict


def log(filename: str = None) -> Callable:
    """
    Декоратор, который логирует вызов функции и ее результат в файл или в консоль.
    filename: Путь к файлу для записи логов. Если не задан, то логи выводятся в консоль.
    Returns: Декорированная функция.
    """

    def wrapper(func: Callable) -> Callable:
        @wraps(func)
        def inner(*args: Any, **kwargs: Dict[str, Any]) -> Any:
            log_message = func.__name__
            if filename:
                with open(filename, "a") as file:
                    file.write(log_message + "\n")
            else:
                print(log_message)

            try:
                result = func(*args, **kwargs)
                log_message = f"{func.__name__} ok"
                if filename:
                    with open(filename, "a") as file:
                        file.write(log_message + "\n")
                else:
                    print(log_message)
                    return result
            except Exception as e:
                log_message = f"{func.__name__} error: {type(e).__name__}. Inputs: {args}, {kwargs}"
                if filename:
                    with open(filename, "a") as file:
                        file.write(log_message + "\n")
                else:
                    print(log_message)
                raise

        return inner

    return wrapper


@log(filename="mylog.txt")
def my_function(x, y):
    return x + y


my_function(1, 2)
