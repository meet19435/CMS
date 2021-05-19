from flask import Flask, request , render_template,redirect,url_for,flash
import os
import mysql.connector as sqlConnect
import matplotlib.pyplot as plt
from datetime import date,datetime
from form import RegistrationForm, LoginForm
from database import *

app = Flask(__name__)

@app.route('/login', methods = ['GET', 'POST'])
def login():
	
	if request.method == 'POST':
		email = request.form.get("email")
	return render_template('login.html', title = 'Login - CMS')

@app.route('/home')
@app.route('/')
def home():
	return render_template('home.html', title = 'Home - CMS')

@app.route('/about')
def about():
	return render_template('about.html', title = 'About - CMS')

if __name__ == '__main__':
	app.run(debug = True)


