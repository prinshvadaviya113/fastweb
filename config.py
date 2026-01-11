import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",   # change this
    database="flask_app"
)

cursor = db.cursor(dictionary=True)
