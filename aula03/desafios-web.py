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


@app.get("/maioridade/{idade}")
def maioridade(idade: int):
    if idade >= 18:
        return "Você é maior de idade"
    else:
        return "Você é menor de idade"


@app.get("/par-ou-impar/{n}")
def par_impar(n: int):
    if n % 2 == 0:
        return "É par"
    else:
        return "É impar"


@app.get("/login/{login}")
def logar(login: str):
    senha = "python123"

    if senha == login:
        return "Acesso permitido"
    else:
        return "Acesso negado"


@app.get("/termometro/{temp}")
def termometro(temp: float):
    if temp > 35:
        return "Muito quente!"
    elif temp > 20:
        return "Agradável"
    else:
        return "Frio"


@app.get("/notas/{nota}")
def notas(nota: float):
    if nota >= 7:
        return "Aprovado"
    elif nota >= 5:
        return "Recuperação"
    else:
        return "Reprovado"


@app.get("/maior/{n1}/{n2}")
def maior(n1: float, n2: float):
    if n1 > n2:
        return f"{n1} é o maior"
    elif n1 < n2:
        return f"{n2} é o maior"
    else:
        return "Eles são iguais"


@app.get("/radar/{velocidade}")
def radar(velocidade: float):
    if velocidade > 80:
        km_excedente = velocidade - 80
        valor_multa = km_excedente * 5
        return f"Valor da multa: {valor_multa:.2f}"
    return "Sem multa"


@app.get("imc/{altura}/{peso}")
def cimc(altura: float, peso: float):
    imc = peso / (altura * altura)

    if imc < 18.5:
        return "Baixo peso"
    elif imc < 25:
        return "Peso ideal"
    elif imc < 30:
        return "Sobrepeso"
    else:
        return "Obesidade"


@app.get("aumento/{sal}")
def aumento(sal: float):
    if sal < 1500:
        novo_sal = sal + (sal * 0.15)
    else:
        novo_sal = sal + (sal * 0.1)

    return f"Novo salário: {novo_sal:.2f}"


@app.get("/triangulos/{l1}/{l2}/{l3}")
def triangulos(l1: float, l2: float, l3: float):
    if (l1 + l2 + l3 - max(l1, l2, l3)) > max(l1, l2, l3):
        return "Pode formar um triângulo"
    else:
        return "Não pode formar um triângulo"


@app.get("/")
def index():
    return "Página inicial"


if (__name__ == "__main__"):
    uvicorn.run("desafios-web:app", port=6001, reload=True)
