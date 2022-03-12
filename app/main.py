from flask import Flask, render_template

app = Flask(__name__)
@app.route('/')
def home():
	   return render_template('home.html')
if __name__ == '__main__':
   app.run()

  # def index():
   # return "<h1>Testing... Testing.. 1..2...3...!</h1>"
