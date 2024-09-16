import time
from datetime import datetime
from bson import Timestamp
from models.Model import Model
from bson.objectid import ObjectId


class BaseRepository:
    def __init__(self, model: Model):
        self._model = model.model()

    def get(self, query: dict):
        return self._model.find_one(query)

    def get_latest(self, query: dict):
        return self._model.find_one(query, sort=[('createdAt', -1)])

    def get_all(self, query: dict):
        return self._model.find(query)

    def get_all_latest_first(self, query: dict):
        return self._model.find(query).sort({"createdAt": -1})

    def create(self, document: dict):
        return self._model.insert_one(document)

    def create_many(self, documents: list):
        return self._model.insert_many(documents)

    def update(self, document_id: str, document: dict):
        current_time = int(time.mktime(datetime.now().timetuple()))

        timestamp = Timestamp(current_time, 1)

        update_document = {**document, "updatedAt": timestamp}
        query = {"_id": ObjectId(document_id)}

        return self._model.find_one_and_update(query, update={"$set": update_document}, return_document=True)

    def update_many(self, query: dict, document: dict):
        return self._model.update_many(query, document)

    def delete(self, query: dict):
        return self._model.delete(query)

    def delete_many(self, query: dict):
        return self._model.delete_many(query)

