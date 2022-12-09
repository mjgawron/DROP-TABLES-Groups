import json
import bcrypt
from flask import Blueprint, make_response, request
import re
from database.account import create_account, add_auth_token, get_user_by_username, delete_token, get_user_by_token, edit_user


account = Blueprint("account", __name__)


@account.route("/login", methods=["POST"])
def post_login_route():
    data = request.json
    user = get_user_by_username(data["username"])
    if bcrypt.checkpw(data["password"].encode(), user["password"]):
        resp = make_response("success")
        resp.set_cookie("auth", add_auth_token(user["id"]), max_age=31556952, httponly=True)
        return resp
    return "failed", 401

@account.route("/register", methods=["POST"])
def post_register_route():
    
    data = request.json
    if not ("username" in data and "password" in data and "name" in data):
        return "missing information", 400

    # check username
    if len(data["username"]) < 4 or re.fullmatch("[a-zA-Z0-9]*", data["username"]) is None or get_user_by_username(data["username"]):
        return "invalid username", 400

    # check password
    if len(data["password"]) < 8:
        return "invalid password", 400
    
    # check name
    if len(data["name"]) == 0 or re.fullmatch("[a-zA-Z ]*", data["name"]) is None:
        return "invalid name", 400

    save_data = {"username": data["username"], "name": data["name"], "password": bcrypt.hashpw(data["password"].encode(), bcrypt.gensalt())}

    user_id = create_account(save_data)

    resp = make_response("success")
    resp.set_cookie("auth", add_auth_token(user_id), max_age=31556952, httponly=True)
    return resp

@account.route("/",methods=["PUT"])
def change_account():
    token = request.cookies.get("auth")
    data = request.json
    if not ("name" in data):
        return "missing information", 400
    if len(data["name"]) == 0 or re.fullmatch("[a-zA-Z ]*", data["name"]) is None:
        return "invalid name", 400
    user:dict = get_user_by_token(token)
    user_id = user.get("id")
    edit_user({"name":data.get("name")},user_id)
    return "success", 200

@account.route("/logout", methods=["POST"])
def post_logout_route():
    token = request.cookies.get("auth")
    if token:
        delete_token(token)
    resp = make_response("success")
    resp.set_cookie("auth", "", 0)
    return resp
    

@account.route("/status", methods=["GET"])
def get_status_route():
    token = request.cookies.get("auth")
    if token:
        result = get_user_by_token(token)
        if result:
            return json.dumps(result)
    return "failed", 401
