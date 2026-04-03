import uvicorn
from fastapi import FastAPI

app = FastAPI()

curriculos = {}


@app.get("/curriculo")
# Validações:
# O nome deve ter no mínimo 3 caracteres.
# A idade deve estar entre 18 e 65 anos.
# O salário deve ser maior que zero.
# O nome do arquivo deve obrigatoriamente terminar com .pdf (Dica: use .endswith('.pdf')).
def curriculo(nome: str, idade: int, sal: float, arquivo: str):
    global curriculo
    nome = nome.strip()
    log = []
    usuario = {}
    usuario["nome"] = nome
    usuario["idade"] = idade
    usuario["salario"] = sal
    usuario["arquivo"] = arquivo

    if len(nome) < 3:
        log.append("O nome deve ter no mínimo 3 caracteres")
    if not 18 <= idade <= 65:
        log.append("O idade deve estar entre 18 e 65")
    if sal <= 0:
        log.append("O salário deve ser maior que zero")
    if not arquivo.endswith(".pdf"):
        log.append("O arquivo deve ser um PDF")

    if len(log) > 0:
        return log

    curriculos[nome] = usuario
    return "Currículo válido"


@app.get("/ler-curriculos")
def ler_curriculos():
    return curriculos


@app.get("/produto")
# Validações:
# O nome do produto não pode ser vazio.
# O preço deve ser um valor positivo.
# A quantidade em estoque não pode ser negativa (zero é permitido).
# A categoria deve ser exatamente uma destas três: "Eletrônicos", "Alimentos" ou "Vestuário".
def produto(nome, preco, quant: int, cat):
    log = []

    nome = nome.strip()
    cat = cat.strip().capitalize()

    try:
        preco = float(preco.replace(',', '.'))
        if preco <= 0:
            log.append("O preço deve ser um valor positivo")
    except:
        log.append("O preço deve ser um número")

    if len(nome) == 0:
        log.append("O nome não pode ser vazio")
    if quant < 0:
        log.append("O quantidade não pode ser negativa")
    if cat != "Eletrônicos" and cat != "Alimentos" and cat != "Vestuário":
        log.append('A categoria deve ser uma destas três: "Eletrônicos", "Alimentos" ou "Vestuário"')

    if len(log) > 0:
        return log

    else:
        return "Produto válido"


if __name__ == "__main__":
    uvicorn.run("reforco:app", port=8001, reload=True)
