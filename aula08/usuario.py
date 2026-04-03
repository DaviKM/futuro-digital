import uvicorn
from fastapi import FastAPI

app = FastAPI()

#variaveis globais
dados = {

}
@app.get("/")
def index(nome, senha, email):
    usuario = {}
    global dados
    usuario["nome"] = nome
    usuario["senha"] = senha
    usuario["email"] = email

    dados[email] = usuario
    return usuario

@app.get("/usuarios")
def listar():
    return dados

if __name__ == "__main__":
    uvicorn.run("usuario:app", port=8002, reload=True)