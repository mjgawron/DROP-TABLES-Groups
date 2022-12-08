from database.database import db, get_next_id

def create_question(data):
    id = get_next_id("questions")
    internal_data = {**data,"id":id, "deleted":False}
    db["questions"].insert_one(internal_data)
    return read_question(id)

def read_question(id):
    result = db["questions"].find_one({"deleted":False,"id":id},{"_id":0,"deleted":0})
    return result

def read_question_course(id:int):
    result = db["questions"].find({"deleted":False,"course_id":id},{"_id": 0, "deleted": 0})
    return list(result)

def read_question_ids_course(id):
    result = read_question_course(id)
    ret_val = []
    for elm in result:
        ret_val.append(elm.get("id"))
    return ret_val

def update_question(id, data):
    db["questions"].update_one({"id": id}, {"$set": data})
    return read_question(id)

def delete_question(id):
    db["questions"].update_one({"id": id}, {"$set": {"deleted": True}})

def list_question():
    result = db["questions"].find({"deleted": False}, {"_id": 0, "deleted": 0})
    return list(result)
