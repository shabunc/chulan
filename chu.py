#!/usr/bin/env python

import __future__
from chulan import projects, locales, items
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
proj_parser.add_argument('-a', '--add', nargs=1)


locale_parser = subparsers.add_parser('locales')
locale_parser.add_argument('--shadow', default='L')
locale_parser.add_argument('--list', action='store_true', default=False)

item_parser = subparsers.add_parser('items')
item_parser.add_argument('--shadow', default='I')
item_parser.add_argument('-p','--project', nargs=1)
item_parser.add_argument('-l','--locale', nargs=1)
item_parser.add_argument('-kv','--keyvalue', nargs=2)
item_parser.add_argument('--list', nargs=2)


args = parser.parse_args()
if args.shadow == 'P':
    if args.list:
        project_list()
    elif args.add:
        (name,) = args.add
        projects().add(name)
elif args.shadow == 'L':
    if args.list:
        locale_list()
elif args.shadow == 'I':
    if args.keyvalue:
        if args.project and args.locale:
            (key, val) = args.keyvalue
            (proj_name,) = args.project
            (locale,) = args.locale
            project = projects().get(proj_name)
            if project:
                items().add(key, val, project, locale)
        else:
            raise Exception("Project and locale should be setted directly")
    elif args.list:
        (proj_name, locale) = args.list;
        for item in items().list(proj_name, locale):
            print "%s \t %s" % (item.key, item.value)
