#!/usr/bin/python3
""" This script showme all states srtarting with N """

if __name__ == "__main__":

    import MySQLdb
    from sys import argv

    data = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3])
    state = data.cursor()
    state.execute("SELECT * FROM states \
                    WHERE name Like BINARY 'N%' ORDER BY states.id ASC")
    query_rows = state.fetchall()
    for row in query_rows:
        print(row)
    state.close()
    data.close()
