#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='chulan',
    version='0.0.3',
    author=u'Shahen Shabunc',
    author_email='shabunc@gmail.com',
    url='https://github.com/shabunc/chulan',
    license='do whatever you want',
    description='A very stupid key-valuy command line interface for i18n',
    zip_safe=False,
    packages=find_packages(),
    install_requires=['sqlalchemy', 'docopt', 'psycopg2'],
    scripts=['chulan/chu']
)
