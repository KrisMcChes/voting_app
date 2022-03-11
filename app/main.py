from flask import Flask

app = Flask(__name__)
@app.route('/')
def index():
    return "<h1>Testing... Testing.. 1..2...3...!</h1>"
