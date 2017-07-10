from base import *
import dj_database_url

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

#DATABASES['default'] = dj_database_url.config("mysql://b4c7ae0105be4f:05f1495d@eu-cdbr-west-01.cleardb.com/heroku_0e30bbd308b60e8")
DATABASES['default'] = dj_database_url.config("CLEARDB_DATABASE_URL")


# Stripe environment variables
STRIPE_PUBLISHABLE = os.getenv('STRIPE_PUBLISHABLE', 'pk_test_lRJ210v4A3Z1wdwpi5469nZj')
STRIPE_SECRET = os.getenv('STRIPE_SECRET', 'sk_test_WQE2qg0XNQ0kqIOw8n0Ht0zu')

# PayPal Settings
SITE_URL = ['http://127.0.0.1:8000', 'http://we-are-social-.herokuapp.com/']
PAYPAL_NOTIFY_URL = ['http://bf49ea06.ngrok.io/a-very-hard-to-guess-url/', 'http://we-are-social-.herokuapp.com/']
PAYPAL_RECEIVER_EMAIL = 'marinka87@gmail.com'