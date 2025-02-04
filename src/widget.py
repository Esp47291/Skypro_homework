from typing import List


# Функции маскировки из предыдущих задач (предполагается, что они уже существуют)
def mask_card_number(card_number: str) -> str:
    """Маскирует номер карты."""
    return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"


def mask_account_number(account_number: str) -> str:
    """Маскирует номер счета."""
    return f"**{account_number[-4:]}"


def mask_account_card(account_info: str) -> str:
    """
    Маскирует информацию о карте или счете.

    :param account_info: Строка формата 'Visa Platinum 7000792289606361' или 'Счет 73654108430135874305'
    :return: Замаскированная строка
    """
    parts: List[str] = account_info.split(maxsplit=1)
    if len(parts) != 2:
        raise ValueError("Неверный формат входных данных")

    name, number = parts
    if name.lower().startswith("счет"):
        return f"{name} {mask_account_number(number)}"
    else:
        return f"{name} {mask_card_number(number)}"
    from datetime import datetime

    def get_date(date_str: str) -> str:
        """
        Преобразует дату из формата ISO 8601 в формат ДД.ММ.ГГГГ.

        :param date_str: Строка даты в формате '2024-03-11T02:26:18.671407'
        :return: Дата в формате '11.03.2024'
        """
        try:
            dt = datetime.fromisoformat(date_str.replace("Z", "+00:00"))
            return dt.strftime("%d.%m.%Y")
        except ValueError:
            raise ValueError("Неверный формат даты")