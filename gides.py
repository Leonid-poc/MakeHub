from flask import Flask, url_for
from datetime import datetime
import os
import smtplib
from random import choice
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from flask import render_template, redirect, request
from flask_restful import abort
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_login import login_user
from loginform import LoginForm
from data import db_session
from data.users import User
from data.product import Product
from forms.user import RegisterForm
from flask_login import login_required
from flask_login import current_user
from flask_login import logout_user
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from forms.product import ProductForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


@app.route('/', methods=['GET', 'POST'])
def start():
    db_sess = db_session.create_session()
    if request.method == 'GET':
        product = db_sess.query(Product).all()
        return render_template('main.html', title='TopSwap', news=product)
    else:
        product = db_sess.query(Product).all()
        result = []
        for i in product:
            if request.form.get('search').lower() in i.title:
                result.append(i)
        return render_template('main.html', title='TopSwap', news=result)


@app.route('/help/<type_help>')
def helping(type_help):
    if type_help == 'team_about':
        return render_template('help.html')
    if type_help == 'faq':
        return render_template('help1.html')
    else:
        return render_template('help2.html')


@app.route('/<category>', methods=['GET'])
def category(category):
    if request.method == 'GET':
        db_sess = db_session.create_session()
        result = db_sess.query(Product).filter(Product.category == category.replace('%20', ' ')).all()
        return render_template('main.html', news=result)


@app.route('/register', methods=['GET', 'POST'])
def reqister():
    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Пароли не совпадают")
        db_sess = db_session.create_session()
        if db_sess.query(User).filter(User.email == form.email.data).first():
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Такой пользователь уже есть")
        user = User(
            surname=form.surname.data,
            name=form.name.data,
            patronymic=form.patronymic.data,
            email=form.email.data,
        )
        user.set_password(form.password.data)
        db_sess.add(user)
        db_sess.commit()
        return redirect('/login')
    return render_template('register.html', title='Регистрация', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(
            User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect("/")
        return render_template('login.html',
                               message="Неправильный логин или пароль",
                               form=form)
    return render_template('login.html', title='Авторизация', form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")


@app.route('/product_add', methods=['GET', 'POST'])
@login_required
def product_add():
    form = ProductForm()
    if form.is_submitted():
        db_sess = db_session.create_session()
        count = len(db_sess.query(Product).all())
        product = Product()
        product.title = form.title.data.lower()
        product.content = form.content.data
        product.connection = form.connection.data
        if not form.connection.data.isdigit() and str(form.connection.data) != 11 and not str(form.connection.data).startswith('8'):
            return render_template('product.html', title='Добавление записи',
                           form=form, message='Неверный формат ввода телефона')
        product.category = request.form['category']
        f = request.files['file']
        if not f.filename.split('.')[1] in ['png', 'jpg', 'bmp', 'ico', 'jpeg', 'gif']:
            return render_template('product.html', title='Добавление записи',
                           form=form, message='Неверный формат картинки')
        f = f.read()
        with open(f'static/img/file{count}.jpg', 'wb') as photo:
            photo.write(f)
        product.photo = str.encode(f'static/img/file{count}.jpg')
        current_user.product.append(product)
        db_sess.merge(current_user)
        db_sess.commit()
        return redirect('/')
    return render_template('product.html', title='Добавление записи',
                           form=form)


@app.route('/product', methods=['GET', 'POST'])
@login_required
def product():
    if request.method == 'GET':
        db_sess = db_session.create_session()
        result = db_sess.query(Product).filter(Product.user == current_user)
        return render_template('index.html', news=result)


@app.route('/product_edit/<int:idi>', methods=['GET', 'POST'])
def edit_product(idi):
    form = ProductForm()
    if request.method == "GET":
        db_sess = db_session.create_session()
        product = db_sess.query(Product).filter(Product.id == idi,
                                                Product.user == current_user
                                                ).first()
        if product:
            form.title.data = product.title.lower()
            form.content.data = product.content
            form.connection.data = product.connection
            form.category.data = product.category
            form.photo.data = product.photo
        else:
            abort(404)
    if request.method == "POST":
        db_sess = db_session.create_session()
        product = db_sess.query(Product).filter(Product.id == idi,
                                                Product.user == current_user
                                                ).first()
        if form.submit.data:
            if product:
                product.title = form.title.data.lower()
                product.content = form.content.data
                product.connection = form.connection.data
                if not form.connection.data.isdigit() and str(form.connection.data) != 11 and not str(form.connection.data).startswith('8'):
                    return render_template('product.html', title='Редактирование новости',
                                form=form, message='Неверный формат ввода телефона', delete=True)
                product.category = request.form['category']
                f = request.files['file']
                if not f.filename:
                    f = product.photo
                    with open(f.decode('utf-8'), mode='rb') as fi:
                        f = fi.read()
                elif not f.filename.split('.')[1] in ['png', 'jpg', 'bmp', 'ico', 'jpeg', 'gif']:
                    return render_template('product.html', title='Редактирование новости',
                                form=form, message='Неверный формат картинки', delete=True)
                else:
                    f = f.read()
                with open(f'static/img/file{idi - 1}.jpg', 'wb') as photo:
                    photo.write(f)
                product.photo = str.encode(f'static/img/file{idi - 1}.jpg')
                db_sess.commit()
                return redirect('/')
            else:
                abort(404)
        else:
            db_sess.delete(product)
            db_sess.commit()
            os.remove(f'static/img/file{product.id - 1}.jpg')
            return redirect('/')
    return render_template('product.html',
                           title='Редактирование новости', form=form, delete=True)


def data_sum(data):
    duration = datetime.now() - data
    duration_in_s = int(duration.total_seconds())
    if duration_in_s < 60:
        return f'Publicate {duration_in_s} seconds ago'
    duration_in_s //= 60
    if duration_in_s < 60:
        return f'Publicate {duration_in_s} minutes ago'
    duration_in_s //= 60
    if duration_in_s < 24:
        return f'Publicate {duration_in_s} hours ago'
    duration_in_s //= 24
    if duration_in_s < 7:
        return f'Publicate {duration_in_s} days ago'
    duration_in_s //= 7
    if duration_in_s < 12:
        return f'Publicate {duration_in_s} weeks ago'
    duration_in_s //= 12
    if duration_in_s < 52:
        return f'Publicate {duration_in_s} mounths ago'
    duration_in_s //= 52
    return f'Publicate {duration_in_s} years ago'


@app.route('/product/<idis>', methods=['GET', 'POST'])
def product_info(idis):
    db_sess = db_session.create_session()
    result = db_sess.query(Product).filter(Product.id == idis).first()
    data = data_sum(result.created_date)
    style = [('bg-primary', 'text-white'), ('bg-success', 'text-white'), ('bg-warning', 'text-dark')]
    if request.method == 'GET':
        return render_template('news.html', file=int(idis) - 1, result=result, data=data, style_of_card=choice(style))
    else:
        try:
            email = db_sess.query(User).filter(User.id == result.user_id).first().email
            addr_to   = email  
            addr_from = 'legeorg2004@gmail.com'
            password  = "legeorg@gmail"
            msg = MIMEMultipart()
            msg['From']    = addr_from
            msg['To']      = addr_to
            msg['Subject'] = 'В вашем товаре заинтересовались😎'

            html = f"""\
                    <html>
                    <head></head>
                    <body>
                        <p>
                        Зайдите на сайт TopSwap, в вашем товаре заинтересован: {current_user.surname} {current_user.name}
                        </p><br>
                        <p>Почта пользователя: {current_user.email}</p>
                        <img src='https://www.meme-arsenal.com/memes/e7955044a296301f97a33e2b33127787.jpg' alt='сорян, чёто гуглёныш подвёл'>
                    </body>
                    </html>
                    """
            msg.attach(MIMEText(html, 'html', 'utf-8'))
            server = smtplib.SMTP_SSL('smtp.mail.ru')
            server.login(addr_from, password)
            server.send_message(msg)
            server.quit()
            return render_template('news.html', file=int(idis) - 1, result=result, data=data, style_of_card=choice(style), message='Удачно')
        except Exception as e:
            print(e)
            return render_template('news.html', file=int(idis) - 1, result=result, data=data, style_of_card=choice(style), message='Неудалось отправить сообщение')


if __name__ == '__main__':
    db_session.global_init("db/blogs.db")
    # port = int(os.environ.get("PORT", 5000))
    app.run(host='127.0.0.1', port=8080, debug=True)
    #app.run(host='0.0.0.0', port=port)
# v)kghmh3*eWaY$B
# pyprojectflask@mail.ru