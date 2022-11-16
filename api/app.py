from flask import Flask
from views.course import course
from views.account import account

app = Flask(__name__)

# enable cors for debug only
if app.debug:
    from flask_cors import CORS
    CORS(app)

# Register each blueprint with its prefix
app.register_blueprint(course, url_prefix="/api/course")
app.register_blueprint(account, url_prefix="/api/account")



if __name__ == '__main__':
    app.run("0.0.0.0", 5000, use_reloader=False)
