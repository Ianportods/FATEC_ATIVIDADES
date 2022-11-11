import email
from flask import Flask,render_template,request,flash,redirect,url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contato')
def contato():
    return render_template("contato.html")

@app.route('/quemsomos')
def quemsomos():
    return render_template("quemsomos.html")



app.run(debug=True)
