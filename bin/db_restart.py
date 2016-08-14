#!/usr/bin/env python

import os

print('Removing database...')
try:
    os.remove('nms.db')
except:
    pass

print('Removing migrations...')
try:
    dir = './nms/migrations'
    files = os.listdir(dir)
    for file in files:
        if not file.startswith('0002_createsuperuser.py'):
            os.remove(os.path.join(dir,file))
except:
    pass
    
#os.system('python manage.py makemigrations')
os.system('python manage.py makemigrations nms')
#os.system('python manage.py migrate')