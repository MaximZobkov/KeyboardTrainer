from flask import Flask, render_template
from flask_login import LoginManager
# import requests
from random import choice
from data import db_session

app = Flask(__name__)
app.config['SECRET_KEY'] = 'clavatrainer.ru'
db_session.global_init("db/blogs.sqlite")


@app.route("/")
def main_page():
    string = ""
    symbol_rus = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя "
    for i in range(60):
        string = string + choice(symbol_rus)
    return render_template("index.html", symbol=symbol_rus, string=string)


def main():
    app.run()


if __name__ == '__main__':
    main()
