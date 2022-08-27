import sqlite3
from flask import Flask, render_template, redirect, request, url_for, session

app = Flask(__name__)
app.config['SECRET_KEY'] = "syncshack2022"


@app.route('/', methods=['GET', 'POST'])

def index():
	conn = get_db_connection()
	posts = conn.execute('SELECT * FROM posts').fetchall()
	conn.close()
	return render_template('index.html', posts=posts)

@app.route('/index', methods=['GET', 'POST'])
def index():
    return render_template("index.html")

@app.route('/signUp')

@app.route('/signIn')