def mask_card(nums: str) -> str:
    """Функция, которая возвращает замаскированный номер карты"""
    return f"{nums[:4]} {nums[4:6]}** **** {nums[-4:]}"


def mask_check(nums: str) -> str:
    """Функция, которая возвращет замаскированный номер счета"""
    return f"**{nums[-4:]}"


def get_masked_number(nums: int | str) -> str:
    """Функция, которая определяет карта это или счет"""
    nums = str(nums)
    if len(nums) == 16 and nums.isdigit():
        return mask_card(nums)
    elif len(nums) == 20 and nums.isdigit():
        return mask_check(nums)
    else:
        return "Введите 16-значное или 20-значное число"
