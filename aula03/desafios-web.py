import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get("/area/{largura}/{altura}")
def area(largura, altura):
    largura = float(largura)
    altura = float(altura)

    areav = largura * altura

    return f"A área do terreno é {areav}"

@app.get("/moedas/{real}")
def converter(real):
    real = float(real)
    dolar = real / 5

    return f"R${real:.2f} equivale à US${dolar:.2f}"

@app.get("/dobrometade/{n}")
def dobrometade(n):
    n = float(n)

    return f"""Dobro: {n * 2}
    Triplo: {n * 3}
    Raiz: {n ** (1 / 2)}"""

@app.get("/")
def index():
    return "Página inicial"

if(__name__ == "__main__"):
    uvicorn.run("desafios-web:app", port=6000, reload=True)