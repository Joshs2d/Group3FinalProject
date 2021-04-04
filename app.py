import mysql.connector
from datetime import date
import datetime

db = mysql.connector.connect(

    host = "us-cdbr-east-03.cleardb.com",
    user = "b2838d74df3cc6",
    password = "1679be15",
    database = "heroku_86594902d2459c3"

)

cursor = db.cursor()

cursor.execute("SHOW TABLES")
print(cursor.fetchone())

#cursor.execute("INSERT INTO Users VALUES (2, 'Bob')")




db.commit()
cursor.close()
db.close()