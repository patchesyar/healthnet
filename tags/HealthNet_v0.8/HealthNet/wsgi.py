"""
WSGI config for HealthNet project.

It exposes the WSGI callable as a module-level variable named ``application``.
dsdhtkjvdhtj,v fhyjggjh
For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "HealthNet.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
