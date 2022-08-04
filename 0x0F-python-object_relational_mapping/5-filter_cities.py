#!/usr/bin/python3
"""Module listing all cities from the state passed in argument"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect("localhost", argv[1], argv[2], argv[3])
    cur = db.cursor()
    cur.execute("""SELECT name
                FROM cities
                WHERE cities.state_id = (SELECT id
                    FROM states
                    WHERE name = %(state)s)
                ORDER BY cities.id ASC;""", {'state': argv[4]})
    res = list(cur.fetchall())
    for i in range(len(res)):
        res[i] = str(res[i][0])
    print(', '.join(res))
    cur.close()
    db.close()
