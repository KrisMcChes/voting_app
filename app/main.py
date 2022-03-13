from flask import Flask, render_template, redirect, url_for, request
app = Flask(__name__, template_folder="iCloud Drive/Desktop/voting_app/app/templates")

@app.route('/')
def homepage():
    return """
<!DOCTYPE html>
<head>
   <title>Voting Application</title>
   <link rel="stylesheet" href="http://stash.compjour.org/assets/css/foundation.css">
</head>
<body style="width: 880px; margin: auto;">  
    <h1>Voting App Homepage</h1>
    <p>Login:</p>
</body>
"""

@app.route('/welcome')
def welcome():
    return render_template('welcome.html')  # render a template


# # Route for handling the login page logic
# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     error = None
#     if request.method == 'POST':
#         if request.form['username'] != 'admin' or request.form['password'] != 'admin':
#             error = 'Invalid Credentials. Please try again.'
#         else:
#             return redirect(url_for('home'))
#     return render_template('iCloud Drive/Desktop/voting_app/app/templates/login.html', error=error)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
