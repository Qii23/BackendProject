from all.database.connection import mycursor,mydb
from flask import Flask, jsonify
from all.controller.register import registers
from all.controller.login import logins
from all.controller.products import inputproduct,updateproductprice,updateproductquantity,deleteproduct
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
import json
import uuid
import pymysql.cursors

app = Flask(__name__)

@app.route("/register/<name>/<gender>/<email>/<password>", methods=['POST'])
def register(name,gender,email,password):
	return registers(name,gender,email,password)

@app.route("/login/<email>/<password>", methods=['GET'])
def login(email,password):
	return logins(email,password)

@app.route("/insertpr/<name>/<quantity>/<price>", methods=['POST'])
def insertpr(name,quantity,price):
	return inputproduct(name,quantity,price)

@app.route("/updateproductquantity/<name>/<quantity>", methods=['PUT'])
def updateprqty(name,quantity):
	return updateproductquantity(name,quantity)

@app.route("/updateproductprice/<name>/<price>", methods=['PUT'])
def updateprprc(name,price):
	return updateproductprice(name,quantity)

@app.route("/deleteproduct/<name>", methods=['DELETE'])
def deletepr(name):
	return deleteproduct(name)
	
for i in x:
	print(i)

if __name__ == "__main__":
	app.run(debug=True)
