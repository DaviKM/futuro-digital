import uvicorn
from fastapi import FastAPI
from sqlalchemy import create_engine, text

DATABASE_URL = 'postgresql://postgres:123@localhost:5432/loja'

app = FastAPI()

@app.get('/J-G1')
def jg1():
    engine = create_engine(DATABASE_URL)
    # Testeee
    try:
        with engine.connect() as con:
            sql = """SELECT c.nome_cliente, p.data_pedido
                     FROM clientes c JOIN pedidos p
                     ON c.id = p.cliente_id
                     WHERE c.cidade = 'São Paulo'"""
            rows = con.execute(text(sql))
            
            result = []
            for row in rows:
                result.append(row._mapping)
            return result
    except Exception as e:
        return e
    engine.dispose()
if __name__ == '__main__':
    uvicorn.run('exercicios:app', port=21000, reload=True)