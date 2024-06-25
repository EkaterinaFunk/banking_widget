import json
import logging
from typing import Dict

logger = logging.getLogger("utils")
file_handler = logging.FileHandler("../logs/utils.log", encoding="utf8", mode="w")
file_formatter = logging.Formatter("%(asctime)s %(name)s %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def get_transactions_from_json(json_file: str) -> list[Dict]:
    """
    Функция, которая принимает на вход путь до JSON-файла и
    возвращает список словарей с данными о финансовых транзакциях.
    :param json_file: путь до JSON-файла
    :return: список словарей с данными о финансовых транзакциях.
    Если файл пустой, содержит не список или не найден, функция возвращает пустой список.
    """

    try:
        with open(json_file, encoding="utf-8") as f:
            data = json.load(f)
            logger.debug(f"Файл {json_file} успешно прочитан.")

            # проверяем является ли data списком
            if isinstance(data, list):
                logger.debug(f"Данные из {json_file} загружены как список.")
                return data
            else:
                logger.warning(f"Файл {json_file} не содержит список транзакций.")
                return []
    # некорректный файл
    except json.decoder.JSONDecodeError:
        logger.error(f"Ошибка декорирования JSON в файле {json_file}.")
        return []
    # файл не найден
    except FileNotFoundError:
        logger.error(f"Файл не найден: {json_file}.")
        return []


if __name__ == "__main__":
    transactions = get_transactions_from_json("../data/operations.json")

    if transactions:
        print("Список транзакций:")
        for transaction in transactions:
            print(transaction)
    else:
        print("Файл не найден, пустой или содержит некорректный JSON.")
