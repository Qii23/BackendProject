from all.database.connection import mycursor,mydb
from flask import Flask, jsonify
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
import json
import uuid
import pymysql.cursors

def inputproduct(name,quantity,price):
	mycursor.execute("""SELECT * FROM product WHERE name = %s""",(name))
	if(mycursor.rowcount==0):
		mycursor.execute("INSERT INTO product(name,quantity,price) VALUES (%s,%s,%s)",(name,quantity,price))
		mydb.commit()
		mycursor.execute("""SELECT * FROM product WHERE name = %s""",(name))
		rv = mycursor.fetchall()
		payload = []
		for result in rv:
			payload.append(result)
		return json.dumps(payload)
	else:
		return("product already registered")

def updateproductquantity(name,quantity):
	mycursor.execute("""SELECT * FROM product WHERE name = %s""",(name))
	if(mycursor.rowcount>0):
		mycursor.execute("UPDATE product set quantity =%s where name = %s",(quantity,name))
		mydb.commit()
		mycursor.execute("""SELECT * FROM product WHERE name = %s""",(name))
		rv = mycursor.fetchall()
		payload = []
		for result in rv:
			payload.append(result)
		return json.dumps(payload)
	else:
		return("product not registered yet")

def updateproductprice(name,price):
	mycursor.execute("""SELECT * FROM product WHERE name = %s""",(name))
	if(mycursor.rowcount>0):
		mycursor.execute("UPDATE product set price =%s where name = %s",(price,name))
		mydb.commit()
		mycursor.execute("""SELECT * FROM product WHERE name = %s""",(name))
		rv = mycursor.fetchall()
		payload = []
		for result in rv:
			payload.append(result)
		return json.dumps(payload)
	else:
		return("product not registered yet")

def deleteproduct(name):
	mycursor.execute("""SELECT * FROM product WHERE name = %s""",(name))
	if(mycursor.rowcount>0):
		mycursor.execute("DELETE FROM product WHERE name= %s",(name))
		mydb.commit()
		mycursor.execute("""SELECT * FROM product WHERE name = %s""",(name))
		rv = mycursor.fetchall()
		payload = []
		for result in rv:
			payload.append(result)
		return json.dumps(payload)
	else:
		return("product not found")