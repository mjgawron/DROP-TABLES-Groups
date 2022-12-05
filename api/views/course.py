import json
from flask import Blueprint, request, abort
from database.course import create_course, read_course, update_course, delete_course, list_course
from database.questions import create_question, read_question, read_question_course, update_question, delete_question, list_question


course = Blueprint("course", __name__)


@course.route("", methods=["POST"])
def post_course_route():
    ### THIS IS NOT SAFE ###
    data = request.json
    return json.dumps(create_course(data)), 201

@course.route("/<int:id>", methods=["GET"])
def get_course_detail_route(id):
    result = read_course(id)
    # check that the course exists
    if not result:
        abort(404)
    return json.dumps(result)

@course.route("/<int:id>", methods=["PUT"])
def put_course_route(id):
    # check that the course exists
    if not read_course(id):
        abort(404)
    ### THIS IS NOT SAFE  ###
    data = request.json
    return json.dumps(update_course(id, data))

@course.route("/<int:id>", methods=["DELETE"])
def delete_course_route(id):
    # check that the course exists
    if not read_course(id):
        abort(404)
    delete_course(id)
    return "deleted", 204

@course.route("", methods=["GET"])
def get_course():
    return json.dumps(list_course())

@course.route("/<int:id>/questions",methods=["GET"])
def get_course_detail_question_route(id):
    return json.dumps(read_question_course(id))