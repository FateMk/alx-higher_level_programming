#!/usr/bin/python3
"""
1-filter_states.py
"""
import sys
import MySQLdb


def init_db():
    """initilizing a db with MySQLdb"""
    db = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3],)
    return db


def print_state_searched(db):
    """prints all states with a name stating with N"""
    cur = db.cursor()
    cur.execute("SELECT * FROM states"
                "WHERE name LIKE BINARY '%{}%'"
                "ORDER BY states.id ASC".format(sys.argv[4]))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()


if __name__ == "__main__":
    print_state_searched(int_db())

