import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def index(senha:str):
    validacoes = []

    if not 6 <= len(senha)<= 10 :
        validacoes.append("Tamanho inválido")

    if senha.find('#') == -1 :
        validacoes.append("Senha não possui #")

    if len(validacoes) > 0:
        return validacoes

    return f"Senha valida"

if __name__ == "__main__":
    uvicorn.run("validar-senha:app", port=7000, reload=True)