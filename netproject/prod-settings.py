from .settings import *


SECRET_KEY = os.environ.get("SECRET_KEY")
DEBUG = int(os.environ.get("DEBUG", default=0))
ALLOWED_HOSTS = os.environ.get("DJANGO_ALLOWED_HOSTS").split(" ")

CONN_MAX_AGE = 300

DATABASES = {
    "default": {
        "ENGINE": os.environ.get("SQL_ENGINE", "django.db.backends.sqlite3"),
        "NAME": os.environ.get("SQL_DATABASE", os.path.join(BASE_DIR, "db.sqlite3")),
        "USER": os.environ.get("SQL_USER", "user"),
        "PASSWORD": os.environ.get("SQL_PASSWORD", "password"),
        "HOST": os.environ.get("SQL_HOST", "localhost"),
        "PORT": os.environ.get("SQL_PORT", "5432"),
    }
}

REDIS_SERVER_NAME = os.environ.get("REDIS_SERVER_NAME",default="redis")

KAVENEGAR_TOKEN = os.environ["KAVENEGAR_TOKEN"]

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME':timedelta(days=60),
    'REFRESH_TOKEN_LIFETIME':timedelta(days=61)
 }


AWS_ACCESS_KEY_ID = os.environ.get("STORAGE_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.environ.get("STORAGE_SECRET_ACCESS_KEY")
AWS_STORAGE_BUCKET_NAME = os.environ.get("STORAGE_BUCKET_NAME")
AWS_S3_ENDPOINT_URL = f"https://s3.ir-thr-at1.arvanstorage.com"
AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl':'max-age=86400'
}

AWS_LOCATION = "static"

# STATICFILES_DIRS = [
#     os.path.join(BASE_DIR, 'static'),
# ]

STATIC_URL = 'https://{AWS_S3_CUSTOM_DOMAIN}/{AWS_LOCATION}/'
# STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
AWS_S3_FILE_OVERWRITE = False
# DEFAULT_FILE_STORAGE = "varknowVod.storage_backends.MediaStorage"

CELERY_BROKER_URL="amqp://{}:{}".format(os.environ.get("RABBITMQ_HOST"), os.environ.get("RABBITMQ_PORT", 5672))
