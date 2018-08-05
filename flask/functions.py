# Flask adalah firmworknya..
# render_template untuk kita bisa merender file HTML dari folder Templates,
# url_for agar kita bisa menghubungkan url ke function / def
# flash semacam aler pada java script
#RegistrationForm frame work untu kreg forms
#LoginForm juga sama
#redirect untuk menhubungkan ke halaman yang di inginkan
from datetime import datetime
from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
# kita sekarang masuk ke dalam databases, mengunakan flask_sqlalchemy
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SECRET_KEY'] = '5b36e59b9c51311fd305c00aa3'

# berikut ini adalah pengaturan dimana databse kita taruh,
# kita akan menggunakan sqlita
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///site.db"
db = SQLAlchemy(app)

class User(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	username = db.Column(db.String(20), unique = True, nullable = False)
	email = db.Column(db.String(120), unique = True, nullable = False)
	image_file = db.Column(db.String(20), nullable = False, default = 'default.jpg')
	password = db.Column(db.String(100), nullable = False, )

	def __repr__(self):
		return "User(f'{self.username}','{self.email}','{self.image_file}')"

class Post(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	title = db.Column(db.String(100), nullable = False )
	date_posted = db.Column(db.DateTime, nullable = False, default = datetime.utcnow)
	content = db.Column(db.Text, nullable = False)

	def __repr__(self):
		return "Post(f'{self.title}','{self.date_posted}')"

posts = [
	{
			"author" : "selastio fadli rahman",
			"title" : "Blog Post 1",
			"content" : "First content blog",
			"date_post" : "April, 20 2018"

	},
	{
			"author" : "tammy suryana",
			"title" : "Blog Post 2",
			"content" : "Second content blog",
			"date_post" : "April, 21 2018"
	}


]



@app.route("/")
@app.route("/home")
def home():
	return render_template("home.html",posts=posts)

@app.route("/about")
def about():
	return render_template("about.html", title="about")

@app.route("/register", methods=['GET','POST'])
def register():
	form = RegistrationForm()
	if form.validate_on_submit():
		flash('account succes created', 'success')
		return redirect(url_for('home'))
	return render_template("register.html", title="register", form=form)

@app.route("/login", methods=["POST","GET"])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		if form.email.data == "fadliselaz@gmail.com" and form.password.data == "fadliselaz13":
			flash("login succesful..","success")
			return redirect(url_for('home'))
		else:
			flash("please check username or password", "danger")
	return render_template("login.html", title="login", form=form)


if __name__ == "__main__":
	app.run(debug = True)
