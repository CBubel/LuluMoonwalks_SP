"""
WSGI config for LuluMoonwalks_SP project.

It exposes the WSGI callable as a module-level variable named ``application``.

wsgi.py is used in Django projects to configure a WSGI server to handle the application's requests. WSGI is a
specification for synchronous servers, which can handle one request at a time. WSGI is a widely supported standard
for serving Python web applications and is supported by many web servers, including Apache and Nginx.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')

application = get_wsgi_application()
