from flask import Flask, render_template, redirect, url_for, request
# from models import db
app = Flask(__name__, template_folder="templates")


# # load config from the config file we created earlier 
# app.config.from_object('config')

# # initialize and create the database 
# db.init_app(app)
# db.create_all(app=app)

@app.route('/', methods=['GET', 'POST'])
def homepage():
   return render_template('homepage.html')  # render a template


@app.route('/welcome', methods=['GET', 'POST'])
def welcome():
    #    if request.method == 'POST':
    #     if request.form.get('action1') == 'VALUE1':
    #         pass # do something
    #     elif  request.form.get('action2') == 'VALUE2':
    #         pass # do something else
    #     else:
    #         pass # unknown
    #    elif request.method == 'GET':
    #     return render_template('welcome.html', form=form)
       return render_template('welcome.html')  # render a template


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
