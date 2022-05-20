import pymysql.cursors
from decouple import config

con = pymysql.connect(
    host="127.0.0.1", 
    user="root",
    password=config("password"),
    port=3306,
    db="aulapythonfull",
    charset="utf8mb4",
    cursorclass = pymysql.cursors.DictCursor)

def criaTabela(nomeTabela):
    try:
        with con.cursor() as cursor:
            cursor.execute(f"create table {nomeTabela}(nome varchar(50))")
        print("Tabela criada com sucesso")
    except Exception as e:
        print(f'Ocorreu um erro {e}')


def removeTabela(nomeTabela):
    try:
        with con.cursor() as cursor:
            cursor.execute(f"drop table {nomeTabela}")
        print("Tabela excluida com sucesso")
    except Exception as e:
        print(f'Ocorreu um erro {e}')


def insereValor(nome):
    try:
        with con.cursor() as cursor:
            cursor.execute(f"INSERT INTO teste VALUES('{nome}')")
        print("Valor inserido com sucesso!")
    except Exception as e:
        print(f'Ocorreu um erro {e}')


con.close()