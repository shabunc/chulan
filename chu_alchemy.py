#!/usr/bin/env python

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, ForeignKeyConstraint, create_engine
from sqlalchemy.orm import sessionmaker, relationship, backref
import config

#http://docs.sqlalchemy.org/en/rel_0_8/orm/tutorial.html

Base = declarative_base()

class Projects(Base):
    __tablename__ = 'projects'
    items = relationship("Items", backref='project_items')

    name = Column(String(200), primary_key=True)
    id = Column(Integer, primary_key=True)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "<Project('%s', %s)>" % (self.name, self.id)



class Locales(Base):
    __tablename__ = 'locales'
    items = relationship("Items", backref='locale_items')
    
    locale = Column(String(2), primary_key=True)

    def __init__(self, locale):
        self.locale = locale

    def __repr__(self):
        return "<Locale('%s')>" % (self.locale)


class Items(Base):
    #http://stackoverflow.com/questions/7504753/relations-on-composite-keys-using-sqlalchemy
    __tablename__ = 'items'
    key = Column(String(200), primary_key=True)
    value = Column(String(400), nullable=False)
    project_id = Column(Integer, primary_key=True)
    project_name = Column(String(200))
    locale_id = Column(String(2), ForeignKey('locales.locale'), primary_key=True)
    __table_args__ = (ForeignKeyConstraint([project_id, project_name], [Projects.id, Projects.name]), {})

    def __init__(self, key, value, project, locale_id):
        self.key = key
        self.value = value
        self.project_name = project.name
        self.project_id  = project.id
        self.locale_id = locale_id

    def __repr__(self):
        return "<Item('%s,%s,%s,%s')>" %(self.key, self.value, self.project_name, self.locale_id)


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
