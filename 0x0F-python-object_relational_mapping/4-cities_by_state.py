#!/usr/bin/python3

""" A script that lists all cities from the database hbtn_0e_4_usa """
import MySQLdb
import sys


def list_all_cities(username, password, db_name):
    """ Lists all cities from the database hbtn_0e_4_usa """
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cursor = db.cursor()
    query = """ SELECT cities.id, cities.name, states.name  FROM cities
                JOIN states ON cities.state_id = states.id
                ORDER BY cities.id ASC """
    cursor.execute(query)
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()


if __name__ == "__main__":
    list_all_cities(sys.argv[1], sys.argv[2], sys.argv[3])
