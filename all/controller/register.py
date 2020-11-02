from all.database.connection import mycursor,mydb
import json
import pymysql.cursors

def ambilemail(email):
		mycursor.execute("""SELECT * FROM User WHERE email = %s""",(email))
		return mycursor

def register(name,gender,email,password):
	ambilemail(email)
	if(mycursor.rowcount==0):
		mycursor.execute("INSERT INTO User(name,gender,email,password,role) VALUES (%s,%s,%s,%s,%s)",(name,gender,email,password,"Client"))
		mydb.commit()
		ambilemail(email)
		rv = mycursor.fetchall()
		payload = []
		for result in rv:
			payload.append(result)
		return json.dumps(payload)
	else:
		return("email already registered")
		