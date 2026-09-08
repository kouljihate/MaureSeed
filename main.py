import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from flask import Flask, session
from config.config import Config
from shared.database import get_db, close_db
from shared.i18n import get_lang, get_translations
from shared.logger import app_logger
from shared.roles import get_current_user, get_role_name
from shared.format import format_number
from BE.routes import bp as api_bp
from FE.routes import bp as fe_bp
from BE.admin_routes import bp as admin_bp


def create_app():
    try:
        app = Flask(
            __name__,
            template_folder=os.path.join(os.path.dirname(__file__), "FE", "templates"),
            static_folder=os.path.join(os.path.dirname(__file__), "assets"),
            static_url_path="/assets",
        )
        app.config.from_object(Config)
        app.secret_key = Config.SECRET_KEY

        app.jinja_env.filters['format_number'] = format_number

        app.register_blueprint(api_bp, url_prefix="/api")
        app.register_blueprint(fe_bp)
        app.register_blueprint(admin_bp)

        @app.context_processor
        def inject_globals():
            try:
                user = get_current_user()
                lang = get_lang()
                return {
                    "lang": lang,
                    "t": get_translations(),
                    "version": Config.VERSION,
                    "app_name": Config.APP_NAME,
                    "app_name_ar": Config.APP_NAME_AR,
                    "current_user": user,
                    "current_role": get_role_name(user.get("role", "guest"), lang),
                }
            except Exception as e:
                app_logger.log_error(e, "inject_globals")
                return {"lang": "fr", "t": {}, "version": "0.0.0", "app_name": "MaureSeed", "app_name_ar": "مورسيد", "current_user": {"role": "guest", "name": "Guest"}, "current_role": "Guest"}

        @app.teardown_appcontext
        def shutdown_db(exception=None):
            try:
                close_db()
            except Exception as e:
                app_logger.log_error(e, "shutdown_db")

        app_logger.info(f"MaureSeed v{Config.VERSION} initialized")
        return app
    except Exception as e:
        app_logger.log_error(e, "create_app")
        raise


app = create_app()

if __name__ == "__main__":
    try:
        app.run(debug=True, host="0.0.0.0", port=5000)
    except Exception as e:
        app_logger.log_error(e, "__main__")
        raise
