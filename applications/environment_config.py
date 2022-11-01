import os

def EnvConfig(server_env='production'):
    """
    Load Server Environment Confirmation
    """
    try:

        if server_env == 'development':

            from config.dev import DevelopmentConfig
            return DevelopmentConfig

        elif server_env == 'uat':

            from config.uat import AUTConfig
            return AUTConfig

        else:
            from config.pro import ProductionConfig
            return ProductionConfig
            #import json
            #app.config.from_file("config.json", load=json.load)

    except ImportError:

        print('Invalid Server Environment')