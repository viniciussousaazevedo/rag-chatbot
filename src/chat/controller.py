from flask import Blueprint
from util.request_handler import *
from util.response_handler import *
import chat.service as service

bp = Blueprint("chat", __name__)

@bp.route("/health", methods=["GET"])
def get_companies():
    return "Up and running!"
