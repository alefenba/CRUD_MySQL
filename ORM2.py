from decouple import config
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from ORM import Pessoa

def RetornaSession():
    USUARIO = "root"
    SENHA = config("password")
    HOST = "127.0.0.1"
    BANCO = "aulapythonfull"
    PORT = "3306"
    CONN = f"mysql+pymysql://{USUARIO}:{SENHA}@{HOST}:{PORT}/{BANCO}"
    engine = create_engine(CONN, echo=True)
    Session = sessionmaker(bind=engine)
    return  Session()

session = RetornaSession()

#Instanciando a classe para adcionar valores ao banco de dados
x = Pessoa(nome = 'Alefe',
           usuario='Alefe182',
           senha='1234546')

y = Pessoa(usuario='Alana182',
           senha='1234546')

#efetuando todas mudanças no BD
session.add_all([x,y])
#Efetuando as alterações do BD
session.commit()

