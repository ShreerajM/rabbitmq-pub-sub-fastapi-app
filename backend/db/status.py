from db import get_collection
from dto.status import Status


def insert_status(status: Status):
    collection = get_collection()
    collection.insert_one(status.model_dump())

def get_status_between(start, end):
    collection = get_collection()
    pipeline = [{"$match": {"timestamp": {"$gte": start, "$lte": end}}}]
    return list(collection.aggregate(pipeline))