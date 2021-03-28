from flask import*
import requests 
from mani import*
#  Hiển thị danh sách sách, tìm kiếm sách theo tên, giá 
@app.route('/book', methods=['GET'])
def all_book() :
    # Hiển thị danh sách sách
    all_book = []
    filter_book = []
    filter_price = []
    books = Book.query.all()
    for book in books :
        name_book = book.name
        all_book.append(name_book )
    #  tìm kiếm sách theo tên , gia 
    name = request.args.get("name_book")
    min_price = request.args.get("min_price")
    max_price = request.args.get("max_price")
    if not name and not min_price and not max_price :
        return ({"all_book" : all_book })
    # loc sach theo ten 
    elif name != None :
        data_book = Book.query.filter_by(name = name).first()
        try :
            filter_book= [data_book.name , data_book.price]
            return ({"name book" : data_book.name ,
            "price" : data_book.price  })
        except :
            return ("The book does not exist")
    # loc sach theo gia
    elif min_price!= None and max_price != None : 
        names = Book.query.filter(Book.price.__gt__(min_price),Book.price.__lt__(max_price)).all()
        for name in names:
            filter_price.append(name.name)
        return ({"filter_price ": filter_price })
    # loc gia tu min price tro len
    elif min_price!= None and max_price == None :
        names = Book.query.filter(Book.price.__gt__(min_price)).all()
        for name in names:
            filter_price.append(name.name)
        return ({"filter_price ": filter_price })
    # loc gia tu max price tro xuong
    elif min_price == None and max_price != None :
        names = Book.query.filter(Book.price.__lt__(max_price)).all()
        for name in names:
            filter_price.append(name.name)
        return ({"filter_price ": filter_price })

# Hiển thị danh sách admin  
@app.route('/all_admin', methods=['GET'])
def all_admin() :
    data = []
    users = Account.query.filter_by(admin = 'yes').all()
    for user in users :
        name = user.username
        data.append(name)
    return ({"data": data})


if __name__=="__main__":
    app.run()