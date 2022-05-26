from lib2to3.pgen2.tokenize import tokenize
from operator import le
import nltk
from nltk import word_tokenize
from flask import jsonify, request, Flask
from flask_restful import Resource, Api
import requests

app = Flask(__name__)
api = Api(app)
nltk.download('punkt')

tokenizer = word_tokenize


@app.route('/tokenize', methods=['POST'])
def tokenize_ans():
    data = request.json
    print(data['content'])
    sentence = data['content']
    return tokenize(sentence)


def tokenize(sentence):
    symbol = [",", ".", "!", ":", "?", "...",
              "-", "(", ")", ";", "[", "]","{","}","`","'","/","|","<",">","%",'"',"@","#","$","^","&","*"]

    sentence = sentence.strip()

    for x in symbol:
        sentence = sentence.replace(x, "")

    words = tokenizer(sentence)
    words2 = tokenizer(sentence)
    words3 = tokenizer(sentence)
    print(words)

    for i in range(len(words)-1):
        words2[i] = words2[i] + " " + words2[i+1]

    print(words2)

    for i in range(len(words)-2):
        words3[i] = words3[i] + " " + words3[i+1] + " " + words3[i+2]

    print(words3)

    ans = {}
    ans["words1"] = words
    ans["words2"] = words2
    ans["words3"] = words3
    return ans


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9370)
# http request gửi 3 arrays dạng json flask
