#!/usr/bin/python3

"""
WSGI config for personal_site project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os
import sys
from .settings import BASE_DIR, ACTIVATE

with open(ACTIVATE) as file_:
    exec(file_.read(), dict(__file__=ACTIVATE))

from django.core.wsgi import get_wsgi_application

sys.path.insert(0, BASE_DIR)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "personal_site.settings")

application = get_wsgi_application()
