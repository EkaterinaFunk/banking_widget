import json
from unittest.mock import patch

from src.utils import get_transactions_from_file


@patch("builtins.open")
def test_get_transactions_from_json(mock_open):
    mock_file = mock_open.return_value.__enter__.return_value

    # Проверка на удачный результат.
    mock_file.read.return_value = json.dumps([{"test": "test"}])
    assert get_transactions_from_file("test.json") == [{"test": "test"}]

    # Проверка на ошибку типа файла.
    mock_file.read.return_value = json.dumps({})
    assert get_transactions_from_file("test.json") == []

    # Проверка на некорректный файл.
    mock_file.read.return_value = json.dumps("testtest")
    assert get_transactions_from_file("test.json") == []

    # Проверка на пустой файл.
    mock_file.read.return_value = ""
    assert get_transactions_from_file("test.json") == []


@patch("pandas.read_csv")
def test_get_transactions_from_csv(mock_read_csv, transactions):
    mock_read_csv.return_value.to_dict.return_value = transactions
    assert get_transactions_from_file("data/transactions.csv") == transactions
    mock_read_csv.assert_called_once_with("data/transactions.csv", encoding="utf8")


@patch("pandas.read_excel")
def test_get_transactions_from_excel(mock_read_excel, transactions):
    mock_read_excel.return_value.to_dict.return_value = transactions
    assert get_transactions_from_file("data/transactions.xlsx") == transactions
    mock_read_excel.assert_called_once_with("data/transactions.xlsx")
