import time
from datetime import datetime
from bson import Timestamp
from database import database
from models.Transaction import Transaction
from repositories.base_repository import BaseRepository


class TransactionRepository(BaseRepository):
    _database = database

    def __init__(self):
        _model = Transaction(self._database)
        super().__init__(_model)

    def store(self, seller_id: str, seller_address: str, chat_id: str, coin_type: str):
        current_time = int(time.mktime(datetime.now().timetuple()))

        timestamp = Timestamp(current_time, 1)

        document = {
            "supplier_id": seller_id,
            "coin_type": coin_type,
            "seller_address": seller_address,
            "chat_id": chat_id,
            "status": "PENDING",
            "customer_id": "",
            "customer_address": "",
            "amount": 0.0,
            'createdAt': timestamp,
            'updatedAt': timestamp,
        }

        transaction = self.create(document)

        return transaction

    def all(self, query: {}):
        return self.get_all(query)

    def get_by_id(self, transaction_id: str):
        return self.get({"_id": transaction_id})

    def last(self, query: {}):
        return self.get_latest(query)
