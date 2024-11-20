from flask import Flask, render_template


app = Flask(__name__)



@app.route('/')
def login_view():
    return render_template('login.html')
