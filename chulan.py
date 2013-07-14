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



class projects:
    def list(self):
        session = chu_alchemy.getSession()
        return session.query(chu_alchemy.Projects).all()


        

    

