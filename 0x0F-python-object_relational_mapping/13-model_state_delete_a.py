#!/usr/bin/python3
"""delete a"""
from sys import argv as a
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base, State


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(a[1], a[2], a[3]))
    Session = sessionmaker(bind=engine)
    session = Session()
    states_name = session.query(State).filter(State.name.like('%a%')).all()
    for x in states_name:
        session.delete(x)
    session.commit()
    session.close()
