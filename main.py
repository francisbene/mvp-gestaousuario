from flask import Flask
from flasgger import Swagger
from config import configure_all

app = Flask(__name__)

swagger = Swagger(app)

configure_all(app)


if __name__ == '__main__':
    app.run(debug=True)