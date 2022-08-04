#!/usr/bin/python3
"""Module listing the state passed as an argument"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect("localhost", argv[1], argv[2], argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name = '{}' ORDER BY id ASC;"
                .format(argv[4]))
    res = cur.fetchone()
    print(res)
    cur.close()
    db.close()
