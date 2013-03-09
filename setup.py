#!/usr/bin/env python
#
# (c) 2013 Joost Yervante Damad <joost@damad.be>
# License: GPL

import glob

from distutils.core import setup

with open('README.md') as file:
    long_description = file.read()

setup(
  name = 'madparts',
  description = 'a functional footprint editor',
  long_description = long_description,
  author = 'Joost Yervante Damad',
  author_email = 'joost@damad.be',
  version = '1.0',
  url = 'http://madparts.org/',
  scripts = ['madparts'],
  packages = [
        'coffee', 
        'export', 
        'grind',
        'gui',
        'inter', 
        'syntax', 
        'util'
        ],
  package_data= { 
        'grind': ['*.coffee'],
        'gui': ['../GPL', '../README.md'], # dirty trick ;)
        },
  data_files = [
    ('share/madparts/contrib/freefont', glob.glob('contrib/freefont/*')),
    ('share/madparts/examples', glob.glob('examples/*.coffee')),
    ],
  platforms = ["Windows", "Linux", "Mac OS-X"],
  )
