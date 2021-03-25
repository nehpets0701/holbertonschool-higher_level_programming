#!/usr/bin/python3
import MySQLdb
import sys
db = MySQLdb.connect(host="localhost",
                     user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
cur = db.cursor()
cur.execute("Select * from states ORDER BY id ASC;")
rows = cur.fetchall()
for row in rows:
    print(row)
