import pymysql
# db=pymysql.connect(host='localhost',user='root',password='13471118',port=3306)
# cursor=db.cursor()
# cursor.execute('select version()')
# data=cursor.fetchone()
# print('database version:',data)
# cursor.execute("create database spiders default character set utf8")
# db.close()
db=pymysql.connect(host='localhost',user='root',password='13471118',port=3306,db='spiders')
# cursor=db.cursor()
# sql='create table if not exists students(id varchar(255) not null,name varchar(255) not null,age int not null'
# cursor.execute(sql)
# db.close()
# id='2012001'
# user='bob'
# age=20
# cursor=db.cursor()
# sql1='insert into students(id,name,age) values(%s,%s,%s)'
# try:
#     cursor.execute(sql1,(id,user,age))
#     db.commit()
# except:
#     db.rollback()
# db.close()
# data={
#     'id':'20120001',
#     'name':'Bob',
#     'age':20
# }
# cursor=db.cursor()
# table='students'
# condition='age>20'
# keys=','.join(data.keys())
# values=','.join(['%s']*len(data))
# sql='insert into {table}({keys}) values ({values})'.format(table=table,keys=keys,values=values)
# sql1="insert into {table}({keys}) values({values}) on duplicate update ".format(table=table,keys=keys,values=values)
# sql2="delete from {table} where {condition}".format(table=table,condition=condition)
# update=','.join(["{key}=%s".format(key=key) for key in data])
# sql1+=update
# try:
#     if cursor.execute(sql1,tuple(data.values())*2):
#         print("successful")
#         db.commit()
# except:
#     print('failed')
#     db.rollback()
# db.close()

# sql3="select * from students where age>20"
# try:
#     cursor.execute(sql3)
#     print('Count: ',cursor.rowcount)
#     row=cursor.fetchone()
#     while row:
#         print('row: ',row)
#         row=cursor.fetchone()
# except:
#     print('error')