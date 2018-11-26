from flask import Flask
from api.auth.views import auths
from api.incident.views import incidents_bp
from instance.config import app_config


def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    # Register blueprints
    app.register_blueprint(auths, url_prefix='/api/v1')
    app.register_blueprint(incidents_bp, url_prefix='/api/v1')
    return app
