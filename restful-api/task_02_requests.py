#!/usr/bin/env python3
"""
This module will introduce the requests methods
"""
import requests
import csv
from flask import Flask, jsonify


def fetch_and_print_posts():
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    if response.status_code == 200:
        posts = response.json()
        print("Status Code: {}".format(response.status_code))
        for post in posts:
            for key in post:
                if key == 'title':
                    print(post[key])


def fetch_and_save_posts():
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    if response.status_code == 200:
        posts = response.json()
        columns = []
        for i in posts[0]:
            columns.append(i)
        with open('posts.csv', 'w+', newline="", encoding='utf8') as file:
            writer = csv.DictWriter(file, fieldnames=columns)

            writer.writeheader()
            writer.writerows(posts)
