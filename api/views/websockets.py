ws_rooms = {}

def broadcast(room, data):
    for connection in ws_rooms[room]:
        connection.send(data)

def join_room(room, connection):
    ws_rooms[room] = ws_rooms.get(room, set()).add(connection)

def leave_room(room, connection):
    ws_rooms[room].remove(connection)

