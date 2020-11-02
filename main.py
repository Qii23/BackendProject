from all.database.connection import mycursor,mydb
from flask import Flask, jsonify
from all.controller.register import register
from all.controller.login import login
from all.controller.products import inputproduct,updateproduct,deleteproduct
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
import json
import uuid
import pymysql.cursors

app = Flask(__name__)

@app.route("/register/<name>/<gender>/<email>/<password>", methods=['POST'])
def rgstr(name,gender,email,password):
	return register(name,gender,email,password)

@app.route("/login/<email>/<password>", methods=['POST'])
def lgn(email,password):
	return login(email,password)

@app.route("/insertproduct/<name>/<quantity>/<price>", methods=['POST'])
def insertpr(name,quantity,price):
	return inputproduct(name,quantity,price)

@app.route("/updateproduct/<name>/<quantity>/<price>", methods=['PUT'])
def updateprdct(name,quantity,price):
	return updateproduct(name,quantity,price)

@app.route("/deleteproduct/<name>", methods=['DELETE'])
def deletepr(name):
	return deleteproduct(name)

if __name__ == "__main__":
	app.run(debug=True)
