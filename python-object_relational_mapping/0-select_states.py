#!/usr/bin/python3
"""
Script to retrieve and print all states from a MySQL database sorted by state id.

Usage:
    ./0-select_states.py <username> <password> <database>
"""
import sys
import MySQLdb

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} username password database".format(sys.argv[0]))
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
try:
db = MySQLdb.connect(
host="localhost",
port=3306,
user=username,
passwd=password,
db=database
)
cursor = db.cursor()
cursor.execute("SELECT * FROM states ORDER BY id ASC")

        rows = cursor.fetchall()
        for row in rows:
            print(row)

        cursor.close()
        db.close()

    except MySQLdb.Error as e:
        print("MySQL Error {}: {}".format(e.args[0], e.args[1]))
        sys.exit(1)
