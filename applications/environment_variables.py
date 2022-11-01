from app import app

class EnvironmentVariables():

    def get_api_key(self):
        return app.config['APP']['API_KEY'] or None