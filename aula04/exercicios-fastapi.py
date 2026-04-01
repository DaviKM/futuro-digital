import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/rpg/{pontuacao}")
def rpg(pontuacao: int):
    if pontuacao > 1000:
        return "Você é uma lenda viva!"
    elif pontuacao > 500:
        return "Você é um mestre da aventura!"
    elif pontuacao > 100:
        return "Você é um aventureiro experiente!"
    else:
        return "Você é um iniciante!"


@app.get("/clima/{gc}")
def clima(gc: float):
    if gc > 25:
        return "Está quente, use roupas leves."
    elif gc > 15:
        return "O clima está agradável, aproveite o dia!"
    else:
        return "Está frio, leve um casaco."


@app.get("/senha/{senha}")
def senha(senha: str):
    if senha == "abracadabra":
        return "Acesso concedido!"
    else:
        return "Senha incorreta. Tente novamente"


@app.get("/validar/{idade}/{classificacao}")
def validar(idade:int, classificacao:int):
    idade = int(idade)
    if idade >= classificacao:
        return "Você pode assistir ao filme"
    else:
        return "Você não pode assistir ao filme"


# Bonus
@app.get("/validar/{idade}")
def validar_site_adulto(idade: int):
    if idade >= 18:
        return "Você pode assistir ao filme"
    else:
        return "Você não pode assistir ao filme"


@app.get("/vingador/{pontos}/{joia}")
def vingador(pontos: int, joia: bool):
    if pontos > 50 and joia == True:
        return "Você é um vingador supremo!"
    else:
        return "Seu poder é insuficiente."


@app.get("/adivinhe/{num}")
def adivinhe_numero(num: int):
    if num == 33:
        return "Parabéns! Você adivinhou o número!"
    else:
        return "Você errou. Tente de novo."


@app.get("/fruta/{fruta}")
def classificar(fruta: str):
    if fruta == "banana":
        return "A banana é uma das frutas mais consumidas no mundo!"
    elif fruta == "morango":
        return "O morango na verdade não é uma fruta e sim um pseudofruto!"
    return "Não conheço essa fruta, mas tenho certeza que é deliciosa!"

@app.get("/bissexto/{ano}")
def calcular_ano_bissexto(ano:int):
    if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
        return f"{ano} é um ano bissexto!"
    return f"{ano} não é um ano bissexto"

@app.get("/calcular-desconto/{valor}/{cupom}")
def calcular_desconto(valor:float, cupom:str):
    if cupom == "DESCONTO10":
        return f"Novo valor com o desconto de 10% -> R${valor - (valor*0.1):.2f}"
    elif cupom == "DESCONTO20":
        return f"Novo valor com o desconto de 20% -> R${valor - (valor*0.2):.2f}"
    else:
        return f"Valor final sem desconto -> {valor}"

if __name__ == "__main__":
    uvicorn.run("exercicios-fastapi:app", port=8080, reload=True)
