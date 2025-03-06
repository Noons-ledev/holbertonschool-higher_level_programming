#!/usr/bin/python3
import MySQLdb
import sys
db = MySQLdb.connect(host='localhost', user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3], port=3306)
cursor = db.cursor()

cursor.execute("SELECT * FROM states;")
tables = cursor.fetchall()
for table in tables:
    print(table)

db.close()