import uvicorn
from fastapi import FastAPI
from sqlalchemy import create_engine, text

DATABASE_URL = 'postgresql://postgres:123@localhost/loja'

app = FastAPI()
@app.get('/L1')
def l1():
    engine = create_engine(DATABASE_URL)

    try:
        with engine.connect() as con:
            sql = """SELECT p.nome_produto, m.nome_marca 
                     FROM produtos p LEFT JOIN marcas m 
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

@app.get('/L2')
def l2():
    engine = create_engine(DATABASE_URL)

    try:
        with engine.connect() as con:
            sql = """SELECT p.nome_produto, m.nome_marca 
                     FROM produtos p LEFT JOIN marcas m 
                     on p.marca_id = m.id
                     WHERE p.preco < 200 ;"""
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

@app.get('/L3')
def l3():
    engine = create_engine(DATABASE_URL)

    try:
        with engine.connect() as con:
            sql = """SELECT m.nome_marca, p.nome_produto 
                     FROM produtos p LEFT JOIN marcas m 
                     on p.marca_id = m.id ;"""
            rows = con.execute(text(sql))
            result = []
            for row in rows:
                result_row = {
                    "Nome da marca": row[0],
                    "Nome do produto": row[1]
                }
                result.append(result_row)
            return result

    except Exception as e:
        return e

@app.get('/R4')
def r4():
    engine = create_engine(DATABASE_URL)

    try:
        with engine.connect() as con:
            sql = """SELECT m.nome_marca, p.nome_produto 
                     FROM marcas m LEFT JOIN produtos p 
                     on p.marca_id = m.id ;"""
            rows = con.execute(text(sql))
            result = []
            for row in rows:
                result_row = {
                    "Nome da marca": row[0],
                    "Nome do produto": row[1]
                }
                result.append(result_row)
            return result

    except Exception as e:
        return e
    
if __name__ == '__main__':
    uvicorn.run('fixacao:app', port=19000, reload=True)