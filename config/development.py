import logging

DEBUG = True
SQLALCHEMY_ECHO = True

LOGGING_ENABLED = False

SQLALCHEMY_DATABASE_URI = 'sqlite:///instance/blindr.db'

import boto
boto.config.load_from_path('instance/boto.cfg')

