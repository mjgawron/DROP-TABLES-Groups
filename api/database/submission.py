from database.database import db, get_next_id

def create_submission(data):
    id = get_next_id("submissions")
    internal_data = {**data,"id":id, "deleted":False}
    db["submissions"].insert_one(internal_data)
    return read_submission(id)

def read_submission(submission_id):
    result = db["submissions"].find_one({"deleted":False,"id":submission_id},{"_id":0,"deleted":0})
    return result

def read_submission_course(course_id:int):
    result = db["submissions"].find({"deleted":False,"course_id":course_id},{"_id": 0, "deleted": 0})
    return list(result)

def read_user_submissions(user_id):
    result = db["submissions"].find({"deleted":False,"user_id":user_id},{"_id":0,"deleted":0})
    return list(result)

def update_submission(submission_id, data):
    db["submissions"].update_one({"id": submission_id}, {"$set": data})
    return read_submission(submission_id)

def delete_submission(submission_id):
    db["submissions"].update_one({"id": submission_id}, {"$set": {"deleted": True}})

def list_submission():
    result = db["submissions"].find({"deleted": False}, {"_id": 0, "deleted": 0})
    return list(result)
