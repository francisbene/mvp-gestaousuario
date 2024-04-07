from routes.home import home_route
from routes.usuario import usuario_route
from database.database import db
from database.models.usuario import Usuario
#from flasgger import Swagger


def configure_all(app):
    configure_routes(app)
    configure_db()
    # configure_swagger(app)


def configure_routes(app):
    app.register_blueprint(home_route)
    app.register_blueprint(usuario_route, url_prefix='/usuarios')

def configure_db():
    db.connect()
    db.create_tables([Usuario])

# def configure_swagger(app):
#     swagger = Swagger(app, template_file='swagger.yml')

