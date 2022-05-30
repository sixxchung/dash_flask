"""Initialize Flask app."""
from flask import Flask
from flask_assets import Environment


def init_app():
    """Construct core Flask application with embedded Dash app."""
    flask_app = Flask(__name__, instance_relative_config=False)
    flask_app.config.from_object("config.Config")
    assets = Environment()
    assets.init_app(flask_app)

    with flask_app.app_context():
        # Import parts of our core Flask app
        from . import routes
        from .assets import compile_static_assets

        # Import Dash application
        from .dashboard import init_dashboard

        dash_app = init_dashboard(flask_app)

        # Compile static assets
        compile_static_assets(assets)

        return dash_app
