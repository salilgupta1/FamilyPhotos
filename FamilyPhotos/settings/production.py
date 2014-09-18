from common import *
DEBUG = False
TEMPLATE_DEBUG = False

ALLOWED_HOSTS = ['*']

ADMINS = (
    ('Salil Gupta', 'salil.gupta323@gmail.com'),
)

MANAGERS = ADMINS

S3_STATICFILES_BUCKET = os.environ.get("S3_STATICFILES_BUCKET")

RAYGUN_API_URL = os.environ.get("RAYGUN_API_URL")
RAYGUN_API_KEY = os.environ.get("RAYGUN_API_KEY")
RAYGUN_API_ENABLED = True

import dj_database_url
DATABASES['default'] = dj_database_url.config()


INSTALLED_APPS = INSTALLED_APPS + (
    'lockdown',
    'storages',
)


STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
MIDDLEWARE_CLASSES += ('lockdown.middleware.LockdownMiddleware', 'raygun_dot_io.middleware.RaygunDotIOMiddleware')
LOCKDOWN_PASSWORDS = (os.environ['STAGE_PASSWORD'],)
LOCKDOWN_FORM = 'lockdown.forms.LockdownForm'

STATIC_URL = 'http://%s.s3.amazonaws.com/' % S3_STATICFILES_BUCKET