from flask import Flask
from controller.controller import login_sigin
from model import* 

# dang nhap ac
@app.route('/login', methods= ['POST'])
def login():
    return login_sigin.login()

# đang ky ac
@app.route('/sigin', methods= ['POST'])
def sigin():
    return login_sigin.sigin()
