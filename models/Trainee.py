from pymongo.errors import CollectionInvalid

from models.Model import Model


class Trainee(Model):
    _collection = "trainees"
    _schema = {
        "$jsonSchema": {
            "bsonType": "object",
            "required": ["name", "age", "address", "qualification"],
            "properties": {
                "name": {
                    "bsonType": "string",
                    "description": "must be a string and is required"
                },
                "age": {
                    "bsonType": "int",
                    "minimum": 0,
                    "maximum": 200,
                    "description": "must be a string and is required"
                },
                "address": {
                    "bsonType": "string",
                    "description": "must be a string and is required"
                },
                "qualification": {
                    "bsonType": "string",
                    "description": "must be a string and is required"
                }
            }
        }
    }
