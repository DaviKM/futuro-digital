from fastapi import APIRouter
from sqlalchemy import create_engine, text

DATABASE_URL = 'postgresql://postgres:123@localhost/loja'

router = APIRouter()

@router.get('/M1')
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
    
@router.get("/M4")
def m4():
    engine = create_engine(DATABASE_URL)

    try:
        with engine.connect() as con:
            sql = """SELECT m.nome_marca, c.nome_cliente
                     FROM marcas m JOIN produtos p ON m.id = p.marca_id 
                     JOIN itens_compra ic ON p.id = ic.produto_id 
                     JOIN pedidos pe ON ic.pedido_id = pe.id 
                     JOIN clientes c ON pe.cliente_id = c.id  ;"""
            rows = con.execute(text(sql))
            result = []
            for row in rows:
                result_row = {
                    "Nome da marca": row[0],
                    "Nome do cliente": row[1]
                }
                result.append(result_row)
            return result
    except Exception as e:
        return e
    

@router.get("/M5")
def m5():
    engine = create_engine(DATABASE_URL)

    try:
        with engine.connect() as con:
            sql = """SELECT c.nome_cliente 
                     FROM clientes c LEFT JOIN pedidos p ON c.id = p.cliente_id 
                     WHERE p.id IS NULL;"""
            rows = con.execute(text(sql))
            result = []
            for row in rows:
                result_row = {
                    "Nome do cliente": row[0]
                }
                result.append(result_row)
            return result
    except Exception as e:
        return e