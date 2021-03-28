#!/usr/bin/python3
"""print state id"""
from sys import argv as a
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base, State


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(a[1], a[2], a[3]))
    Base.metadata.create_all(engine)
    index = 0
    while a[4][index].isalpha() and index < len(a[4]) - 1:
        index += 1
    if a[4][index].isalpha():
        index += 1
    a[4] = a[4][slice(index)]

    Session = sessionmaker(bind=engine)
    session = Session()
    states_name = session.query(State)\
        .filter(State.name.like(a[4])).first()
    try:
        print(states_name.id)
    except:
        print("Not found")
    session.close()
