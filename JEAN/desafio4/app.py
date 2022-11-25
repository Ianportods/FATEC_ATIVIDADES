import email
from flask import Flask,render_template,request,flash,redirect,url_for
from flask_mysqldb import MySQL
 
app = Flask(__name__)
 
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'fatec'
app.config['MYSQL_DB'] = 'desafio4'
 
mysql = MySQL(app)


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
        cur.execute(''' INSERT INTO desafio4(email,assunto,descricao) VALUES(%s,%s,%s)''',[email,assunto, descricao])
        mysql.connection.commit()
        cur.close()
        return f"Done!!"
    return render_template("contato.html")
    
@app.route('/quemsomos')
def quemsomos():
    return render_template("quemsomos.html")



app.run(debug=True)
