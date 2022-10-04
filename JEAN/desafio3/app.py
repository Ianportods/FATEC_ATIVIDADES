import email
from flask import Flask,render_template,request,flash,redirect,url_for

app = Flask(__name__)

@app.contato('/contato/')
def contato():
    if email != "":
        return render_template('index.html')


app.run(debug=True)
