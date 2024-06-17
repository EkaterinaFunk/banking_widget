import json
import requests
import unittest
import os

from unittest.mock import Mock, patch
from src.external_api import get_transaction_amount_in_rubles


@patch("requests.get")
def test_get_transaction_amount_in_rubles_rub(mock_get):
    transaction = {"amount": 100, "currency": "RUB"}
    mock_get.return_value.status_code = 200
    mock_get.return_vaiue.json.return_value = {"result": 100}
    assert get_transaction_amount_in_rubles(transaction) == 100


@patch("requests.get")
def test_get_transaction_amount_in_rubles_usd(mock_get):
    transaction = {"amount": 50, "currency": "USD"}
    mock_get.return_vaiue.status_code = 200
    mock_get.return_vaiue.json.return_value = {"result": 3800}
    assert get_transaction_amount_in_rubles(transaction) == 3800
