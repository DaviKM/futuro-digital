import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def index(email):
    email = email.strip()
    endereco = email.split("@")

    logs = []

    if len(endereco) == 1:
        logs.append("Um e-mail válido deve conter um @")
    else:
        if endereco[1].find(".") == -1:
            logs.append("O e-mail deve ter pelo menos um . após o @")

        if endereco[1].find(".") == 0:
            logs.append("Deve haver algum caractere entre o @ e o .")

    if len(endereco) > 2:
        logs.append("O e-mail deve ter apenas um @")
    if email.startswith("@"):
        logs.append("O e-mail não pode começar com @")
    if email.endswith("@"):
        logs.append("O e-mail não pode terminar com @")

    if email.startswith("."):
        logs.append("O e-mail não pode começar com .")
    if email.endswith("."):
        logs.append("O e-mail não pode terminar com .")

    if len(logs) > 0:
        return logs
    return "E-mail válido"


if __name__ == "__main__":
    uvicorn.run("validar-email:app", port=7001, reload=True)
