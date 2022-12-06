import json
from flask import Blueprint, request, abort
from database.submission import list_submission, read_submission, read_submission_course, create_submission, delete_submission, update_submission, read_user_submissions

submission = Blueprint("submission",__name__)