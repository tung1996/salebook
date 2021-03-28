from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column , Integer,String, Float , ForeignKey,func
from sqlalchemy.orm import relationship

app = Flask (__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:@localhost/sales_manager?charset=utf8mb4"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]= 'False'
db = SQLAlchemy(app=app)

class Book(db.Model):
    __tablename__= "book"
    id = Column( Integer , primary_key = True , autoincrement = True , nullable = False )
    name = Column( String(255) , nullable = False)
    price = Column( Float() , nullable = False)
    orderdetail = relationship("Orderdetail" , backref = "book" , lazy= False)
    def __init__(self , name, price ):
        self.name = name
        self.price = price

class Account(db.Model):
    __tablename__= "account"
    id = Column( Integer , primary_key=True , autoincrement = True , nullable = False )
    username = Column( String(30) , nullable = False)
    password = Column( String(8), nullable = False) 
    fullname = Column ( String(50) , nullable = False)
    admin = Column( String(11) , nullable = False) # neu la ad thi note là "yes" con khong phai note vào "no"
    book = relationship("Allorder" , backref = "account" , lazy= False)
    def __init__(self , username , password ,fullname , admin ) :
        self.username = username
        self.password = password
        self.fullname = fullname
        self.admin = admin
    
class Allorder(db.Model):
    __tablename__= "allorder"
    id = Column( Integer , primary_key=True , autoincrement = True , nullable = False)
    account_id = Column( Integer ,ForeignKey(Account.id), nullable = False )
    total_money = Column ( Float() , default = 0 , nullable = False)
    orderdetail = relationship("Orderdetail" , backref = "orderdetail" , lazy= False)
    def __init__(self , account ,total_money ):
        self.account = account
        self.total_money = total_money

class Orderdetail(db.Model):
    __tablename__= "orderdetail"
    id = Column( Integer , primary_key=True , autoincrement = True , nullable = False)
    order_id = Column( Integer , ForeignKey(Allorder.id) , nullable = False )
    book_id = Column( Integer ,ForeignKey(Book.id) , nullable = False )
    quantity = Column(Integer ,default = 0 )
    into_money = Column (Float() ,default = 0  )
    def __init__(self ,orderdetail , book , quantity ,into_money ):
        self.orderdetail  = orderdetail
        self.book = book
        self.quantity = quantity
        self.into_money = into_money 

db.create_all()

# ac1 = Account("nguyen dinh thi " , "000001" ,"nguyen dinh thi", "yes")
# db.session.add(ac1)
# db.session.commit()


# ac2 = Allorder(ac1 ,170000)
# db.session.add(ac2)
# db.session.commit()

ac3 = Book("hai con duong" ,100000)
db.session.add(ac3)
db.session.commit()

# ac4 = Orderdetail(ac2 , ac3, 2,19000)
# db.session.add(ac4)
# db.session.commit()



