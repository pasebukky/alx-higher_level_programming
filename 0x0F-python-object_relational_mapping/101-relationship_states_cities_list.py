#!/usr/bin/python3
""" A script that lists all State objects, and corresponding
    City objects, contained in the database hbtn_0e_101_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_city import City
from relationship_state import Base, State


def list_state_and_their_cities(username, password, db_name):
    """ Lists states and their corresponding cities """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(username, password, db_name),
                           pool_pre_ping=True)

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    for state in session.query(State).order_by(State.id):
        print('{}: {}'.format(state.id, state.name))
        for city in state.cities:
            print("    ", end="")
            print('{}: {}'.format(city.id, city.name))


if __name__ == "__main__":
    list_state_and_their_cities(*sys.argv[1:])
