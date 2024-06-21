import unittest
from unittest.mock import patch

import requests

from src.external_api import get_transaction_amount_in_rubles


@patch("requests.get")
def test_get_transaction_amount_in_rubles_rub(mock_get):
    transaction = {"amount": 100, "currency": "RUB"}
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {"result": 100}
    assert get_transaction_amount_in_rubles(transaction) == 100


@patch("requests.get")
def test_get_transaction_amount_in_rubles_usd(mock_get):
    transaction = {"amount": 50, "currency": "USD"}
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {"result": 4340.0814}
    assert get_transaction_amount_in_rubles(transaction) == 4340.0814


@patch("requests.get")
def test_get_transaction_amount_in_rubles_eur(mock_get):
    transaction = {"amount": 150, "currency": "EUR"}
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {"result": 13974.2193}
    assert get_transaction_amount_in_rubles(transaction) == 13974.2193


@patch("requests.get")
def test_get_transaction_amount_in_rubles_unknown_currency(mock_get):
    transaction = {"amount": 100, "currency": "JPY"}
    with unittest.TestCase().assertRaises(ValueError) as context:
        get_transaction_amount_in_rubles(transaction)
        assert "Неизвестная валюта JPY." in str(context.exception)
