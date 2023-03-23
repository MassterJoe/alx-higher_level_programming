#!/usr/bin/python3
"""
Start link class to table in database
"""
import sys
from model_state import Base, State
from model_city import City
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
    # Query
    cities = session.query(State.name,City.id, City.name).filter(State.id==City.state_id)
    for city in cities:
        print("{}: ({}) {}".format(city[0],str(city[1]), city[2]))
