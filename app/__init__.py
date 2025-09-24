from flask import Flask
from flasgger import Swagger

def create_app(config_object):
    app = Flask(__name__)
    app.config.from_object(config_object)
    
    swagger_config = {
        "headers": [],
        "specs": [
            {
                "endpoint": 'api_spec',
                "route": '/api/spec.json',
                "rule_filter": lambda rule: True,
                "model_filter": lambda tag: True,
            }
        ],
        "static_url_path": "/flasgger_static",
        "swagger_ui": True,
        "swagger_hide_bar_with_no_route": False,
        "specs_route": "/api/docs/",
        "host": 'your-project-name.onrender.com', # <--- Update this with your live URL
        "schemes": ["https"]  # <--- Change this to https
    }
    
    Swagger(app, config=swagger_config)
    
    # ... any other code you have for blueprints, etc.
    
    return app