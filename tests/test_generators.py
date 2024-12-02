import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


def test_filter_by_currency_usd(transactions):
    generator = filter_by_currency(transactions, "USD")
    assert next(generator)["id"] == 939719570
    assert next(generator)["id"] == 142264268
    assert next(generator)["id"] == 895315941


def test_filter_by_currency_rub(transactions):
    generator = filter_by_currency(transactions, "rub")
    assert next(generator)["id"] == 873106923
    assert next(generator)["id"] == 594226727


def test_filter_by_currency_keyerror(transactions):
    generator = filter_by_currency(transactions, "EUR")
    with pytest.raises(StopIteration):
        next(generator)


def test_transaction_descriptions(transactions):
    generator = transaction_descriptions(transactions)
    assert next(generator) == "Перевод организации"
    assert next(generator) == "Перевод со счета на счет"
    assert next(generator) == "Перевод со счета на счет"
    assert next(generator) == "Перевод с карты на карту"
    assert next(generator) == "Перевод организации"


def test_card_number_generator():
    generator = card_number_generator(1, 3)
    assert next(generator) == "0000 0000 0000 0001"
    assert next(generator) == "0000 0000 0000 0002"
    assert next(generator) == "0000 0000 0000 0003"
