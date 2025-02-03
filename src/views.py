import json
from datetime import datetime
from src.utils import load_transactions, get_currency_rates, get_stock_prices, get_greeting


def main_view(date_time_str):
    """
        Генерирует JSON-ответ для главной страницы.

        Args:
            date_time_str (str): Строка с датой и временем в формате "YYYY-MM-DD HH:MM:SS".

        Returns:
            str: JSON-ответ.
        """
    transactions = load_transactions("data/operations.xlsx")
    date_time = datetime.strptime(date_time_str, "%Y-%m-%d %H:%M:%S")
    start_date = date_time.replace(day=1)
    end_date = date_time

    filtered_transactions = transactions[(transactions["Дата операции"]
                                          >= start_date) & (transactions["Дата операции"] <= end_date)]

    greeting = get_greeting(date_time_str)

    cards = []
    for card in filtered_transactions["Номер карты"].unique():
        card_transactions = filtered_transactions[filtered_transactions["Номер карты"] == card]
        total_spent = card_transactions["Сумма платежа"].sum()
        cashback = total_spent * 0.01
        cards.append({
            "last_digits": card,
            "total_spent": total_spent,
            "cashback": cashback
        })

    top_transactions = filtered_transactions.nlargest(5, "Сумма платежа")[["Дата операции",
                                                                           "Сумма платежа", "Категория", "Описание"]]
    top_transactions = top_transactions.rename(columns={"Дата операции": "date", "Сумма платежа": "amount",
                                                        "Категория": "category", "Описание": "description"})
    top_transactions = top_transactions.to_dict(orient="records")

    with open("user_settings.json") as f:
        user_settings = json.load(f)

    currency_rates = get_currency_rates(user_settings["user_currencies"])
    stock_prices = get_stock_prices(user_settings["user_stocks"])

    response = {
        "greeting": greeting,
        "cards": cards,
        "top_transactions": top_transactions,
        "currency_rates": [{"currency": currency, "rate": rate} for currency, rate in currency_rates.items()],
        "stock_prices": [{"stock": stock, "price": price} for stock, price in stock_prices.items()]
    }

    return json.dumps(response, ensure_ascii=False, indent=4)
