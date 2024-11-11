import json
import csv
import re
import pandas as pd
from src.widget import hide_card_details


def filter_transactions_by_description(transactions: list, search_string: str) -> list:
    """
    Функция, которая принимает список словарей с данными о банковских операциях и строку поиска,
    а возвращает список словарей, у которых в описании есть данная строка.

    :param transactions: Список словарей с данными о банковских операциях.
    :param search_string: Строка поиска.

    :return: Список словарей, у которых в описании есть данная строка.
    """
    pattern = re.compile(search_string, re.IGNORECASE)
    return [t for t in transactions if pattern.search(t['description'])]


def count_transactions_by_category(transactions: list, categories: list) -> dict:
    """
    Функция, которая принимает список словарей с данными о банковских операциях и список категорий операций,
    а возвращает словарь, в котором ключи — это названия категорий,
    а значения — это количество операций в каждой категории.

    :param transactions: Список словарей с данными о банковских операциях.
    :param categories: Список категорий операций.

    :return: Словарь, в котором ключи — это названия категорий, а значения — это количество операций в каждой категории.
    """
    transaction_counts = {category: 0 for category in categories}
    for transaction in transactions:
        for category in categories:
            if category.lower() in transaction['description'].lower():
                transaction_counts[category] += 1
    return transaction_counts


def load_transactions_from_json(file_path: str) -> list:
    """
    Функция, которая загружает данные о банковских операциях из JSON-файла.

    :param file_path: Путь к JSON-файлу.

    :return: Список словарей с данными о банковских операциях.
    """
    with open(file_path, 'r', encoding="utf8") as f:
        transactions = json.load(f)
    return transactions


def load_transactions_from_csv(file_path: str) -> list:
    """
    Функция, которая загружает данные о банковских операциях из CSV-файла.

    :param file_path (str): Путь к CSV-файлу.

    :return: Список словарей с данными о банковских операциях.
    """
    transactions = []
    with open(file_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f, delimiter=';')
        for row in reader:
            transactions.append(row)
    return transactions


def load_transactions_from_xlsx(file_path: str) -> list:
    """
    Функция, которая загружает данные о банковских операциях из XLSX-файла.

    :param file_path: Путь к XLSX-файлу.

    :return: Список словарей с данными о банковских операциях.
    """
    df = pd.read_excel(file_path)
    transactions = df.to_dict('records')
    return transactions


def validate_state(state: str) -> bool:
    """
    Функция, которая проверяет корректность введенного статуса.

    :param state: Введенный статус.

    :return: True, если статус корректен, False - в противном случае.
    """
    return state.upper() in ['EXECUTED', 'CANCELED', 'PENDING']


def filter_transactions_by_state(transactions: list, state: str) -> list:
    """
    Функция, которая фильтрует список транзакций по заданному статусу.

    :param transactions: Список словарей с данными о банковских операциях.
    :param state: Статус, по которому нужно отфильтровать транзакции.

    :return: Список отфильтрованных транзакций.
    """

    return [t for t in transactions if
            isinstance(t.get('state', ''), str) and t.get('state', '').upper() == state.upper()]


def sort_transactions(transactions: list, field: str, reverse: bool = False) -> list:
    """
    Функция, которая сортирует список транзакций по заданному полю.

    :param transactions: Список словарей с данными о банковских операциях.
    :param field: Поле, по которому нужно отсортировать транзакции.
    :param reverse: Флаг, указывающий на необходимость сортировки в обратном порядке.

    :return: Отсортированный список транзакций.
    """
    return sorted(transactions, key=lambda x: x[field], reverse=reverse)


def print_transactions(transactions: list, typefile: str):
    """
    Функция, которая выводит информацию о транзакциях.

    :param typefile: Тип файла
    :param transactions: Список словарей с данными о банковских операциях.
    """
    print("Распечатываю итоговый список транзакций...")
    print("Всего банковских операций в выборке:", len(transactions))
    for i, transaction in enumerate(transactions):
        if 'перевод' in transaction['description'].lower():
            if typefile == '1':
                amount = transaction.get('operationAmount', {}).get('amount', 0)
            elif typefile == '2':
                amount = transaction.get('amount', 0)
            elif typefile == '3':
                amount = transaction.get('amount', 0)

            check_from = hide_card_details(transaction.get('from', 'Нет информации'))
            check_to = hide_card_details(transaction.get('to', 'Нет информации'))
            currency = transaction.get('currency', '')
            print(f"{i + 1}. {transaction.get('date', '')} {transaction['description']}"
                  f"\nСчет: {check_from} -> {check_to}"
                  f"\nСумма: {amount} {currency}")

        elif 'вклад' in transaction['description'].lower():
            if typefile == '1':
                amount = transaction.get('operationAmount', {}).get('amount', 0)
            elif typefile == '2':
                amount = transaction.get('amount', 0)
            elif typefile == '3':
                amount = transaction.get('amount', 0)

            check = hide_card_details(transaction.get('to', 'Нет информации'))
            currency = transaction.get('currency', '')
            print(f"{i + 1}. {transaction.get('date', '')} {transaction['description']}"
                  f"\nСчет: {check}"
                  f"\nСумма: {amount} {currency}")

        else:
            if typefile == '1':
                amount = transaction.get('operationAmount', {}).get('amount', 0)
            elif typefile == '2':
                amount = transaction.get('amount', 0)
            elif typefile == '3':
                amount = transaction.get('amount', 0)

            check = transaction.get('from', 'Нет информации')
            currency = transaction.get('currency', '')
            print(f"{i + 1}. {transaction.get('date', '')} {transaction['description']}"
                  f"\nСчет: {check}"
                  f"\nСумма: {amount} {currency}")
    if len(transactions) == 0:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")


def main():
    """
    Функция, которая отвечает за основную логику проекта.
    """
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")

    transactions = None
    while not transactions:
        print("Выберите необходимый пункт меню:")
        print("1. Получить информацию о транзакциях из JSON-файла")
        print("2. Получить информацию о транзакциях из CSV-файла")
        print("3. Получить информацию о транзакциях из XLSX-файла")
        choice = input()
        if choice == '1':
            file_path = "../data/operations.json"
            transactions = load_transactions_from_json(file_path)
        elif choice == '2':
            file_path = "../data/transactions.csv"
            transactions = load_transactions_from_csv(file_path)
        elif choice == '3':
            file_path = "../data/transactions_excel.xlsx"
            transactions = load_transactions_from_xlsx(file_path)
        else:
            print("Некорректный выбор.")

    while True:
        state = ''
        while state not in ['EXECUTED', 'CANCELED', 'PENDING']:
            state = input("Введите статус, по которому необходимо выполнить фильтрацию."
                          "\nДоступные для фильтровки статусы: EXECUTED, CANCELED, PENDING\n").upper().strip()
            if validate_state(state):
                filtered_transactions = filter_transactions_by_state(transactions, state)
                print(f"Операции отфильтрованы по статусу \"{state}\"")
            else:
                print(f"Программа: Статус операции \"{state}\" недоступен.")

        sort_by_date = ''
        while sort_by_date not in ['да', 'нет']:
            sort_by_date = input("Отсортировать операции по дате? Да/Нет\n").lower()
            if sort_by_date.strip() == 'да':
                sort_order = None
                while sort_order not in ['по возрастанию', 'по убыванию']:
                    sort_order = input("Отсортировать по возрастанию или по убыванию?\n").lower()
                    if sort_order == 'по возрастанию':
                        filtered_transactions = sort_transactions(filtered_transactions, 'date')
                    elif sort_order == 'по убыванию':
                        filtered_transactions = sort_transactions(filtered_transactions, 'date', reverse=True)
                    else:
                        print("Некорректный выбор.")

        show_only_rub = ''
        while show_only_rub.strip() not in ['да', 'нет']:
            show_only_rub = input("Выводить только рублевые транзакции? Да/Нет\n").lower()
            if show_only_rub == 'да':
                if choice == '1':
                    filtered_transactions = [t for t in filtered_transactions if
                                             t.get("operationAmount", {}).get('currency', '').get('code', '') == 'RUB']
                if choice == '2':
                    filtered_transactions = [t for t in filtered_transactions
                                             if t.get('currency_code', '') == 'RUB']
                if choice == '3':
                    filtered_transactions = [t for t in filtered_transactions
                                             if t.get('currency_code', '') == 'RUB']
                break

        filter_by_description = ''
        while filter_by_description.strip() not in ['да', 'нет']:
            filter_by_description = input("Отфильтровать список транзакций по определенному слову "
                                          "в описании? Да/Нет\n").lower()
            if filter_by_description == 'да':
                search_string = input("Введите слово для фильтрации: ")
                filtered_transactions = filter_transactions_by_description(filtered_transactions, search_string)

        if filtered_transactions:
            print_transactions(filtered_transactions, choice)
            break
        else:
            print('По вашему выбору не найдено транзакций, попробуйте снова.')


if __name__ == "__main__":
    main()
