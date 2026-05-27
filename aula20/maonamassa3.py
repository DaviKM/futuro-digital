from fastapi import APIRouter
from sqlalchemy import create_engine, text

DATABASE_URL = 'postgresql://postgres:123@localhost/loja'

router = APIRouter()

@app.get('/M1')
def m1():
    engine = create_engine(DATABASE_URL)

    try:
        with engine.connect() as con:
            sql = """SELECT p.nome_produto, m.nome_marca
                     FROM produtos p \
                              LEFT JOIN marcas m \
                                        on p.marca_id = m.id;"""
            rows = con.execute(text(sql))
            result = []
            for row in rows:
                result_row = {
                    "Nome do produto": row[0],
                    "Nome da marca": row[1]
                }
                result.append(result_row)
            return result