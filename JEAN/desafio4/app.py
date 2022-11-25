import email
from flask import Flask,render_template,request,flash,redirect,url_for
from flask_mysqldb import MySQL
 
app = Flask(__name__)
 
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '123456'
app.config['MYSQL_DB'] = 'cadastro'
 
mysql = MySQL(app)

#Creating a connection cursor

 
#Executing SQL Statements



 
#Saving the Actions performed on the DB
 
#Closing the cursor

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contato', methods = ['POST', 'GET'])
def contato():
     
    if request.method == 'POST':
        email = request.form['email']
        assunto = request.form['assunto']
        descricao = request.form['descricao']
        cur = mysql.connection.cursor()
        cur.execute(''' INSERT INTO cadastro(email,assunto,descricao) VALUES(%s,%s,%s)''',[email,assunto, descricao])
        mysql.connection.commit()
        cur.close()
        return f"Done!!"
    return render_template("contato.html")
    
@app.route('/quemsomos')
def quemsomos():
    return render_template("quemsomos.html")



app.run(debug=True)
