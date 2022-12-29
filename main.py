from werkzeug.security import generate_password_hash, check_password_hash
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pizza.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)



@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run('localhost', 5000, debug=True)
