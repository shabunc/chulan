#!/usr/bin/env python

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.orm import sessionmaker, relationship, backref
import config

#http://docs.sqlalchemy.org/en/rel_0_8/orm/tutorial.html

Base = declarative_base()

class Projects(Base):
    __tablename__ = 'projects'
    items = relationship("Items")

    name = Column(String(200), primary_key=True)
    id = Column(Integer, primary_key=True)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "<Project('%s')>" % (self.name)



class Locales(Base):
    __tablename__ = 'locales'
    items = relationship("Items")
    
    locale = Column(String(2), primary_key=True)

    def __init__(self, locale):
        self.locale = locale

    def __repr__(self):
        return "<Locale('%s')>" % (self.locale)


class Items(Base):
    __tablename__ = 'items'
    key = Column(String(200), primary_key=True)
    value = Column(String(400))
    pid = Column(Integer, ForeignKey('projects.id'))
    locale = Column(String(2), ForeignKey('locales.locale'))

    def __init__(self, key, value, pid, locale):
        self.key = key
        self.value = value
        self.pid = pid
        self.locale = locale

    def __repr__(self):
        return "<Item('%s,%s,%s,%s')>" %(self.key, self.value, self.pid, self.locale)


def bindEngine():
    conf = config.get_config()
    url = "postgresql://%s:%s@localhost:5432/%s" % (conf.dbuser, conf.dbpassword, conf.dbname)
    engine = create_engine(url)
    return engine

def getSession():
    return sessionmaker(bind=bindEngine())()


if __name__ == "__main__":
    from sqlalchemy import create_engine
    
    def create():
        engine = bindEngine()
        Base.metadata.create_all(engine) 
        print(engine)

    create()
