import mysql.connector as mc
mydb = mc.connect(host="127.0.0.1", user="root", password="nilesh",database="emp")
mcur = mydb.cursor()
mcur.execute("drop database emp")
mydb.commit()