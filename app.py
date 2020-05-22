import os

from flask import Flask, request, render_template, url_for, redirect, flash
from flask_mail import Mail, Message

app = Flask(__name__)
app.config.from_pyfile('config.py')
app.secret_key = os.urandom(16)
mail = Mail(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        if not (name and email):
            flash('We need your name and your email to send you updates 🤔')
            return redirect(url_for('index'))
        msg = Message(
            subject="Hello",
            sender=email,
            recipients=["to@example.com"],
            body=name
        )
        mail.send(msg)
        flash('Your form was sent ✌️')
        return render_template('layout.html')
    return render_template('index.html')
