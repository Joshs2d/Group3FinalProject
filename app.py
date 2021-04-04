import mysql.connector
from flask import Flask, render_template, url_for, request, redirect
#from flask_mysql_connector import MySQL
#from flask_sqlalchemy import SQLAlchemy
from models.Users import Users


app = Flask(__name__, template_folder='templates')
#app.config['MYSQL_USER'] = 'b2838d74df3cc6'
#app.config['MYSQL_PASSWORD'] = "1679be15" 
#app.config['MYSQL_DATABASE'] = 'heroku_86594902d2459c3'


db = mysql.connector.connect(

    host = "us-cdbr-east-03.cleardb.com",
    user = "b2838d74df3cc6",
    password = "1679be15",
    database = "heroku_86594902d2459c3"

)

cursor = db.cursor()




@app.route('/')
def index():
    return render_template('index.html')


@app.route('/', methods = ['POST', 'GET'])
def post():

    if request.method == 'POST':

        new_recipe = Users(0, '')
        cursor.execute("SELECT * FROM Recipes;")
        rows = len(cursor.fetchall()) + 1
        text = request.form['content']

        SQL = "INSERT INTO Recipes VALUES(" + "{v1}, '{v2}');".format(v1 = rows, v2 = text)

        try:
            cursor.execute(SQL)
            db.commit()
            return render_template('index.html')

        except:
            return 'There was an issue adding a new recipe.'

    else:
        
        return render_template('index.html')




    



if __name__ == "__main__":
    app.run(debug=True)