#!/usr/bin/python3
"""
    A script that prints all City objects from the database hbtn_0e_14_usa
"""
import sys
from model_city import Base, City
from model_state import State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def fetch_cities_by_state(username, password, db_name):
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(username, password, db_name),
                           pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    cities = session.query(City, State).filter(City.state_id == State.id) \
                                       .order_by(City.id).all()

    for city, state in cities:
        print('{}: ({}) {}'.format(state.name, city.id, city.name))

    session.close()


if __name__ == "__main__":
    fetch_cities_by_state(*sys.argv[1:])
