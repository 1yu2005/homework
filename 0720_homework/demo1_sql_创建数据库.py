from pymysql import Connection

#pymysql在执行数据插入或其它产生数据更改的SQL语句时，默认是需要提交更改的，即，需要通过代码“确认”这种更改行为。
#通过链接对象.commit() 即可确认此行为  conn.commit()


# 创建到 MySQL 的数据库连接
conn = Connection(
    host="localhost",
    port=3306,
    user="root",
    password="123456",
    autocommit=True  #设置为自动提交，就不需要 链接对象.commit()
)

#print(coon.get_server_info())  #8.0.46 当前MySQL Server的版本

# 获取游标对象
cursor = conn.cursor()


## 执行非查询性质SQL
# 1. 创建数据库（如果不存在）
cursor.execute("create database if not exists test;")

# 2. 选择数据库
conn.select_db("test")  # 或者 cursor.execute("use test;")

# 3. 创建表
cursor.execute("""
    create table if not exists test_pymysql(
        id int,
        name varchar(100), 
        age int
    );
""")

# 执行查询性质SQL
conn.select_db("world")
cursor.execute("select * from student")
result = cursor.fetchall() #游标对象使用fetchall()方法，得到的是全部的查询结果，是一个元组。这个元组内部嵌套了元组，嵌套的元组就是一行查询结果
print(result)
for row in result:
    print(row)

cursor.execute("""
    insert into student
    values(10006,'小诺',25,'男');
""")

#关闭到数据库的连接
conn.close()