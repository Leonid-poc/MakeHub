from flask import Flask, render_template

app = Flask(__name__)

# Test

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run('localhost', 5000, debug=True)
# Тест для Ранила с большой буквы