import pytest
import pandas as pd
from datetime import datetime
from src.reports import spending_by_category, spending_by_workday


@pytest.fixture
def sample_transactions():
    """
    Фикстура для создания примера транзакций.
    """
    data = {
        "Дата операции": [
            datetime(2023, 10, 1),
            datetime(2023, 10, 2),
            datetime(2023, 10, 3),
            datetime(2023, 10, 4),
            datetime(2023, 10, 5)
        ],
        "Категория": ["Переводы", "Переводы", "Продукты", "Продукты", "Продукты"],
        "Сумма платежа": [100, 200, 300, 400, 500]
    }
    return pd.DataFrame(data)


def test_spending_by_category(sample_transactions):
    """
    Тест для функции spending_by_category.
    """
    result = spending_by_category(sample_transactions, "Переводы", "2023-10-05")
    assert "category" in result
    assert "total_spent" in result
    assert "Переводы" in result
    assert "300" in result


def test_spending_by_workday(sample_transactions):
    """
    Тест для функции spending_by_workday.
    """
    result = spending_by_workday(sample_transactions, "2023-10-05")
    assert "workday_spending" in result
    assert "weekend_spending" in result
    assert "350.0" in result  # Сумма трат в рабочий день
    assert "100.0" in result  # Сумма трат в выходной день
