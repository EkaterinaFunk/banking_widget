import json
import logging
from typing import Dict

import pandas as pd

logger = logging.getLogger("utils")
file_handler = logging.FileHandler("../logs/utils.log", encoding="utf8", mode="w")
file_formatter = logging.Formatter("%(asctime)s %(name)s %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def get_transactions_from_file(file_path: str) -> list[Dict]:
    """
    Функция, которая принимает на вход путь до файла и
    возвращает список словарей с данными о финансовых транзакциях.
    :param file_path: путь до файла. Поддерживаемые расширения файлов: [.csv, .json, .xlsx].
    :return: список словарей с данными о финансовых транзакциях.
    Если файл пустой, содержит не список или не найден, функция возвращает пустой список.
    """

    try:
        if ".csv" in file_path:
            logger.debug(f"Чтение CSV-файла: {file_path}")
            file_data = pd.read_csv(file_path, encoding="utf8")
            return file_data.to_dict(orient="records")
        elif ".json" in file_path:
            logger.debug(f"Чтение JSON-файла: {file_path}")
            with open(file_path, encoding="utf-8") as f:
                data = json.load(f)
                logger.debug(f"Файл {file_path} успешно прочитан.")

                # проверяем является ли data списком
                if isinstance(data, list):
                    logger.debug(f"Данные из {file_path} загружены как список.")
                    return data
                else:
                    logger.warning(f"Файл {file_path} не содержит список транзакций.")
                    return []
        elif ".xlsx" in file_path:
            logger.debug(f"Чтение XLSX-файла: {file_path}")
            file_data = pd.read_excel(file_path)
            return file_data.to_dict(orient="records")
        else:
            logger.warning(f"Неподдерживаемый формат файла: {file_path}")
            return []
    # некорректный файл
    except json.decoder.JSONDecodeError:
        logger.error(f"Ошибка декорирования JSON в файле {file_path}.")
        return []
    # файл не найден
    except FileNotFoundError:
        logger.error(f"Файл не найден: {file_path}.")
        return []
    except Exception as e:
        logger.error(f"Ошибка при чтении файла {file_path}: {e}")
        return []


if __name__ == "__main__":
    # Проверка JSON-файла
    transactions = get_transactions_from_file("../data/operations.json")
    if transactions:
        print("Список транзакций:")
        for transaction in transactions:
            print(transaction)
    else:
        print("Файл не найден, пустой или содержит некорректный формат.")

    # Проверка CSV-файла
    transactions_csv = get_transactions_from_file("../data/transactions.csv")
    if transactions_csv:
        print("Список транзакций из CSV-файла:")
        for transaction in transactions_csv:
            print(transaction)
    else:
        print("Ошибка при чтении CSV-файла.")

    # Проверка XLSX-файла
    transactions_excel = get_transactions_from_file("../data/transactions_excel.xlsx")
    if transactions_excel:
        print("\nСписок транзакций из XLSX-файла:")
        for transaction in transactions_excel:
            print(transaction)
    else:
        print("Ошибка при чтении XLSX-файла.")
