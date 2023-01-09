from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import current_user, login_user, logout_user, LoginManager, login_required, UserMixin
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pizza.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'filesystem'
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

db = SQLAlchemy(app)

class User(db.Model, UserMixin):
    is_active = True
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    surname = db.Column(db.String(50), nullable=False)
    phone = db.Column(db.String(11), nullable=False)
    email = db.Column(db.Text, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    cart = db.Column(db.Text, default='[]')

    def get_id(self):
        return self.id

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    desc = db.Column(db.Text, default='')
    price = db.Column(db.Integer, nullable=False)
    photo = db.Column(db.Text, default='/img/products/default.png')

login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return db.session.query(User).get(user_id)

@app.route('/')
def index():
    return render_template('index.html', user=current_user)

@app.route('/login.html', methods=["GET", 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        db_session = db.session
        email = request.form['email']
        password = request.form['password']
        remember = 'remember' in request.form.keys()

        user = db_session.query(User).filter(email == User.email).all()
        if not user:
            return render_template('login.html', message='Пользователя с такой почтой не существует', email=email)
        user = user[0]
        if not check_password_hash(user.password, password):
            return render_template('login.html', message='Неверный пароль, Попробуйте ещё раз', email=email)
        login_user(user, remember=remember)
        current_user.is_active = True
        return redirect('/')

@app.route('/logout.html')
@login_required
def logout():
    current_user.is_active = False
    logout_user()
    return redirect("/")

@app.route('/register.html', methods=["GET", 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    else:
        db_session = db.session
        name = request.form.get('name')
        surname = request.form.get('surname')
        phone = request.form.get('phone')
        email = request.form.get('email')
        password = request.form.get('password')
        data = {'name': name, 'surname': surname, 'phone': phone, 'email': email}
        if db.session.query(User).filter(email == User.email).first():
            return render_template('register.html', message='Пользователь с такой почтой уже существует', data=data)
        elif db.session.query(User).filter(phone == User.phone).first():
            return render_template('register.html', message='Пользователь с таким номером телефона уже существует', data=data)
        elif not email:
            return render_template('register.html', message='Заполните поля', data=data)
        new_user = User(name=name, surname=surname, phone=phone, email=email, password=generate_password_hash(password))
        db_session.add(new_user)
        db_session.commit()
        login_user(new_user, remember=False)
        current_user.is_active = True
        return redirect('/')

if __name__ == '__main__':
    app.run('localhost', 5000, debug=True)
