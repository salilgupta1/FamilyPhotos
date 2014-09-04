from common import *
DEBUG = False
TEMPLATE_DEBUG = False

ALLOWED_HOSTS = ['*']

ADMINS = (
    ('Salil Gupta', 'salil.gupta323@gmail.com'),
)

MANAGERS = ADMINS

import dj_database_url
DATABASES['default'] = dj_database_url.config()

'''
RAVEN_CONFIG = {
    'dsn': os.environ['SENTRY_DSN']
}
'''

INSTALLED_APPS = INSTALLED_APPS + (
#    'raven.contrib.django.raven_compat',
    'lockdown',
)


MIDDLEWARE_CLASSES += ('lockdown.middleware.LockdownMiddleware', )
LOCKDOWN_PASSWORDS = (os.environ['STAGE_PASSWORD'],)
LOCKDOWN_FORM = 'lockdown.forms.LockdownForm'