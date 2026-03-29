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



if __name__ == "__main__":
    uvicorn.run("strings:app", port=3000, reload=True)