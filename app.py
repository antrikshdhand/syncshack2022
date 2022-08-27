from multiprocessing import connection
from flask import Flask, render_template, redirect, request, session, url_for
from helpers import get_db_connection, add_subjects, add_user
from forms import SignUp1, SignUp2, SignUp3, Login

import json

app = Flask(__name__)
app.config['SECRET_KEY'] = "syncshack2022"


class Application:

	def __init__(self, email):
		self.user_state = 0

		self.email = email #email

		#Connect to database and get course and faculty from users table
		connection = get_db_connection()
		cur = connection.cursor()
		cur.execute("SELECT * FROM users WHERE Email='{}'".format(self.email))
		row = cur.fetchone()
		cur.close()

		self.course = row['Course'] #course string
		self.faculty = row['Faculty'] #faculty string
		self.user_subjects = []

		#reset connection and get subjects from enrolled table
		cur = connection.cursor()
		cur.execute("SELECT UnitOfStudy FROM enrolled WHERE Email='{}'".format(self.email))
		subjects = cur.fetchall()
		for subject in subjects:
			self.user_subjects.append(subject[0])
		cur.close()

		#set up active_users
		self.active_users = []
		self.invited_users = []
		self.accepted_users = []

	def get_units_of_study(self):
		return self.user_subjects
	
	def preferences(self, subject):
		preffered_buddies = []

		connection = get_db_connection()
		cur = connection.cursor()
		#get only users with status online
		cur.execute("SELECT Email FROM users natural join enrolled where status=1 and UnitOfStudy='{} and Email != {}'".format(subject, self.email))
		online_users = cur.fetchall()
		if online_users[0] not in preffered_buddies:
			if len(preffered_buddies) == 5:
				return preffered_buddies
			preffered_buddies.append(online_users[0])



		cur.execute("SELECT Email FROM users where status=1 and Course = {}".format(self.course))
		online_users = cur.fetchall()
		if online_users[0] not in preffered_buddies:
				if len(preffered_buddies) == 5:
					return preffered_buddies
				preffered_buddies.append(online_users[0])



		cur.execute("SELECT Email FROM users where status=1 and Faculty = {}".format(self.faculty))
		online_users = cur.fetchall()
		if online_users[0] not in preffered_buddies:
				if len(preffered_buddies) == 5:
					return preffered_buddies
				preffered_buddies.append(online_users[0])



		cur.execute("SELECT Email FROM users where status=1")
		online_users = cur.fetchall()
		if online_users[0] not in preffered_buddies:
				if len(preffered_buddies) == 5:
					return preffered_buddies
				preffered_buddies.append(online_users[0])

		
		return preffered_buddies
	
	def get_buddy_data(self, subject):
		buddies = []
		self.active_users = self.preferences(subject)
		connection = get_db_connection()
		cur = connection.cursor()
		
		#for each email
		for user in self.active_users:
			cur.execute("SELECT * FROM users WHEN Email={}".format(user))
			row = cur.fetchone()
			#append the email, name, unit of study
			buddies.append([row['Email'], row['name'], subject])
		
		return buddies
			
	def get_invited_data(self, subject):
		users = []
		connection = get_db_connection()
		cur = connection.cursor()
		for user in self.invited_users:
			cur.execute("SELECT * FROM users WHEN Email={}".format(user))
			row = cur.fetchone()
			users.append([row['Email'], row['name'], subject])
		return users



	def add_invitaiton( self , user ):
		self.active_users.remove(user)
		self.invited_users.append(user)
		conn = get_db_connection()
		cur = conn.cursor()
		cur.execute("Insert into invites (inviter, invitee) values ( {} , {}))".format( self.email, user))
		cur.close

	def incoming_invitation(self,user):
		conn = get_db_connection()
		cur = conn.cursor()
		cur.execute("select * form invites WHEN invitee = {}".format(self.email))
		
		result = cur.fetchall()
		#review
		#REALLY REVIEW
		
		if result != '': 
			return result[0]
		
		cur.close()

	



@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
@app.route('/index.html', methods=['GET', 'POST'])
def index():
	conn = get_db_connection()
	posts = conn.execute('SELECT * FROM posts').fetchall()
	conn.close()
	return render_template('index.html', posts=posts)

@app.route('/signUp1', methods=['GET', 'POST'])
def signUp1():
	signUpForm1 = SignUp1()
	if signUpForm1.is_submitted():
		result_dict = request.form.to_dict()
		session['form1'] = json.dumps(result_dict)
		print(session['form1'])
		profile = list(result_dict.values())[:-1]
		# send profile to Jack

		# print(profile)
				
		# return redirect(url_for("myprofile"))
		return redirect(url_for("signUp2"))
	return render_template("signup1.html", form = signUpForm1)

@app.route('/signUp2', methods=['GET', 'POST'])
def signUp2():
	signUpForm2 = SignUp2()
	if signUpForm2.is_submitted():
		course_info = request.form.to_dict()
		session['form2'] = (course_info)
		print(session['form2'])
		# send course_info to Jack

		return redirect(url_for("signUp3"))

	return render_template("signup2.html", form = signUpForm2)

@app.route('/signUp3', methods=['GET', 'POST'])
def signUp3():
	signUpForm3 = SignUp3()
	form2 = session['form2']
	print(form2)
	units = form2['noOfUnits']
	

	if signUpForm3.is_submitted():
		result_dict = request.form.to_dict()
		unit_list = list(result_dict.values())[:-1]
		# send unit list to Jack

		return redirect(url_for("myprofile"))
	return render_template("signup3.html", form = signUpForm3, units = units)

@app.route('/login', methods=['GET', 'POST'])
def login():
    loginForm = Login()
    if loginForm.is_submitted():
        result_dict = request.form.to_dict()
        session['login'] = (result_dict)
        return redirect(url_for("myprofile"))
    return render_template("login.html", form = loginForm)

@app.route('/myprofile', methods=['GET', 'POST'])
def myprofile():
	form2 = session['form2']
	print(form2)
	# units = form2['noOfUnits']
	return render_template("myprofile.html", len=5)
