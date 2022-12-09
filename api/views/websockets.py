import json
from threading import Thread
from time import sleep
from flask import request
from database.submission import create_submission
from database.questions import disable_question, enable_question, read_question
from database.course import is_enrolled, is_instructor

from database.account import get_user_by_token


ws_rooms = {}

def websocket_handler(ws, id):
    token = request.cookies.get("auth")
    user:dict = get_user_by_token(token)
    join_room(id, ws)
    while True:
        rec_data = ws.receive()
        if rec_data == 'close':
            leave_room(id, ws)
            break
        decoded_data = json.loads(rec_data)
        course_id = read_question(id)["course_id"]
        if decoded_data["action"] == 'start' and is_instructor(user["id"], course_id):
            time = decoded_data['time']
            thread = Thread(target = timer, args=(time, id))
            thread.start()

        if decoded_data["action"] == 'submit' and is_enrolled(user["id"], course_id):
            save_data = {"user_id": user["id"], "question_id": id, "choice": decoded_data["choice"]}
            create_submission(save_data)

def broadcast(room, data):
    for connection in ws_rooms.get(room, set()):
        try:
            connection.send(data)
        except: 
            pass

def join_room(room, connection):
    ws_rooms[room] = ws_rooms.get(room, set())
    ws_rooms[room].add(connection)

def leave_room(room, connection):
    ws_rooms[room].remove(connection)

def timer(starting_second, room):
    enable_question(room)
    for rem in range(starting_second, -1, -1):
        broadcast(room, json.dumps({"action": "timer", "timeRemaining": rem}))
        sleep(1)
    disable_question(room)
    

