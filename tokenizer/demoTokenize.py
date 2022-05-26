from turtle import clear
from matplotlib.pyplot import get
import mysql.connector
import getToken
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="minhtriet290601",
    database="ml"
)

mycursor = mydb.cursor()

mycursor.execute("select content from content")

result = mycursor.fetchall()
for x in result:
    getToken.tokenize(str(x[0]))
