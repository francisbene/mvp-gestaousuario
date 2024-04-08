from routes.home import home_route
from routes.usuario import usuario_route
from database.database import db
from database.models.usuario import Usuario


def configure_all(app):
    configure_routes(app)
    configure_db()


def configure_routes(app):
    app.register_blueprint(home_route)
    app.register_blueprint(usuario_route, url_prefix='/usuarios')

def configure_db():
    db.connect()
    db.create_tables([Usuario])



