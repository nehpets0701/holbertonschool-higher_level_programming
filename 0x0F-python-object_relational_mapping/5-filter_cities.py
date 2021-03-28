#!/usr/bin/python3
"""sql injection safe"""
if __name__ == "__main__":
    import MySQLdb
    from sys import argv as a
    db = MySQLdb.connect(host="localhost", user=a[1], passwd=a[2], db=a[3])
    c = db.cursor()
    c.execute("SELECT cities.name from cities WHERE cities.state_id IN (SELECT\
    states.id FROM states WHERE states.name = %(input)s) ORDER BY id ASC;",
              {'input': a[4]})
    rows = c.fetchall()
    if len(rows) > 0:
        for x in range(0, len(rows)):
            if len(rows) - 1 > x:
                print(rows[x][0], end=", ")
        print(rows[x][0])
    c.close()
    db.close()
