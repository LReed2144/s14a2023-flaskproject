from flask import Flask, render_template, request, redirect, url_for, session
import json

import requests
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail, Message
import uuid

db = SQLAlchemy()

app = Flask(__name__)
app.secret_key = 'ABCDEFG'

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'lyndsey@gmail.com'
app.config['MAIL_PASSWORD'] = '1234'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)

postgres_connection_string = "postgresql://doadmin:AVNS_8l9GVHut1Gdw3ZxvSLB@db-postgresql-sfo3-s14a2023-do-user-14318939-0.b.db.ondigitalocean.com:25060/s14a2023?sslmode=require"
app.config["SQLALCHEMY_DATABASE_URI"] = postgres_connection_string

db.init_app(app)

links = [
    {"label": "Login", "url": "/login"},
    {"label": "Home", "url": "/home"},
    {"label": "About", "url": "/about"},
    {'label': 'List', 'url': '/list'},
    {'label': 'Contact', 'url': '/contact'},
    {'label': 'Users', 'url': '/users'}
]


class Users(db.Model):
    email = db.Column(db.String)
    phonenumber = db.Column(db.String)
    updated_at = db.Column(db.String)
    status = db.Column(db.Integer)
    is_admin = db.Column(db.Boolean)
    id = db.Column(db.Integer, primary_key=True, nullable=False)

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
    

# class Order(db.Model):
#     id = db.Column(db.Integer)
#     item_name = db.Column(db.String)
#     item_count = db.Column(db.Integer)
#     total = db.Column(db.Integer)
#     user_id = db.Column(db.Integer)
    

#     def as_dict(self):
#         return {c.name: getattr(self, c.name) for c in self.__table__.columns}


@app.route("/users")
def userList():
    session['visited_list'] = True
    # Query the whole table
    userList = Users.query.order_by(Users.email).all()
    return render_template('users.html', users=userList)


@app.route('/adduser', methods=['POST'])
def add():
    if request.method == 'POST':
        email = request.form['email']
        status = request.form['status']
        is_admin = request.form['is_admin']
        new_user = Users(email=email, status=status, is_admin=is_admin)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('userList'))



@app.route('/updateuser', methods=['POST'])
def update():
    return redirect(url_for('userList'))


@app.route('/deleteuser', methods=['POST'])
def delete_user():
    user_id = int(request.form.get('user_id'))
    user = Users.query.get(user_id)

    if user:
        db.session.delete(user)
        db.session.commit()

    return redirect(url_for('userList',navigation=links))


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
        table = json.load(f)
    return render_template('list.html', col='List', navigation=links, table=table)


@app.route('/registration')
def registration():
    return render_template('registration.html', title='Registration', navigation=links)


@app.route('/login')
def login():
    return render_template('login.html', title='Login', navigation=links)


@app.route('/contact')
def contact():
    return render_template('contact.html', title='contact', navigation=links)

if __name__ == "__main__":
    app.run(debug=False)
