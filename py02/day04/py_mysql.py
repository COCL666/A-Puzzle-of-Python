#!/usr/local/bin/python3

import pymysql

# 建立连接
conn = pymysql.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    password='123456',
    db='nsd1909',
    charset='utf8'
)

# 创建游标,类似于文件对象,通过文件对象对文件读写,通过游标对数据库进行操作
cur = conn.cursor()

# 编写并执行相应的sql语句
mk_dep = '''CREATE TABLE departments(
dep_id INT, dep_name VARCHAR (20),
PRIMARY KEY (dep_id)
)
'''

mk_emp = '''CREATE TABLE employees(
emp_id INT, emp_name VARCHAR (20), email VARCHAR (50),dep_id INT,
PRIMARY KEY (emp_id), FOREIGN KEY (dep_id) REFERENCES departments(dep_id)
)'''

mk_sal = '''CREATE TABLE salary(
id INT, date DATE, emp_id INT, basic INT, awards INT,
PRIMARY KEY (id), FOREIGN KEY (id) REFERENCES employees(emp_id)
)'''

cur.execute(mk_dep)
cur.execute(mk_emp)
cur.execute(mk_sal)

# 确认
conn.commit()

# 关闭游标,关闭连接
cur.close()
conn.close()