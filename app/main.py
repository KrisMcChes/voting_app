from flask import Flask, render_template, redirect, url_for, request
# from flask_bootstrap import Bootstrap
# from flask_wtf import FlaskForm
# from wtforms import StringField, SubmitField
# from wtforms.validators import DataRequired
# from flask.cli import with_appcontext
# import sqlite3
# import click

voteapp = Flask(__name__, template_folder="templates")

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
# voteapp.config['SECRET_KEY'] = 'admin'
# Bootstrap(app)


@voteapp.route('/', methods=['GET', 'POST'])
def homepage():
   return render_template('homepage.html')  # render a template


@voteapp.route('/welcome', methods=['GET', 'POST'])
def welcome():
         return render_template('welcome.html')  # render a template

@voteapp.route('/makevote', methods=['GET', 'POST'])
def makevote():
         return render_template('makevote.html')  # render a template

# Route for handling the login page logic
@voteapp.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Login. Try again or ask an Admin for help.'
        else:
            return redirect(url_for('welcome'))
    return render_template('login.html', error=error)

if __name__ == '__main__':
    voteapp.run(debug=True, use_reloader=True)
