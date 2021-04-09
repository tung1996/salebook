from flask import*
from flask import Blueprint , Request
from flask_sqlalchemy import SQLAlchemy
from flask_login import current_user, login_user
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash
from model import *
# from book.router.router import *

class login_sigin() :
    def login(self) :
        login = LoginManager(app)
        body = request.get_json()
        if not "username" in body or not "password" in body :
            return ("username or password empty")
        else :
            user = Account.query.filter_by(username = body["username"]).first() 
            try :                                       
                username = user.username
                check = check_password_hash(user.password ,body["password"])
                if check == True :
                    login_user(user = user)
                    return ("Logged in successfully")
                else :
                    return ("wrong password")
            except :    
                return ("Account does not exist")

    

    def sigin(self) :
        body = request.get_json()
        if not "username" in body  or not "password" in body  or not "password_retype" in body or not "fullname" in body or not "admin" in body :
            return ("lack of information")
        else :
            if body["password"] == body["password_retype"] :
                try :
                    user = user.username 
                    return ("Username already exists")
                except : 
                    try :
                        password = generate_password_hash(body["password"])
                        new_ac = Account(body["username"] , password ,body["fullname"] ,body["admin"])
                        db.session.add(new_ac)
                        db.session.commit()
                        return ("create account successfully")
                    except :
                        return ("Syntax error")
            else :
                return ("password error")           



login_sigin = login_sigin()





