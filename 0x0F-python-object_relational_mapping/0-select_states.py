#!/usr/bin/python3
"""Module listing all states from the database"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect("localhost", argv[1], argv[2], argv[3])
    cur = db.cursor()
    cur.execute("SELECT id, name FROM states ORDER BY id ASC;")
    res = cur.fetchall()
    for r in res:
        print(r)
