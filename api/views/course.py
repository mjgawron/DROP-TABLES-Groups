import json
from flask import Blueprint, request, abort
from database.chat import create_chat, list_chat
from database.course import create_course, is_member, read_course, update_course, delete_course, list_course, enroll_student, courses_by_enrollment, courses_can_enroll, is_instructor, courses_by_ownership
from database.questions import create_question, read_question, read_question_course, update_question, delete_question, list_question
from database.account import get_user_by_token, get_user_by_id

course = Blueprint("course", __name__)

#Post request for creating a course, makes user that submitted post request an instructor, SAFE
@course.route("", methods=["POST"])
def post_course_route():
    token = request.cookies.get("auth")
    data = request.json
    user:dict = get_user_by_token(token)
    save_data = {"name":data["name"],"description":data["description"],"instructors":[user.get("id")],"students":[]}
    return json.dumps(create_course(save_data)), 201

#Post request for adding a user to the enrolled students array inside a course collection
@course.route("/<int:id>/join",methods=["POST"])
def post_course_route_join(id):
    course_id = id
    token = request.cookies.get("auth")
    user:dict = get_user_by_token(token)
    user_id = user.get("id")
    if(is_instructor(user_id,course_id)):
        abort(400)
    enroll_student(user_id,course_id)
    return "success" , 201

#Get request for recieving a single course given an id
@course.route("/<int:id>", methods=["GET"])
def get_course_detail_route(id):
    result = read_course(id)
    # check that the course exists
    if not result:
        abort(404)
    return json.dumps(result)

#Put request for editing updating a course, must be an instructor or aborts
@course.route("/<int:id>", methods=["PUT"])
def put_course_route(id):
    token = request.cookies.get("auth")
    data = request.json
    user:dict = get_user_by_token(token)
    current_course:dict = read_course(id)
    # check that the course exists
    if not current_course:
        abort(404)
    # check user is an instructor
    if not is_instructor(user.get("id"),id):
        abort(400)
    save_data = {"name":data["name"],"description":data["description"],"instructors":user.get("id")}
    return json.dumps(update_course(id, save_data))

#Delete request for removing a course, must be an instructor or aborts
@course.route("/<int:id>", methods=["DELETE"])
def delete_course_route(id):
    token = request.cookies.get("auth")
    user:dict = get_user_by_token(token)
    current_course:dict = read_course(id)
    # check that the course exists
    if not current_course:
        abort(404)
    # check user is an instructor
    if not is_instructor(user.get("id"),id):
        abort(400) 
    delete_course(id)
    return "deleted", 204

#Get request for /api/course/ gets all available courses
@course.route("", methods=["GET"])
def get_course():
    return json.dumps(list_course())

#Get request for /api/course/course_id/questions gets all questions for that course
@course.route("/<int:id>/questions",methods=["GET"])
def get_course_detail_question_route(id):
    return json.dumps(read_question_course(id))

#Get request for /api/course/member, gets user id from auth token and gets all courses they are enrolled in
@course.route("/member",methods=["GET"])
def get_courses_user():
    token = request.cookies.get("auth")
    user:dict = get_user_by_token(token)
    user_id = user.get("id")    
    
    courses_as_student = courses_by_enrollment(user_id)
    courses_as_instructor = courses_by_ownership(user_id)
    result = courses_as_student + courses_as_instructor
    reformed:list = []
    for course in result:
        instructor_list = course.get("instructors")
        new_instructors = []
        for user_id in instructor_list:
            new_instructors.append({"id":user_id,"name":get_user_by_id(user_id).get("name")})
        reformated = {"instructors":new_instructors,"name":course.get("name"),"description":course.get("description"),"id":course.get("id")}
        reformed.append(reformated)
    return json.dumps(reformed)

@course.route("/<int:id>/chat", methods=["GET"])
def get_courses_chat(id):
    token = request.cookies.get("auth")
    user:dict = get_user_by_token(token)
    user_id = user.get("id")
    if is_member(user_id, id):
        return json.dumps(list_chat(id))
    return "error", 400

@course.route("/<int:id>/chat", methods=["POST"])
def post_courses_chat(id):
    token = request.cookies.get("auth")
    user:dict = get_user_by_token(token)
    user_id = user.get("id")
    if is_member(user_id, id):
        data = request.json
        save_data = {"message": data["message"], "course_id": id, "user": user["name"]}
        create_chat(save_data)
        return "success"
    return "error", 400
    
#Get request for /api/course/user/joinable, gets user id from auth token and gets all courses they aren't enrolled in
@course.route("/user/joinable",methods=["GET"])
def get_courses_user_joinable():
    token = request.cookies.get("auth")
    user:dict = get_user_by_token(token)
    user_id = user.get("id")
    result:list[dict] = courses_can_enroll(user_id)
    reformed:list = []
    for course in result:
        instructor_list = course.get("instructors")
        new_instructors = []
        for user_id in instructor_list:
            new_instructors.append({"id":user_id,"name":get_user_by_id(user_id).get("name")})
        reformated = {"instructors":new_instructors,"name":course.get("name"),"description":course.get("description"),"id":course.get("id")}
        reformed.append(reformated)
    return json.dumps(reformed)

@course.route("/<int:id>/roster",methods=["GET"])
def get_course_roster(id):
    token = request.cookies.get("auth")
    user:dict = get_user_by_token(token)
    if not is_instructor(user.get("id"),id):
        abort(400)
    course:dict = read_course(id)
    course_roster = course.get("students")
    roster = []
    for student_id in course_roster:
        student = get_user_by_id(student_id)
        roster.append({"name":student.get("name"),"username":student.get("username")})
    return json.dumps(roster)

@course.route("/<int:id>/instructor",methods=["GET"])
def instructor_verification(id):
    user = get_user_by_token(request.cookies.get("auth"))
    user_id = user.get("id")
    verify = is_instructor(user_id,id)
    return(json.dumps(verify))