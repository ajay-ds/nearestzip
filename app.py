#initial file 

from flask import Flask

app=Flask(__name__)

@app.route("/")
def welcome ():
    return "welcomem"

@app.route("/home")
def home ():
    return "home paßge"

#controller --> model ( main code)

import controller.user_controller as user_controller

from controller import *