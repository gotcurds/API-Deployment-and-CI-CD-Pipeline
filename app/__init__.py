from flask import Flask

def create_app(config_object):
    app = Flask(__name__)
    app.config.from_object(config_object)
    
    # ... any other code you have for blueprints, etc.
    
    return app