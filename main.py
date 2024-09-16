from database import client
from services.transaction_service import TransactionService

transaction_service = TransactionService()


def start_transaction():
    try:
        new_transaction = transaction_service.store("First Last", "first transaction", "chatter", "BTC")

        print(new_transaction)
    except Exception as e:
        print(e)


def all_transactions():
    try:
        transactions = transaction_service.all()

        print(transactions)
    except Exception as e:
        print(e)


def update_transaction():
    try:
        update = {
            "customer_id": "nothing here",
            "customer_address": "098765567890jeue",
            "status": "COMPLETED"
        }

        transaction = transaction_service.update("66e85a3bc49697d32c2c2dcf", update)

        print(transaction)
    except Exception as e:
        print(e)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # start_transaction()
    # all_transactions()

    # update_transaction()

    print(transaction_service.last())

    client.close()
