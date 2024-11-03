#!/usr/bin/python3
"""script that displays all values in the states table"""
import MySQLdb
import sys

if __name__ == "__main__":
    # Function that lists all states from database hbtn_0e_0_usa
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])

    # Creating cursor object
    cur = db.cursor()

    # Using parameterized query to prevent SQL injection
    query = "SELECT * FROM states WHERE name LIKE BINARY %s ORDER BY id"
    state_name = (sys.argv[4],)

    # Executing parameterized query
    cur.execute(query, state_name)

    # Obtaining Query Result & prints the result in rows
    rows = cur.fetchall()
    for row in rows:
        print(row)

    # Clean Up
    cur.close()
    db.close()
