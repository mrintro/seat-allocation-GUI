import mysql.connector

mydb = mysql.connector.connect(host="localhost",user="root",database = "josaa")
mycursor = mydb.cursor()
mycursor.execute("select * from college")
res = mycursor.fetchall()
for i in res:
	print(i)
