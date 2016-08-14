#!/usr/bin/env python

import os
import string
import datetime
import json

count = 0
animals = []
f = open('animals.csv')
for line in f:
    vals = line.split(',')
    animal = vals[1].strip()
    if animal:
        animal = animal.split(' ')
        if len(animal) == 1:
            animal = animal[0].split('-')
            if len(animal) == 1:
                print animal[0]
                animal = animal[0].replace('"', '')
                animals.append(animal)
                count += 1
f.close()

print count

f_py = open('animals.py', 'w')
f_py.write("animals = []\n")
for animal in animals:
    f_py.write("animals.append('" + animal.strip().lower().capitalize() + "')\n")
f_py.close()