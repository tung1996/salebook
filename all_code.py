from flask import*
import requests 
from mani import*
# dang nhap ac 
@app.route('/login', methods= ['POST'])
def login():
    body = request.get_json()
    if not "username" in body or not "password" in body :
        return ("username or password empty")
    else :
        user = Account.query.filter_by(username=body["username"]).first()                                        
        try :
            username = user.username
            if user.password == body["password"] :
                return ("Logged in successfully")
            else :
                return ("wrong password")
        except :
            return ("username does not exist")
      
#  dang ky ac
@app.route('/sign_up', methods=['POST'])
def sign_up():
    body = request.get_json()
    if not "username" in body  or not "password" in body  or not "password_retype" in body or not "fullname" in body or not "admin" in body :
       return ("lack of information")
    else :
        if body["password"] == body["password_retype"]:
            user = Account.query.filter_by(username=body["username"]).first() 
            try :
                user = user.username 
                return ("Username already exists")
            except : 
                try :
                    new_ac = Account(body["username"] , body["password"] ,body["fullname"] ,body["admin"])
                    db.session.add(new_ac)
                    db.session.commit()
                    return ("create account successfully")
                except :
                    return ("Syntax error")
        else :
                return ("password error")

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

from flask import*
import requests 
from mani import*
@app.route('/bull', methods=['GET'])
def bull():
    name_book = []
    Information = []
    account_id = request.args.get("account_id")
    try :
        orders = Allorder.query.filter_by(account_id = account_id).all()
        for order in orders :
            books = Orderdetail.query.filter_by(order_id = order.id).all()
            for book in books :
                name_book = db.session.query(Book.name , Orderdetail.quantity , Book.price , Orderdetail.into_money ).join(Orderdetail).filter(Orderdetail.book_id == book.id).all()
        return ({"name_book" : name_book })
    except :
        return ("You have no orders")

if __name__=="__main__" :
    app.run()
