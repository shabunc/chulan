#!/usr/bin/env python
"""
Chulan, a simple and stupid localization
key-value storage

Usage:
    chu show locales
    chu show projects
    chu add locale <locale>
    chu add project <project>
    chu <project> <locale> rm <key>
    chu <project> <locale> add <key> <value> 
    chu <project> <locale> export props
    chu <project> <locale> export json
    chu <project> <locale> export xml
    chu <project> stats

Options:
  -h --help     Show this screen.
  --version     Show version.

"""

from docopt import docopt
import chulan as ch
import json
from lxml import etree

def show_locales():
    for l in ch.locales().list():
        print l.locale

def show_projects():
    for p in ch.projects().list():
        print p.name

def add_project(new_project):
    print ("adding %s" % new_project)
    ch.projects().add(new_project)

def add_locale(new_locale):
    print ("adding %s" % new_locale)
    ch.locales().add(new_locale)

def export_props(project, locale):
    for item in ch.items().list(project, locale):
         print "%s=%s" % (item.key, item.value)

def export_json(project, locale):
    data = {locale: {}}
    for item in ch.items().list(project, locale):
        data[locale][item.key] = item.value
    print(json.dumps(data))

def export_xml(project, locale):
    root = etree.Element('items', locale=locale)
    for item in ch.items().list(project, locale):
        child = etree.Element('item', key=item.key, value=item.value)
        root.append(child)
    print etree.tostring(root, pretty_print=True, xml_declaration=True, encoding='utf-8')

def add_to_project(project_name, locale, key, value):
    project = ch.projects().get(project_name)
    if project:
        item, error = ch.items().add(key, value, project, locale)
        print("%s %s %s %s" % (project_name, locale, key, value))

def remove_key(project, locale, key):
    item = None
    item = ch.items().remove(project, locale, key)
    if item is None:
        print "[FAILED] Key %s  no found in %s/%s; nothing had been removed" % (key, project, locale)
    else:
        print "[OK] Key %s succesfully removed from %s/%s" % (key, project, locale)

args = (docopt(__doc__, version="0.0.2"))

if args['show']:
    locales, projects = args['locales'], args['projects']
    if locales:
        show_locales()
    if projects:
        show_projects()
elif args['export']:
    project = args['<project>']
    locale = args['<locale>']
    as_props, as_json, as_xml = args['props'], args['json'], args['xml']
    if as_props:
        export_props(project, locale)
    elif as_json:
        export_json(project, locale)
    elif as_xml:
        export_xml(project, locale)
elif args['add']:
    project, locale = args['<project>'], args['<locale>']
    key, value = args['<key>'], args['<value>']
    new_project, new_locale = args['project'], args['locale']
    if new_project:
        add_project(project)
    elif new_locale:
        add_locale(locale)
    elif project:
        add_to_project(project, locale, key, value)
elif args['rm']:
    project_name, locale, key = args['<project>'], args['<locale>'], args['<key>']
    remove_key(project_name, locale, key)

