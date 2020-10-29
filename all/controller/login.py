from all.database.connection import mycursor,mydb
from flask import Flask, jsonify
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
import json
import uuid
import pymysql.cursors

def logins(email,password):
	mycursor.execute("""SELECT * FROM User WHERE email = %s and password =%s""",(email,password))
	if(mycursor.rowcount>0):
		mycursor.execute("""SELECT * FROM User WHERE email = %s""",(email))
		rv = mycursor.fetchall()
		payload = []
		for result in rv:
			payload.append(result)
		return json.dumps(payload)
	else:
		return("wrong email or password")