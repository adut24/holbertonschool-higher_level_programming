#!/usr/bin/python3
"""Module listing all Cities"""
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sys import argv

if __name__ == "__main__":
    url = f'mysql+mysqldb://{argv[1]}:{argv[2]}@localhost/{argv[3]}'
    engine = create_engine(url, pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)
    for city in session.query(City).order_by(City.id.asc()).all():
        print('{}: {} -> {}'.format(city.id, city.name, city.state.name))
    session.close()
