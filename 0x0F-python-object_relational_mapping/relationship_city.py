#!/usr/bin/python3
"""
    City class definition
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from relationship_state import Base
from sqlalchemy.ext.declarative import declarative_base


class City(Base):
    """
        City class representation.
    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True,
                unique=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
