from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column , Integer,String, Float , ForeignKey,func
from sqlalchemy.orm import relationship
from config import *
app = Flask (__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:@localhost/order?charset=utf8mb4"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]= 'False'
db = SQLAlchemy(app=app)



class Order(db.Model):
    __tablename__= "Order"
    id = Column( Integer , primary_key=True , autoincrement = True , nullable = False)
    account_id = Column( Integer , nullable = False )
    book_id = Column( Integer , nullable = False )
    total_money = Column ( Float() , default = 0 , nullable = False)
    cart = relationship("Cart" , backref = "order" , lazy= False)

    def __init__(self , account_id ,book_id , total_money ):
        self.account = account
        self.book_id = book_id
        self.total_money = total_money

class Cart(db.Model):
    __tablename__= "cart"
    id = Column( Integer , primary_key=True , autoincrement = True , nullable = False)
    order_id = Column( Integer , ForeignKey(Order.id) , nullable = False )
    quantity = Column(Integer ,default = 0 )
    into_money = Column (Float() ,default = 0  )
    def __init__(self ,order_id , quantity ,into_money ):
        self.order  = order
        self.quantity = quantity
        self.into_money = into_money 