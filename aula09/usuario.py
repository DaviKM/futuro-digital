import uvicorn
from fastapi import FastAPI

app = FastAPI()

# variaveis globais
dados = {}  # fora da função


@app.get('/usuario')
def cadastrar_usuario(nome, senha, email):
    # validações
    global dados

    # definição do dicionário
    usuario = {
        'data_cadastro': '2024-06-01',
        'endereco': []
    }

    # alteração do dicionário
    usuario['nome'] = nome
    usuario['senha'] = senha
    usuario['email'] = email

    # vinculo com o mapa global
    dados[email] = usuario

    return usuario


@app.get("/adicionarEndereco")
def adicionar_endereco(email, rua, numero, cidade, estado):
    global dados

    # criei o meu dicionario/objeto para endereço
    endereco = {
        'rua': rua,
        'numero': numero,
        'cidade': cidade,
        'estado': estado
    }

    # recuperei o usuario
    usuario = dados[email]

    # alterei o endereco do usuario
    usuario['endereco'].append(endereco)


@app.get("/usuarios")
def todos_usuarios():
    return dados


if __name__ == "__main__":
    uvicorn.run(
        "usuario:app",
        port=9001,
        reload=True
    )
