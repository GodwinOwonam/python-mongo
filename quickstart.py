from pymongo import MongoClient
import re
import pprint

from models.Trainee import Trainee

uri = "mongodb://localhost:27017/"
client = MongoClient(uri)

try:
    database = client.get_database("sample_training")
    db_users = database.get_collection("users")
    db_trainees = Trainee(database).model()

    # Query for a movie that has the title 'Back to the Future'
    # query = {
    #     "userName": {
    #         "$regex": re.compile("darshan", re.IGNORECASE)
    #     },
    # }
    #
    # database.create_collection()
    #
    # users = db_users.find(query).limit(3)
    #
    # for user in users:
    #     pprint.pprint(user)

    db_trainees.insert_one({
        "name": "Marcora",
        "age": 25,
        "address": "Bangalore",
        "qualification": "B.E"
    })

    db_users.find_one()

    client.close()

except Exception as e:
    raise Exception("Unable to find the document due to the following error: ", e)
