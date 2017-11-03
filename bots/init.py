#!/usr/bin/env python
# encoding: utf-8

def setup_django_env():
    import os, django, sys
    DJANGO_PROJECT_PATH = '/root/workspace/skystrike'
    DJANGO_SETTINGS_MODULE = "skystrike.settings"

    sys.path.insert(0, DJANGO_PROJECT_PATH)
    os.environ['DJANGO_SETTINGS_MODULE'] = DJANGO_SETTINGS_MODULE
    django.setup()

def check_db_connection():
    from django.db import connection

    if connection.connection:
        if not connection.is_usable():
            connection.close()
