#!/usr/bin/python3
"""print city"""
from sys import argv as a
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base, State
from model_city import City
Base = declarative_base()


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(a[1], a[2], a[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    states_name = session.query(State, City).join(City).order_by(City.id).all()
    for x in states_name:
        print("{}: ({}) {}".format(x[0].name, x[1].id, x[1].name))
    session.close()
