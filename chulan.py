#!/usr/bin/env python

import __future__
import os
import imp
import psycopg2
import chu_alchemy



class locales:
    def add(self, name):
        loc = chu_alchemy.Locales(name)
        session = chu_alchemy.getSession()
        session.add(loc)
        session.commit()
    def list(self):
        session = chu_alchemy.getSession()
        return session.query(chu_alchemy.Locales).all()

class items:
    def add(self, key, value, project, locale):
        item = chu_alchemy.Items(key, value, project, locale)
        session = chu_alchemy.getSession()
        session.add(item)
        session.commit()
    def list(self, project_name, locale="RU"):
        session = chu_alchemy.getSession()
        items = session.query(chu_alchemy.Items).filter_by(project_name=project_name,locale_id=locale).all()
        return items;
        



class projects:
    def list(self):
        session = chu_alchemy.getSession()
        return session.query(chu_alchemy.Projects).all()
    def add(self, name):
        session = chu_alchemy.getSession()
        project = chu_alchemy.Projects(name)
        session.add(project)
        session.commit()
    def get(self, name):
        session = chu_alchemy.getSession()
        res = session.query(chu_alchemy.Projects).filter_by(name=name).first()
        return res;


        

    

