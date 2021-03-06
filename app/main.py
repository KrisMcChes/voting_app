from flask import Flask, render_template, redirect, url_for, request, jsonify
app = Flask(__name__)
from app import db
from app import app
from app.models import User

"""
# Adafruit Library
import adafruit_fingerprint
from app import scanfinger
"""

# to delete database
# db.drop_all() 
db.create_all()
# to check
# print(User.query.all())
is_admin = False;
is_user = False;
 
@app.route('/', methods=['GET', 'POST'])
def homepage():
    global is_admin
    global is_user
    is_admin = False;
    is_user = False;
    return render_template('homepage.html')  # render a template

@app.route('/welcome', methods=['GET', 'POST'])
def welcome():
    if (is_admin == True): 
        return render_template('welcome.html')  # render a template
    else:
        return render_template('error.html')  

@app.route('/user', methods=['GET', 'POST'])
def user():
    if (is_user == True): 
        return render_template('user.html')  # render a template
    else:
        return render_template('error.html')  # render a template

@app.route('/createpoll', methods=['GET', 'POST'])
def createpoll():
    if (is_admin == True): 
           return render_template('createpoll.html')  # render a template
    else:
        return render_template('error.html') 

@app.route('/makevote', methods=['GET', 'POST'])
def makevote():
    if (is_admin == True): 
        return render_template('makevote.html')  # render a template
    else:
        return render_template('error.html')  # render a template

@app.route('/vote', methods=['GET', 'POST'])
def vote():
    if (is_user == True): 
        return render_template('vote.html')  # render a template
    else:
        return render_template('error.html')  # render a template

""" Fingerprint Functions """
@app.route('/scanner', methods=['GET', 'POST'])
def scanner():
    if (is_admin == True): 
        return render_template('scanner.html')  # render a template
    else:
        return render_template('error.html')  # render a template

@app.route('/enrollFinger')
def enrollFinger():
    scanfinger.enroll_finger(scanfinger.get_num())
    print('In enrollFinger')
    return "Nothing"
    
@app.route('/runScanner')
def runScanner():
    print('In Run Scanner Function')
    scanfinger.run_scanner()
    return
""" **************** """

@app.route("/register", methods=["GET", "POST"])
def register():
    if (is_admin == True): 
        # check the request method to ensure the handling of POST request only
        if request.method == "POST":
            # store the form value
            user_name = request.form["username"]
            password = request.form["password"]
            admin = request.form["admin"]
            fingerprint1 = 0
            fingerprint2 = 0

            # create an instance of the user table
            user = User(username = user_name, user_password = password, is_admin = admin, fingerprint1 = fingerprint1, fingerprint2 = fingerprint2)
            db.session.add(user)
            db.session.commit()

            # print(User.query.all())

            return redirect(url_for('scanner'))
        return render_template('register.html')
    else:
        return render_template('error.html')  # render a template


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
                Kris_variable = user.fingerprint2
                print(Kris_variable)
                userNameFound = user
                break
        if userNameFound == None:
            error = 'Invalid Username. Try again or ask an Admin for help.'
        elif userNameFound.user_password != password:
            error = 'Invalid password. Try again or ask an Admin for help.'
        elif userNameFound.is_admin == "Y":
            global is_admin
            is_admin = True;
            return redirect(url_for('welcome'))
        else: 
            global is_user
            is_user = True;
            return redirect(url_for('user'))
    return render_template('login.html', error=error)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)


# Things I may want to do:
# Get the isadmin into a checkbox to work with true/false - Have the checkbox working but I don't know
# what it ouputs or how to use that (get boolean in database)
# How do I set the thing to false to shutoff the warning? In init?
# Getting vote/polls logic to work with the databse