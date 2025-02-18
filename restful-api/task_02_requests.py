#!/usr/bin/env python3
"""
This module will introduce the requests methods
"""
import requests
import csv
from flask import Flask, jsonify
"""
My import documentation
"""


def fetch_and_print_posts():
    """
    this function is used to implement a get request and format to JSON
    """
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    if response.status_code == 200:
        posts = response.json()
        print("Status Code: {}".format(response.status_code))
        for post in posts:
            for key in post:
                if key == 'title':
                    print(post[key])


def fetch_and_save_posts():
    """
    This function is used to implement a get request
    and if it worked, save the content in a csv file with columns (dictwriter)
    """
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    if response.status_code == 200:
        posts = response.json()
        columns = []
        with open('posts.csv', 'w+', newline="", encoding='utf8') as file:
            writer = csv.DictWriter(file, fieldnames=['id', 'title', 'body'], extrasaction="ignore")

            writer.writeheader()
            writer.writerows(posts)
