from flask import render_template, redirect, url_for, request
from app import db
from app import app
from app.models import User
"""
import adafruit_fingerprint
from app import scanfinger
"""

# to delete database
# db.drop_all() 
db.create_all()
# to check
# print(User.query.all())
 
@app.route('/', methods=['GET', 'POST'])
def homepage():
   return render_template('homepage.html')  # render a template

@app.route('/welcome', methods=['GET', 'POST'])
def welcome():
    return render_template('welcome.html')  # render a template

@app.route('/user', methods=['GET', 'POST'])
def user():
   return render_template('user.html')  # render a template

@app.route('/createpoll', methods=['GET', 'POST'])
def createpoll():
   return render_template('createpoll.html')  # render a template

@app.route('/makevote', methods=['GET', 'POST'])
def makevote():
    return render_template('makevote.html')  # render a template

@app.route('/vote', methods=['GET', 'POST'])
def vote():
    return render_template('vote.html')  # render a template

"""
@app.route('/scanner', methods=['GET', 'POST'])
def scanner():
    scanfinger.run_scanner()
    return render_template('scanner.html')  # render a template
"""

@app.route("/register", methods=["GET", "POST"])
def register():
    # check the request method to ensure the handling of POST request only
    if request.method == "POST":
        # store the form value
        user_name = request.form["username"]
        password = request.form["password"]
        admin = request.form["admin"]
        
        # create an instance of the user table
        user = User(username = user_name, user_password = password, is_admin = admin)
        db.session.add(user)
        db.session.commit()

        # print(User.query.all())

        return redirect(url_for('welcome'))
    return render_template('register.html')

# Route for handling the login page logic
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        userName = request.form['username']
        password = request.form['password']
        userNameFound = None
        for user in User.query.all():
            if userName == user.username:
                userNameFound = user
                break
        if userNameFound == None:
            error = 'Invalid Username. Try again or ask an Admin for help.'
        elif userNameFound.user_password != password:
            error = 'Invalid password. Try again or ask an Admin for help.'
        elif userNameFound.is_admin == "Y":
            return redirect(url_for('welcome'))
        else: 
            return redirect(url_for('user'))
    return render_template('login.html', error=error)

# Create another database just for admins or redirect admins to another page

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)


# Things I may want to do:
# Get the isadmin into a checkbox to work with true/false
# Prevent people from just manually writing in the URL
# Adding fingerprint fields. 
# Is there a way to build in a file input so that an admin can select the fingerprint file from their computer?
# How do I set the thing to false to shutoff the warning? In init?