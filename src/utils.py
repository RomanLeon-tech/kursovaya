import pandas as pd
import requests
from datetime import datetime


def load_transactions(file_path):
    """
        Загружает транзакции из Excel-файла.

        Args:
            file_path (str): Путь к Excel-файлу с транзакциями.

        Returns:
            pd.DataFrame: DataFrame с транзакциями.
        """
    return pd.read_excel(file_path, engine='openpyxl')


def get_currency_rates(currencies):
    """
        Получает курсы валют с использованием API.

        Args:
            currencies (list): Список валют для получения курсов.

        Returns:
            dict: Словарь с курсами валют.
        """
    url = "https://api.exchangerate-api.com/v4/latest/USD"
    response = requests.get(url)
    rates = response.json()["rates"]
    return {currency: rates.get(currency, None) for currency in currencies}


def get_stock_prices(stocks):
    """
        Получает цены на акции с использованием API.

        Args:
            stocks (list): Список акций для получения цен.

        Returns:
            dict: Словарь с ценами на акции.
        """
    url = "https://api.example.com/stocks"
    response = requests.get(url)
    prices = response.json()
    return {stock: prices.get(stock, None) for stock in stocks}


def get_greeting(time_str):
    """
        Возвращает приветствие в зависимости от времени суток.

        Args:
            time_str (str): Строка с временем в формате "YYYY-MM-DD HH:MM:SS".

        Returns:
            str: Приветствие.
        """
    time = datetime.strptime(time_str, "%Y-%m-%d %H:%M:%S").time()
    if time.hour < 6:
        return "Доброй ночи"
    elif time.hour < 12:
        return "Доброе утро"
    elif time.hour < 18:
        return "Добрый день"
    else:
        return "Добрый вечер"
