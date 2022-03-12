from flask import Flask
app = Flask(__name__)

@app.route('/')
def homepage():
    return """
<!DOCTYPE html>
<head>
   <title>My title</title>
   <link rel="stylesheet" href="http://stash.compjour.org/assets/css/foundation.css">
</head>
<body style="width: 880px; margin: auto;">  
    <h1>Voting App Homepage</h1>
    <p>Login:</p>
</body>
"""

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)