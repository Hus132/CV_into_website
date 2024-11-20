from flask import Flask, render_template, flash, redirect
from .forms import LoginForm
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SECRET_KEY"] = "4766539ea38fd12b0f01bccbd9dd7075"

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///C:\\Users\\Dom\\PycharmProjects\\lesson1\\warehouse\\database.db"
db = SQLAlchemy(app)


@app.route('/')
def main_view():
    return render_template('home.html')
@app.route('/login', methods=['GET', 'POST'])
def login_view():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}. remember_me={}'.format(
            form.username.data, form.remember_me.data
        ))
        return redirect('home.html')
    return render_template('login.html', form = form)



