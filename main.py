from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import current_user, login_user, logout_user
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pizza.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    surname = db.Column(db.String(50), nullable=False)
    phone = db.Column(db.String(11), nullable=False)
    email = db.Column(db.Text, nullable=False)
    password = db.Column(db.String(30), nullable=False)
    cart = db.Column(db.Text, default='[]')

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    desc = db.Column(db.Text, default='')
    price = db.Column(db.Integer, nullable=False)
    photo = db.Column(db.Text, default='/img/products/default.png')

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run('localhost', 5000, debug=True)
