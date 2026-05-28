from fastapi import APIRouter
from sqlalchemy import create_engine, text

DATABASE_URL = 'postgresql://postgres:123@localhost/loja'

router = APIRouter()

@router.get('/M2')
def m1():
    engine = create_engine(DATABASE_URL)

    try:
        with engine.connect() as con:
            sql = """SELECT c.nome_cliente, pr.nome_produto, ic.quantidade
                     FROM clientes c JOIN pedidos pe ON c.id = pe.cliente_id 
                     JOIN itens_compra ic ON pe.id = ic.pedido_id 
                     JOIN produtos pr ON ic.produto_id = pr.id ;"""
            rows = con.execute(text(sql))
            result = []
            for row in rows:
                result_row = {
                    "Nome do cliente": row[0],
                    "Nome do produto": row[1],
                    "Quantidade": row[2]
                }
                result.append(result_row)
            return result
    except Exception as e:
        return e

@router.get("/M2")
def m2():
    engine = create_engine(DATABASE_URL)

    try:
        with engine.connect() as con:
            sql = """SELECT c.nome_cliente, p.data_pedido, p.status 
                     FROM clientes c JOIN pedidos p 
                     ON c.id = p.cliente_id"""
            rows = con.execute(text(sql))
            result = []
            for row in rows:
                result_row = {
                    "Nome do cliente": row[0],
                    "Data do pedido": row[1],
                    "Status do pedido": row[2]
                }
                result.append(result_row)
            return result
    except Exception as e:
        return e

@router.get("/M3")
def m3():
    engine = create_engine(DATABASE_URL)

    try:
        with engine.connect() as con:
            sql = """SELECT p.nome_produto, sum(ic.quantidade * ic.preco_unitario) AS total_pago
                     FROM produtos p JOIN itens_compra ic ON p.id = ic.produto_id 
                     GROUP BY p.nome_produto ;"""
            rows = con.execute(text(sql))
            result = []
            for row in rows:
                result_row = {
                    "Nome do produto:": row[0],
                    "Total pago": row[1],
                }
                result.append(result_row)
            return result
    except Exception as e:
        return e