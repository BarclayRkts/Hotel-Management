import os
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user=os.environ.get("user"),
    passwd=os.environ.get("passwd"),
    database="hospital"
)

def createPatient(data):
    mycursor = mydb.cursor()
    try:
        sql_insert = "INSERT INTO Patients VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        mycursor.execute(sql_insert,data)
        mydb.commit()
    except Exception as e:
        print(e)
        return 1
        
def getID():
    mycursor = mydb.cursor()
    id = mycursor.lastrowid
    return id
