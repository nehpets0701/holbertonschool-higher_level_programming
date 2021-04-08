#!/usr/bin/python3
"""sqlalchemy"""
from sys import argv as a
from sqlalchemy import create_engine, Column, Integer, String
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(a[1], a[2], a[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    states_name = session.query(State).order_by(State.id).all()
    for x in states_name:
        print("{}: {}".format(x.id, x.name))
    session.close()
