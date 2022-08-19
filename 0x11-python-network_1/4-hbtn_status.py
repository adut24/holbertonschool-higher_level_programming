#!/usr/bin/python3
"""Fetch from the site with requests"""
import requests


if __name__ == "__main__":
    session = requests.Session()
    response = session.get('https://intranet.hbtn.io/status').text
    print('Body response:')
    print('\t- type: {}'.format(type(response)))
    print('\t- content: {}'.format(response))
