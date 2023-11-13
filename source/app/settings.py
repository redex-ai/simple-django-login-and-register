import os
import logging

IS_PRODUCTION = os.environ.get('IS_PRODUCTION')

if IS_PRODUCTION:
    from .conf.production.settings import *
else:
    from .conf.development.settings import *

# Logging configuration
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'INFO',
    },
    'loggers': {
        'accounts.views': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': True,
        },
    },
}
