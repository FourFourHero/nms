#!/usr/bin/env python

import os
import string
import datetime
import json

count = 0
colors = []
f = open('colors.csv')
for line in f:
    vals = line.split(',')
    color = vals[1].strip()
    color = color.split(' ')
    if len(color) == 1:
        color = color[0].split('-')
        if len(color) == 1:
            print color[0]
            color = color[0].replace('"', '')
            colors.append(color)
            count += 1
f.close()

print count

f_py = open('colors.py', 'w')
f_py.write("colors = []\n")
for color in colors:
    f_py.write("colors.append('" + color.strip().lower().capitalize() + "')\n")
f_py.close()