from flask import Flask,render_template,request,flash,redirect,url_for
from flask_sqlalchemy import SQLAlchemy

app= Flask(__name__)
app.config["SECRET_KEY"] = "4766539ea38fd12b0f01bccbd9dd7075"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///C:\\Users\\Dom\\PycharmProjects\\lesson1\\final\\database.db"

db=SQLAlchemy(app)



class Feedback(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String)
    email = db.Column(db.String)
    text = db.Column(db.String)
    rating = db.Column(db.Integer)


with app.app_context():
    db.create_all()
@app.route('/')
def index_view():
    feedback_from_database = Feedback.query.all()
    return render_template('index.html', feedback = feedback_from_database)

@app.route('/Experience')
def experience_view():
    return render_template('experience.html')

@app.route('/skills')
def skills_view():
    return render_template('skills.html')
@app.route('/feedback', methods = ['GET','POST'])
def feedback_view():
    if request.method == 'POST':
        name = request.form.get('name')
        email= request.form.get('email')
        text = request.form.get('message')
        rating = request.form.get('rating')
        feedback = Feedback(name = name, email = email,text = text,rating = rating)
        flash("Thank you for sending your feedback")
        db.session.add(feedback)
        db.session.commit()
        return redirect(url_for('index_view'))







    return render_template('feedback.html')

@app.route('/contact')
def contact_view():
    return render_template('contact.html')