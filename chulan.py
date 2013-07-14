#!/usr/bin/env python

import __future__
import os
import imp
import psycopg2
import chu_alchemy



class locales:
    def add(self, name):
        loc = chu_alchemy.Locales(name)
        print(loc)
        #chu_alchemy.getSession().add(loc)
        #chu_alchemy.getSession().add(loc)


class projects:
    config = None
    conn = None

    def getConfig(self):
        path = os.path.join(os.path.expanduser('~'),'.chulan')
        self.config = imp.load_source('.chulan', path)

    def connect(self):
        conn = psycopg2.connect(
            dbname = self.config.dbname,
            user = self.config.dbuser,
            password = self.config.dbpassword
        )
        self.conn = conn
        return conn

    def close(self):
        self.conn.close()
 

    def __init__(self):
        self.getConfig()

    def ping(self):
        print("Trying to reach DB using folowing credentials")
        print("DB name is %s" % self.config.dbname)
        print("DB user is  %s" % self.config.dbuser)
        print("DB connection password is  %s" % self.config.dbpassword)


    def list(self):
        cur = self.conn.cursor()
        cur.execute('SELECT name, id FROM projects')
        return cur.fetchall()


        

    

