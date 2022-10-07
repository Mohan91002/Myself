import os
import mysql.connector
os.system("cls")

# mydb = mysql.connector.connect(
#     host="localhost",
#     user="Leo",
#     password="Radha@85209"
# )
# print(mydb)

mydb = mysql.connector.connect(
                                   host="localhost",
                                   user="Leo",
                                   password="Radha@85209"
                            )
mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE mydatabase") 