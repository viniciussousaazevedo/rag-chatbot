from flask import jsonify
from flask import Flask

class BadRequestError(Exception):
    def __init__(self, message="Bad Request"):
        self.message = message
        super().__init__(self.message)

def register_error_handlers(flask_app: Flask):
    @flask_app.errorhandler(BadRequestError)
    def handle_bad_request(err):
        response = jsonify({"error": err.message})
        return response, 400
