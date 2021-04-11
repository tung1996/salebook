from flask import Flask
from flask import Blueprint
from flask_sqlalchemy import SQLAlchemy
from flask import Request
from flask_admin import Admin
from model import *
from flask_login import current_user, login_user


admin = Blueprint("admin" , __name__)
@admin.route("/all_user") 
def all_user():
    if current_user.is_authenticated :
        if current_user.admin == 1 :
            all_user = []
            users = Account.query.filter_by(admin = '0').all()
            for user in users :
                all_user.append(user.username)
            return ({"all_user": all_user})
        else :
            return "You are not an administrator"
    else :
        return "You need to log in"



