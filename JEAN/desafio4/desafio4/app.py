
from flask import Flask,render_template,request
from flask_mysqldb import MySQL
 
app = Flask(__name__)
 
app.config['MYSQL_HOST'] = '100.26.194.138'
app.config['MYSQL_USER'] = 'fatec'
app.config['MYSQL_PASSWORD'] = 'fatec'
app.config['MYSQL_DB'] = 'desafio5'
 
mysql = MySQL(app)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contato', methods = ['POST', 'GET'])
def contato():
     
    if request.method == 'POST':
        email = request.form['email']
        assunto = request.form['assunto']
        descrisao = request.form['descricao']
        cur = mysql.connection.cursor()
        cur.execute(''' INSERT INTO desafio5(email,assunto,descrisao) VALUES(%s,%s,%s)''',[email,assunto, descrisao])
        mysql.connection.commit()
        cur.close()
        return f"Done!!"
    return render_template("contato.html")
    
@app.route('/quemsomos')
def quemsomos():
    return render_template("quemsomos.html")



app.run(debug=True)
