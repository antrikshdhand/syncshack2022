# This file contains all helper functions used in app.py runner file 

import sqlite3

def get_db_connection():
	conn = sqlite3.connect('DB/database.db')
	conn.row_factory = sqlite3.Row
	return conn


def add_user(user_attributes):
	#establish connection
	
	connection = get_db_connection()
	cur = connection.cursor()

	#Validation of user_attributes
	if user_attributes[:-18] != "@uni.sydney.edu.au":
		return False

	if user_attributes[2] == '':
		user_attributes[2] = user_attributes[0]
	


	#adds userdata into the database
	cur.execute("INSERT INTO users (FirstName, LastName, PrefName, Email, Passw, UserStatus, Course, Faculty) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
	tuple(user_attributes))

	cur.close()
	return True

	
	
