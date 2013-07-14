#!/usr/bin/env python

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

#http://docs.sqlalchemy.org/en/rel_0_8/orm/tutorial.html

Base = declarative_base()

class Projects(Base):
    __tablename__ = 'projects'

    name = Column(String(200), primary_key=True)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "<Project('%s')>" % (self.name)

class Locales(Base):
    __tablename__ = 'locales'
    
    locale = Column(String(2), primary_key=True)

    def __init__(self, locale):
        self.locale = locale

    def __repr__(self):
        return "<Locale('%s')>" % (self.locale)
