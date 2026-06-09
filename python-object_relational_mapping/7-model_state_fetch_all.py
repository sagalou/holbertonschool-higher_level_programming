#!/usr/bin/python3
"""Module that list all State object"""


import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]),
        pool_pre_ping=True)
    session = Session(engine)
    Base.metadata.create_all(engine)
    query_rows = session.query(State).order_by(State.id).all()
    for row in query_rows:
        print("{}: {}".format(row.id, row.name))
    session.close()
