import hashlib
from random import choices
import string
from database.database import db, get_next_id


def create_account(data):
    id = get_next_id("account")
    internal_data = {**data, "id": id, "deleted": False}
    db["accounts"].insert_one(internal_data)
    return id

def add_auth_token(user_id):
    token = ''.join(choices(string.ascii_letters + string.digits, k=120))
    hashed = hashlib.sha256(token.encode()).hexdigest()
    db["accounts"].update_one({'id': user_id}, { '$push': { 'token': hashed } })
    return token

def get_user_by_token(token):
    hashed = hashlib.sha256(token.encode()).hexdigest()
    result = db["accounts"].find_one({"token": hashed, "deleted": False}, {"_id": 0, "deleted": 0, "password": 0})
    return result

def get_user_by_username(username):
    result = db["accounts"].find_one({"username": username, "deleted": False}, {"_id": 0, "deleted": 0})
    return result

def delete_token(token):
    hashed = hashlib.sha256(token.encode()).hexdigest()
    db["accounts"].update_one({'token': hashed}, { '$pull': { 'token': hashed } })




def read_account(id):
    pass

def update_account(id, data):
    db["accounts"].update_one({"id": id}, {"$set": data})
    return read_account(id)

def delete_account(id):
    db["accounts"].update_one({"id": id}, {"$set": {"deleted": True}})
