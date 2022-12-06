import json
from flask import Blueprint, request, abort
from database.questions import create_question, read_question, read_question_course, update_question, delete_question, list_question
from database.account import get_user_by_token
from database.course import read_course
from html import escape

question = Blueprint("question", __name__)

@question.route("", methods=["POST"])
def post_question_route():
    data = request.json
    
    course_id = data["course_id"]
    token = request.cookies.get("auth")
    
    if ( not _verify_instructor(token,course_id)):
        abort(400)
    
    save_data = {"course_id":course_id,"question_detail":escape(data["question_detail"]),"answer_a":escape(data["answer_a"]),"answer_b":escape(data["answer_b"]),"answer_c":escape(data["answer_c"]),"answer_d":escape(data["answer_d"]),"answer":escape(data["answer"])}
    return json.dumps(create_question(save_data)), 201

@question.route("/<int:id>", methods=["GET"])
def get_question_detail_route(id):
    result = read_question(id)
    # check that the question exists
    if not result:
        abort(404)
    return json.dumps(result)

@question.route("/<int:id>", methods=["PUT"])
def put_question_route(id):
    # check that the question exists
    current_question:dict = read_question(id)
    if not current_question:
        abort(404)
    
    #check client is instructor for course
    course_id = current_question.get("course_id")
    token = request.cookies.get("auth")
    if ( not _verify_instructor(token,course_id)):
        abort(400)

    data = request.json
    save_data = {"course_id":course_id,"question_detail":escape(data["question_detail"]),"answer_a":escape(data["answer_a"]),"answer_b":escape(data["answer_b"]),"answer_c":escape(data["answer_c"]),"answer_d":escape(data["answer_d"]),"answer":escape(data["answer"])}
    return json.dumps(update_question(id, data))

@question.route("/<int:id>", methods=["DELETE"])
def delete_question_route(id):
    current_question:dict = read_question(id)
    # check that the question exists
    if not current_question:
        abort(404)
    #check client is instructor for course prior to modification
    course_id = current_question.get("course_id")
    token = request.cookies.get("auth")
    if ( not _verify_instructor(token,course_id)):
        abort(400)
    delete_question(id)
    return "deleted", 204

@question.route("", methods=["GET"])
def get_question():
    return json.dumps(list_question())


def _verify_instructor(token,course_id):
    user:dict = get_user_by_token(token)
    selected_course:dict = read_course(course_id)
    if(user.get("id") not in selected_course.get("instructors")):
        return False
    return True