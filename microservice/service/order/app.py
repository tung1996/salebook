from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from config import *
from model import *

db.create_all()