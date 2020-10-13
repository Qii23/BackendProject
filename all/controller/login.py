from all.database.connection import mycursor,mydb
from flask import Flask, jsonify
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
import json
import uuid
import pymysql.cursors

def login(name):
	mydict = create_dict()
	mycursor.execute("""SELECT * FROM User WHERE name = %s""",(name))
	rv = mycursor.fetchall()
	payload = []
	content = {}
	for result in rv:
		content = {'id': result[1], 'name': result[2], 'gender': result[3], 'role': result[4]}
		payload.append(content)
		content = {}
	return jsonify(payload)