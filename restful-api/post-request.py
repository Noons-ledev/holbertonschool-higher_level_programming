#!/usr/bin/python3

import requests

url = 'http://localhost:5000/add_user'
data = {
    'name': 'Bob',
    'age': '30',
    'city': 'New-York'
}
reponse = requests.post(url, json=data)
print(reponse)
