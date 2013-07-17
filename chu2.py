#!/usr/bin/env python
"""
Chulan, a simple and stupid localization
key-value storage

Usage:
    chu show locales
    chu show projects
    chu add locale <locale>
    chu add project <project>
    chu <project> add <key> <value> to <locale>
    chu <project> export props <locale>
    chu <project> export json <locale>
    chu <project> stats

Options:
  -h --help     Show this screen.
  --version     Show version.

"""

from docopt import docopt
import chulan as ch
import json

def show_locales():
    for l in ch.locales().list():
        print l.locale

def show_projects():
    for p in ch.projects().list():
        print p.name

def export_props(project, locale):
    for item in ch.items().list(project, locale):
         print "%s=%s" % (item.key, item.value)

def export_json(project, locale):
    data = {locale: {}}
    for item in ch.items().list(project, locale):
        data[locale][item.key] = item.value
    print(json.dumps(data))

args = (docopt(__doc__, version="0.0.2"))

if args['show']:
    locales, projects = args['locales'], args['projects']
    print(locales, projects)
    if locales:
        show_locales()
    if projects:
        show_projects()
if args['export']:
    project = args['<project>']
    locale = args['<locale>']
    as_props, as_json = args['props'], args['json']
    if as_props:
        export_props(project, locale)
    elif as_json:
        export_json(project, locale)
