from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import current_user, login_user, logout_user, LoginManager
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
    password = db.Column(db.String(200), nullable=False)
    cart = db.Column(db.Text, default='[]')

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    desc = db.Column(db.Text, default='')
    price = db.Column(db.Integer, nullable=False)
    photo = db.Column(db.Text, default='/img/products/default.png')

login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    db_sess = db.create_session()
    return db_sess.query(User).get(user_id)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login.html', methods=["GET", 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        print(request.form)
        return redirect('/')

@app.route('/register.html', methods=["GET", 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    else:
        db_session = db.create_session()
        name = request.form.get('name')
        surname = request.form.get('surname')
        phone = request.form.get('phone')
        email = request.form.get('email')
        password = request.form.get('password')
        if db.session.query(User).filter(email == User.email).first():
            return render_template('register.html', message='Пользователь с такой почтой уже существует')
        elif db.session.query(User).filter(phone == User.phone).first():
            return render_template('register.html', message='Пользователь с таким номером телефона уже существует')
        new_user = User(name=name, surname=surname, phone=phone, email=email, password=generate_password_hash(password))
        db_session.add(new_user)
        db_session.commit()
        return redirect('/')

if __name__ == '__main__':
    app.run('localhost', 5000, debug=True)
