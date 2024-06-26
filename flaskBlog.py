from flask import Flask, render_template, url_for
app = Flask(__name__)

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

if __name__ == '__main__':
    app.run(debug=True)