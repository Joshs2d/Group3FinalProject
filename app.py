from flask import Flask, render_template, url_for, request, redirect

import time

from sqlalchemy import DDL, event, select
from sqlalchemy import Column, Integer, String, Table, MetaData
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.inspection import inspect


from models.Users import Users
from models.Recipes import Recipes
from models.Ingredientlist import Ingredientlist

from models.Recipes2 import Recipes2
from models.Ingredientlist2 import Ingredientlist2
from models import initialize_sql, Session, session


app = Flask(__name__, template_folder='templates')


DB_URL = 'mysql+pymysql://b2838d74df3cc6:1679be15@us-cdbr-east-03.cleardb.com/heroku_86594902d2459c3?'
engine = create_engine(DB_URL, echo=True, pool_pre_ping=True)

metadata = MetaData()
connection = engine.connect()
initialize_sql(engine)


curr_user = None
PK = 0


@app.route('/')
def index():

    recipes = getTableContent('recipes2')

    return render_template('index.html', viewer=recipes)
    


@app.route('/login')
def page_login():
    
    return render_template('login.html')


@app.route('/signup')
def page_signup():
    
    return render_template('signup.html')


@app.route('/aboutus')
def page_aboutus():

    return render_template('aboutus.html')

@app.route('/blog')
def page_blog():

    return render_template('blog.html')

@app.route('/aboutus')
def page_aboutus():
    
    return render_template('aboutus.html')



@app.route('/blog')
def page_blog():
    
    return render_template('blog.html')



@app.route('/myfridge')
def page_myFridge():

    print("curr_user == None is: ", curr_user == None)
    
    if curr_user == None:
        
        return render_template('login.html')

    else:

        usersFridge = getTableContent('Users')
        return render_template('myfridge.html', content = usersFridge, methods = ['GET', 'POST'])



@app.route('/acfn_login', methods = ['POST'])
def login():
    
    global curr_user
    EM = request.form['EM']
    PW = request.form['PW']
    local_instance = [EM, PW]

    if(curr_user == None):

        if request.method == 'POST':

            server_instance = getTableContent('users')
            #[0] vali? [1] PK
            valResult = validate(server_instance, local_instance)
            global PK
            PK = valResult[1]
            
            if valResult[0]:

                print("Login Successful")
                curr_user = Users(UID = valResult[1])

                print(curr_user)
                return render_template('index.html')

            else:
                
                print("Login Failed")
                return render_template('login_fail.html')

    else:

        return render_template('index.html')



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



@app.route('/acfn_addRecipe', methods = ['POST', 'GET'])
def post():

    global PK

    if request.method == 'POST':

        RecName = request.form['RecName']
        RecIns = request.form['RecIns']

        IngreList = request.form.getlist('IngreList')
        IngreString = ', '.join(IngreList)
        new_ingredientlist = Ingredientlist2(Ingredient = IngreString)

        addIngredientList(new_ingredientlist)
        FK = int(getPK('ingredientlist2'))
        print("FK is: ", FK)
        
        new_rec = Recipes2(RecName = RecName, RecDescription = RecIns, PersonID = PK, IngredientListID = FK)
        session.add(new_rec)

        session.commit()
        

        return render_template('myfridge.html')

    else:

        return render_template('login_fail.html')



def addIngredientList(obj):

    session.add(obj)
    session.commit()



def getTableContent(tableName):

    #Fetching data from 'user' table.
    census = Table(tableName, metadata, autoload=True, autoload_with=engine)
    query = select([census])
    proxy = connection.execute(query)
    result = proxy.fetchall()

    return result



#Get the PK of the last entry in a table.
def getPK(tableName):

    result = getTableContent(tableName)
    print("Length is", len(result), result)
    
    if len(result) == 1:
        return result[0][0]

    else:
        return result[len(result)-1][0]



def validate(server_instance, local_instance):

    for i in server_instance:

        print("Server Instance", i)

        #Email&Password validation:
        if i[4] == local_instance[0] and i[5] == local_instance[1]:

            return True, server_instance[0]




if __name__ == "__main__":
    app.run(debug=True)