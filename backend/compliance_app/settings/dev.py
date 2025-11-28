"""
Django settings for compliance_app project - Development Environment.

This module contains development-specific settings.
Use this for local development with DEBUG=True.
"""

from .base import *

# ПРЕДУПРЕЖДЕНИЕ БЕЗОПАСНОСТИ: не запускайте с включённым debug в production!
DEBUG = True

# Разрешить все хосты в режиме разработки
ALLOWED_HOSTS = ['*']

# База данных
# Используйте SQLite для простой локальной разработки или PostgreSQL с DATABASE_URL
DATABASES = {
    'default': env.db('DATABASE_URL', default='sqlite:///' + str(BASE_DIR / 'db.sqlite3'))
}

# Email Backend - вывод в консоль для разработки
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_HOST = env('EMAIL_HOST', default='localhost')
EMAIL_PORT = env.int('EMAIL_PORT', default=587)
EMAIL_USE_TLS = env.bool('EMAIL_USE_TLS', default=True)
EMAIL_HOST_USER = env('EMAIL_HOST_USER', default='')
EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD', default='')
DEFAULT_FROM_EMAIL = env('DEFAULT_FROM_EMAIL', default='noreply@localhost')
ADMIN_EMAIL = env('ADMIN_EMAIL', default='admin@localhost')

# Отключить перенаправления на HTTPS в режиме разработки
SECURE_SSL_REDIRECT = False
SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False

# Настройки CORS для разработки (если используется отдельный фронтенд)
CORS_ALLOW_ALL_ORIGINS = True

# Дополнительные приложения для разработки
INSTALLED_APPS += [
    # Uncomment for development tools
    # 'debug_toolbar',
    # 'django_extensions',
]

# Промежуточное ПО для разработки
# MIDDLEWARE += [
#     'debug_toolbar.middleware.DebugToolbarMiddleware',
# ]

# IВнутренние IP-адреса для панели отладки (debug toolbar)
INTERNAL_IPS = [
    '127.0.0.1',
    'localhost',
]

# Логирование в режиме разработки — более подробное
LOGGING['root']['level'] = 'DEBUG'

# Токен Replicate не требуется в разработке (будет использоваться фиктивное значение)
if not REPLICATE_API_TOKEN:
    REPLICATE_API_TOKEN = 'dummy_token_for_dev'

# Режим eager Celery для разработки (задачи выполняются синхронно)
# Uncomment to test without Celery/Redis running
# CELERY_TASK_ALWAYS_EAGER = True
# CELERY_TASK_EAGER_PROPAGATES = True
