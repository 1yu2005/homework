from pymysql import Connection

conn = Connection(
    host="localhost",
    port=3306,
    user="root",
    password="123456",
    autocommit=True  #设置为自动提交，就不需要 链接对象.commit()
)

cursor = conn.cursor()

cursor.execute("create database if not exists test0721")

conn.close()
