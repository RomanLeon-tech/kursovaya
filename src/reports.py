import json
from datetime import datetime, timedelta
import pandas as pd


def report_decorator(filename=None):
    """
    Декоратор для сохранения отчетов в файл.

    Args:
        filename (str, optional): Имя файла для сохранения отчета. По умолчанию None.

    Returns:
        function: Декорированная функция.
    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if filename:
                with open(filename, "w") as f:
                    f.write(result)
            else:
                with open("report.json", "w") as f:
                    f.write(result)
            return result
        return wrapper
    return decorator


@report_decorator()
def spending_by_category(transactions, category, date=None):
    """
    Генерирует отчет о тратах по категории.

    Args:
        transactions (pd.DataFrame): DataFrame с транзакциями.
        category (str): Категория для анализа.
        date (str, optional): Дата для анализа в формате "YYYY-MM-DD". По умолчанию None.

    Returns:
        str: JSON-отчет.
    """
    if date is None:
        date = datetime.now()
    else:
        date = datetime.strptime(date, "%Y-%m-%d")

    start_date = date - timedelta(days=90)
    filtered_transactions = transactions[(transactions["Дата операции"] >= start_date) &
                                         (transactions["Дата операции"] <= date) &
                                         (transactions["Категория"] == category)]
    total_spent = filtered_transactions["Сумма платежа"].sum()

    return json.dumps({"category": category, "total_spent": int(total_spent)}, ensure_ascii=False, indent=4)


@report_decorator()
def spending_by_workday(transactions, date=None):
    """
    Генерирует отчет о тратах в рабочий и выходной день.

    Args:
        transactions (pd.DataFrame): DataFrame с транзакциями.
        date (str, optional): Дата для анализа в формате "YYYY-MM-DD". По умолчанию None.

    Returns:
        str: JSON-отчет.
    """
    if date is None:
        date = datetime.now()
    else:
        date = datetime.strptime(date, "%Y-%m-%d")

    start_date = date - timedelta(days=90)
    filtered_transactions = transactions[(transactions["Дата операции"] >= start_date) &
                                         (transactions["Дата операции"] <= date)]
    filtered_transactions["weekday"] = filtered_transactions["Дата операции"].dt.weekday
    workday_spending = filtered_transactions[filtered_transactions["weekday"] < 5]["Сумма платежа"].mean()
    weekend_spending = filtered_transactions[filtered_transactions["weekday"] >= 5]["Сумма платежа"].mean()

    return json.dumps({"workday_spending": float(workday_spending), "weekend_spending": float(weekend_spending)},
                      ensure_ascii=False, indent=4)
