from lib2to3.pgen2 import token
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
tokens = {}
mycursor.execute("select content from content")

result = mycursor.fetchall()
for x in result:
    tokens = getToken.tokenize(str(x[0]))
    tokens1 = {
    "token": tokens["words1"],
    "length": 1
    }
    print(tokens1)
    tokens2 = {
    "token": tokens["words2"],
    "length": 2
    }
    tokens3 = {
    "token": tokens["words3"],
    "length": 3
    }

# tao http request
