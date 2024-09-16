from collections import OrderedDict

from pymongo.errors import CollectionInvalid


class Model:
    _collection = "companies"
    _schema = {}

    def __init__(self, database):
        self.database = database

    def up(self):
        try:
            self.database.create_collection(self._collection, validator=self._schema)
        except Exception as e:
            raise Exception("Unable to create collection due to the following error: ", e)
        except CollectionInvalid as invalid:
            raise Exception("Unable to create collection due to the following error: ", invalid)

    def update(self):
        try:
            cmd = OrderedDict([('collMod', self._collection),
                               ('validator', self._schema),
                               ('validationLevel', 'strict')])

            self.database.command(cmd)
        except Exception as e:
            raise Exception("Unable to find the document due to the following error: ", e)
        except CollectionInvalid as invalid:
            raise Exception("Unable to drop collection due to the following error: ", invalid)

    def down(self):
        try:
            self.database.drop_collection(self._collection)
        except Exception as e:
            raise Exception("Unable to find the document due to the following error: ", e)
        except CollectionInvalid as invalid:
            raise Exception("Unable to drop collection due to the following error: ", invalid)

    def model(self):
        return self.database.get_collection(self._collection)

    def describe(self):
        return self._collection
