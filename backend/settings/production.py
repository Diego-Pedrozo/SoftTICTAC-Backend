from .base import *

# Lee las variables de entorno cargadas en el sistema
DB_NAME = os.getenv('MYSQL_DATABASE')
DB_HOST = os.getenv('DATABASE_HOST')
DB_USER = os.getenv('MYSQL_USER')
DB_PASSWORD = os.getenv('MYSQL_PASSWORD')
DB_PORT = os.getenv('DATABASE_PORT')
SECRET_KEY = os.getenv('SECRET_KEY')

STATICFILES_STORAGE = "django.contrib.staticfiles.storage.ManifestStaticFilesStorage"

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': DB_NAME,
        'USER': DB_USER,
        'PASSWORD': DB_PASSWORD,
        'HOST': DB_HOST,  # Nombre del servicio de MySQL en Docker Compose
        'PORT': DB_PORT,
    }
}
STATIC_URL = "static/"
STATIC_ROOT = os.path.join(BASE_DIR, '../static')
MEDIA_URL = "media/"
MEDIA_ROOT = os.path.join(BASE_DIR, '../media')

ALLOWED_HOSTS = ['*']

CORS_ORIGIN_WHITELIST = [
    '',
]

CORS_ALLOWED_ORIGINS = [
    "",
    ""
]

USE_X_FORWARDED_HOST = True
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

EMAIL_BACKEND = ''
MAILJET_API_KEY = ''
MAILJET_API_SECRET = ''
