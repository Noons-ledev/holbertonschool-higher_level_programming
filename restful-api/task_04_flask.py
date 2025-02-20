#!/usr/bin/python3
"""
First use of flask in this module
"""
from flask import Flask, jsonify, request
"""
So first we need the Flask class
"""

app = Flask(__name__)
users = {}


@app.route('/')
def home():
    """
    Method doc
    """
    return "Welcome to the Flask API!"


@app.route('/data')
def data():
    """
    Method doc
    """
    mylist = []
    for key in users:
        mylist.append(key)
    return jsonify(mylist)


@app.route('/status')
def status():
    """
    Method doc
    """
    return "OK"


@app.route('/users/<username>')
def UserInfo(username):
    """
    Method doc
    """
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        str = {'error': "User not found"}, 404
        return jsonify(str)


@app.route('/add_user', methods=['POST'])
def AddUser():
    """
    Method doc
    """
    data = request.get_json()
    data_name = data.get('username')
    if not data_name:
        return jsonify({"error": "Username is required"}), 400
    response = {"message": "User added", "user": data}
    user_name = data['username']
    users[user_name] = data
    return jsonify(response)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
