#!/usr/bin/python3

"""
    A script that lists all states with a name starting with N (upper N)
    from the database hbtn_0e_0_usa
"""
import MySQLdb
import sys


def filter_state_names_starting_with_N(username, password, db_name):
    """ Lists all states with a name starting with N (upper N) """
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cursor = db.cursor()
    cursor.execute("""
                      SELECT * FROM states WHERE name LIKE BINARY 'N%'
                      ORDER BY id ASC""")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()


if __name__ == "__main__":
    filter_state_names_starting_with_N(sys.argv[1], sys.argv[2], sys.argv[3])
