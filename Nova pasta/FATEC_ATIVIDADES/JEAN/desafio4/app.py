import email
from flask import Flask,render_template,request,flash,redirect,url_for
from flask_mysqldb import MySQL
 
app = Flask(__name__)
 
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'flask'
 
mysql = MySQL(app)

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
