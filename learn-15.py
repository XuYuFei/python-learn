""" 15 - 使用Python操作数据库 """
''' 15.1 - 数据库编程接口 '''
# 15.1.1 - 连接对象
# 15.1.1 - 1 - 获取连接对象
import pymysql
conn = pymysql.connect(host = 'localhost',
                       user = 'root',
                       password = '',
                       db = 'python',
                       charset = 'utf8',
                       cursorclass = pymysql.cursors.DictCursor)
print(conn)

# 15.1.1 - 2 - 连接对象的方法
"""
    connect()函数返回连接对象，这个对象表示目前和数据库的会话。
    连接对象方法： 
        - close()
        - commit()
        - rollback()
        - cursor()：获取游标对象，操作数据库        
"""

# 15.1.2 - 游标对象
"""
    游标对象(Cursor Object)：代表数据库中的游标，用于抓取数据操作的上下文。
        - 主要提供执行SQL语句、调用存储过程、获取查询结果等方法
    游标对象属性：
        - description：数据库列类型和值的描述信息；
        - rowcount：回返结果的行数统计信息，如SELECT,UPDATE，CALLPROC等； 
    游标对象方法：
        - callproc(procname, [, parameters])：调用存储过程，需要数据库支持
        - close()：关闭当前游标
        - execute(operation[, parameters])：执行数据库操作，SQL语句或数据库命令
        - executemany(operation, seq_of_params)：用于批量操作
        - fetchone()：获取查询结果集中的下一条记录
        - fetchmany(size)：获取指定数量的记录
        - fetchall()：获取结果集的所有记录
        - nextset()：跳至下一个可用的结果集
        - arraysize：指定使用fetchmany()获取的行数，默认为1
        - setinputsizes(sizes)：设置在调用execute*()方法时分配的内存区域的大小
        - setoutputsize(sizes)：设置缓冲区大小，对大数据列如LONGS和BLOBS尤其有用
"""

''' 15.2 - 使用SQLite '''
"""
    SQLite：
        - 一种嵌入式数据库，它的数据库就是一个文件；
        - C语言编写的，体积小
        - Python中内置了SQLite3,可以直接使用
"""
# 15.2.1 - 创建数据库文件
"""
    通用流程：开始 -> 
             创建connection -> 
             获取cursor -> 
             执行SQL语句，处理数据结果 ->
             关闭cursor ->
             关闭connection ->
             结束
    示例：创建数据库learn-15.db，并创建用户表user
"""
'''
import sqlite3
conn = sqlite3.connect('learn-15.db')
cursor = conn.cursor()
cursor.execute('create table user (id int(10) primary key, name varchar(20))')
cursor.close()
conn.close()
'''
# 15.2.2 - 操作SQLite
# 15.2.2 - 1 - 新增用户数据信息
"""
    insert into 表名(字段1, 字段2, ..., 字段n) values (字段值1, 字段值2, ..., 字段值n)
"""
'''
import sqlite3
conn = sqlite3.connect('learn-15.db')
cursor = conn.cursor()
cursor.execute('insert into user (id, name) values("2", "Luli")')
cursor.close()
conn.close()
'''

# 15.2.2 - 2 - 查看用户数据信息
""" 
    select * from 表名 where 查询条件
    查询方式：
        - fetchone()
        - fetchmany(size)
        - fetchall()
"""
import sqlite3
conn = sqlite3.connect('learn-15.db')
cursor = conn.cursor()
sql = "select * from user"
cursor.execute(sql)
result1 = cursor.fetchone()
result2 = cursor.fetchmany(2)
result3 = cursor.fetchall()
print(result1)
print(result2)
print(result3)
cursor.close()
conn.close()

# 15.2.2 - 3 - 修改数据
""" 
    update 表名 set 字段名 = 字段值 where 查询条件
    cursor = conn.cursor()
    cursor.execute('update user set name = ? where id = ?', ('Hello', 1))
"""

# 15.2.2 - 4 - 删除数据
# delete from table where ...

''' 15.3 - 使用mysql '''
# 15.3.1 - 下载安装MySQL
"""
    net start mysql57：启动mysql
    mysql -u root -p：进入mysql
"""

# 15.3.2 - 安装PyMySQL
"""
    命令：pip install PyMySQL
"""

# 15.3.3 - 连接数据库
import pymysql
db = pymysql.connect('localhost', 'root', '', 'python')
cursor = db.cursor()
cursor.execute('SELECT VERSION()')
data = cursor.fetchone()
print('Database version ：%s' % data)
db.close()

# 15.3.4 - 创建数据表
import pymysql
db = pymysql.connect('localhost', 'root', '', 'python')
cursor = db.cursor()
cursor.execute('DROP TABLE IF EXISTS books')
sql = """
CREATE TABLE books (
    id int(8) NOT NULL AUTO_INCREMENT,
    name varchar(50) NOT NULL,
    category varchar(50) NOT NULL,
    price decimal(10, 2) DEFAULT NULL,
    publish_time date DEFAULT NULL,
    PRIMARY KEY (id)
) ENGINE = MyISAM AUTO_INCREMENT = 1 DEFAULT CHARSET = utf8;
"""
cursor.execute(sql)
db.close()

# 15.3.5 - 操作MySQL数据表
import pymysql
db = pymysql.connect('localhost', 'root', '', 'python', charset="utf8")
cursor = db.cursor()
data = [('零基础学习Python', 'python', 89.90, '2019-10-23'),
    ('零基础学习PHP', 'PHP', 90.20, '2016-12-23'),
    ('零基础学习PHP', 'PHP', 90.20, '2016-12-23'),
    ('零基础学习PHP', 'PHP', 90.20, '2016-12-23'),
    ('零基础学习PHP', 'PHP', 90.20, '2016-12-23'),
    ('零基础学习PHP', 'PHP', 90.20, '2016-12-23')]
try:
    res = cursor.executemany("insert into books (name, category, price, publish_time) values (%s, %s, %s,%s)", data)
    db.commit()
except:
    db.rollback()
db.close()