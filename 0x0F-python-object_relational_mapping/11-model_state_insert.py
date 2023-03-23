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

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(user,passwd,db), pool_pre_ping=True)

    # create a session
    Session = sessionmaker(bind=engine)
    session = Session()
    
    #add new state
    new_state = State(name="Louisiana")
    session.add(new_state)
    
    # Query
    states = session.query(State).filter(State.name == 'Louisiana').first()
    print("{} : {}".format(states.id, states.name))
    session.commit()          
