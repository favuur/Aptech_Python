#import mysql.connector as go
"""con= go.connect(host="localhost",user="root",password="")
conn=con.cursor()
conn.execute("show databases")
for x in conn:
    print(x)"""


#low= go.connect(host="localhost",user="root",password="",database="church")
#lowo=low.cursor()
"""lowo.execute("create database church")
print("created successfully")

lowo.execute("create table members(fname varchar(20),lname varchar(20),sex varchar(10))")

lowo.execute("insert into members values('favour','oluwa','female')")

lowo.execute("show tables")
for x in lowo:
    print(x)

lowo.execute("select *from members")
for x in lowo:
    print(x)

fro="insert into members(fname,lname,sex) values(%s,%s,%s)"
val=[('funke','ola','F'),('femi','olu','M'),('Great','Ademi','M'),('ase','rer','M')]
lowo.executemany(fro,val)

import sys
print("whats your name")
name=sys.stdin.readline()
print('hello',name)"""

import mysql.connector as fr
f=fr.connect(host="localhost",user="root",password="")
goat=f.cursor()
goat.execute("show databases")
for x in goat:
    print(x)




