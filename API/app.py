# Api - É um lugar para disponibilizar recursos e/ou funcionalidades
# 1 - objetivo - Criar um api que disponibiliza a consulta, criação, edição e exclusão de livros.
# 2 - url Base - localhost.com -
# 3 - endpoints -
# - localhost/livros (GET)
# - Localhost/livros/id (GET)
# - localhost/livros/id (PUT)
# - localhost/livros/id (DELETE)
# 4 - Quais recurso - Livros
from flask import Flask, jsonify, request

app = Flask(__name__)

livros = [
    {
        'id': 1,
        'título': 'O Senhor dos Anéis - A sociedade do Anel',
        'autor': 'J.R.R Tolkien'
    },
    {
        'id': 2,
        'título': 'Harry Potter e a Pedra filosofal',
        'autor': 'J.K Howling'
    },
    {
        'id': 3,
        'título': 'Hábitos Atômicos',
        'autor': 'James Clear'
    },
]

# consultar(todos)


@app.route('/livros', methods=['GET'])
def obter_livros():
    return jsonify(livros)
# consultar(id)


@app.route('/livros/<int:id>', methods=['GET'])
def obter_livros_por_id(id):
    for livro in livros:
        if livro.get('id') == id:
            return jsonify(livro)
# Editar


@app.route('/livros/<int:id>', methods=['PUT'])
def editar_livros_por_id(id):
    livro_alterado = request.get_json()
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            livros[indice].update(livro_alterado)
            return jsonify(livros[indice])
# Criar


@app.route('/livros', methods=['POST'])
def incluir_novo_livro():
    novo_livro = request.get_json()
    livros.append(novo_livro)

    return jsonify(livros)

# # excluir


@app.route('/livros/<int:id>', methods=['DELETE'])
def exluir_livro(id):
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            del livros[indice]

    return jsonify(livros)


app.run(port=5000, host='localhost', debug=True)
