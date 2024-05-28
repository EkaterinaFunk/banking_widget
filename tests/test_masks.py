from src.masks import get_masked_number, mask_card, mask_check


def test_mask_card(card):
    assert mask_card("7000792289606361") == card


def test_mask_check(check):
    assert mask_check("73654108430135874305") == check


# проверяем карты
def test_get_masked_card():
    assert get_masked_number(7000792289606361) == "7000 79** **** 6361"
    assert get_masked_number("7000792289606361") == "7000 79** **** 6361"


# проверяем счета
def test_get_masked_check():
    assert get_masked_number(73654108430135874305) == "**4305"
    assert get_masked_number("73654108430135874305") == "**4305"


# проверяем другие случаи
def test_get_masked_other():
    assert get_masked_number(12398776548) == "Введите 16-значное или 20-значное число"
    assert get_masked_number("1239877654868") == "Введите 16-значное или 20-значное число"
    assert get_masked_number("Visa Platinum 7000792289608765") == "Введите 16-значное или 20-значное число"
