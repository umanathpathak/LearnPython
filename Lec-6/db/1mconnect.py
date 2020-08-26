
import mysql.connector as mc
mydb = mc.connect(host="127.0.0.1", user="root", password="nilesh")
mcur = mydb.cursor()
mcur.execute("create database emp")

'''
import mysql.connector as mc
mydb = mc.connect(host="127.0.0.1", user="root", password="nilesh")
mcur = mydb.cursor()
mcur.execute("show databases")
for i in mcur:
    print(i)
'''