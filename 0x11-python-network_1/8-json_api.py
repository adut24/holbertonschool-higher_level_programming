#!/usr/bin/python3
"""Print the id and name"""
import requests
import sys


if __name__ == "__main__":
    try:
        data = {'q': sys.argv[1]}
    except Exception:
        data = {'q': ''}
    session = requests.Session()
    response = session.post('http://0.0.0.0:5000/search_user', data=data)
    try:
        json = response.json()
        if len(json) == 0:
            print('No result')
        else:
            print('[{}] {}'.format(json['id'], json['name']))
    except Exception:
        print('Not a valid JSON')
