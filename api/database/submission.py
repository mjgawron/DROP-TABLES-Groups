from database.database import db, get_next_id
from database.questions import read_question, read_question_ids_course
from database.course import is_member, is_enrolled, is_instructor, read_course
from database.account import get_user_by_id

def create_submission(data):
    id = get_next_id("submissions")
    
    user_id = data["user_id"]    
    student_choice = data["choice"]
    question_id = data["question_id"]
    
    user:dict = get_user_by_id(user_id)

    question:dict = read_question(question_id)
    course_id = question.get("course_id")
    correct_choice = question.get("answer")
    
    correct = student_choice == correct_choice

    save_data = {"course_id":course_id,"question_id":question_id,"user_id":user_id,"user_name":user.get("name"),"correct":correct}
    

    internal_data = {**save_data,"id":id, "deleted":False}
    db["submissions"].insert_one(internal_data)
    return read_submission(id)

def read_submission(submission_id):
    result = db["submissions"].find_one({"deleted":False,"id":submission_id},{"_id":0,"deleted":0})
    return result

def read_submission_course(course_id:int):
    result = db["submissions"].find({"deleted":False,"course_id":course_id},{"_id": 0, "deleted": 0})
    return list(result)

def read_submission_student(user_id,question_id):
    result = db["submissions"].find_one({"deleted":False,"user_id":user_id,"question_id":question_id},{"_id":0,"deleted":0})
    return result

def already_submitted(user_id,question_id):
    result = db["submissions"].find_one({"deleted":False,"question_id":question_id,"user_id":user_id})
    return result != None

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
