from typing import Any, Dict, Iterator


def filter_by_currency(operations: list[Dict[Any, Any]], currency: str) -> Iterator:
    """
    Функция-генератор
    :param operations: принимает список словарей с банковскими операциями
    :param currency: ключ словаря operation["operationAmount"]["currency"]["code"]
    :return: возвращает итератор, который выдает по очереди операции, в которых указана currency
    """
    code_list = []
    for operation in operations:
        # отлавливаем ошибку, если в списке словарей отсутствует нужный ключ
        try:
            operation_code = operation["operationAmount"]["currency"]["code"]
        except KeyError:
            continue

        if operation_code == currency.upper():
            code_list.append(operation)

    for data in code_list:
        yield data


def transaction_descriptions(operations: list[Dict[Any, Any]]) -> Iterator:
    """
    Функция-генератор
    :param operations: принимает список словарей с банковскими операциями
    :return: возвращает описание каждой операции по очереди по ключу "description"
    """
    for operation in operations:
        if operation.get("description"):
            yield operation["description"]


def card_number_generator(start: int, stop: int) -> Iterator:
    """
    Функция-генератор
    Генерируется номера карт в формате XXXX XXXX XXXX XXXX, где X — цифра.
    От 0000 0000 0000 0001 до 9999 9999 9999 9999
    :return: возвращает итераторы с номерами карт
    """
    for num in range(start, stop + 1):
        card_number = f"{num:016}"
        yield " ".join([card_number[i : i + 4] for i in range(0, 16, 4)])
