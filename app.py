from flask import Flask, render_template, url_for, request, redirect

from sqlalchemy import DDL, event, select
from sqlalchemy import Column, Integer, String, Table, MetaData
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models.Users import Users
from models.Recipes import Recipes


app = Flask(__name__, template_folder='templates')

DB_URL = 'mysql+pymysql://b2838d74df3cc6:1679be15@us-cdbr-east-03.cleardb.com/heroku_86594902d2459c3?'
engine = create_engine(DB_URL, echo=True)

metadata = MetaData()
connection = engine.connect()

Session = sessionmaker(bind=engine)
session = Session()
@app.route('/')
def index():

    return render_template('index.html')



@app.route('/login')
def page_login():

    return render_template('login.html')



@app.route('/signup')
def page_signup():

    return render_template('signup.html')

@app.route('/fridge', methods = ["POST", "GET"])
def myFridge():
    usersFridge = getTableContent('Users')
    return render_template('myfridge.html', content = usersFridge, methods = ['GET', 'POST'])

@app.route('/acfn_login', methods = ['POST'])
def login():

    EM = request.form['EM']
    PW = request.form['PW']
    local_instance = [EM, PW]

    print("Local Instance: ", local_instance)

    if request.method == 'POST':

        server_instance = getTableContent('users')
        
        if validate(server_instance, local_instance):

            print("Login Successful")
            return render_template('index.html')
        
        else:

            print("Login Failed")
            return render_template('login_fail.html')



@app.route('/acfn_signup', methods = ['POST'])
def signup():

    if request.method == 'POST':

        FN = request.form['FN']
        LN = request.form['LN']
        PH = request.form['PH']
        EM = request.form['EM']
        PW = request.form['PW']
        CPW = request.form['CPW']

        if PW == CPW:

            new_user = Users(Fname = FN, Lname = LN, Phone = PH, Email = EM, UPassword = PW)
            session.add(new_user)
            session.commit()
            
        else:

            print("Passwords don't match!")
            return

    return render_template('login.html')



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



def getTableContent(tableName):

    #Fetching data from 'user' table.
    census = Table(tableName, metadata, autoload=True, autoload_with=engine)
    query = select([census])
    proxy = connection.execute(query)
    result = proxy.fetchall()

    return result



def validate(server_instance, local_instance):

    for i in server_instance:

        print("Server Instance", i)

        #Email&Password validation:
        if i[4] == local_instance[0] and i[5] == local_instance[1]:

            return True



if __name__ == "__main__":
    app.run(debug=True)