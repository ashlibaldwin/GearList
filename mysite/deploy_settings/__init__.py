import dj_database_url
from ..settings import *

DEBUG = False
TEMPLATE_DEBUG = DEBUG 
SSLIFY_DISABLE = False

ALLOWED_HOSTS = [
'localhost',
'.pythonanywhere.com',
'.mygearroom.com',
]

SECRET_KEY = get_env_variable("SECRET_KEY")
EMAIL_HOST_PASSWORD = get_env_variable("EMAIL_HOST_PASSWORD")
db_from_env = dj_database_url.config()
DATABASES["default"].update(db_from_env)
