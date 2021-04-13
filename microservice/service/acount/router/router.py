from flask import Flask
from controller.controller import login_sigin
from model import* 
from controller.controller_all_user import admin
from flask_login import current_user, login_user

# dang nhap ac
@app.route('/login', methods= ['POST'])
def login():
    return login_sigin.login()

# đang ky ac
@app.route('/sigin', methods= ['POST'])
def sigin():
    return login_sigin.sigin()

# hien thi tat ca user
app.register_blueprint(admin, url_prefix = "/admin" )


#check account
@app.route('/check', methods= ['GET'])
def check():
    return login_sigin.check()



