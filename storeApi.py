from werkzeug.wrappers import request, Response
from flask import Flask, jsonify, request
from store import getProducts, allsoap, allshampoo


app = Flask(__name__)
@app.route('/store', methods = ['GET'])
def home():
    if(request.method == 'GET'):
        return getProducts()

@app.route('/soap', methods = ['GET'])
def soap():
    if(request.method == 'GET'):
        return allsoap()

@app.route('/shampoo', methods = ['GET'])
def shampoo():
    if(request.method == 'GET'):
        return allshampoo()

if __name__ == '__main__':
  from werkzeug.serving import run_simple
  run_simple('localhost', 5000, app)