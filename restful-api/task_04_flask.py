#!/usr/bin/python3
"""
First use of flask in this module
"""
from flask import Flask, jsonify, request
"""
So first we need the Flask class
"""

app = Flask(__name__)
users = {"jane": {"name": "Jane", "age": 28, "city": "Los Angeles"},
         "jone": {"name": "Jone", "age": 28, "city": "Los Angeles"}}


@app.route('/')
def home():
    return "<p>Welcome to the Flask API!</p>"


@app.route('/data')
def data():
    mylist = []
    for key in users:
        mylist.append(key)
    return jsonify(mylist)


@app.route('/status')
def status():
    return "<p>Ok</p>"


@app.route('/users/<username>')
def UserInfo(username):
    user = users.get(username)
    if user is not None:
        user['username'] = username
        return jsonify(user)
    else:
        str = {'error': "User not found"}
        return jsonify(str)


@app.route('/add_user', methods=['POST'])
def AddUser():
    data = request.get_json()
    if data['username'] is None:
        return jsonify({"error": "Username is required"})
    response = {"message": "User added", "user": data}
    user_name = data['username']
    users[user_name] = data
    return response


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
