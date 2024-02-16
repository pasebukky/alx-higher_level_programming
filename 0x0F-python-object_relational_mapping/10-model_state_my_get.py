#!/usr/bin/python3
"""
    A script that prints the State object with the name passed
    as argument from the database hbtn_0e_6_usa
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def get_state(username, password, db_name, state_name):
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(username, password, db_name),
                           pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()
    state = session.query(State).filter(State.name.like(state_name)).first()
    if state:
        print(state.id)
    else:
        print("Not found")
    session.close()


if __name__ == "__main__":
    get_state(*sys.argv[1:])
