import pytest

from src.widget import get_date, hide_card_details


@pytest.mark.parametrize(
    "value, expected",
    [
        ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
        ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("Счет 64686473678894779589", "Счет **9589"),
    ],
)
def test_hide_card_details(value, expected):
    assert hide_card_details(value) == expected


def test_get_data():
    assert get_date("2018-07-11T02:26:18.671407") == "11.07.2018"
