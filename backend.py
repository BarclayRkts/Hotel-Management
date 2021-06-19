import os
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user=os.environ.get("user"),
    passwd=os.environ.get("passwd"),
    database="hospital"
)


