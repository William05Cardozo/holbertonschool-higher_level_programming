#!/usr/bin/python3
"""List all cities in my DataBase"""

if __name__ == "__main__":

    import MySQLdb
    import sys

    data = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3])
    state = data.cursor()
    state.execute("SELECT cities.id, cities.name, states.name\
                FROM cities LEFT JOIN states\
                ON states.id = cities.states_id\
                ORDER BY cities.id ASC")

    query_rows = states.fetchall()
    for row in query_rows:
        print(row)

    state.close()
    data.close()
