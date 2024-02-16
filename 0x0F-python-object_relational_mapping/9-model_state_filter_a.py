#!/usr/bin/python3
"""
    A script that lists all State objects that contain the
    letter a from the database hbtn_0e_6_usa
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def list_all_states_with_char_a(username, password, db_name):
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(username, password, db_name),
                           pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()
    states_with_a = session.query(State).filter(State.name.like('%a%')) \
                                        .order_by(State.id).all()
    for state in states_with_a:
        print('{}: {}'.format(state.id, state.name))
    session.close()


if __name__ == "__main__":
    list_all_states_with_char_a(*sys.argv[1:])
