from decouple import config
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import or_
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
x = session.query(Pessoa).filter(Pessoa.id == 3).all()
#Atualizando inforamção dentro do BD
x[0].senha = '123456'

session.commit()