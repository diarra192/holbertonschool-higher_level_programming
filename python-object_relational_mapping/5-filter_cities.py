#!/usr/bin/python3
"""script that takes the name of a state as an argument and lists all cities"""


import MySQLdb
import sys

if __name__ == "__main__":
    # Function that lists all states from database hbtn_0e_0_usa
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])

    # Creating cursor object
    cur = db.cursor()

# Executing MySql Query
    cur.execute("SELECT name FROM cities WHERE state_id = \
                (SELECT id FROM states WHERE name = '{}')\
                ORDER BY id".format(sys.argv[4]))

    # Obtaining Query Result & prints the result in rows
    rows = cur.fetchall()
    tabl = []
    for row in rows:
        tabl.append(row[0])
    print(', '.join(tabl))

    # Clean Up
    cur.close()
    db.close()
