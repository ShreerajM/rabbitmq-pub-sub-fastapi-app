from pymongo import MongoClient


# MongoDB setup
def get_collection():
    client = MongoClient("localhost", 27017)
    db = client["status_data"]
    collection = db["statuses"]
    return collection
