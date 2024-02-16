#!/usr/bin/python3
"""
    A script that changes the name of a State object
    from the database hbtn_0e_6_usa
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def change_state_name(username, password, db_name):
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(username, password, db_name),
                           pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()
    update_state = session.query(State).filter_by(id=2).first()
    if update_state:
        update_state.name = "New Mexico"
        session.commit()
    session.close()


if __name__ == "__main__":
    change_state_name(*sys.argv[1:])
