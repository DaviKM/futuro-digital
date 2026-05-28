from fastapi import APIRouter
from sqlalchemy import create_engine, text
from pydantic import BaseModel

router = APIRouter(prefix="/cliente", tags=["Clientes"])
DATABASE_URL = 'postgresql://postgres:123@localhost:5432/loja'

class Id(BaseModel):
    id: int

@router.get("/cadastrar")
def cadastrar_cliente(nome, email, cidade):
    engine = create_engine(DATABASE_URL)

    try:
        with engine.begin() as con:
            sql = "INSERT INTO clientes (nome_cliente, email, cidade) VALUES (:nome, :email, :cidade)"
            dados = {
                "nome": nome,
                "email": email,
                "cidade": cidade
            }
            con.execute(text(sql), dados)
            return 'Cliente cadastrado com sucesso!'
    except Exception as erro:
        return erro

@router.post("/buscar")
def buscar(id : Id):
    engine = create_engine(DATABASE_URL)
    try:
        with engine.connect() as conn:
            sql = f"SELECT id,nome_produto,preco FROM public.produtos WHERE id = :id"
            dados = {
                'id': id.id
            }

            result = conn.execute(text(sql), dados)
            prod = result.fetchone()
            return prod._mapping #atalho
    except Exception as e:
        return e
