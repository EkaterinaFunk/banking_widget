import logging

logger = logging.getLogger("masks")
file_handler = logging.FileHandler("../masks.log", encoding="utf8", mode="w")
file_formatter = logging.Formatter("%(asctime)s %(name)s %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def mask_card(nums: str) -> str:
    """Функция, которая возвращает замаскированный номер карты"""
    logger.info(f"Передан номер карты: {nums}.")
    masked_number = f"{nums[:4]} {nums[4:6]}** **** {nums[-4:]}"
    logger.debug(f"Замаскированный номер карты: {masked_number}.")
    return masked_number


def mask_check(nums: str) -> str:
    """Функция, которая возвращет замаскированный номер счета"""
    logger.info(f"Передан номер счета: {nums}.")
    masked_number = f"**{nums[-4:]}"
    logger.debug(f"Замаскированный номер карты: {masked_number}.")
    return masked_number


def get_masked_number(nums: int | str) -> str:
    """Функция, которая определяет карта это или счет"""
    nums = str(nums)
    if len(nums) == 16 and nums.isdigit():
        logger.debug("Вызов функции mask_card.")
        return mask_card(nums)
    elif len(nums) == 20 and nums.isdigit():
        logger.debug("Вызов функции mask_check.")
        return mask_check(nums)
    else:
        logger.warning("Введен некорректный номер.")
        return "Введите 16-значное или 20-значное число"


if __name__ == "__main__":
    get_masked_number(7000792289606361)

    get_masked_number(70007922896063615674)

    get_masked_number(654583)
