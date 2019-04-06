from flask import Flask
from flask import Blueprint, flash, redirect, render_template, request, session, abort
import os
from sqlalchemy.orm import sessionmaker
from model import *
from db import *
from service_api.api import user_api

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tutorial.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.register_blueprint(user_api)
db.init_app(app)


@app.route('/')
def home():
	if not session.get('logged_in'):
		return render_template('login.html')
	else:
		username = session.get('username')
		return "Hello "+username+"!  <a href=""/logout"">Logout</a>"
 
@app.route('/login', methods=['POST'])
def do_admin_login():
	POST_USERNAME = str(request.form['username'])
	POST_PASSWORD = str(request.form['password'])
 
	Session = sessionmaker(bind=engine)
	s = Session()
	query = s.query(User).filter(User.username.in_([POST_USERNAME]), User.password.in_([POST_PASSWORD]) )
	result = query.first()
	
	if result:
		session['logged_in'] = True
		session['username'] = POST_USERNAME
	else:
		flash('wrong password!')
	return home()
 
@app.route("/logout")
def logout():
	session['logged_in'] = False
	return home()
 
if __name__ == "__main__":
	app.secret_key = os.urandom(12)
	app.run(debug=True,host='127.0.0.1', port=5000)
