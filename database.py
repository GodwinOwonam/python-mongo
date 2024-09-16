from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

uri = os.getenv("CONNECTION_STRING")
database_name = os.getenv("DATABASE_NAME")
client = MongoClient(uri)

database = client.get_database(database_name)