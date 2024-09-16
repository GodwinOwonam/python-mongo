from datetime import datetime
import pprint

from repositories.transaction_repository import TransactionRepository
from services.base_service import BaseService


class TransactionService(BaseService):
    def __init__(self):
        self._repository = TransactionRepository()

    def store(self, seller_id: str, seller_address: str, chat_id: str, coin_type: str):
        transaction = self._repository.store(seller_id, seller_address, chat_id, coin_type)

        return self.success_response(data=transaction)

    def all(self):
        db_transactions = self._repository.all({})

        transactions = []

        for transaction in db_transactions:
            transactions.append({
                "id": str(transaction["_id"]),
                "supplier_id": transaction["supplier_id"],
                "coin_type": transaction["coin_type"],
                "seller_address": transaction["seller_address"],
                "chat_id": transaction["chat_id"],
                "amount": 0.0 if 'amount' not in transaction else transaction['amount'],
                "customer_id": "" if 'customer_id' not in transaction else transaction['customer_id'],
                "customer_address": "" if 'customer_address' not in transaction else transaction['customer_address'],
                "created_at": "" if 'createdAt' not in transaction else datetime.fromtimestamp(transaction['createdAt'].time).strftime("%Y-%m-%d %H:%M:%S"),
                "updated_at": "" if 'updatedAt' not in transaction else datetime.fromtimestamp(transaction['updatedAt'].time).strftime("%Y-%m-%d %H:%M:%S"),
                "status": transaction["status"],
            })

            pprint.pprint(transaction)

        return self.success_response(data=transactions)

    def last(self):
        db_transaction = self._repository.last({})

        transaction = {
            "id": str(db_transaction["_id"]),
            "supplier_id": db_transaction["supplier_id"],
            "coin_type": db_transaction["coin_type"],
            "seller_address": db_transaction["seller_address"],
            "chat_id": db_transaction["chat_id"],
            "amount": 0.0 if 'amount' not in db_transaction else db_transaction['amount'],
            "customer_id": "" if 'customer_id' not in db_transaction else db_transaction['customer_id'],
            "customer_address": "" if 'customer_address' not in db_transaction else db_transaction['customer_address'],
            "created_at": "" if 'createdAt' not in db_transaction else datetime.fromtimestamp(db_transaction['createdAt'].time).strftime("%Y-%m-%d %H:%M:%S"),
            "updated_at": "" if 'updatedAt' not in db_transaction else datetime.fromtimestamp(db_transaction['updatedAt'].time).strftime("%Y-%m-%d %H:%M:%S"),
            "status": db_transaction["status"],
        }

        return self.success_response(data=transaction)

    def update(self, transaction_id: str, data: dict):
        updated_transaction = self._repository.update(transaction_id, data)

        return self.success_response(data=updated_transaction)
