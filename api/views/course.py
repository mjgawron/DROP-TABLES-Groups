import json
from flask import Blueprint, request, abort
from database.chat import create_chat, list_chat
from database.course import create_course, is_member, read_course, update_course, delete_course, list_course, enroll_student, courses_by_enrollment, courses_can_enroll
from database.questions import create_question, read_question, read_question_course, update_question, delete_question, list_question
from views.account import get_user_by_token
from html import escape

course = Blueprint("course", __name__)

#Post request for creating a course, makes user that submitted post request an instructor, SAFE
@course.route("", methods=["POST"])
def post_course_route():
    token = request.cookies.get("auth")
    data = request.json
    user:dict = get_user_by_token(token)
    save_data = {"name":escape(data["name"]),"description":escape(data["description"]),"instructors":[user.get("id")],"students":[]}
    return json.dumps(create_course(save_data)), 201

#Post request for adding a user to the enrolled students array inside a course collection
@course.route("/<int:id>/join",methods=["POST"])
def post_course_route_join():
    course_id = id
    token = request.cooksies.get("auth")
    user:dict = get_user_by_token(token)
    user_id = user.get("id")
    return json.dumps(enroll_student(user_id,course_id)) , 201

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
    if user.get("id") not in current_course.get("instructors"):
        abort(400)    
    save_data = {"name":escape(data["name"]),"description":escape(data["description"]),"instructors":[user.get("id")]}
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
    if user.get("id") not in current_course.get("instructors"):
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

#Get request for /api/course/user, gets user id from auth token and gets all courses they are enrolled in
@course.route("/user",methods=["GET"])
def get_courses_user():
    token = request.cookies.get("auth")
    user:dict = get_user_by_token(token)
    user_id = user.get("id")
    return json.dumps(courses_by_enrollment(user_id))

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
        save_data = {"message": escape(data["message"]), "course_id": id, "user": user["name"]}
        return create_chat(save_data)
    return "error", 400
    
#Get request for /api/course/user/joinable, gets user id from auth token and gets all courses they aren't enrolled in
@course.route("/user/joinable",methods=["GET"])
def get_courses_user_joinable():
    token = request.cookies.get("auth")
    user:dict = get_user_by_token(token)
    user_id = user.get("id")
    return json.dumps(courses_can_enroll(user_id))
