from flask import*
from flask import Request
from controller.controller import buy
from model import*
import requests

@app.route('/buy_book', methods= ['GET'])
def buy_book():
    return  buy.order()
    
    