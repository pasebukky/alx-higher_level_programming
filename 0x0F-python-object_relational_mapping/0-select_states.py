#!/usr/bin/python3

""" A script that lists all states from the database hbtn_0e_0_usa """
import MySQLdb
import sys


def list_all_states(username, password, db_name):
    """ Lists all states from the database hbtn_0e_0_usa """
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()


if __name__ == "__main__":
    list_all_states(sys.argv[1], sys.argv[2], sys.argv[3])
