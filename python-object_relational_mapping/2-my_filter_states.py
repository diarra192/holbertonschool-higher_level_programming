#!/usr/bin/python3
"""script that lists all states with a name starting with N (upper N)"""
import MySQLdb
import sys

if __name__ == "__main__":
    # Function that lists all states from database hbtn_0e_0_usa
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])

    # Creating cursor object
    cur = db.cursor()

    # Using format to create the SQL query with user input
    query = (
        "SELECT * FROM states "
        "WHERE name LIKE BINARY '{}' "
        "ORDER BY id"
    ).format(sys.argv[4])
    cur.execute(query)

    # Obtaining Query Result & prints the result in rows
    rows = cur.fetchall()
    for row in rows:
        print(row)

    # Clean Up
    cur.close()
    db.close()
