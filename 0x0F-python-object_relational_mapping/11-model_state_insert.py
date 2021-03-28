#!/usr/bin/python3
"""add louisiana"""
from sys import argv as a
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base, State
Base = declarative_base()


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(a[1], a[2], a[3]))
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    states_name = session.query(State.name, State.id).all()
    new_state = State()
    new_state.id = len(states_name) + 1
    new_state.name = "Louisiana"
    print(new_state.id)
    session.add(new_state)
    session.commit()
    session.close()
