from crypt import methods
from typing_extensions import dataclass_transform
from app import app
from model.user_model import user_model
from flask import request
obj=user_model()
@app.route("/user/getall")

def get_controller():
    return obj.user_getall_model()

@app.route("/model-input/getNearestZip",methods=['POST'])

def get_nearzip_controller():
    data=request.get_json()
    print(data)
    return obj.getnearzip_model(data)

