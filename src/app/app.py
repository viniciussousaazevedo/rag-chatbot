from dotenv import load_dotenv; load_dotenv()
import os; import sys; sys.path.insert(0, os.path.abspath(os.getenv("PYTHONPATH")))

from app.errors.bad_request import register_error_handlers
from app.routes import register_routes
from flask import Blueprint, Flask

bp = Blueprint("flask_app", __name__)
@bp.route("/health", methods=["GET"])
def get_companies():
    return "Up and running!"

def setup_app(flask_app):
    register_error_handlers(flask_app)

def create_app():
    flask_app = Flask(__name__)
    setup_app(flask_app)
    register_routes(flask_app, bp)
    
    return flask_app

if __name__ == "__main__":
    flask_app = create_app()
    flask_app.run(host="0.0.0.0", port=5000)


