import uvicorn
from fastapi import FastAPI

usuarios = {}
app = FastAPI()

@app.get("/criar-usuario")
def criar_usuario(id, nome, idade, email, cidade):
    usuario = {
        'id': id,
        'nome': nome,
        'idade': idade,
        'email': email,
        'cidade': cidade
    }

    usuarios[id] = usuario
    return usuario
@app.get("/perfil/{id}")
def perfil_usuario(id):
    usuario = usuarios[id]

    return usuario

@app.get("/todos")
def todos():
    return usuarios

if __name__ == '__main__':
    uvicorn.run("perfil_usuario:app", port=9002, reload=True)