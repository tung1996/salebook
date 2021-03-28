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

if __name__=="__main__":
    app.run()





