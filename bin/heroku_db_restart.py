#!/usr/bin/env python

import os

#print('Stopping web dyno...')
os.system('heroku ps:stop web')
print('Removing database...')
os.system('heroku pg:reset DATABASE --confirm nms-naming')
#os.system('heroku run python manage.py makemigrations')
#os.system('heroku run python manage.py makemigrations mft')
os.system('heroku run python manage.py migrate')
#print('Starting web dyno...')
#os.system('heroku ps:start web')
print('Complete.')