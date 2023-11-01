from flask import Blueprint, jsonify


home = Blueprint('home', __name__)

@home.route('/')
def some():
    print("haha")
    return jsonify({'datservice' : 'HOME'})

