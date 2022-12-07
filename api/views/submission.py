import json
from flask import Blueprint, request, abort
from database.submission import list_submission, read_submission, read_submission_course, create_submission, delete_submission, update_submission, read_user_submissions
from views.account import get_user_by_token

submission = Blueprint("submission",__name__)

@submission.route("",methods=["POST"])
def post_submission_route():
    data = request.json

    course_id = data["course_id"]
    question_id = data["question_id"]

    token = request.cookies.get("auth")
    user:dict = get_user_by_token(token)


@submission.route("/<int:course_id>/grades",methods=["GET"])
def get_course_grades():
    #if instructor returns list of dicts [{student_id: {question_id: correctness}}]
    return
