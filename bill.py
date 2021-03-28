from flask import*
import requests 
from mani import*
@app.route('/bull', methods=['GET'])
def bull():
    name_book = []
    Information = []
    account_id = request.args.get("account_id")
    # user , ten sach , so luong , don gia , thanh tien)
    try :
        orders = Allorder.query.filter_by(account_id = account_id).all()
        for order in orders :
            books = Orderdetail.query.filter_by(order_id = order.id).all()
            for book in books :
                # quantity = book.quantity
                name_book = db.session.query(Book.name , Orderdetail.quantity , Book.price , Orderdetail.into_money ).join(Orderdetail).filter(Orderdetail.book_id == book.id).all()

        return ({"name_book" : name_book })
    except :
        return ("You have no orders")



if __name__=="__main__" :
    app.run()