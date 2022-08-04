#!/usr/bin/python3
"""Module listing the id of the state passed in argument"""
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sys import argv

if __name__ == "__main__":
    url = f'mysql+mysqldb://{argv[1]}:{argv[2]}@localhost/{argv[3]}'
    engine = create_engine(url, pool_pre_ping=True)

    session = Session(engine)
    state = session.query(State).filter(State.name.like(argv[4])).first()
    if state is None:
        print('Not found')
    else:
        print("{}".format(state.id))
    session.close()
