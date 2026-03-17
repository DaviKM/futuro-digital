# Dependências
import uvicorn
from fastapi import FastAPI

app = FastAPI()  # Criando a aplicação em memória


@app.get("/temperatura/{temp}")
def temperatura(temp):
    temp = float(temp)

    if temp > 35:
        return "Muito quente!"
    elif temp > 20:
        return "Agradável"
    else:
        return "Frio"


@app.get("/saudar/{n}")
def nome(n):
    saudacao = f"Seu nome é {n}"
    print(saudacao)
    return saudacao


@app.get("/")  # atalho para essa função (determinado pela rota)
def index():
    print("oiiii")
    nome("joão")
    return "roblox"


if __name__ == "__main__":  # Testa se é execução python
    uvicorn.run("meu-primeiro-app-web.py:app", port=5000, reload=True)
