import os

class ProductionConfig(object):
    # Defined Root Path
    ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

    # Flask Server Info
    HOST = "0.0.0.0"
    PORT = 80
    DEBUG = True

    # Defined Application Variables
    APP = {
        'API_KEY': '1111111111111',
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