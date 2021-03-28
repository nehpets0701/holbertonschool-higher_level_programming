#!/usr/bin/python3
"""list all cities in database"""
if __name__ == "__main__":
    import MySQLdb
    import sys
    db = MySQLdb.connect(host="localhost",
                         user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()
    c.execute("SELECT cities.id, cities.name, states.name FROM cities LEFT JOIN\
               states ON cities.state_id = states.id ORDER BY cities.id ASC;")
    rows = c.fetchall()
    for row in rows:
        print(row)
    c.close()
    db.close()
