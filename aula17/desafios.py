import uvicorn
from dns import exception
from fastapi import FastAPI
from sqlalchemy import create_engine, text

DATABASE_URL = "postgresql://postgres:123@localhost/loja"

app = FastAPI()
@app.get('/J1')
def j1():
    engine = create_engine(DATABASE_URL)

    try:
        with engine.connect() as con:
            sql = """SELECT p.nome_produto, m.nome_marca 
                     FROM produtos p JOIN marcas m 
                     on p.marca_id = m.id ;"""
            rows = con.execute(text(sql))
            result = []
            for row in rows:
                result_row = {
                    "Nome do produto": row[0],
                    "Nome da marca": row[1]
                }
                result.append(result_row)
            return result

    except Exception as e:
        return e

@app.get('/J2')
def j2():
    engine = create_engine(DATABASE_URL)

    try:
        with engine.connect() as con:
            sql = """SELECT p.nome_produto, p.preco, m.pais_origem 
                     FROM produtos p JOIN marcas m 
                     ON p.marca_id = m.id ;"""
            rows = con.execute(text(sql))
            result = []
            for row in rows:
                result_row = {
                    "Nome do produto": row[0],
                    "Preço": row[1],
                    "País de origem": row[2]
                }
                result.append(result_row)
            return result

    except Exception as e:
        return e

@app.get('/J3')
def j3():
    engine = create_engine(DATABASE_URL)

    try:
        with engine.connect() as con:
            sql = """SELECT p.nome_produto, m.nome_marca
                     FROM produtos p join marcas m 
                     ON p.marca_id = m.id
                     WHERE p.preco > 500 ;"""
            rows = con.execute(text(sql))
            result = []
            for row in rows:
                result_row = {
                    "Nome do produto": row[0],
                    "Nome da marca": row[1]
                }
                result.append(result_row)
            return result

    except Exception as e:
        return e

@app.get("/J4")
def j4():
    engine = create_engine(DATABASE_URL)

    try:
        with engine.connect() as con:
            sql = """SELECT m.nome_marca, p.nome_produto, p.preco 
                     FROM produtos p JOIN marcas m 
                     ON p.marca_id = m.id
                     ORDER BY m.nome_marca ASC, p.preco DESC ;"""
            rows = con.execute(text(sql))
            result = []
            for row in rows:
                result_row = {
                    "Nome do produto": row[0],
                    "Nome da marca": row[1]
                }
                result.append(result_row)
            return result

    except Exception as e:
        return e

@app.get('/J5')
def j5():
    engine = create_engine(DATABASE_URL)

    try:
        with engine.connect() as con:
            sql = """SELECT p.nome_produto, p.preco 
                     FROM produtos p JOIN marcas m 
                     ON p.marca_id = m.id 
                     WHERE m.pais_origem = 'Brasil';"""
            rows = con.execute(text(sql))
            result = []
            for row in rows:
                result_row = {
                    "Nome do produto": row[0],
                    "Preço": row[1],
                }
                result.append(result_row)
            return result

    except Exception as e:
        return e

@app.get('/J6')
def j6():
    engine = create_engine(DATABASE_URL)

    try:
        with engine.connect() as con:
            sql = """SELECT p.nome_produto, m.nome_marca, p.estoque  
                     FROM produtos p JOIN marcas m 
                     ON p.marca_id = m.id 
                     WHERE m.nome_marca  = 'TechWave' or m.nome_marca = 'StyleWear';"""
            rows = con.execute(text(sql))
            result = []
            for row in rows:
                result_row = {
                    "Nome do produto": row[0],
                    "Nome da marca:": row[1],
                    "Preço": row[2],
                }
                result.append(result_row)
            return result

    except Exception as e:
        return e

@app.get('/J7')
def j7():
    engine = create_engine(DATABASE_URL)

    try:
        with engine.connect() as con:
            sql = """SELECT p.nome_produto, m.nome_marca  
                     FROM produtos p JOIN marcas m 
                     ON p.marca_id = m.id 
                     ORDER BY p.preco DESC LIMIT 1;"""
            row = con.execute(text(sql)).fetchone()
            result = {
                "Nome do produto": row[0],
                "Nome da marca": row[1]
            }
            return result

    except Exception as e:
        return e


if __name__ == "__main__":
    uvicorn.run("desafios:app", port=17000, reload=True)