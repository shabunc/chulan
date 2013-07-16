#!/usr/bin/env python

import __future__
from chulan import projects, locales, items
import argparse
import sys
import json

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
locale_parser.add_argument('-a', '--add', nargs=1)
locale_parser.add_argument('--list', action='store_true', default=False)

item_parser = subparsers.add_parser('items')
item_parser.add_argument('--shadow', default='I')
item_parser.add_argument('-p','--project', nargs=1)
item_parser.add_argument('-l','--locale', nargs=1)
item_parser.add_argument('-kv','--keyvalue', nargs=2)
item_parser.add_argument('--list', nargs=2)
item_parser.add_argument('-v','--verbose', action='store_true', default=False)
format_group = item_parser.add_mutually_exclusive_group()
format_group.set_defaults(format='props')
format_group.add_argument('--json', action='store_const', dest='format', const='json')
format_group.add_argument('--props', action='store_const', dest='format', const='props')
format_group.add_argument('--xml', action='store_const', dest='format', const='props')

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
    elif args.add:
        (locale,) = args.add
        locales().add(locale)
elif args.shadow == 'I':
    if args.keyvalue:
        if args.project and args.locale:
            (key, val) = args.keyvalue
            (proj_name,) = args.project
            (locale,) = args.locale
            project = projects().get(proj_name)
            key = key.lower()
            if project:
                item, error = items().add(key, val, project, locale)
                if error:
                    if args.verbose:
                        sys.exit('%s' % error)
                    else:
                        sys.exit("item has not been added")
                else:
                    print("keyval pair (%s, %s) has been added" % (key, val)) 
            else:
                raise Exception("project %s does not exist" % proj_name)
        else:
            raise Exception("Project and locale should be setted directly")
    elif args.list:
        (proj_name, locale) = args.list;
        its = items().list(proj_name, locale)
        if args.format == 'props':
            for item in its:
                print "%s=%s" % (item.key, item.value)
        elif args.format == 'json':    
            print(json.dumps(its))
