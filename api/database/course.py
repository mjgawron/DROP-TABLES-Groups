from database.database import db, get_next_id

#inserts into db a course
def create_course(data):
    id = get_next_id("courses")
    internal_data = {**data, "id": id, "deleted": False}
    db["courses"].insert_one(internal_data)
    return read_course(id)

#reads a single course from the db
def read_course(id):
    result = db["courses"].find_one({"id": id, "deleted": False}, {"_id": 0, "deleted": 0})
    return result

#updates a single course in db by id and data
def update_course(id, data):
    db["courses"].update_one({"id": id}, {"$set": data})
    return read_course(id)

#delets a course
def delete_course(id):
    db["courses"].update_one({"id": id}, {"$set": {"deleted": True}})

#lists all available courses
def list_course():
    result = db["courses"].find({"deleted": False}, {"_id": 0, "deleted": 0})
    return list(result)

#enrolls a student in course by adding their student id to the students list in the course document
def enroll_student(student_id,course_id):
    result = db["courses"].update_one({'id':course_id}, { '$push': { 'students': student_id } })
    return result

#unenrolls a student from course by removing their student id from the student list in the course document
def unenroll_student(student_id,course_id):
    result = db["courses"].update_one({'id':course_id},{'$pull',{'students':student_id}})
    return result

#returns all the courses the student_id is in 
def courses_by_enrollment(student_id):
    result = db["courses"].find({'students':student_id})
    return list(result)

#returns all the courses the student_id is not in
def courses_can_enroll(student_id):
    result = db["courses"].find({'students':{'$ne':student_id}}, {"_id": 0, "deleted": 0})
    return list(result)

#given a student_id and a course_id returns a true/false if that student is currently enrolled in that course
def is_enrolled(student_id,course_id):
    result:dict = db["courses"].find_one({'id':course_id})
    return student_id in result.get("students")

def is_instuctor(user_id, course_id):
    result:dict = db["courses"].find_one({'id':course_id})
    return user_id in result.get("instructors")

def is_member(user_id, course_id):
    return is_enrolled(user_id, course_id) or is_instuctor(user_id, course_id)