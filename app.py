from flask import Flask, request , render_template,redirect,url_for,flash
import os
import mysql.connector as sqlConnect
import matplotlib.pyplot as plt
from datetime import date,datetime
from form import RegistrationForm, LoginForm

app = Flask(__name__)

@app.route('/login', methods = ['GET', 'POST'])
def login():
	if request.method == 'POST':
		email = request.form.get("email")
	return render_template('login.html', title = 'login')

if __name__ == '__main__':
	app.run(debug = True)


