#!/usr/bin/python3
"""This script take an argument and displays all values in the table"""

if __name__ == "__main__":
    import MySQLdb
    import sys

    D = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                        passwd=sys.argv[2], db=sys.argv[3])
    state = data.cursor()
    state.execute("SELECT * FROM states WHERE name LIKE BINARY '{}%'; "
                  .format(sys.argv[4]))
    qry_rows = state.fetchall()
    for row in qry_rows:
        print(row)
    state.close()
    d.close()
