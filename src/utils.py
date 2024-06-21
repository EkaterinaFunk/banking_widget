import json
from typing import Dict


def get_transactions_from_json(json_file: str | None) -> list[Dict]:
    """
    Функция, которая принимает на вход путь до JSON-файла и
    возвращает список словарей с данными о финансовых транзакциях.
    :param json_file: путь до JSON-файла
    :return: список словарей с данными о финансовых транзакциях.
    Если файл пустой, содержит не список или не найден, функция возвращает пустой список.
    """

    try:
        with open("../data/operations.json", encoding="utf-8") as f:
            data = json.load(f)

            # проверяем является ли data списком
            if isinstance(data, list):
                return data
            else:
                return []
    # некорректный файл
    except json.decoder.JSONDecodeError:
        return []
    # файл не найден
    except FileNotFoundError:
        return []
