import uvicorn
from fastapi import FastAPI

app = FastAPI()

loja = {
    'categorias': {},
    'depositos': {},
    'cliente': {},
    'cupons': {},
    'fornecedores': {}
}
categorias = loja['categorias']
depositos = loja['depositos']
clientes = loja['cliente']
cupons = loja['cupons']
fornecedores = loja['fornecedores']

@app.get("/cadastrar-categoria")
def cadastrar_categoria(nome):
    if nome not in categorias:
        categorias[nome] = {}
        return "Categoria criada"
    return "Categoria já existe"


@app.get("/adicionar-produto")
def adicionar_produto(nome, categoria, preco: float):
    if categoria not in categorias:
        return "Categoria não existe"
    produto = {
        "nome": nome.strip(),
        "preco": preco
    }

    lista = categorias[categoria]
    lista[produto['nome']] = produto
    return produto


@app.get("/cadastrar-deposito")
def cadastrar_deposito(nome, cidade):
    if nome in depositos:
        return "Deposito já existe"
    deposito = {
        "nome": nome.strip(),
        "cidade": cidade.strip().capitalize(),
        "estoque": {}
    }

    depositos[nome] = deposito
    return deposito


@app.get("/abastecer-estoque")
def abastecer_estoque(nome_deposito, item, quant:int):
    if nome_deposito in depositos:
        deposito = depositos[nome_deposito]["estoque"]
    else:
        return 'Deposito não existe'

    if item not in deposito:
        estoque = {
            "item": item.strip(),
            "quantidade em estoque": quant
        }
        deposito[item] = estoque
        return estoque
    else:
        deposito[item]["quantidade em estoque"] += quant
        return deposito[item]

@app.get('/cadastrar-cliente')
def cadastrar_cliente(nome, senha, email):
    if nome in clientes:
        return 'Cliente já existe'

    cliente = {
        "nome": nome.strip().capitalize(),
        "senha": senha.strip(),
        "email": email.strip().lower(),
        "pedidos": {}
    }
    clientes[email] = cliente
    return cliente

@app.get('/criar-pedido')
def criar_pedido(email, id_pedido):
    if email in clientes:
        clientes[email]['pedidos'][id_pedido] = []
        return clientes[email]['pedidos']
    return 'Email nao encontrado'

@app.get('/adicionar-item-pedido')
def adicionar_item_pedido(email, id_pedido, item, valor:float):
    produto = {
        "nome": item,
        "valor": valor
    }
    # AO INVES DE PASSAR UMA STRING TEM QUE SER O OBJETO    
    if email in clientes and id_pedido in clientes[email]['pedidos'] :
        clientes[email]['pedidos'][id_pedido].append(produto)
        return clientes[email]['pedidos']
    return 'Email ou pedido não existe'

@app.get('/criar-cupom')
def criar_cupom(codigo, desconto):
    codigo = codigo.upper()
    try:
        desconto = float(desconto)
        if not (0 < desconto < 100):
            return 'Desconto deve ser entre 0% e 100%'
    except:
        return 'O desconto deve ser um número'
    cupom = {
        'codigo': codigo,
        'desconto': desconto
    }
    cupons[codigo] = cupom
    return cupom

@app.get('/aplicar-cupom-produto')
def aplicar_cupom(categoria, nome_produto, codigo_cupom):
    codigo_cupom = codigo_cupom.upper()
    if categoria in categorias:
        if nome_produto in categorias[categoria]:
            if codigo_cupom in cupons:
                desconto = cupons[codigo_cupom]['desconto']
                valor = categorias[categoria][nome_produto]['preco']
                categorias[categoria][nome_produto]['preco'] = valor - valor * desconto/100
                return categorias[categoria][nome_produto]

    return "Valores inválidos"

@app.get('/registrar-fornecedor')
def registrar_fornecedor(cnpj, nome_empresa):
    fornecedor = {
        "cnpj": cnpj,
        "nome_empresa": nome_empresa,
        'catalogo': {}
    }
    fornecedores[cnpj] = fornecedor
    return fornecedor

@app.get('/adicionar-ao-catalogo')
def adicionar_ao_catalogo(cnpj, nome_item, modelo):
    item = {
        "nome_item": nome_item,
        "modelo": modelo,
        "detalhes": {}
    }
    if cnpj in fornecedores:
        fornecedores[cnpj]['catalogo'][nome_item] = item
        return item
    else:
        return 'Fornecedor não existe'

@app.get('/adicionar-especificacao')
def adicionar_especificacao(cnpj, nome_item, chave, valor):
    especificacao = {
        chave: valor
    }
    if cnpj not in fornecedores:
        return "Fornecedor inválido"
    if nome_item not in fornecedores[cnpj]['catalogo']:
        return 'Item inválido'
    fornecedores[cnpj]['catalogo'][nome_item]['detalhes'][chave] = []
    fornecedores[cnpj]['catalogo'][nome_item]['detalhes'][chave].append(especificacao)
    return especificacao
@app.get("/")
def ver_loja():
    return loja

@app.get("/ver-deposito")
def ver_deposito():
    return depositos


if __name__ == "__main__":
    uvicorn.run('categorias:app', port=10001, reload=True)
