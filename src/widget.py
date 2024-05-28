from .masks import get_masked_number


def hide_card_details(bank_card: str) -> str:
    """Функция, которая возвращает исходную строку с замаскированным номером карты/счета"""
    card_parts = bank_card.split()
    card_parts[-1] = get_masked_number(card_parts[-1])
    return " ".join(card_parts)


def get_date(date: str) -> str:
    """Функция, которая принимает на вход дату и выводит в необходимом формате"""
    desired_date = date[:10]
    format_the_date = desired_date.split("-")
    year, month, day = format_the_date
    return f"{day}.{month}.{year}"
