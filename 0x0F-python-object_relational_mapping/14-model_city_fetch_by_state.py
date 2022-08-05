#!/usr/bin/python3
"""Module joining 2 tables"""
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sys import argv

if __name__ == "__main__":
    url = f'mysql+mysqldb://{argv[1]}:{argv[2]}@localhost/{argv[3]}'
    engine = create_engine(url, pool_pre_ping=True)

    session = Session(engine)
    for city, state in session.query(
            City, State).join(State).order_by(City.id.asc()).all():
        print('{}: ({}) {}'.format(state.name, city.id, city.name))
    session.close()
