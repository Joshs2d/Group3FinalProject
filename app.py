from flask import Flask, render_template, url_for, request, redirect
<<<<<<< Updated upstream
=======
#from flask_mysql_connector import MySQL
#from flask_sqlalchemy import SQLAlchemy
from models.Users import Users

 
app = Flask(__name__, template_folder='templates')
#app.config['MYSQL_USER'] = 'b2838d74df3cc6'
#app.config['MYSQL_PASSWORD'] = "1679be15" 
#app.config['MYSQL_DATABASE'] = 'heroku_86594902d2459c3'

>>>>>>> Stashed changes

from sqlalchemy import DDL, event
from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models.Users import Users
from models.Recipes import Recipes


app = Flask(__name__, template_folder='templates')

DB_URL = 'mysql+pymysql://b2838d74df3cc6:1679be15@us-cdbr-east-03.cleardb.com/heroku_86594902d2459c3?'
engine = create_engine(DB_URL, echo=True)
Session = sessionmaker(bind=engine)
session = Session()



@app.route('/')
def index():
    return render_template('index.html')



@app.route('/', methods = ['POST', 'GET'])
def post():

    if request.method == 'POST':

        text = request.form['content']
        new_rec = Recipes(RECName = text)
        session.add(new_rec)
        session.commit()

        return render_template('index.html')

    else:
        return render_template('index.html')



if __name__ == "__main__":
    app.run(debug=True)