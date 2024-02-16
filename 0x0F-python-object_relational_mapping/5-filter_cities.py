#!/usr/bin/python3

"""
    A script that takes in the name of a state as an argument and lists all
    cities of that state, using the database hbtn_0e_4_usa
"""
import MySQLdb
import sys


def list_all_cities_in_specific_state(username, password, db_name, state_name):
    """
        Lists all cities of a particular state from
        the database hbtn_0e_4_usa
    """
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cursor = db.cursor()
    query = """ SELECT cities.name FROM cities
                JOIN states ON cities.state_id = states.id
                WHERE states.name = %s ORDER BY cities.id ASC """
    cursor.execute(query, (state_name, ))
    rows = cursor.fetchall()
    cities = [row[0] for row in rows]
    print(', '.join(cities))
    cursor.close()
    db.close()


if __name__ == "__main__":
    list_all_cities_in_specific_state(sys.argv[1], sys.argv[2], sys.argv[3],
                                      sys.argv[4])
