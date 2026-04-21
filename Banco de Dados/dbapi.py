import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent

conexao = sqlite3.connect(ROOT_PATH / "meu_banco.db")
cursor = conexao.cursor()

def criar_tabela(conexao, cursor):
    cursor.execute(
        'CREATE TABLE IF NOT EXISTS clientes (id INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR(100), email VARCHAR(150))'
    )
    conexao.commit()

def inserir_cliente(conexao, cursor, nome, email):
    data = (nome, email)
    cursor.execute('INSERT INTO clientes (nome, email) VALUES (?, ?);', data)
    conexao.commit()

def atualizar_registro(conexao, cursor, nome, email, id):
    data = (nome, email, id)
    cursor.execute('UPDATE clientes SET nome = ?, email = ? WHERE id = ?;', data)
    conexao.commit()

def deletar_registro(conexao, cursor, id):
    data = (id,)
    cursor.execute('DELETE FROM clientes WHERE id = ?;', data)
    conexao.commit()

def inserir_muitos_registros(conexao, cursor, dados):
    cursor.executemany('INSERT INTO clientes (nome, email) VALUES (?, ?);', dados)
    conexao.commit()


def recuperar_clientes(conexao, cursor, id):
    cursor.execute('SELECT * FROM clientes WHERE id = ?;', (id,))
    return cursor.fetchone()

def listar_clientes(conexao, cursor):
    return cursor.execute('SELECT * FROM clientes ORDER BY nome ASC;')

cliente = recuperar_clientes(conexao, cursor, 2)
print(cliente)

clientes = listar_clientes(conexao, cursor)
for cliente in clientes:
    print(cliente)

# Inserir muitos registros
# dados = [
#     ('João', 'joao@example.com'),
#     ('Maria', 'maria@example.com'),
#     ('Pedro', 'pedro@example.com'),
#     ('Ana', 'ana@example.com'),
#     ('Carlos', 'carlos@example.com'),
#     ('Laura', 'laura@example.com'),
#     ('Marcelo', 'marcelo@example.com'),
# ]
# inserir_muitos_registros(conexao, cursor, dados)