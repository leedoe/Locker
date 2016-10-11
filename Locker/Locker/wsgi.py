"""
WSGI config for Locker project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

import newrelic.agent

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Locker.settings")

newrelic.agent.initialize('/home/ssulocker/django_project/ssuitcabin/Locker/Locker/newrelic.ini')
application = get_wsgi_application()
application = newrelic.agent.wsgi_application()(application)

