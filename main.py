from flask import Flask
from flasgger import Swagger
from config import configure_all
# from routes.usuario import usuario_route
# from routes.home import home_route

# from models.user import db, User

app = Flask(__name__)

# app.register_blueprint(home_route)
# app.register_blueprint(usuario_route)

swagger = Swagger(app)

configure_all(app)


if __name__ == '__main__':
    app.run(debug=True)