#!/usr/bin/python3
"""
    A script that deletes all State objects with a name containing the
    letter a from the database hbtn_0e_6_usa
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def delete_all_states(username, password, db_name):
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(username, password, db_name),
                           pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()
    delete_state = session.query(State).filter(State.name.like('%a%')).all()
    for state in delete_state:
        session.delete(state)
    session.commit()
    session.close()


if __name__ == "__main__":
    delete_all_states(*sys.argv[1:])
