from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['flower-iris.herokuapp.com']

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
        'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'd1me1tu80o2lah',
        'USER': 'rlhcflogcttgha',
        'PASSWORD': 'bd04c2382456a027c96625a8aaf4bc058ce87b53635998a54646e25ac48a55d4',
        'HOST':'ec2-52-200-48-116.compute-1.amazonaws.com',
        'DATABASE_PORT':'5432',
   }
}