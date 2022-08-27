import sqlite3
from flask import Flask, render_template, redirect, request, url_for, session

def get_db_connection():
	conn = sqlite3.connect('database.db')
	conn.row_factory = sqlite.Row
	return conn

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
