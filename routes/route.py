from fastapi import APIRouter
from pydantic import BaseModel
from typing import Optional, List

from database.db import livro_db,add_livro

appRouter = APIRouter()

class Livro(BaseModel):
    id: int
    titulo:str
    autor:str
    ano_publicacao:int
    lido:Optional[bool] = False


@appRouter.get("/listarlivros", response_model=List[Livro])
def livros():
    return livro_db 

    
@appRouter.post("/adicionarlivro")
def adicionar_livro(livro: Livro):
    try:
        livro_dict = livro.dict()
        novo_livro = add_livro(livro_dict)
        return {"mensagem": "Livro adicionado com sucesso", "livro": novo_livro}
    except Exception as erro:
        return {"mensagem": erro}


@appRouter.put("/atualizarlivro/{id}")
def atualizar_livro(id: int, livro: Livro):  
    for i, l in enumerate(livro_db):
        if l["id"] == id:
            livro_db[i] = livro.dict() 
            return {"mensagem": "Livro atualizado com sucesso", "livro": livro_db[i]}
    return {"erro": "Livro não encontrado"}



@appRouter.delete("/deletarlivro/{id}")
def deletar_livro(id: int):
    for i, l in enumerate(livro_db):
        if l["id"] == id:
            livro_db.pop(i)
            return {"mensagem": "Livro deletado com sucesso"}
    return {"erro": "Livro não encontrado"}
