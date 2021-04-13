from flask import *
from flask_sqlalchemy import SQLAlchemy
from flask import request
from model import *

class search() :
    # hien thi tat ca danh sach sach
    def all_book (self) :
        all_book = []
        books = Book.query.all()
        for book in books :
            name_book = book.name
            all_book.append(name_book )
        return ({"all_book" : all_book })
    # tim kiem sach theo ten
    def search_name_book (self , name ) :
        data_book = []
        id = []
        price = []
        books = Book.query.filter(Book.name.startswith(name)).all()
        try :
            for book in books :
                data_book.append(book.name )
                id.append(book.id)
                price.append(book.price)
            return ({"book" : data_book ,"price": price , "id":id})
        except :
            return ("The book does not exist")

    # tim kiem sach theo gia
    def search_price (self, min_price ,max_price ) :
        data_price = []
        try :
            if min_price!= None and max_price != None :
                prices = Book.query.filter(Book.price.__gt__(min_price),Book.price.__lt__(max_price)).all()
                for price in prices:
                    data_price.append(price.name)
                return ({"filter_price ": data_price })
             # loc gia tu min price tro len
            elif min_price!= None and max_price == None :
                prices = Book.query.filter(Book.price.__gt__(min_price)).all()
                for price in prices:
                    data_price.append(price.name)
                return ({"filter_price ": data_price })
            # loc gia tu max price tro xuong
            elif min_price == None and max_price != None :
                prices = Book.query.filter(Book.price.__lt__(max_price)).all()
                for price in prices:
                    data_price.append(price.name)
                return ({"filter_price ": data_price })
        except :
            return ("there are no matching books") 
            
              
class filter_all() :
    def filter(self) :
        name = request.args.get("name_book")
        min_price = request.args.get("min_price")
        max_price = request.args.get("max_price")
        if not name and not min_price and not max_price :
            return search.all_book()
        elif name != None : 
            return search.search_name_book(name)
        elif min_price or max_price != None :
            return search.search_price(min_price , max_price)          


search = search()
filter_all = filter_all()

