#!/usr/bin/python3
"""
Start link class to table in database
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
if __name__ == "__main__":
    #Arguments
    user = sys.argv[1]
    passwd = sys.argv[2]
    db = sys.argv[3]
    item = sys.argv[4]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(user,passwd,db), pool_pre_ping=True)

    # create a session
    Session = sessionmaker(bind=engine)
    session = Session()
    # Query
    states = session.query(State).filter(State.name == item)
    try:
        print("{}".format(states[0].id))
    except IndexError:
        print("Not found")
              
