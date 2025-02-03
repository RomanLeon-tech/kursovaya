import pandas as pd

from src.views import main_view
from src.services import find_transactions_with_phone_numbers, find_transfers_to_individuals
from src.reports import spending_by_category, spending_by_workday
from src.utils import load_transactions


def main():
    """
          Основная функция для запуска всех реализованных функциональностей.
          """
    transactions = load_transactions("data/operations.xlsx").to_dict(orient="records")

    print("Main View:")
    print(main_view("2023-10-01 12:00:00"))

    print("Transactions with Phone Numbers:")
    print(find_transactions_with_phone_numbers(transactions))

    print("Transfers to Individuals:")
    print(find_transfers_to_individuals(transactions))

    print("Spending by Category:")
    print(spending_by_category(pd.DataFrame(transactions), "Переводы"))

    print("Spending by Workday:")
    print(spending_by_workday(pd.DataFrame(transactions)))


if __name__ == "__main__":
    main()
