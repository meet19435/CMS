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



def addComplainant(form):
	firstName = form.get("firstName")
	middleName = form.get("middleName")
	lastName = form.get("lastName")
	email = form.get("email")
	aadharCard = form.get("aadharCard")
	houseNo = form.get("houseNo")
	society = form.get("society")
	pinCode = form.get("pinCode")
	locality = form.get("locality")
	mobileNumber = form.get("mobileNumber")

	query = 'insert into complainant values (?,?,?,?,?,?,?,?,?,?)'
	data_1 = connect()
	cursor = getCursor(data_1)
	cursor.execute(query, (int(aadharCard),str(firstName),str(middleName),str(lastName),str(email),int(houseNo),str(society),str(locality),int(pinCode),int(mobileNumber)))

	#AadharCard bigint UN PK 
# First_Name varchar(50) 
# Middle_Name varchar(50) 
# Last_Name varchar(50) 
# Email varchar(150) 
# H_NO int 
# Society varchar(100) 
# Locality varchar(100) 
# PinCode int UN 
# MobileNo bigint UN