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
def info_usuario(usuario_id):
    """ exibir informações do usuário """
    
    usuario = list(filter(lambda user: user['id'] == usuario_id, USUARIOS)) [0]
    
    return render_template('info_usuario.html', usuario=usuario)


@usuario_route.route('/<int:usuario_id>/edit')
def edit_usuario(usuario_id):
    """ formulário para editar um usuário """
    
    usuario = None
    for user in USUARIOS:
        if user['id'] == usuario_id:
            usuario = user
    
    return render_template('new_usuario.html', usuario=usuario)


@usuario_route.route('/<int:usuario_id>/update', methods=['PUT'])
def atualizar_usuario(usuario_id):
    """ Atualizar informações de um usuário """
    usuario_atualizado = None
    # obter dados do formulario de edicao
    data = request.json
    
    # obter usuario pelo id
    
    for user in USUARIOS:
        if user['id'] == usuario_id:
            user['nome'] = data['nome']
            user['email'] = data['email']
            
            usuario_atualizado  = user
    
    # editar usuario
    return render_template('item_usuario.html', usuario=usuario_atualizado)
    
    

@usuario_route.route('/<int:usuario_id>/delete', methods=['DELETE'])
def deletar_usuario(usuario_id):
    global USUARIOS
    USUARIOS = [ user for user in USUARIOS if user['id'] != usuario_id ]
    
    return {'deleted': 'ok'}
    

    


