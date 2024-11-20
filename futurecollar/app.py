from flask import Flask, render_template,request,flash,redirect,url_for
import json
from flask_sqlalchemy import SQLAlchemy #base model for database



app = Flask (__name__)
app.config["SECRET_KEY"] = "4766539ea38fd12b0f01bccbd9dd7075" # to be able to use flash
#creating a database
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///C:\\Users\\Dom\\PycharmProjects\\lesson1\\database.db" #link to the location of the database to be created

db = SQLAlchemy(app) #create a database that will have connection with the aplication
# action_list=[]
#creating a table in the database
class Users(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    email = db.Column(db.String)
    password = db.Column(db.String)
    age = db.Column(db.String)

# a new table called History containing a message from app about tasks done
class History(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    record = db.Column(db.String)


# class Users(db.Table):
#     id = db.Column(db.Integer,primary_key=True)
#     email = db.Column(db.String)
#     password = db.Column(db.String)


with app.app_context():
    db.create_all()   #create a database file


#
# with open('users.json', 'r') as file:
#     # Load the contents of the file
#     users = json.load(file)
#
# def write_to_json(users_data):
#     with open('users.json', 'w') as file:
#         json.dump(users_data, file)  # indent=4 makes the JSON formatted nicely

@app.route("/")
def index_view():
    return render_template('index.html')


#creating a new view for displaying users
@app.route("/users")
def users_view():
    users_from_database = Users.query.all() #converting every every recod in database to python format
    return render_template('users.html',registered_users=users_from_database)
#
@app.route("/register", methods= ['GET','POST'])
def register_view():
    if request.form:
        email_from_form=request.form.get('email')

        existing_user = Users.query.filter(Users.email == email_from_form).first()
        if existing_user:
            flash('this email already exists', "warning")
        else:
            password_from_form = request.form.get('password')
            user = Users(email = email_from_form,password = password_from_form)
            db.session.add(user)

            message_to_data = f"{email_from_form} has been created"
            history1 = History(record = message_to_data)
            db.session.add(history1)
            db.session.commit() #collect allt that we have in session and send to database
            flash('email created successfully', 'message')
            return redirect(url_for('users_view'))

    return render_template('register_user.html')

@app.route('/history')
def history_view():
    actions = History.query.all()
    return render_template("history.html",actions = actions)

@app.route('/change-password', methods = ['GET','POST'])
def change_password_view():
    if request.form:
        email = request.form.get('email')
        existing_user = Users.query.filter(Users.email == email).first()
        if not existing_user:
            flash('email not registered',"warning")
            return render_template('change-password.html')
        current_password = request.form.get('current_password')
        if existing_user.password != current_password:
            flash("password does not match")
            return render_template('change-password.html')
        new_password = request.form.get('new_password')
        existing_user.password = new_password
        db.session.commit()





        current_password = request.form.get('current_password')
        new_password = request.form.get('new_password')


    return render_template('change-password.html')



