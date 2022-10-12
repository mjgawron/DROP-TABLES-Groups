from flask import Flask
from views.course import course


app = Flask(__name__)

# Register each blueprint with its prefix
app.register_blueprint(course, url_prefix="/course")


if __name__ == '__main__':
    app.run("0.0.0.0", 5000)
