#!/usr/bin/python3

"""
    A script that takes in an argument and displays all values in the states
    table of hbtn_0e_0_usa where name matches the argument.
"""
import MySQLdb
import sys


def specific_state_name_search(username, password, db_name, state_name):
    """ Searches for specific state names from the database hbtn_0e_0_usa """
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cursor = db.cursor()
    cursor.execute("""
                      SELECT * FROM states WHERE name LIKE BINARY '{}'
                      ORDER BY id ASC""".format(sys.argv[4]))
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()


if __name__ == "__main__":
    specific_state_name_search(sys.argv[1], sys.argv[2], sys.argv[3],
                               sys.argv[4])
