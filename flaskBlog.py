from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = 'ff68d2a4488eeccf02bd672209001b65'

posts = [
  {
    'author': 'Joyce Guo',
    'title': 'Blog 1',
    'content': 'Just started this tutorial',
    'date_posted': 'June 25, 2024'
  },
  {
    'author': 'Joyce Guo',
    'title': 'Blog 2',
    'content': 'Made a bet with Brian to see who finishes this first',
    'date_posted': 'June 25, 2024'
  },
  
]

@app.route("/home")
def home():
  return render_template('home.html', posts=posts)

@app.route("/about")
def about():
  return render_template('about.html', title = 'About')

@app.route("/register")
def register():
  form = RegistrationForm()
  return render_template('register.html', title = 'Register', form = form)

@app.route("/login")
def login():
  form = LoginForm()
  return render_template('login.html', title = 'Login', form = form)


if __name__ == '__main__':
    app.run(debug=True)