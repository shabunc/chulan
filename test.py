#!/usr/bin/env python

import __future__
from chulan import chulan

chu = chulan()
chu.connect()

print(chu.list())

chu.close()
