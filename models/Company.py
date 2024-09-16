from models.Model import Model


class Company(Model):
    _collection = "companies"
    _schema = {
        "$jsonSchema": {
            "bsonType": "object",
            "required": ["name", "industry", "location", "size"],
            "properties": {
                "name": {
                    "bsonType": "string",
                    "description": "must be a string and is required"
                },
                "industry": {
                    "bsonType": "string",
                    "description": "must be a string and is required"
                },
                "location": {
                    "bsonType": "string",
                    "description": "must be a string and is required"
                },
                "size": {
                    "bsonType": "string",
                    "description": "must be a string and is required"
                }
            }
        }
    }
