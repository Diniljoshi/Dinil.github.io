import mysql.connector
mydb = mysql.connector.connect(host="localhost",user="root",password="")
if mydb:
    print("Connection established")
else:
    print("No connection")
