import json
from flask import Blueprint, request, abort
from database.submission import list_submission, read_submission, read_submission_course, create_submission, delete_submission, update_submission, read_user_submissions, already_submitted, read_submission_student
from database.questions import read_question, read_question_ids_course
from database.course import is_member, is_enrolled, is_instructor, read_course
from database.account import get_user_by_token

submission = Blueprint("submission",__name__)

@submission.route("/<int:course_id>/grades",methods=["GET"])
def get_course_grades(course_id):
    #if instructor returns list of dicts [{student_id: id, score_list: {question_id: correctness}} . . .]
    #else returns list of singular dict  [{student_id: id, score_list: {question_id: correctness}} . . .] for that student
    user:dict = get_user_by_token(request.cookies.get("auth"))
    user_id = user.get("id")


    if not is_member(user_id,course_id):
        abort(400)
        
    instructor_status = is_instructor(user_id,course_id)
    course:dict = read_course(course_id)

    if instructor_status:
        roster = course.get("students")
        question_ids = read_question_ids_course(course_id)
        gradeList = []
        for student_id in roster:
            score_list = []
            for question_id in question_ids:
                chosen_correctly = False
                if already_submitted(student_id,question_id):
                    student_submission:dict = read_submission_student(student_id,question_id)
                    chosen_correctly = student_submission.get("correct")
                score_list.append({"correctness":chosen_correctly,"question_id":question_id})
            gradeList.append({"student_id":student_id,"score_list":score_list})
        return gradeList
    
    else:
        student_id = user_id
        question_ids = read_question_ids_course(course_id)
        gradeList = []
        
        score_list = []
        for question_id in question_ids:
            chosen_correctly = False
            if already_submitted(student_id,question_id):
                student_submission:dict = read_submission_student(student_id,question_id)
                chosen_correctly = student_submission.get("correct")
            score_list.append({"correctness":chosen_correctly,"question_id":question_id})
        gradeList.append({"student_id":student_id,"score_list":score_list})
        return gradeList