from database.database import db, get_next_id

def create_chat(data):
    id = get_next_id("chat")
    internal_data = {**data,"id":id, "deleted":False}
    db["chat"].insert_one(internal_data)
    return 

def list_chat(course_id):
    result = db["chat"].find({"deleted": False}, {"_id": 0, "deleted": 0})
    return list(result)