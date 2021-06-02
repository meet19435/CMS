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
	query = "select * from users where email = '" + str(email) + "' and pass = '"  + password+"'"
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
	User_Id = form.get("aadharCard")
	Username = form.get("userName")
	Pass = form.get("pwd")
	Type_ = "Complainant"
	query = 'insert into complainant (aadharcard, first_name,middle_name,last_name,email,h_no,society,locality, pincode,mobileno) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
	data_1 = connect()
	cursor = getCursor(data_1)
	data = (int(aadharCard),firstName,middleName,lastName,email,houseNo,society,locality,int(pinCode),int(mobileNumber))
	cursor.execute(query, data)
	
	# cursor.execute("select * from complainant limit 10")
	# for i in cursor:
	#     print(i)

	query = 'insert into users (User_Id, Email,Username,Pass,Type_) values (%s,%s,%s,%s,%s)'
	query = query.lower()
	data = (int(User_Id),email,Username,Pass,Type_)
	cursor.execute(query, data)
	
	# cursor.execute("select * from users where Type_= 'Complainant';")
	# query = query.lower()
	# for i in cursor:
	#     print(i)
	data_1.commit()
