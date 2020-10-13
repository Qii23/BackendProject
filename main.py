from all.database.connection import mycursor,mydb
from flask import Flask, jsonify
from all.controller.register import register
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
import json
import uuid
import pymysql.cursors

app = Flask(__name__)

@app.route("/register/<name>/<gender>", methods=['POST'])
def register(name,gender):
	return register(name,gender)

@app.route("/login/<name>", methods=['GET'])
def login(name):
	return login(name)
	
mycursor.execute("SELECT * FROM User")
x = mycursor.fetchall()

for i in x:
	print(i)

if __name__ == "__main__":
	app.run(debug=True)
