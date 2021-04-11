from flask import *
from flask_sqlalchemy import SQLAlchemy
from flask import Request
import requests
import jsonify
from model import *
from flask_login import current_user, login_user
from flask_admin import Admin


class buy() :
    def order(self) :
        id = request.args.get("id") 
        data = requests.get("http://0.0.0.0:5001/check?id="+id+"")

        # else :
        #     return "kkkk"






        # name = request.args.get("name_book") 
        # quantity = request.args.get("quantity") 
        # data = requests.get("http://127.0.0.1:5000/book?name_book="+name+"")
        # book = data.json()
        # id = book["id"]
        # price = book["price"]


        
         

    




buy = buy ()