import mysql.connector as mc
mydb = mc.connect(host="127.0.0.1", user="root", password="nilesh",database="emp")
mcur = mydb.cursor()
mcur.execute("select * from empdetail")
#mcur.execute("select * from empdetail where id=2")
for i in mcur:
    print(i)