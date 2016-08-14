#!/usr/bin/env python

import os
import string
import datetime
import json

feelings = []
f = open('feelings.txt')
for line in f:
    feelings.append(line.strip())
f.close()
print len(feelings)

f_json = open('feelings.py', 'w')
f_json.write("feelings = []\n")
for feeling in feelings:
    f_json.write("feelings.append('" + feeling.strip().lower().capitalize() + "')\n")
f_json.close()