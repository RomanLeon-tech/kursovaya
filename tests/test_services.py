import pytest
from src.services import find_transactions_with_phone_numbers, find_transfers_to_individuals


@pytest.mark.parametrize("transactions, expected", [
    ([
        {"Описание": "Перевод на карту +7 921 11-22-33"},
        {"Описание": "Покупка в магазине"},
        {"Описание": "Перевод на карту +7 981 33-44-55"}
    ], ["Перевод на карту +7 921 11-22-33", "Перевод на карту +7 981 33-44-55"]),
    ([
        {"Описание": "Покупка в магазине"},
        {"Описание": "Перевод на карту +7 981 33-44-55"}
    ], ["Перевод на карту +7 981 33-44-55"]),
])
def test_find_transactions_with_phone_numbers(transactions, expected):
    """
    Тест для функции find_transactions_with_phone_numbers.
    """
    result = find_transactions_with_phone_numbers(transactions)
    for item in expected:
        assert item in result


@pytest.mark.parametrize("transactions, expected", [
    ([
        {"Категория": "Переводы", "Описание": "Валерий А."},
        {"Категория": "Переводы", "Описание": "Покупка в магазине"},
        {"Категория": "Переводы", "Описание": "Сергей З."}
    ], ["Валерий А.", "Сергей З."]),
    ([
        {"Категория": "Переводы", "Описание": "Покупка в магазине"},
        {"Категория": "Переводы", "Описание": "Сергей З."}
    ], ["Сергей З."]),
])
def test_find_transfers_to_individuals(transactions, expected):
    """
    Тест для функции find_transfers_to_individuals.
    """
    result = find_transfers_to_individuals(transactions)
    for item in expected:
        assert item in result
