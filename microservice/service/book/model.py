from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column , Integer,String, Float , ForeignKey
from config import *


class Book(db.Model):
    __tablename__= "book"
    id = Column( Integer , primary_key = True , autoincrement = True , nullable = False )
    name = Column( String(255) , nullable = False)
    price = Column( Float() , nullable = False)
    def __init__(self , name, price ):
        self.name = name
        self.price = price

db.create_all()
