from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '8ef72f366f117819272af4c0205107ff52ecbbd9'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

class user(db.model):
	id = db.column(db.Integer, primary_key=True)
	username = db.column(db.String(10), unique=True, nullable=False)
	email = db.column(db.String(10), unique=True, nullable=False)
	image = db.column(db.String(20), nullable=False, default='default.jpg')
	password = db.column(db.String(60), nullable=False)

	def __repr__(self):
		return f"user('{self.username}', '{self.email}', '{self.image}')"
		
posts = [
	{
		'author': "Gladys Gachoka",
		'title': "Blog post 1",
		'content': "My first post content",
		'date_posted': "May 9, 2018"
	},
	{
		'author': "Joan Gachoka",
		'title': "Blog post 2",
		'content': "My second post content",
		'date_posted': "May 10, 2018"
	}
]

@app.route("/")
@app.route("/home")
def home():
	return render_template("home.html", posts=posts)

@app.route("/about")
def about():
	return render_template("about.html", title="About")

@app.route("/register", methods=['GET', 'POST'])
def register():
	form = RegistrationForm()
	if form.validate_on_submit():
		flash(f'Account created for {form.username.data}!', 'success')
		return redirect(url_for('home'))
	return render_template("register.html", title="Register", form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		if form.email.data == "gladys@gmail.com" and form.password.data == "sssss":
			flash('You have been logged in!', 'success')
			return redirect(url_for('home'))
		else:
			flash('Login unsuccessful. Please check username and password', 'danger')
	return render_template("login.html", title="Login", form=form)

if __name__ == "__main__":
    app.run(debug=True) #the debug will automatically update the code on the browser