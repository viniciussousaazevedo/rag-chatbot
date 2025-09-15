from flask import jsonify
from typing import List

def to_json(obj):
    return [c.__dict__ for c in obj] if isinstance(obj, List) else obj.__dict__

def response(obj):
    return jsonify(to_json(obj))