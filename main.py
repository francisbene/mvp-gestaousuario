from flask import Flask
from flasgger import Swagger
from flask_cors import CORS
from config import configure_all

app = Flask(__name__)

swagger = Swagger(app)

CORS(app)

configure_all(app)


if __name__ == '__main__':
    app.run(debug=True)