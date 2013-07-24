#!/usr/bin/env python

import __future__
import os
import imp

def get_config():
    path = os.path.join(os.path.expanduser('~'),'.chulan')
    return imp.load_source('.chulan', path)
