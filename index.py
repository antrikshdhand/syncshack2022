import sqlite3
from flask import Flask, render_template, redirect, request, url_for, session

app = Flask(__name__)
app.config['SECRET_KEY'] = "syncshack2022"


@app.route('/', methods=['GET', 'POST'])

@app.route('/index', methods=['GET', 'POST'])
def index():
    return render_template("index.html")

@app.route('/signUp', methods=['GET', 'POST'])
def signup():
    return render_template("signup.html")

@app.route('/signUp/SignUpSubmit', methods=['GET', 'POST'])
def signup_click():
    return render_template("index.html")

