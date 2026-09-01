import os
import dj_database_url

from .base import *

# ==============================================================================
# SÉCURITÉ
# ==============================================================================

SECRET_KEY = os.environ.get('SECRET_KEY')
DEBUG = False
ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', '').split(',')
##ALLOWED_HOSTS = ['todo-list-backend-ljex.onrender.com']


# ==============================================================================
# BASE DE DONNÉES
# ==============================================================================

DATABASES = {
    'default': dj_database_url.config(
        conn_max_age=600,
        ssl_require=True
    )
}

# ==============================================================================
# FICHIERS STATIQUES (WHITENOISE)
# ==============================================================================

STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Configuration CORS plus restrictive pour la production
# On lit les origines autorisées depuis une variable d'environnement
CORS_ALLOWED_ORIGINS = os.environ.get('CORS_ALLOWED_ORIGINS', '').split(',')