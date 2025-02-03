from unittest.mock import patch, Mock
from src.views import main_view
from datetime import datetime
import pandas as pd


@patch('src.views.load_transactions')
@patch('src.views.get_currency_rates')
@patch('src.views.get_stock_prices')
def test_main_view(mock_load_transactions, mock_get_currency_rates, mock_get_stock_prices):
    """
    Тест для функции main_view с использованием Mock и patch.
    """
    # Создаем мок-объекты
    mock_transactions = Mock()
    mock_transactions.return_value = pd.DataFrame({
        "Дата операции": [datetime(2023, 10, 1), datetime(2023, 10, 2)],
        "Номер карты": ["1234", "5678"],
        "Сумма платежа": [100, 200],
        "Категория": ["Переводы", "Продукты"],
        "Описание": ["Перевод на карту", "Покупка продуктов"]
    })
    mock_currency_rates = {'USD': 1.0, 'EUR': 1.1}
    mock_stock_prices = {'AAPL': 150.0, 'MSFT': 300.0}

    # Настраиваем мок-объекты
    mock_load_transactions.return_value = mock_transactions
    mock_get_currency_rates.return_value = mock_currency_rates
    mock_get_stock_prices.return_value = mock_stock_prices

    # Вызываем функцию
    result = main_view("2023-10-01 12:00:00")

    # Проверяем результат
    assert "greeting" in result
    assert "cards" in result
    assert "top_transactions" in result
    assert "currency_rates" in result
    assert "stock_prices" in result
