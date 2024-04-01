from flask import Blueprint, render_template, request
from database.models.usuario import Usuario

usuario_route = Blueprint('usuario', __name__)

@usuario_route.route('/')
def lista_usuarios():
    """ Listar usuários """
    usuarios = Usuario.select()
    return render_template('lista_usuarios.html', usuarios=usuarios)

@usuario_route.route('/', methods=['POST'])
def inserir_usuario():
    """ inserir os dados do usuário no formulário """

    data = request.json

    novo_usuario = Usuario.create(
        nome=data['nome'],
        email=data['email'],
    )

    return render_template('item_usuario.html', usuario=novo_usuario)

@usuario_route.route('/new')
def new_usuario():
    """ inserir novo usuário no formulário """
    return render_template('new_usuario.html')


@usuario_route.route('/<int:usuario_id>')
def info_usuario(usuario_id):
    """ exibir informações do usuário """
<<<<<<< HEAD
    
    usuario = list(filter(lambda user: user['id'] == usuario_id, USUARIOS)) [0]
    
=======

    usuario = Usuario.get_by_id(usuario_id)

>>>>>>> d8b5f562f9b21949b0c65d9685c24a2e60b6423c
    return render_template('info_usuario.html', usuario=usuario)


@usuario_route.route('/<int:usuario_id>/edit')
def edit_usuario(usuario_id):
    """ formulário para editar um usuário """
<<<<<<< HEAD
    
    usuario = None
    for user in USUARIOS:
        if user['id'] == usuario_id:
            usuario = user
    
=======

    usuario = Usuario.get_by_id(usuario_id)

>>>>>>> d8b5f562f9b21949b0c65d9685c24a2e60b6423c
    return render_template('new_usuario.html', usuario=usuario)


@usuario_route.route('/<int:usuario_id>/update', methods=['PUT'])
def atualizar_usuario(usuario_id):
    """ Atualizar informações de um usuário """
<<<<<<< HEAD
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
    

    
=======

    data = request.json

    usuario_atualizado  = Usuario.get_by_id(usuario_id)
    usuario_atualizado.nome = data['nome']
    usuario_atualizado.email = data['email']
    usuario_atualizado.save()

    return render_template('item_usuario.html', usuario=usuario_atualizado)

@usuario_route.route('/<int:usuario_id>/delete', methods=['DELETE'])
def deletar_usuario(usuario_id):
    usuario = Usuario.get_by_id(usuario_id)
    usuario.delete_instance()
    return {'deleted': 'ok'}



>>>>>>> d8b5f562f9b21949b0c65d9685c24a2e60b6423c



