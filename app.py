from flask import Flask
from routes import blueprint
from flask_cors import CORS


app = Flask(__name__)


app.register_blueprint(blueprint)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
