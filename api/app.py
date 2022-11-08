from flask import Flask
from flask_sock import Sock
from views.course import course
from views.question import question

app = Flask(__name__)
app.config['SOCK_SERVER_OPTIONS'] = {'ping_interval': 25}

sock = Sock(app)

# enable cors for debug only
if app.debug:
    from flask_cors import CORS
    CORS(app)

# Register each blueprint with its prefix
app.register_blueprint(course, url_prefix="/api/course")
app.register_blueprint(question, url_prefix="/api/question")

@sock.route('/api/ws/<int:id>')
def ws_handler(ws, id):
    print(id)
    while True:
        data = ws.receive()
        if data == 'close':
            break
        ws.send(data)


if __name__ == '__main__':
    app.run("0.0.0.0", 5000, use_reloader=False)
