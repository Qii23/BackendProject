from all.database.connection import mycursor,mydb
import json
import pymysql.cursors

def register(name,gender):
	mycursor.execute("INSERT INTO User(name,gender,role) VALUES (%s,%s,%s)",(name,gender,"Client"))
	mydb.commit()
	x = mycursor.fetchall(mycursor.execute("""SELECT * FROM User WHERE name = %s""",(name)))
	y = []
	for i in x:
		y.append(i)
	return json.dumps(y)