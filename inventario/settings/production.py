from .base import *
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['proyectoinvent.herokuapp.com']
# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'd5vbc3na2hu74b',
        'USER': 'hzfqnrwoojvbmr',
        'PASSWORD': 'bbe17fafb70ef648d4c0eba802af45a1bcd7ca38c49b8ccf2c33a7008712f23c',
        'HOST': 'ec2-52-212-228-71.eu-west-1.compute.amazonaws.com',
        'PORT': 5432,
    }
}
