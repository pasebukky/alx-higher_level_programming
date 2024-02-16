#!/usr/bin/python3
"""
    A script that fetches the first state objects from database hbtn_0e_6_usa
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def fetch_first_state(username, password, db_name):
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(username, password, db_name),
                           pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()
    first_state = session.query(State).first()
    if first_state is None:
        print("Nothing")
    else:
        print('{}: {}'.format(first_state.id, first_state.name))
    session.close()


if __name__ == "__main__":
    fetch_first_state(*sys.argv[1:])
