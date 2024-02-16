#!/usr/bin/python3

"""
    A script that takes in an argument and displays all values in the states
    table of hbtn_0e_0_usa where name matches the argument and is safe from
    MySQL injection
"""
import MySQLdb
import sys


def safe_specific_state_name_search(username, password, db_name, state_name):
    """
        Safely searches for specific state names from the
        database hbtn_0e_0_usa
    """
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cursor = db.cursor()
    query = "SELECT * FROM states WHERE name LIKE %s ORDER BY id ASC"
    cursor.execute(query, (state_name, ))
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()


if __name__ == "__main__":
    safe_specific_state_name_search(sys.argv[1], sys.argv[2], sys.argv[3],
                                    sys.argv[4])
