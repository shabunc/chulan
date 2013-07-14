#!/usr/bin/env python

import __future__
from chulan import projects, locales
import argparse

def list():
    chu = projects()
    chu.connect()
    for project in chu.list():
        (name, uid) = project
        print(name)
    chu.close()


#http://docs.python.org/2/library/argparse.html
parser = argparse.ArgumentParser(description='A command-line API for using Chulan')
parser.add_argument('--list', action='store_true', default=False)
parser.add_argument('--locale', action='store_true', default=False)
parser.add_argument('-a', nargs=1)

args = parser.parse_args()
if (args.list):
    list()
elif (args.a):
    (name,) = args.a
    if (args.locale):
        locales().add(name)

