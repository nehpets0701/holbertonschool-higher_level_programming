#!/usr/bin/python3
"""sql injection safe"""
if __name__ == "__main__":
    import MySQLdb
    from sys import argv as a
    db = MySQLdb.connect(host="localhost", user=a[1], passwd=a[2], db=a[3])
    c = db.cursor()
    c.execute("SELECT * from states WHERE name LIKE %(input)s ORDER BY id;",
              {'input': a[4]})
    rows = c.fetchall()
    for row in rows:
        print(row)
    c.close()
    db.close()
