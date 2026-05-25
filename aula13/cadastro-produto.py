import uvicorn
from fastapi import FastAPI
from sqlalchemy import create_engine, text

app = FastAPI()

# postgresql://usuario:senha@servidor:porta/banco   padrão
DATABASE_URL = 'postgresql://postgres:123@localhost:5432/loja'


@app.get("/cadastrar")
def cadastrar(nome, valor, categoria):
    try:
        valor = valor.replace(',', '.')
        valor = float(valor)
    except:
        return 'Valor inválido'
    engine = create_engine(DATABASE_URL)
    try:
        with engine.begin() as conn:
            sql = f"INSERT INTO public.produto(nome, preco, categoria) VALUES (:nomezinho, :valorzinho, :categoria);"
            dados = {
                'nomezinho': nome,
                'valorzinho': valor,
                'categoria': categoria
            }
            conn.execute(text(sql), dados)  # Mapa para evitar SQL Injection // Prepare stateman
    except Exception as erro:
        return erro
    engine.dispose()
    return 'foi'


@app.get("/deletar")
def deletar(linha):
    engine = create_engine(DATABASE_URL)
    try:
        with engine.begin() as conn:
            sql = "DELETE FROM public.produto WHERE id_produto = :linha;"
            dados = {
                'linha': linha
            }
            conn.execute(text(sql), dados)

    except Exception as erro:
        return erro
    engine.dispose()
    return 'apagado'


@app.get("/atualizar")
def atualizar(nome, valor, categoria, id):
    try:
        valor = valor.replace(',', '.')
        valor = float(valor)
    except:
        return 'Valor inválido'
    engine = create_engine(DATABASE_URL)
    try:
        with engine.begin() as conn:
            sql = "UPDATE public.produto SET nome=:nome, preco=:preco, categoria=:categoria WHERE id_produto = :id;"
            dados = {
                'nome': nome,
                'preco': valor,
                'categoria': categoria,
                'id': id
            }
            conn.execute(text(sql), dados)
    except Exception as erro:
        return erro
    engine.dispose()
    return 'atualizado'

@app.get("/buscar/{id}")
def buscar(id : int):
    engine = create_engine(DATABASE_URL)
    try:
        with engine.begin() as conn:
            sql = f"SELECT id_produto,nome,preco FROM public.produto WHERE id_produto = :id"
            dados = {
                'id': id
            }

            result = conn.execute(text(sql), dados)
            prod = result.fetchone()
            return prod._mapping #atalho
    except Exception as e:
        return e

@app.get("/listar")
def listar():
    engine = create_engine(DATABASE_URL)
    try:
        with engine.connect() as conn:
            sql = "SELECT id, nome_produto, preco, estoque, marca_id FROM public.produtos"
            result = conn.execute(text(sql))
            linhas = result.fetchall()

            produtos = []

            for linha in linhas:
                produtos.append(linha._mapping)
            return linhas._mapping
    except Exception as e:
        return e

@app.get("/")
def index():
    return {"Hello": "World"}


if __name__ == "__main__":
    uvicorn.run('cadastro-produto:app', port=13000, reload=True)
