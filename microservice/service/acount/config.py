from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask (__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:@localhost/account?charset=utf8mb4"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]= 'False'
db = SQLAlchemy(app=app)


login = LoginManager(app = app)
app.secret_key = "14#11125!"