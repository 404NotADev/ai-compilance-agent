"""
Django settings module selector.

This module determines which settings to load based on DJANGO_SETTINGS_MODULE
or DJANGO_ENV environment variable.

Default: production settings (prod.py)

To use development settings:
    export DJANGO_SETTINGS_MODULE=compliance_app.settings.dev
    or
    export DJANGO_ENV=development

To use production settings:
    export DJANGO_SETTINGS_MODULE=compliance_app.settings.prod
    or
    export DJANGO_ENV=production (or leave unset)
"""

import os

# Определить, какой модуль настроек использовать
django_env = os.environ.get('DJANGO_ENV', 'production').lower()

if django_env in ('dev', 'development', 'local'):
    from .dev import *
elif django_env in ('prod', 'production'):
    from .prod import *
else:
    # По умолчанию использовать production для безопасности
    from .prod import *
