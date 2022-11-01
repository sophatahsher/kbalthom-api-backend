import os

class DevelopmentConfig(object):

    # Defined Root Path
    ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

    # Flask Server Info
    HOST = "localhost"
    PORT = 8000
    DEBUG = True

    # Defined Application Variables
    APP = {
        'API_KEY': '123456789',
        'API_SECRET_KEY': '************'
    }

    # Defined Database Configuration
    DATABASE = {
        'PGSQL': {
            'HOST': '0.0.0.0',
            'NAME': 'kbalthom_db',
            'USER': 'kbalthom',
            'PWD': '*******',
            'PORT': '5432'
        }
    }