import uvicorn
from fastapi import FastAPI

app = FastAPI()

curriculos = {}
produtos = {}
usuarios = {}
inscritos = {}

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
def vproduto(nome, preco, quant: int, cat):
    log = []

    nome = nome.strip()
    cat = cat.strip().capitalize()

    produto = {}
    produto["nome"] = nome
    produto["preco"] = preco
    produto["quantidade"] = quant
    produto["categoria"] = cat

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
        produtos[nome] = produto
        return "Produto válido"


@app.get("/ver-produtos")
def ler_produtos():
    return produtos


@app.get("/login")
def login(nome: str, senha: str, confirmacao: str, email: str):
    log = []

    nome = nome.strip()
    senha = senha.strip()
    confirmacao = confirmacao.strip()
    email = email.strip()

    usuario = {
        'nome': nome,
        'senha': senha,
        'email': email
    }

    if len(nome) < 5:
        log.append("O nome deve ter 5 ou mais caracteres")
    elif len(nome) > 15:
        log.append("O nome deve ter 15 ou menos caracteres")
    if len(senha) < 8:
        log.append("O senha deve ter 8 ou mais caracteres")
    if senha != confirmacao:
        log.append("As senhas não coincidem")
    # VALIDAÇÃO DO E-MAIL
    endereco = email.split("@")

    if len(endereco) == 1:
        log.append("Um e-mail válido deve conter um @")
    else:
        if endereco[1].find(".") == -1:
            log.append("O e-mail deve ter pelo menos um . após o @")

        if endereco[1].find(".") == 0:
            log.append("Deve haver algum caractere entre o @ e o .")

    if len(endereco) > 2:
        log.append("O e-mail deve ter apenas um @")
    if email.startswith("@"):
        log.append("O e-mail não pode começar com @")
    if email.endswith("@"):
        log.append("O e-mail não pode terminar com @")

    if email.startswith("."):
        log.append("O e-mail não pode começar com .")
    if email.endswith("."):
        log.append("O e-mail não pode terminar com .")

    if len(log) > 0:
        return log
    usuarios[email] = usuario
    return 'Usuário logado!'


@app.get("/ver-usuarios")
def ver_usuarios():
    return usuarios


@app.get("/inscricao-maratona")
def inscricao_maratona(nome, distancia, cpf, tempo_estimado):
    log = []
    distancias = [5, 10, 21, 42]
    nome = nome.strip()
    tempo_estimado = int(tempo_estimado)
    try:
        distancia = int(distancia)
    except:
        log.append("A distância deve ser um número inteiro")
    try:
        if len(cpf) != 11:
            log.append('O cpf deve ter 11 digitos')
        cpf = int(cpf)
    except:
        log.append("O cpf deve ter apenas números")
    if len(nome.split(' ')) < 2:
        log.append("O nome deve conter um sobrenome")

    if distancia not in distancias:
        # t erminar
        log.append("A distância deve ser uma das seguintes: 5, 10, 21 ou 42 km")

    if tempo_estimado >= 300:
        log.append("O tempo estimado deve ser menor que 300 minutos")

    if len(log) > 0:
        return log
    else:
        inscritos[cpf] = {
            'nome': nome,
            'distancia': distancia,
            'cpf': cpf,
            'tempo_estimado': tempo_estimado,
        }
        return "Inscrição realizada com sucesso!"

@app.get("/ver-inscricao")
def ver_inscricao():
    return inscritos
if __name__ == "__main__":
    uvicorn.run("reforco:app", port=8001, reload=True)
