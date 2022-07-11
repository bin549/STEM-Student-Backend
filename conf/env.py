import os

DATABASE_ENGINE = "django.db.backends.postgresql"
DATABASE_NAME =  "stem"
DATABASE_HOST = "47.107.50.178"
DATABASE_USER = "postgres"
DATABASE_PASSWORD = "__2018bb"
DATABASE_PORT = "5432"

DEBUG = int(os.environ.get("DEBUG", default=0))
ALLOWED_HOSTS = os.environ.get("DJANGO_ALLOWED_HOSTS").split(" ")
