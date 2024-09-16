from pymongo.errors import CollectionInvalid

from models.Model import Model


class Transaction(Model):
    _statuses = ['PENDING', 'COMPLETED', 'FAILED', 'CANCELLED', 'IN_ARBITRATION']
    _collection = "transactions"
    _schema = {
        "$jsonSchema": {
            "bsonType": "object",
            "required": ["supplier_id", "coin_type", "seller_address", "chat_id"],
            "properties": {
                "supplier_id": {
                    "bsonType": "string",
                    "description": "must be a string and is required"
                },
                "coin_type": {
                    "bsonType": "string",
                    "description": "must be a string and is required"
                },
                "seller_address": {
                    "bsonType": "string",
                    "description": "must be a string and is required"
                },
                "chat_id": {
                    "bsonType": "string",
                    "description": "must be a string and is required"
                },
                "amount": {
                    "bsonType": "double",
                    "minimum": 0,
                    "description": "must be a decimal"
                },
                "customer_id": {
                    "bsonType": "string",
                    "description": "must be a string"
                },
                "customer_address": {
                    "bsonType": "string",
                    "description": "must be a string"
                },
                "status": {
                    "bsonType": "string",
                    "description": "must be a string",
                    "enum": _statuses,
                },
                'createdAt': {
                    'bsonType': 'timestamp',
                    'description': 'must be a date',
                },
                'updatedAt': {
                    'bsonType': 'timestamp',
                    'description': 'must be a date'
                }
            }
        }
    }
