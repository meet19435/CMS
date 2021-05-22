from flask import Flask, request , render_template,redirect,url_for,flash
import os
import mysql.connector as sqlConnect
import matplotlib.pyplot as plt
from datetime import date,datetime

user = "u2u9vvqbisjn9scr"
password = "fs01OrKhu9QPHYPi2UMq"
host = "bh10m2ejj9e6d5tqgjko-mysql.services.clever-cloud.com"
database = "bh10m2ejj9e6d5tqgjko"

def connect():
	data = sqlConnect.connect(user = user,password = password, host = host, database = database)
	return data

def getCursor(database):
	return database.cursor()

def executeQuery(query,cursor):
	temp_data = cursor.execute(query)
	arr = []
	for x in cursor:
		arr.append(x)
	return arr

def checkCredentials(email,password):

	data_1 = connect()
	cursor = getCursor(data_1)
	query = "select * from users where email = '" + str(email) + "' and pass = "  + password
	ans = executeQuery(query,cursor)
	
	if(len(ans) > 0):
		return True
	else:
		return False


