#!/usr/bin/python3
"""
This script list cities from a state passed as argument
"""
import MySQLdb
import sys

if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost",
                           user=sys.argv[1],
                           passwd=sys.argv[2],
                           db=sys.argv[3],
                           port=3306)

    cur = conn.cursor()
    query = "SELECT cities.name FROM cities \
            JOIN states ON cities.state_id = states.id \
            WHERE states.name = %s\
            ORDER BY cities.id ASC;"
    cur.execute(query, (sys.argv[4], ))
    cities = cur.fetchall()
    print(", ".join(name for (name, ) in cities))
    cur.close()
    conn.close()
