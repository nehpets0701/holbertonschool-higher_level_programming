#!/usr/bin/python3
"""list all states in database"""
if __name__ == "__main__":
    import MySQLdb
    import sys
    db = MySQLdb.connect(host="localhost",
                         user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()
    c.execute("Select * from states ORDER BY id ASC;")
    rows = c.fetchall()
    for row in rows:
        print(row)
    c.close()
    db.close()
