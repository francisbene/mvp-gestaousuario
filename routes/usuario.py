from flask import Blueprint, render_template, request
from database.usuario import USUARIOS

usuario_route = Blueprint('usuario', __name__)

@usuario_route.route('/')
def lista_usuarios():
    """ Listar usuários """
    return render_template('lista_usuarios.html', usuarios=USUARIOS)
    

@usuario_route.route('/', methods=['POST'])
def inserir_usuario():
    """ inserir os dados do usuário no formulário """
   
    data = request.json
    
    novo_usuario = {
        "id": len(USUARIOS) +1,
        "nome": data['nome'],
        "email": data['email'],
    }
    
    USUARIOS.append(novo_usuario)
    
    return render_template('item_usuario.html', usuario=novo_usuario)

@usuario_route.route('/new')
def new_usuario():
    """ inserir novo usuário no formulário """
    return render_template('new_usuario.html')

@usuario_route.route('/<int:usuario_id>')
def info_usuario(cliente_id):
    """ exibir informações do usuário """
    return render_template('info_usuario.html')

@usuario_route.route('/<int:usuario_id>/edit')
def edit_usuario(cliente_id):
    """ formulário para editar um usuário """
    return edit_usuario('edit_usuario.html')

@usuario_route.route('/<int:usuario_id>/update', methods=['PUT'])
def atualizar_usuario(cliente_id):
    """ Atualizar informações de um usuário """
    pass

@usuario_route.route('/<int:usuario_id>/delete', methods=['DELETE'])
def deletar_usuario(cliente_id):
    """ Deletar usuário """
    pass

    



