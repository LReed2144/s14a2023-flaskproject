from flask import Flask, render_template
import json


app = Flask(__name__)
links = [
    {"label": "Login", "url": "/login"},
    {"label": "Home", "url": "/home"},
    {"label": "About", "url": "/about"},
    {'label': 'List', 'url': '/list'},
    {'label': 'Contact', 'url': '/contact'}
]
# extra line
@app.route("/")
def index():
    return render_template('index.html', navigation=links)


@app.route("/home")
def home():
    return render_template('home.html', navigation=links)


@app.route('/about')
def about():
    return render_template('about.html', title='About', navigation=links)


@app.route('/list')
def list():
    with open('data.json', 'r') as f:
        table_data = json.load(f)
    return render_template('list.html', title='List', navigation=links, table_data=table_data)


@app.route('/registration')
def registration():

    return render_template('registration.html', title='Registration', navigation=links)


@app.route('/login')
def login():

    return render_template('login.html', title='Login', navigation=links)


@app.route('/contact')
def contact():
    return render_template('contact.html', title='contact', navigation=links)


