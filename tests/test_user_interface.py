from src.user_interface import (count_transactions_by_category, filter_transactions_by_description,
                                filter_transactions_by_state, sort_transactions, validate_state)


def test_filter_transactions_by_description():
    transactions = [
        {"description": "Перевод 1"},
        {"description": "Оплата 1"},
        {"description": "Перевод 2"},
        {"description": "Оплата 2"},
    ]
    filtered_transactions = filter_transactions_by_description(transactions, "Перевод")
    assert len(filtered_transactions) == 2


def test_count_transactions_by_category():
    transactions = [
        {"description": "Перевод 1"},
        {"description": "Оплата 1"},
        {"description": "Перевод 2"},
        {"description": "Оплата 2"},
    ]
    categories = ["Перевод", "Оплата"]
    transaction_counts = count_transactions_by_category(transactions, categories)
    assert transaction_counts["Перевод"] == 2
    assert transaction_counts["Оплата"] == 2


def test_validate_state():
    assert validate_state("EXECUTED")
    assert validate_state("CANCELED")
    assert validate_state("PENDING")
    assert not validate_state("INVALID")


def test_filter_transactions_by_state():
    transactions = [
        {"state": "EXECUTED"},
        {"state": "PENDING"},
        {"state": "EXECUTED"},
        {"state": "CANCELED"},
    ]
    filtered_transactions = filter_transactions_by_state(transactions, "EXECUTED")
    assert len(filtered_transactions) == 2


def test_sort_transactions():
    transactions = [
        {"description": "Перевод 1", "date": "2023-04-20"},
        {"description": "Оплата 1", "date": "2023-04-19"},
        {"description": "Перевод 2", "date": "2023-04-18"},
    ]
    sorted_transactions = sort_transactions(transactions, "date")
    assert sorted_transactions[0]["description"] == "Перевод 2"
    assert sorted_transactions[1]["description"] == "Оплата 1"
    assert sorted_transactions[2]["description"] == "Перевод 1"


if __name__ == "__main__":
    test_filter_transactions_by_description()
    test_count_transactions_by_category()
    test_validate_state()
    test_filter_transactions_by_state()
    test_sort_transactions()
    print("All tests passed!")
