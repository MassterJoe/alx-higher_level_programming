#!/usr/bin/python3
import MySQLdb
import sys
if __name__=="__main__": # will not exceute when imported
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3])
    cur = db.cursor()
    match = sys.argv[4]
    cur.execute("SELECT * FROM states WHERE name LIKE %s",(match,))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
