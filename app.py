from flask import Flask, render_template
from helpers import get_db_connection

app = Flask(__name__)
app.config['SECRET_KEY'] = "syncshack2022"

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

@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template("login.html")

@app.route('/login/LoginSubmit', methods=['GET', 'POST'])
def login_click():
    return render_template("main.html")
