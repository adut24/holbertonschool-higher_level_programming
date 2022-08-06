#!/usr/bin/python3
"""Delete the state with an 'a' in their name"""
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sys import argv

if __name__ == "__main__":
    url = f'mysql+mysqldb://{argv[1]}:{argv[2]}@localhost/{argv[3]}'
    engine = create_engine(url, pool_pre_ping=True)

    session = Session(engine)
    for state in session.query(State).filter(State.name.contains('a')):
        session.delete(state)
    session.commit()
    session.close()
