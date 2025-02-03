import json
import re


def find_transactions_with_phone_numbers(transactions):
    """
        Находит транзакции, содержащие номера телефонов.

        Args:
            transactions (list): Список транзакций.

        Returns:
            str: JSON-ответ с транзакциями, содержащими номера телефонов.
        """
    phone_pattern = re.compile(r'\+7 \d{3} \d{2}-\d{2}-\d{2}')
    matching_transactions = [transaction for transaction
                             in transactions if phone_pattern.search(transaction["Описание"])]
    return json.dumps(matching_transactions, ensure_ascii=False, indent=4)


def find_transfers_to_individuals(transactions):
    """
        Находит транзакции, относящиеся к переводам физическим лицам.

        Args:
            transactions (list): Список транзакций.

        Returns:
            str: JSON-ответ с транзакциями, относящимися к переводам физическим лицам.
        """
    transfer_pattern = re.compile(r'Переводы')
    name_pattern = re.compile(r'\b[А-Яа-я]+\b [А-Яа-я]\.')
    matching_transactions = [transaction for transaction
                             in transactions if transfer_pattern.search(transaction["Категория"])
                             and name_pattern.search(transaction["Описание"])]
    return json.dumps(matching_transactions, ensure_ascii=False, indent=4)
