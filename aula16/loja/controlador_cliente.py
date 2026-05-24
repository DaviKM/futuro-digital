from fastapi import APIRouter
from sqlalchemy import create_engine, text

router = APIRouter(prefix="/cliente", tags=["Clientes"])
DATABASE_URL = 'postgresql://postgres:123@localhost:5432/loja'

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