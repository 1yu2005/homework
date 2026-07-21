from pymysql import Connection

conn = Connection(
    host="localhost",
    port=3306,
    user="root",
    password="123456",
    autocommit=True  #设置为自动提交，就不需要 链接对象.commit()
)
cursor = conn.cursor()

conn.select_db("test0721")

cursor.execute("""
    delete from test0721_pymysql
    where id=10006 if exists;
""")

cursor.execute("""
    insert into test0721_pymysql
    values
    (10006,'小诺',25),
    (10007,'小绿',26),
    (10008,'小蓝',27);
""")

cursor.execute("""
    update test0721_pymysql
    set age=99
    where id=10007;
   """)



conn.close()

