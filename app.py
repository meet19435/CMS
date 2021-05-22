from flask import Flask, request , render_template,redirect,url_for,flash
import os
import mysql.connector as sqlConnect
import matplotlib.pyplot as plt
from datetime import date,datetime
##from form import RegistrationForm, LoginForm
from database import *
from news import run


app = Flask(__name__)
app.config['SECRET_KEY']='2b293a243de5cb3f6d6e4eb4a0b526fa'


@app.route('/login', methods = ['GET', 'POST'])
def login():
	
	if request.method == 'POST' and request.form['action'] =='Login':
		
		email = request.form.get("email")
		password = request.form.get("pwd")
		isValid = checkCredentials(email,password)

		if(isValid):
			flash('Welcome to CMS','Success')
		else:
			flash('Incorrect Password or Email','failure')

		return redirect(url_for('login'))

	elif request.method == 'POST' and request.form['action'] == 'sign-up':
		
		return redirect(url_for('login'))

	return render_template('login.html', title = 'Login - CMS')

@app.route('/home')
@app.route('/')
def home():
	data_news = run(5)
	# test_news1 = data_news[0]
	# test_news2 = data_news[1]
	# test_news3 = data_news[2]
	# test_news4 = data_news[3]
	# test_news5 = data_news[4]
	return render_template('home.html', title = 'Home - CMS', news =data_news)

@app.route('/about')
def about():
	return render_template('about.html', title = 'About - CMS')

if __name__ == '__main__':
	app.run(debug = True)


