from all.database.connection import mycursor,mydb
from flask import Flask, jsonify
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
import json
import uuid
import pymysql.cursors

def ambilnama(name):
		mycursor.execute("""SELECT * FROM product WHERE name = %s""",(name))
		return mycursor

def inputproduct(name,quantity,price):
	ambilnama(name)
	if(mycursor.rowcount==0):
		mycursor.execute("INSERT INTO product(name,quantity,price) VALUES (%s,%s,%s)",(name,quantity,price))
		mydb.commit()
		ambilnama(name)
		rv = mycursor.fetchall()
		payload = []
		for result in rv:
			payload.append(result)
		return json.dumps(payload)
	else:
		return("product already registered")

def updateproduct(name,quantity,price):
	ambilnama(name)
	if(mycursor.rowcount>0):
		mycursor.execute("UPDATE product set quantity =%s, price=%s where name = %s",(quantity,price,name))
		mydb.commit()
		ambilnama(name)
		rv = mycursor.fetchall()
		payload = []
		for result in rv:
			payload.append(result)
		return json.dumps(payload)
	else:
		return("product not registered yet")

def deleteproduct(name):
	ambilnama(name)
	if(mycursor.rowcount>0):
		mycursor.execute("DELETE FROM product WHERE name= %s",(name))
		mydb.commit()
		ambilnama(name)
		rv = mycursor.fetchall()
		payload = []
		for result in rv:
			payload.append(result)
		return json.dumps(payload)
	else:
		return("product not found")
		