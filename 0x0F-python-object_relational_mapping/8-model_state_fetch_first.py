#!/usr/bin/python3
"""print first"""
from sys import argv as a
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base, State


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(a[1], a[2], a[3]))
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    states_name = session.query(State).order_by(State.id).first()
    try:
        print("{}: {}".format(states_name.id, states_name.name))
    except:
        print("Nothing")
    session.close()
