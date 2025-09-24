from flask_pymongo import PyMongo

mongo = PyMongo()

def init_extensions(flask_app):
    mongo.init_app(flask_app)
