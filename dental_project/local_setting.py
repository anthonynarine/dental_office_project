
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-bzjm4de(nl29yzuu$6c3-_a8-ib$y#=jt!j+8d+^=)j=g!((hz"


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "dental_database",
        "HOST": "localhost",
        "USER": "root",
        "PASSWORD": "Julia2021!"
    }
}