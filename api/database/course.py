from database.database import db, get_next_id


def create_course(data):
    id = get_next_id("courses")
    internal_data = {**data, "id": id, "deleted": False}
    db["courses"].insert_one(internal_data)
    return read_course(id)

def read_course(id):
    result = db["courses"].find_one({"id": id, "deleted": False}, {"_id": 0, "deleted": 0})
    return result

def update_course(id, data):
    db["courses"].update_one({"id": id}, {"$set": data})
    return read_course(id)

def delete_course(id):
    db["courses"].update_one({"id": id}, {"$set": {"deleted": True}})

def list_course():
    result = db["courses"].find({"deleted": False}, {"_id": 0, "deleted": 0})
    return list(result)

def enroll_student(student_id,course_id):
    result = db["courses"].update_one({'id':course_id}, { '$push': { 'students': student_id } })
    return result

def unenroll_student(student_id,course_id):
    result = db["courses"].update_one({'id':course_id},{'$pull',{'students':student_id}})
    return result

def courses_by_enrollment(student_id):
    result = db["courses"].find({'students':student_id})
    return result