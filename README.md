# Python Flask Tutorial: Personal Blog

- To run on local host:
  - Windows: set FLASK_APP = flaskBlog.py
  - Mac: export FLASK_APP = flaskBlog.py
  - flask run

- To open debugger:
  - Windows: set FLASK_DEBUG = 1
  - Mac: export FLASK_DEBUG = 1

### Running and Using Database
- To create db file:
  - from flaskBlog import app, db
  - app.app_context().push()
  - db.create_all()

- To import User and Post
  - from flaskBlog import User, Post

- To add an user:
  - user_X = User(username = 'Enter username', email = 'Enter email', password = 'Enter password')
  - db.session.add(user_X)
  - Note: userId is auto-incremented int as Primary Key for User table

- To commit:
  - db.session.commit()

- To view list of User:
  - User.query.all()

- To view a particular User: 
  - db.session.get(User, 1)
  - db.session.get(User, X)
  - User.query.first() // works only for first one

- To filter Users by username:
  -  User.query.filter_by(username = 'Enter username').all()
