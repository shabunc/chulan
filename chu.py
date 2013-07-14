#!/usr/bin/env python

import __future__
from chulan import projects, locales
import argparse

def project_list():
    for p in projects().list():
        print p.name

def locale_list():
    for l in locales().list():
        print l.locale


#http://docs.python.org/2/library/argparse.html
parser = argparse.ArgumentParser(description='A command-line API for using Chulan')
parser.add_argument('--list', action='store_true', default=False)
parser.add_argument('--locale', action='store_true', default=False)
parser.add_argument('-a', nargs=1)

args = parser.parse_args()
if (args.list):
    if (args.locale):
        locale_list()
    else:
        project_list()
elif (args.a):
    (name,) = args.a
    if (args.locale):
        locales().add(name)

