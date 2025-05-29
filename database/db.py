livro_db = [{
    "id": 1,
    "titulo": "Entendendo Algoritmos",
    "autor": "Aditya Y. Bhargava",
    "ano_publicacao": 2005,
    "lido": True
}]


def add_livro(livro):
    livro_db.append(livro)
    return livro