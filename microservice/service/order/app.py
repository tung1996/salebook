from flask import Flask
from flask_sqlalchemy import SQLAlchemy



from config import *
from model import *
from router.router import*
from flask_login import LoginManager




if __name__ == "__main__" :
    app.run(host= "0.0.0.0" ,port=5002)
    
   
    
