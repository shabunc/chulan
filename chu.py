#!/usr/bin/env python

import __future__
from chulan import chulan
import argparse

def list():
    chu = chulan()
    chu.connect()
    for project in chu.list():
        (name, uid) = project
        print(name)
    chu.close()


#http://docs.python.org/2/library/argparse.html
parser = argparse.ArgumentParser(description='A command-line API for using Chulan')
parser.add_argument('--list', action='store_true', default=False)

args = parser.parse_args()
if (args.list):
    list()

