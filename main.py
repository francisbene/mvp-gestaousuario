from flask import Flask
from routes.home import home_route #importando a variavel home de home.py
from routes.usuario import usuario_route


# inicializacao
app = Flask(__name__)

 #registrando o app
app.register_blueprint(home_route)
app.register_blueprint(usuario_route, url_prefix='/usuarios')

# execucao
app.run(debug=True)

