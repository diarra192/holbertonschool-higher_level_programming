#!/usr/bin/python3
"""Module to list all states from database hbtn_0e_0_usa"""

import MySQLdb
import sys

if __name__ == "__main__":
    """Function that lists all states from database hbtn_0e_0_usa"""
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])

    # Create a cursor object
    cursor = db.cursor()

    # Execute the query
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # print rows in a list of lists
    for row in cursor.fetchall():
        print(row)

    # Clean up
    cursor.close()
    db.close()
