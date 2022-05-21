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

x = session.query(Pessoa).all()
x = session.query(Pessoa).filter_by(usuario='Alefe182',nome='Alefe').all()
for i in x:
    print (i.id)