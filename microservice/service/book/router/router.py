
from flask import*
from flask import Request
import requests
from controller.controller import filter_all 
from model import* 

# tim kiem sach
@app.route('/book', methods= ['GET'])
def book():
    return filter_all.filter()
  



