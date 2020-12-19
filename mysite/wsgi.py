"""
WSGI config for mysite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os
import sys
from pathlib import Path,os
from django.core.wsgi import get_wsgi_application

BASE_DIR = Path(__file__).resolve(strict=True).parent.parent
path = r'D:/data from other partiton/python/django_test/'
if path not in sys.path:
    sys.path.append(path)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

application = get_wsgi_application()
