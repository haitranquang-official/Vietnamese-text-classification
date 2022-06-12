from turtle import clear
from matplotlib.pyplot import get
import csv
import requests
import getToken
file = open("F:\Code\HUST\Vietnamese-text-classification\content.csv", encoding="utf8")
csvreader = csv.reader(file)
header = next(csvreader)
result = []
for row in csvreader:
    result.append(row)
for x in result:
    strArr = getToken.tokenize(str(x))
    elements_count = {}

# iterating over the elements for frequency
    for element in strArr:
        if element in elements_count:
            elements_count[element] += 1
        else:
            elements_count[element] = 1

        # printing the elements frequencies
        # for key, value in elements_count.items():
        #     print(f"{key}: {value}")
    
    send_element = {}
    send_element['url'] = 'https://vnexpress.net/viem-nao-mo-cau-benh-nguy-hiem-co-the-lay-lan-sau-covid-4459615.html'
    send_element['frequencyMap'] = elements_count
    try:
        requests.post('http://192.168.1.200:1092/api/token',json=send_element)
    except:
        continue
