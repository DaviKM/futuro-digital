import uvicorn
from fastapi import FastAPI

app = FastAPI()

# 1º exercicio
@app.get("/verificador-de-nome")
def verificador_nome(nome:str):
    return f""""{nome.upper()}      {nome.lower()}      {nome.capitalize()}"""

@app.get("/limpador-de-frases")
def limpar_frases(frase:str):
    return frase.strip()

@app.get("/sensor-palavroes")
def sensor_palavroes(frase:str):
    frase = frase.strip().replace("chato", "*****")
    return frase

@app.get("/contar-vogal")
def contar_vogal(frase:str):
    frase = frase.strip()
    return frase.count('a')

@app.get("/validar-senha")
def validar_senha(senha:str):
    if 6 <= len(senha) <= 10:
        return "Senha valida"
    else:
        return "A senha deve ter entre 6 e 10 caracteres"

@app.get("/verificar-arquivo")
def verificar_arquivo(arquivo:str):
    log = []
    arquivo = arquivo.strip().lower()
    if arquivo.startswith("relatorio"):
        log.append('O arquivo começa com "relatorio"')
    if arquivo.endswith(".pdf"):
        log.append('O arquivo termina com ".pdf"')

    if not log:
        return "O arquivo não atende aos critérios"
    return log

@app.get("/criar-apelido")
def criar_apelido(nome):
    nome = nome.strip().split(" ")

    return "-".join(nome)

@app.get("/localizar-palavra")
def localizar_palavra(frase:str, chave:str):
    if frase.find(chave) == -1:
        return "A palavra não foi encontrada"
    return "Palavra encontrada"

@app.get("/verificar-email")
def verificar_email(email:str):
    email = email.strip().lower()
    if email.find("@") != -1 and email.endswith(".com"):
        return "Email válido"
    return "Email inválido"

@app.get("/analisar-frase")
def analisar_frase(frase:str):
    frase = frase.strip().upper()
    sem_vogais = frase.replace("A", "*")
    sem_vogais = sem_vogais.replace("E", "*")
    sem_vogais = sem_vogais.replace("I", "*")
    sem_vogais = sem_vogais.replace("O", "*")
    sem_vogais = sem_vogais.replace("U", "*")

    return f"""{sem_vogais}       Quant. de E = {frase.count('e')}     Tamanho total: {len(frase)}"""
if __name__ == "__main__":
    uvicorn.run("strings:app", port=3000, reload=True)