from flask import Flask, render_template
from helpers import get_db_connection

app = Flask(__name__)
app.config['SECRET_KEY'] = "syncshack2022"


class Application:

	def __init__(self, email):
		self.user_state = 0

		self.email = email #email

		conn = get_db_connection()

		self.user_subjects = () #subject list
		self.course = "" #course string
		self.faculty = "" #faculty string

		self.active_users = ()
		self.invited_users = ()
		self.accepted_users = ()
	
	def preferences(self):
		pass		


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
	conn = get_db_connection()
	posts = conn.execute('SELECT * FROM posts').fetchall()
	conn.close()
	return render_template('index.html', posts=posts)

@app.route('/signUp', methods=['GET', 'POST'])
def signup():
    return render_template("signup.html")

@app.route('/signUp/SignUpSubmit', methods=['GET', 'POST'])
def signup_click():
    return render_template("index.html")
