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
            db=sys.argv[3])
    return db


def print_states_N(db):
    """prints all states with a name stating with N"""
    cur = db.cursor()
    cur.execute("SELECT * FROM states"
                "WHERE name LIKE BINARY 'N%' "
                "ORDER BY states.id ASC")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()


if __name__ == "__main__":
    print_states_N(int_db())

