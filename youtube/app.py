from flask import Flask,render_template,flash, redirect,url_for
from youtube import forms
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = '952447e6f6b2de95d33f254c4d150141'

posts=[
    {"author":"Corey Schafer",
     "title":"Blog Post 1",
     "content":"first post content",
     "date_posted":"April 20, 2019"},
    {"author":"jane dpe",
         "title":"Blog Post 2",
         "content":"second post content",
         "date_posted": "April 21, 2019"}
]

#routes are what we type in the browser to go to different pages
@app.route("/")
def home():
    return render_template("home.html", posts=posts) #rendering

@app.route("/about")
def about():
    return render_template("about.html",title='About')

@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm() #create an instance of class to send to the app
    if form.validate_on_submit(): #check
        flash(f"Account created for {form.username.data}!", 'success')
        return redirect(url_for('home'))
    return render_template('register.html',title='register',form=form) #render form object

@app.route("/login", methods = ['GET','POST'])
def login():
    form = LoginForm() #create an instance of class to send to the app
    return render_template('login.html',title='Login',form=form)


if __name__ == '__main__':
    app.run(debug=True)



