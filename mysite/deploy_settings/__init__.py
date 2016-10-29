from ..settings import *

DEBUG = False
TEMPLATE_DEBUG = DEBUG 

ALLOWED_HOSTS = [
'localhost',
'.pythonanywhere.com',
'.mygearroom.com',
]

SECRET_KEY = get_env_variable("SECRET_KEY")

