
import mysql.connector as mc
mydb = mc.connect(host="127.0.0.1", user="root", password="nilesh",database="emp")
mcur = mydb.cursor()
mcur.execute("create table empdetail (id INT(3), fname VARCHAR(50), lname VARCHAR(250))")
mydb.commit()
'''
import mysql.connector as mc
mydb = mc.connect(host="127.0.0.1", user="root", password="nilesh", database="emp")
mcur = mydb.cursor()
mcur.execute("desc empdetail")
for i in mcur:
    print(i)
'''