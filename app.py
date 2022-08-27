from flask import Flask, render_template, redirect, request, session, url_for
from helpers import get_db_connection
from forms import SignUp, Login

import json

app = Flask(__name__)
app.config['SECRET_KEY'] = "syncshack2022"


class Application:

	def __init__(self, email):
		self.user_state = 0

		self.email = email #email

		

		self.user_subjects = () #subject list
		self.course = "" #course string
		self.faculty = "" #faculty string

		self.active_users = ()
		self.invited_users = ()
		self.accepted_users = ()
	
	def preferences(self):
		pass		


	def add_invitaiton( self , user ):
		
		conn = get_db_connection()
		cur = conn.cursor()
		cur.execute("Insert into invites (inviter, invitee) values ( {} , {}))".format( self.email, user))
		cur.close

	def incoming_invitation(self,user):
		conn = get_db_connection()
		cur = conn.cursor()
		cur.execute("select * form invites wehre invitee = {}".format(self.email))
		
		result = cur.fetchall
		
		if result != '': 
			return result[0]
		
		cur.close



@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
	conn = get_db_connection()
	posts = conn.execute('SELECT * FROM posts').fetchall()
	conn.close()
	return render_template('index.html', posts=posts)

@app.route('/signUp', methods=['GET', 'POST'])
def signUp():
    signUpForm = SignUp()
    if signUpForm.is_submitted():
        result_dict = request.form.to_dict()
        session['form1'] = json.dumps(result_dict)
        return redirect(url_for("index"))
    return render_template("signup.html", form = signUpForm)


@app.route('/login', methods=['GET', 'POST'])
def login():
    loginForm = Login()
    if loginForm.is_submitted():
        result_dict = request.form.to_dict()
        session['form1'] = json.dumps(result_dict)
        return redirect(url_for("index"))
    return render_template("login.html", form = loginForm)
