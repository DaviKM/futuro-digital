import uvicorn
from fastapi import FastAPI
from sqlalchemy import create_engine, text

app = FastAPI()
DATABASE_URL = 'postgresql://postgres:123@localhost:5432/loja'

@app.get("/cadastrar-cliente")
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

if __name__ == "__main__":
    uvicorn.run("loja:app", port=16000, reload=True)