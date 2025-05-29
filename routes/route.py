from fastapi import APIRouter
from pydantic import BaseModel
from typing import Optional, List

from database.db import livro_db

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
    pass


@appRouter.put("/atualizarlivro/{id}")
def atualizar_livro(id: int):
    pass


@appRouter.delete("/deletarlivro/{id}")
def deletar_livro(id: int):
    pass