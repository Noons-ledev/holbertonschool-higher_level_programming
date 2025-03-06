#!/usr/bin/python3
"""
This script list states corresponding to names passed as arg
"""
import MySQLdb
import sys

if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost",
                           user=sys.argv[1],
                           passwd=sys.argv[2],
                           db=sys.argv[3],
                           port=3306)
    query = "SELECT * FROM states WHERE name =" \
        " '{}' ORDER BY id ASC;".format(sys.argv[4])
    cur = conn.cursor()
    cur.execute(query)
    states = cur.fetchall()
    for state in states:
        print(state)
    cur.close()
    conn.close()
