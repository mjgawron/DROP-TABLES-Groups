import json
from flask import Blueprint, request, abort
from database.question import create_question, delete_question, list_question, read_question, update_question

question = Blueprint("question", __name__)

@question.route("", methods=["POST"])
def post_question_route():
    ### THIS IS NOT SAFE ###
    data = request.json
    return json.dumps(create_question(data)), 201

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
    if not read_question(id):
        abort(404)
    ### THIS IS NOT SAFE  ###
    data = request.json
    return json.dumps(update_question(id, data))

@question.route("/<int:id>", methods=["DELETE"])
def delete_question_route(id):
    # check that the question exists
    if not read_question(id):
        abort(404)
    delete_question(id)
    return "deleted", 204

@question.route("", methods=["GET"])
def get_question():
    return json.dumps(list_question())