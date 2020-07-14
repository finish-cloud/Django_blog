from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['yourcustomdomain.com', '.yourcustomdomain.com']

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'メールアドレス'
EMAIL_HOST_PASSWORD = 'アプリ パスワード'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
