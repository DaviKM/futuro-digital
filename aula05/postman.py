import uvicorn
from fastapi import FastAPI
from datetime import datetime

app = FastAPI()


@app.get("/postman")
def index(nome, senha, email, diaNasc, mesNasc, anoNasc):
    nome = nome.strip().title()
    senha = senha.strip()
    email = email.strip()
    diaNasc = int(diaNasc)
    mesNasc = int(mesNasc)
    anoNasc = int(anoNasc)
    email_validator = email.split("@")

    dia = int(datetime.now().strftime("%d"))
    mes = int(datetime.now().strftime("%m"))
    ano = int(datetime.now().strftime("%Y"))

    if len(senha.strip()) < 8:
        return "Senha inválida! Tente novamente"

    if len(email_validator) != 2 or email_validator[1].find(".") < 1 or email.startswith("@") or email.startswith(
            ".") or email.endswith("."):
        return "E-mail inválido! Tente novamente"

    if diaNasc < 1 or diaNasc > 31:
        return "Dia de nascimento invalido! Tente novamente"

    if mesNasc < 1 or mesNasc > 12:
        return "Mês de nascimento inválido! Tente novamente"

    if anoNasc > ano or mesNasc > mes and anoNasc >= ano or diaNasc > dia and mesNasc >= mesNasc and anoNasc >= ano:
        return "Data de nascimento invalido! Tente novamente"
    return "Cadastro validado!"


if __name__ == "__main__":
    uvicorn.run("postman:app", port=8000, reload=True)
