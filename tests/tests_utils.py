import json
from unittest.mock import patch

from src.utils import get_transactions_from_json


@patch("builtins.open")
def test_get_transactions_from_json(mock_open):
    mock_file = mock_open.return_value.__enter__.return_value

    # Проверка на удачный результат.
    mock_file.read.return_value = json.dumps([{"test": "test"}])
    assert get_transactions_from_json("test.json") == [{"test": "test"}]

    # Проверка на ошибку типа файла.
    mock_file.read.return_value = json.dumps({})
    assert get_transactions_from_json("test.json") == []

    # Проверка на некорректный файл.
    mock_file.read.return_value = json.dumps("testtest")
    assert get_transactions_from_json("test.json") == []

    # Проверка на пустой файл.
    mock_file.read.return_value = ""
    assert get_transactions_from_json("test.json") == []
