def get_mask_card_number(card_number: int) -> str:
    """
    Принимает номер карты в виде числа и возвращает строку
    с маской формата: XXXX XX** **** XXXX

    :param card_number: номер карты, например 7000792289606361
    :return: маска номера, например '7000 79** **** 6361'
    """
    # Сначала превратим число в строку, чтобы легче манипулировать
    card_str = str(card_number)
    # Предположим, что номер карты состоит из 16 цифр.
    # Возьмём первые 6, потом две **, затем 4 звёздочки ****,
    # и последние 4.
    # Формируем нужные нам блоки:
    first_4 = card_str[:4]  # первые 4 цифры
    next_2 = card_str[4:6]  # следующие 2 цифры
    middle_2_mask = "**"  # замена следующих 2 цифр на **
    middle_4_mask = "****"  # замена 4 цифр на ****
    last_4 = card_str[-4:]  # последние 4 цифры

    # Собираем итоговую строку с пробелами
    masked = f"{first_4} {next_2}{middle_2_mask} {middle_4_mask} {last_4}"

    return masked


def get_mask_account(account_number: int) -> str:
    """
    Принимает номер счета в виде числа и возвращает строку
    с маской формата: **XXXX

    :param account_number: номер счёта, например 73654108430135874305
    :return: маска номера, например '**4305'
    """
    account_str = str(account_number)
    # Последние 4 символа - это видимые цифры:
    last_4 = account_str[-4:]
    # Две звёздочки перед ними
    masked = f"**{last_4}"

    return masked
"""
Модуль для обработки банковских операций.
Содержит функции для фильтрации и сортировки операций по различным критериям.
"""

from typing import List, Dict, Any
from datetime import datetime


def filter_by_state(operations: List[Dict[str, Any]], state: str = "EXECUTED") -> List[Dict[str, Any]]:
    """
    Фильтрует список банковских операций по заданному статусу (state).

    :param operations: Список операций, где каждая операция представлена словарём.
                       Пример элемента списка:
                       {
                           "id": 41428829,
                           "state": "EXECUTED",
                           "date": "2019-07-03T18:35:29.512364"
                       }
    :param state: Статус, по которому нужно отфильтровать (по умолчанию "EXECUTED").
    :return: Новый список операций, содержащий только те, у которых "state" совпадает со значением, переданным в функцию.
    """
    return [op for op in operations if op.get("state") == state]


def sort_by_date(operations: List[Dict[str, Any]], descending: bool = True) -> List[Dict[str, Any]]:
    """
    Сортирует список банковских операций по дате (ключ "date").

    :param operations: Список операций, где каждая операция представлена словарём.
    :param descending: Порядок сортировки. True = по убыванию (самые последние даты в начале),
                       False = по возрастанию. По умолчанию True.
    :return: Новый список, отсортированный по ключу "date" в заданном порядке.
    """
    # Чтобы корректно сортировать по дате, конвертируем строку в datetime
    # и используем её при сортировке.
    def get_date(op: Dict[str, Any]) -> datetime:
        return datetime.fromisoformat(op["date"])

    return sorted(operations, key=get_date, reverse=descending)
