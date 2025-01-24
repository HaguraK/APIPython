from flask import Blueprint, jsonify, request
from app.models import Book

books = [
    {
        'id': 1,
        'titulo': 'O Senhor dos Aneis - A Sociedade do Anel',
        'autor': 'J.R.R Tolkien'
    },
    {
        'id': 2,
        'titulo': 'Harry Potter e a Pedra Filosofal',
        'autor': 'J.K Howling'
    },
    {
        'id': 3,
        'titulo': 'James Clear',
        'autor': 'Habitos Atomicos',
    },
]

books_bp = Blueprint('books_bp', __name__)

# Consultar (todos)
@books_bp.route('/books',methods=['GET'])
def obter_livros():
    return jsonify(books)

# Consultar (id)
@books_bp.route('/books/<int:id>',methods=['GET'])
def obter_livros_por_id(id):
    for livro in books:
        if livro.get('id') == id:
            return jsonify(livro)
# Editar
@books_bp.route('/books/<int:id>',methods=['PUT'])
def editar_livro_por_id(id):
    livro_alterado = request.get_json()
    for indice,livro in enumerate(books):
        if livro.get('id') == id:
            books[indice].update(livro_alterado)
            return jsonify(books[indice])
# Criar
@books_bp.route('/books',methods=['POST'])
def incluir_novo_livro():
    novo_livro = request.get_json()
    books.append(novo_livro)

    return jsonify(books)
# Excluir
@books_bp.route('/books/<int:id>',methods=['DELETE'])
def excluir_livro(id):
    for indice, livro in enumerate(books):
        if livro.get(id) == id:
            del books[indice]

    return jsonify(books)