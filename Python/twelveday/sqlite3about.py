
import sqlite3

conn = sqlite3.connect('francis.db')

cursor = conn.cursor()

#cursor.execute('create table user(id varchar(20) primary key, name varchar(20))')
cursor.execute('insert into user (id, name) values (\'3\', \'wangong\')')

print('rowcount =', cursor.rowcount)

conn.commit()

cursor.close()
conn.close()

#select
conn = sqlite3.connect('francis.db')
cursor = conn.cursor()

cursor.execute('select * from user where id=?', '2')

values = cursor.fetchall()
print(values)
cursor.close()
conn.close()
