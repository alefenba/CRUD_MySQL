import pymysql.cursors
from decouple import config

con = pymysql.connect(
    host="127.0.0.1", 
    user="root",
    password=config("password"),
    port=3306,
    charset="utf8mb4",
    cursorclass = pymysql.cursors.DictCursor)
