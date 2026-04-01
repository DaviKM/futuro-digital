import uvicorn
from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def index(email):
    endereco = email.split("@")
    logs = []

    if len(endereco) != 2:
        logs.append("O e-mail deve ter apenas um @")
    if endereco[1].find(".")  == -1 :
            logs.append("O e-mail deve ter pelo menos um . após o arroba")
    if endereco[1].find(".") == 0:
            logs.append("Deve haver algum caractere entre o @ e o .")




if __name__ == "__main__":
    uvicorn.run("validar_email:app", port=4000, reload=True)