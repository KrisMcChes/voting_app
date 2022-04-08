from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy

# from app import views
# from app import models

# from flask_bootstrap import Bootstrap
# from flask_wtf import FlaskForm
# from wtforms import StringField, SubmitField
# from wtforms.validators import DataRequired
# from flask.cli import with_appcontext
# import sqlite3
# import click

app = Flask(__name__, template_folder="templates")

app.config["SECRET_KEY"] = 'admin'
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///registration.db'

db = SQLAlchemy(app)

def init_db():
    db.init_app(app)
    db.app = app
    db.create_all()

class UserDetails(db.Model):
    # table column id
    user_id = db.Column(db.Integer, primary_key = True)
    
    # table column name with data type of String
    user_name = db.Column(db.String, nullable = False) 

class User(db.Model):
    id = db.Column(db.Integer, primary_key =True)
    username = db.Column(db.String(100), nullable = False)
    user_email = db.Column(db.String(100), nullable= False)
    user_password = db.Column(db.String(150), nullable = False)

# #db stuff
# def get_db():
#     if 'db' not in g:
#         g.db = sqlite3.connect(
#             current_app.config['DATABASE'],
#             detect_types=sqlite3.PARSE_DECLTYPES
#         )
#         g.db.row_factory = sqlite3.Row

#     return g.db

# def close_db(e=None):
#     db = g.pop('db', None)

#     if db is not None:
#         db.close()

# def init_db():
#     db = get_db()

#     with current_app.open_resource('schema.sql') as f:
#         db.executescript(f.read().decode('utf8'))

# @click.command('init-db')
# @with_appcontext
# def init_db_command():
#     """Clear the existing data and create new tables."""
#     init_db()
#     click.echo('Initialized the database.')

# def init_app(app):
#     app.teardown_appcontext(close_db)
#     app.cli.add_command(init_db_command)

# Flask-WTF requires an encryption key - the string can be anything
# app.config['SECRET_KEY'] = 'admin'
# Bootstrap(app)


@app.route('/', methods=['GET', 'POST'])
def homepage():
   return render_template('homepage.html')  # render a template

@app.route('/welcome', methods=['GET', 'POST'])
def welcome():
         return render_template('welcome.html')  # render a template

@app.route('/makevote', methods=['GET', 'POST'])
def makevote():
         return render_template('makevote.html')  # render a template

@app.route('/register', methods=['GET', 'POST'])
def register():
         return render_template('register.html')  # render a template

# Route for handling the login page logic
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Login. Try again or ask an Admin for help.'
        else:
            return redirect(url_for('welcome'))
    return render_template('login.html', error=error)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
