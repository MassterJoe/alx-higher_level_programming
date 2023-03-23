#!/usr/bin/python3
from sqlalchemy import Column, ForeignKey, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base

mymetadata = MetaData()
Base = declarative_base(metadata=mymetadata)  #an instance of the declarative_base() function, this will be used to generate the SQL schema for the database

class City(Base):
    __tablename__ = 'cities' # This specifies the name of the table
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False) #create id column with its properties
    name = Column(String(128), nullable=False) #create name column
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
