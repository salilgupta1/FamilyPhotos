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


INSTALLED_APPS = INSTALLED_APPS + (
    'lockdown',
    'storages',
)


STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
MIDDLEWARE_CLASSES += ('lockdown.middleware.LockdownMiddleware', )
LOCKDOWN_PASSWORDS = (os.environ['STAGE_PASSWORD'],)
LOCKDOWN_FORM = 'lockdown.forms.LockdownForm'

STATIC_URL = 'http://%s.s3.amazonaws.com/' % os.environ.get('S3_STATICFILES_BUCKET')