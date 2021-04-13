from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column , Integer,String, Float , ForeignKey
from flask_login import UserMixin
from config import *



class Account(db.Model,UserMixin):
    __tablename__= "account"
    id = Column( Integer , primary_key=True , autoincrement = True , nullable = False )
    username = Column( String(30) , nullable = False)
    password = Column( String(255), nullable = False) 
    fullname = Column ( String(50) , nullable = False)
    admin = Column( Integer , autoincrement = True) # neu la ad thi note là "1" con khong phai note vào "0"
    def __init__(self , username , password ,fullname , admin ) :
        self.username = username
        self.password = password
        self.fullname = fullname
        self.admin = admin

# @login.user_loader
# def load_user(id):
#     return Account.query.get(int(id))

db.create_all()
