import mysql.connector as mc
mydb = mc.connect(host="127.0.0.1", user="root", password="nilesh",database="emp")
mcur = mydb.cursor()
sql = "INSERT INTO empdetail (id, fname, lname) VALUES (%s, %s, %s)"
val = (1, "Nilesh", "Indore")
#val = [ (2, "Arnav", "Indore"), (3, "Mayura", "Indore"), (4, "Manisha", "Indore") ]
mcur.execute(sql,val)
#mcur.executemany(sql,val)
mydb.commit()
print(mcur.rowcount, "record inserted") 
