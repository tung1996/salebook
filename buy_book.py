from flask import*
import requests 
from mani import*
# Mua sách (user)
@app.route('/buy_books', methods=['GET'])
def buy_books() :
    name = request.args.get("username")
    if not name :
        return("You need to login account")
    else :
        user = Account.query.filter_by(username = name ).first()
        if user.admin == "no" :
         # Hiển thị danh sách sách để  lựa chọn 
            all_book = []
            filter_book = []
            cart = []
            name_book = request.args.get("name_book")
            if not name_book :
                books = Book.query.all()
                for book in books :
                    name_book = book.name
                    all_book.append(name_book ) 
                return ({"all_book":all_book})
            else :
                data_book = Book.query.filter_by(name = name_book).first()
                try : 
                    filter_book = [data_book.name , data_book.price]
                    buy_book = request.args.get("buy_book") #1 là đặt hàng , 0 là thoát ve trang truoc
                    quantity = request.args.get("quantity")
                    quantity_new = float(quantity)   # ep kieu int ve float
                    total_price_book = quantity_new * data_book.price
                    if buy_book == '1':
                        # map id account vao bang Allorder
                        account = Account(user.username , user.password , user.fullname ,user.admin )
                        buy_Allorder = Allorder( account, total_price_book)
                        db.session.add( buy_Allorder )
                        db.session.commit()
                        # map id Book vao bang Allorder
                        book = Book(data_book.name , data_book.price)
                        buy_Orderdetail = Orderdetail(buy_Allorder ,book , quantity , total_price_book  )
                        db.session.add( buy_Orderdetail )
                        db.session.commit()                  
                        return ("ordered successfully")                  
                    else :
                        return ("return to the previous page")
                except :
                    return ("The book does not exist")
        else :
            return ("You are an administrator and cannot make purchases")

if __name__=="__main__":
    app.run()