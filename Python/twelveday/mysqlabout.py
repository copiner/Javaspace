import mysql.connector

config = {
        'host':'127.0.0.1',
        'user':'root',
        'password':'',
        'database':'test',
        'port':'3396',
        'charset':'utf8'
       }
try:
    conn = mysql.connector.connect(**config)
except mysql.connector.Error as e:
    print('connect fail... '.format(e))

cursor = conn.cursor()
#cursor.execute('create table user(id varchar(20) primary key, name varchar(20))')
cursor.execute('insert into user (id, name) values(%s, %s)', ('2', 'francis'))

print('rowcount =', cursor.rowcount)

conn.commit()
cursor.close()

#select
cursor = conn.cursor()
cursor.execute('select * from user where id=%s', ('2',))

values = cursor.fetchall()
print(values)
cursor.close()
conn.close()
