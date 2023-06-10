
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import pymongo



uri = "mongodb+srv://muneeb:seen123@muneeb.ibv9fe8.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
db = client["Bank"]
collection = db["AccountInfo"]

x = collection.delete_many({})

collection.find_one
print(x.deleted_count, " documents deleted.")