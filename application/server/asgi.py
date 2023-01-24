"""
ASGI config for LuluMoonwalks_SP project.

It exposes the ASGI callable as a module-level variable named ``application``.

asgi.py is used in Django projects to configure an ASGI server to handle the application's requests. ASGI is a
specification for asynchronous servers, which can handle multiple requests simultaneously. This makes ASGI a good
choice for handling high-concurrency, high-performance web applications.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')

application = get_asgi_application()
