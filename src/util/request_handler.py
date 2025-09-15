from flask import request, jsonify

def body_as(clazz):
    data = request.get_json()
    if not data:
        return jsonify({"error": "JSON body missing"}), 400
    try:
        return clazz(**data)
    except TypeError as e:
        raise TypeError(f"error while trying to convert JSON request to {clazz.__name__}: {e}")