from pymongo import MongoClient
import os

host = os.environ.get("MONGO_HOST", "mongo")
client = MongoClient(host)
db = client["project"]

def get_next_id(collection): 
    """Takes the name of a collection, returns an integer that increments with each call starting at 1"""

    # find the existing next_id if one exists for given collection
    result = db["ids"].find_one({"collection": collection})
    if result:
        next_id = result["increment"] + 1
        db["ids"].update_one({"collection": collection}, {"$set": {"increment": next_id}})
        return next_id

    # no existing id for the collection, create a new next_id for the given collection
    db["ids"].insert_one({"collection": collection, "increment": 1})
    return 1
