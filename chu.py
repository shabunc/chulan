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
#http://docs.python.org/dev/library/argparse.html#argparse.ArgumentParser.add_subparsers
subparsers = parser.add_subparsers(help='sub-command help')

proj_parser = subparsers.add_parser('projects')
proj_parser.add_argument('--shadow', default='P')
proj_parser.add_argument('--list', action='store_true', default=False)


locale_parser = subparsers.add_parser('locales')
locale_parser.add_argument('--shadow', default='L')
locale_parser.add_argument('--list', action='store_true', default=False)

args = parser.parse_args()
if args.shadow == 'P':
    if args.list:
        project_list()
elif args.shadow == 'L':
    if args.list:
        locale_list()
