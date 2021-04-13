from flask import *
from flask_sqlalchemy import SQLAlchemy
from flask import Request
import requests
from config import *
from model import *

class buy() :
    def order(self) :
        books = []
        buy = []
        account_id = request.args.get("id")
        name_quantity = {"hai so phan" : "1" , "nha gia kim" : "1"}
        data = requests.get("http://0.0.0.0:5001/check?id="+id+"")
        user = data.json()
        admin = user["admin"]
        if admin == 1 :
            return "You are the admin, so you can not buy"
        else :
            order = Order(account_id)
            db.session.add(order)
            db.session.commit()
            for name,quantity in name_quantity.items() :
                data_book = requests.get("http://127.0.0.1:5000/book?name_book="+name+"")
                book = data_book.json()
                book_id = book["id"]
                price = book["price"]
                etails = Order_etails(order ,book_id , quantity ,price )
                db.session.add(etails)
                db.session.commit()

            user = User.query.get(5)
            user.name = 'New Name'
            db.session.commit()




            return "you have placed your order successfully"
            
buy = buy ()

