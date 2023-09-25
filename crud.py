import mysql.connector

db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='1234565',
    database='bancopi',
)

cursor = db.cursor()


def inserir_produto(nome, descricao, quantidade, preco, data_entrada):
    sql = "INSERT INTO estoque1 (nome_produto, descricao, quantidade, preco_unitario, data_entrada) VALUES (%s, %s, %s, %s, %s)"
    values = (nome, descricao, quantidade, preco, data_entrada)
    cursor.execute(sql, values)
    db.commit()

def inserir_fornecedor(nome, contato, endereco):
    sql = "INSERT INTO fornecedores (nome_fornecedor, contato, endereco) VALUES (%s, %s, %s)"
    values = (nome, contato, endereco)
    cursor.execute(sql, values)
    db.commit()


def listar_produtos():
    sql = "SELECT * FROM estoque1"
    cursor.execute(sql)
    result = cursor.fetchall()
    for row in result:
        print(row)

def listar_fornecedores():
    sql = "SELECT * FROM fornecedores"
    cursor.execute(sql)
    result = cursor.fetchall()
    for row in result:
        print(row)

def atualizar_produto(id, quantidade):
    sql = "UPDATE estoque1 SET quantidade = %s WHERE id = %s"
    values = (quantidade, id)
    cursor.execute(sql, values)
    db.commit()


def deletar_produto(id):
    sql = "DELETE FROM estoque1 WHERE id = %s"
    values = (id,)
    cursor.execute(sql, values)
    db.commit()


inserir_produto("ronald", "Descrição do Produto C", 50, 10.99, "2023-08-26")
inserir_fornecedor("Fornecedor XYZ", "Maria Santos", "Rua do Fornecedor, 456")

listar_produtos()
listar_fornecedores()

atualizar_produto(1, 40)
deletar_produto(1)

cursor.close()
db.close()

