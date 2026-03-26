import uvicorn
from fastapi import FastAPI
from pydantic.v1.utils import to_lower_camel

app = FastAPI()


@app.get("/frete")
def frete(valor, estado: str):
    try:
        valor = float(valor.replace(',', '.'))
    except:
        return "Número inválido"
    valor_frete = 25
    estado = estado.lower().strip()
    print(estado)

    if estado == "sp":
        valor_frete = 200
    elif estado == "rj":
        valor_frete = 15
    return valor + valor_frete


@app.get("/")
def index():
    return {"Hello": "World"}


if __name__ == "__main__":
    uvicorn.run("frete:app", port=9000, reload=True)
