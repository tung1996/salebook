from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column , Integer,String, Float , ForeignKey,func
from sqlalchemy.orm import relationship
from config import *



class Order(db.Model):
    __tablename__= "order"
    id = Column( Integer , primary_key=True , autoincrement = True , nullable = False)
    account_id = Column( Integer , nullable = False )
    total_money = Column ( Float() , default = 0 , nullable = False)
    Order_etails = relationship("Order_etails" , backref = "order" , lazy= False)
    def __init__(self , account_id ,book_id , total_money ):
        self.account = account
        self.total_money = total_money

class Order_etails (db.Model):
    __tablename__= "order_etails"
    id = Column( Integer , primary_key=True , autoincrement = True , nullable = False)
    order_id = Column( Integer , ForeignKey(Order.id) , nullable = False )
    book_id = Column( Integer , nullable = False )
    quantity = Column(Integer ,default = 0 )
    into_money = Column (Float() ,default = 0 )
    def __init__(self ,order_id , quantity ,into_money ):
        self.order  = order
        self.book_id = book_id
        self.quantity = quantity
        self.into_money = into_money 

db.create_all()