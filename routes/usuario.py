from flask import Blueprint, render_template, request, jsonify
from database.models.usuario import Usuario

usuario_route = Blueprint('usuario', __name__)

@usuario_route.route('/', methods=['GET'])
def lista_usuarios():
    """
    Lista todos os usuários.
    ---
    responses:
      200:
        description: Lista de usuários.
    """
    usuarios = Usuario.select()
    content_type = request.headers.get('Accept')
    if 'application/json' in content_type:
        return jsonify([{'id': usuario.id, 'nome': usuario.nome, 'email': usuario.email} for usuario in usuarios])
    else:
        return render_template('lista_usuarios.html', usuarios=usuarios)

@usuario_route.route('/', methods=['POST'])
def inserir_usuario():
    """
    Insere um novo usuário.
    ---
    parameters:
      - in: body
        name: user
        description: Dados do usuário a serem inseridos.
        required: true
        schema:
          type: object
          properties:
            nome:
              type: string
              description: Nome do usuário.
            email:
              type: string
              format: email
              description: Endereço de e-mail do usuário.
    responses:
      200:
        description: Usuário inserido com sucesso.
    """
    data = request.json
    novo_usuario = Usuario.create(nome=data['nome'], email=data['email'])
    return render_template('item_usuario.html', usuario=novo_usuario)

# Rotas /new, /<int:usuario_id>, /<int:usuario_id>/edit e /<int:usuario_id>/delete podem ser documentadas de forma semelhante

@usuario_route.route('/new')
def new_usuario():
    """
    Exibe o formulário para criar um novo usuário.
    """
    return render_template('new_usuario.html')

@usuario_route.route('/<int:usuario_id>')
def info_usuario(usuario_id):
    """
    Exibe informações de um usuário específico.
    ---
    parameters:
      - in: path
        name: usuario_id
        description: ID do usuário a ser exibido.
        required: true
        type: integer
    responses:
      200:
        description: Detalhes do usuário.
      404:
        description: Usuário não encontrado.
    """
    usuario = Usuario.get_by_id(usuario_id)
    return render_template('info_usuario.html', usuario=usuario)

@usuario_route.route('/<int:usuario_id>/edit')
def edit_usuario(usuario_id):
    """
    Exibe o formulário para editar um usuário.
    ---
    parameters:
      - in: path
        name: usuario_id
        description: ID do usuário a ser editado.
        required: true
        type: integer
    responses:
      200:
        description: Formulário de edição do usuário.
      404:
        description: Usuário não encontrado.
    """
    usuario = Usuario.get_by_id(usuario_id)
    return render_template('new_usuario.html', usuario=usuario)

@usuario_route.route('/<int:usuario_id>/update', methods=['PUT'])
def atualizar_usuario(usuario_id):
    """
    Atualiza as informações de um usuário.
    ---
    parameters:
      - in: path
        name: usuario_id
        description: ID do usuário a ser atualizado.
        required: true
        type: integer
      - in: body
        name: user
        description: Dados atualizados do usuário.
        required: true
        schema:
          type: object
          properties:
            nome:
              type: string
              description: Novo nome do usuário.
            email:
              type: string
              format: email
              description: Novo endereço de e-mail do usuário.
    responses:
      200:
        description: Informações do usuário atualizadas com sucesso.
      404:
        description: Usuário não encontrado.
    """
    data = request.json
    usuario_atualizado  = Usuario.get_by_id(usuario_id)
    if usuario_atualizado:
        usuario_atualizado.nome = data['nome']
        usuario_atualizado.email = data['email']
        usuario_atualizado.save()
        return render_template('item_usuario.html', usuario=usuario_atualizado)
    else:
        return jsonify({'error': 'User not found'}), 404

@usuario_route.route('/<int:usuario_id>/delete', methods=['DELETE'])
def deletar_usuario(usuario_id):
    """
    Deleta um usuário.
    ---
    parameters:
      - in: path
        name: usuario_id
        description: ID do usuário a ser deletado.
        required: true
        type: integer
    responses:
      200:
        description: Usuário deletado com sucesso.
      404:
        description: Usuário não encontrado.
    """
    usuario = Usuario.get_by_id(usuario_id)
    if usuario:
        usuario.delete_instance()
        return {'message': 'User deleted successfully'}
    else:
        return jsonify({'error': 'User not found'}), 404