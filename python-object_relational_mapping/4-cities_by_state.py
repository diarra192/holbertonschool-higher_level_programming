#!/usr/bin/python3
"""script that lists all cities"""


import MySQLdb
import sys

if __name__ == "__main__":
    # Function that lists all states from database hbtn_0e_0_usa
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])

    # Creating cursor object
    cur = db.cursor()

# Executing MySql Query
    cur.execute("SELECT cities.id, cities.name,\
                states.name FROM cities INNER JOIN states ON\
                cities.state_id = states.id ORDER BY cities.id")


# Obtaining Query Result & prints the result in rows
    rows = cur.fetchall()
    for row in rows:
        print(row)

    # Clean Up
    cur.close()
    db.close()
