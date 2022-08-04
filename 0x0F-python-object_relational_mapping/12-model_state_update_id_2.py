#!/usr/bin/python3
"""Update the state with the id 2"""
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sys import argv

if __name__ == "__main__":
    url = f'mysql+mysqldb://{argv[1]}:{argv[2]}@localhost/{argv[3]}'
    engine = create_engine(url, pool_pre_ping=True)

    session = Session(engine)
    state = session.query(State).filter(State.id.like(2)).first()
    state.name = 'New Mexico'
    session.commit()
    session.close()
