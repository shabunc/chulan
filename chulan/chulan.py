#!/usr/bin/env python

import __future__
import os
import imp
import chu_alchemy
import sqlalchemy
import re

ESCAPE_REGEXP = re.compile(r"^[ ]+")

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
        try:
            session.commit()
            return (item, False)
        except sqlalchemy.exc.IntegrityError as error:
            return (item, error)    
    def escape(self, val):
        return ESCAPE_REGEXP.sub('\ ', val)
    def list(self, project_name, locale="RU",format="properties"):
        session = chu_alchemy.getSession()
        items = session.query(chu_alchemy.Items).filter_by(project_name=project_name,locale_id=locale).order_by(chu_alchemy.Items.key).all()
        return [self.escape(item) for item in items];
    def remove(self, project, locale, key):
        session = chu_alchemy.getSession()
        item = session.query(chu_alchemy.Items).filter_by(
                   key=key,
                   project_name=project,
                   locale_id=locale
               ).first()
        if not item is None:
            session.delete(item)
            session.commit();
        return item
    def edit(self, project, locale, key, value):
        session = chu_alchemy.getSession()
        item = session.query(chu_alchemy.Items).filter_by(
                   key=key,
                   project_name=project,
                   locale_id=locale
               ).first()
        if not item is None:
            item.value = value
            session.commit()
        return item
        
        


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


        

    

