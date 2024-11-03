if __name__ == "__main__":
    from sys import argv
    import MySQLdb

    # Connect to the MySQL server
    db = MySQLdb.connect(
        host="localhost",
        user=argv[1],
        passwd=argv[2],
        db=argv[3],
        port=3306
    )


    # Create a cursor object to interact with the database
    cursor = db.cursor()

    # Execute the SQL query to retrieve states where name matches the argument and is injection safe
    cursor.execute("SELECT * FROM states\
                    WHERE name LIKE %s\
                    ORDER BY states.id ASC", (argv[4],))

    # Fetch all the rows
    states = cursor.fetchall()

    # Display the results
    for state in states:
        print(state)


    # Close the cursor and connection
    cursor.close()
    db.close()
